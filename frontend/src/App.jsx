import { useState, useEffect, useCallback } from 'react'
import LobbyScreen from './screens/LobbyScreen'
import PlayersScreen from './screens/PlayersScreen'
import DraftScreen from './screens/DraftScreen'
import ResultScreen from './screens/ResultScreen'

const UNIVERSE_UI = {
  onepiece:   { codename: "GRAND LINE" },
  naruto:     { codename: "HIDDEN LEAF" },
  bleach:     { codename: "GOTEI" },
  invincible: { codename: "VILTRUM" },
}

const enrichUniverse = u => ({
  ...u,
  codename: UNIVERSE_UI[u.id]?.codename || u.name.toUpperCase(),
  accent: `var(--u-${u.id})`,
  blurb: "",
  sample: u.positions,
})

const App = () => {
  const [screen, setScreen]                 = useState("lobby")
  const [config, setConfig]                 = useState(null)
  const [selectedId, setSelectedId]         = useState("onepiece")
  const [universeConfig, setUniverseConfig] = useState(null)
  const [p1, setP1]                         = useState("")
  const [p2, setP2]                         = useState("")
  const [mode, setMode]                     = useState("draft")
  const [draft, setDraft]                   = useState(null)
  const [layout, setLayout]                 = useState({ scale: 1, x: 0, y: 0 })

  const [updateInfo, setUpdateInfo]         = useState(null)
  const [updateStatus, setUpdateStatus]     = useState("idle")
  const [updateProgress, setUpdateProgress] = useState(0)
  const [updateDismissed, setUpdateDismissed] = useState(false)

  const [volume, setVolume] = useState(
    () => parseFloat(localStorage.getItem("hakiVolume") ?? "0.9")
  )
  useEffect(() => { localStorage.setItem("hakiVolume", volume) }, [volume])

  // ── Responsive layout: scale + center the 1920×1080 stage ────────────────
  useEffect(() => {
    const updateLayout = () => {
      const w = window.innerWidth
      const h = window.innerHeight
      const s = Math.min(w / 1920, h / 1080)
      setLayout({ scale: s, x: (w - 1920 * s) / 2, y: (h - 1080 * s) / 2 })
    }
    const onResize = () => requestAnimationFrame(updateLayout)
    updateLayout()
    window.addEventListener("resize", onResize)
    document.addEventListener("fullscreenchange", onResize)
    return () => {
      window.removeEventListener("resize", onResize)
      document.removeEventListener("fullscreenchange", onResize)
    }
  }, [])

  // ── F11 fullscreen toggle ─────────────────────────────────────────────────
  useEffect(() => {
    const onKey = e => {
      if (e.key === "F11") {
        e.preventDefault()
        window.pywebview?.api?.toggle_fullscreen()
      }
    }
    document.addEventListener("keydown", onKey)
    return () => document.removeEventListener("keydown", onKey)
  }, [])

  // ── Wait for pywebview API then load config ───────────────────────────────
  useEffect(() => {
    const loadConfig = async () => {
      const cfg = await window.pywebview.api.get_config()
      setConfig({
        ...cfg,
        universes: cfg.universes.map(enrichUniverse),
      })
    }
    if (window.pywebview) {
      loadConfig()
    } else {
      window.addEventListener("pywebviewready", loadConfig, { once: true })
    }
  }, [])

  // ── Check for updates once config is loaded (pywebview is ready) ─────────
  useEffect(() => {
    if (!config) return
    ;(async () => {
      try {
        const result = await window.pywebview.api.check_update()
        if (result.hasUpdate) setUpdateInfo(result)
      } catch {}
    })()
  }, [config])

  // ── Poll download progress ─────────────────────────────────────────────────
  useEffect(() => {
    if (updateStatus !== "downloading") return
    const interval = setInterval(async () => {
      try {
        const p = await window.pywebview.api.get_update_progress()
        setUpdateProgress(p.value)
        if (p.status === "done") {
          setUpdateStatus("done")
          clearInterval(interval)
        } else if (p.status === "error") {
          setUpdateStatus("error")
          clearInterval(interval)
        }
      } catch {}
    }, 500)
    return () => clearInterval(interval)
  }, [updateStatus])

  const handleDownloadUpdate = async () => {
    setUpdateStatus("downloading")
    await window.pywebview.api.start_download_update(updateInfo.downloadUrl)
  }

  const handleApplyUpdate = async () => {
    await window.pywebview.api.apply_update()
  }

  // ── Image URL helper — assets are at dist root after Vite build ───────────
  const imgUrl = useCallback((charName, ext = "jpeg") => {
    if (!charName || !universeConfig) return null
    const folder = universeConfig.assetFolder.replace(/^assets\//, '')
    return `./${folder}/${encodeURIComponent(charName)}.${ext}`
  }, [universeConfig])

  // ── Universe picker ───────────────────────────────────────────────────────
  const handleSelectUniverse = universeId => {
    setSelectedId(universeId)
    const u = config.universes.find(u => u.id === universeId)
    setUniverseConfig(u)
    setMode(u.defaultFilter)
    setScreen("players")
  }

  // ── Start game ────────────────────────────────────────────────────────────
  const handleStartGame = async () => {
    const u = universeConfig
    const result = await window.pywebview.api.start_match(
      u.id, mode,
      p1 || "Player 1", p2 || "Player 2"
    )
    setDraft(result)
    setScreen("draft")
  }

  // ── Draft actions (call Python, update draft state) ───────────────────────
  const handleGacha = async () => {
    const result = await window.pywebview.api.gacha()
    setDraft(result)
    return result
  }

  const handleAssign = async positionName => {
    const result = await window.pywebview.api.assign(positionName)
    setDraft(result)
  }

  const handleSkip = async () => {
    const result = await window.pywebview.api.skip()
    setDraft(result)
  }

  const handleSwitch = async (posA, posB) => {
    const result = await window.pywebview.api.switch_positions(posA, posB)
    setDraft(result)
  }

  const handleUndo = async () => {
    const result = await window.pywebview.api.undo()
    setDraft(result)
  }

  const handlePass = async () => {
    const result = await window.pywebview.api.pass_turn()
    setDraft(result)
  }

  const handleFinish = () => setScreen("result")

  const handleRestart = async () => {
    await window.pywebview.api.reset()
    setDraft(null)
    setP1("")
    setP2("")
    setScreen("lobby")
  }

  // ── Loading ───────────────────────────────────────────────────────────────
  if (!config) {
    return (
      <div style={{
        position: "fixed", inset: 0, background: "#07080c",
        display: "grid", placeItems: "center",
        fontFamily: "monospace", color: "#5b6076", letterSpacing: "0.28em", fontSize: 13,
      }}>
        LOADING…
      </div>
    )
  }

  const universe = config.universes.find(u => u.id === selectedId) || config.universes[0]

  return (
    <>
    <div className="stage-wrap">
      <div className="stage" style={{ transform: `scale(${layout.scale})`, left: layout.x, top: layout.y }}>
        {screen === "lobby" && (
          <LobbyScreen
            universes={config.universes}
            onSelect={handleSelectUniverse}
            selectedId={selectedId}
            setSelectedId={setSelectedId}
            version={config.version}
            volume={volume}
            onVolumeChange={setVolume}
          />
        )}

        {screen === "players" && universeConfig && (
          <PlayersScreen
            universe={universe}
            mode={mode}
            setMode={setMode}
            p1={p1}
            p2={p2}
            setP1={setP1}
            setP2={setP2}
            onBack={() => setScreen("lobby")}
            onStart={handleStartGame}
            quickNames={config.quickNames}
            version={config.version}
          />
        )}

        {screen === "draft" && draft && (
          <DraftScreen
            universe={universe}
            p1={p1 || "Player 1"}
            p2={p2 || "Player 2"}
            draft={draft}
            onFinish={handleFinish}
            mode={mode}
            onGacha={handleGacha}
            onAssign={handleAssign}
            onSkip={handleSkip}
            onSwitch={handleSwitch}
            onUndo={handleUndo}
            imgUrl={imgUrl}
            onMenu={handleRestart}
            onPlayers={() => setScreen("players")}
            onPass={handlePass}
            version={config.version}
            volume={volume}
          />
        )}

        {screen === "result" && draft && (
          <ResultScreen
            universe={universe}
            p1={p1 || "Player 1"}
            p2={p2 || "Player 2"}
            draft={draft}
            onRestart={handleRestart}
            imgUrl={imgUrl}
            version={config.version}
          />
        )}
      </div>
    </div>

    {updateInfo && !updateDismissed && (
      <div style={{
        position: "fixed", bottom: 24, right: 24, zIndex: 9999,
        width: 288,
        background: "rgba(11, 13, 20, 0.96)",
        border: "1px solid rgba(255,255,255,0.10)",
        borderRadius: 12,
        padding: "16px 18px",
        fontFamily: "Inter, system-ui, sans-serif",
        color: "#f4f5fa",
        boxShadow: "0 8px 40px rgba(0,0,0,0.6)",
        backdropFilter: "blur(16px)",
      }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 12 }}>
          <div>
            <div style={{ fontSize: 10, color: "#5b6076", letterSpacing: "0.14em", textTransform: "uppercase", marginBottom: 3 }}>
              Atualização disponível
            </div>
            <div style={{ fontSize: 14, fontWeight: 600, lineHeight: 1.3 }}>
              v{updateInfo.latestVersion}
              <span style={{ color: "#5b6076", fontWeight: 400, fontSize: 11, marginLeft: 6 }}>
                (atual v{updateInfo.currentVersion})
              </span>
            </div>
          </div>
          <button
            onClick={() => setUpdateDismissed(true)}
            style={{
              background: "none", border: "none", color: "#5b6076",
              cursor: "pointer", fontSize: 18, lineHeight: 1, padding: "0 2px",
              marginTop: -2,
            }}
          >×</button>
        </div>

        {updateStatus === "idle" && (
          <button
            onClick={handleDownloadUpdate}
            style={{
              width: "100%", padding: "9px 0",
              background: "oklch(0.74 0.16 35)",
              border: "none", borderRadius: 6,
              color: "#07080c", fontWeight: 700, fontSize: 12,
              cursor: "pointer", letterSpacing: "0.10em",
            }}
          >BAIXAR ATUALIZAÇÃO</button>
        )}

        {updateStatus === "downloading" && (
          <div>
            <div style={{ display: "flex", justifyContent: "space-between", fontSize: 11, color: "#8a8fa3", marginBottom: 7 }}>
              <span>Baixando…</span>
              <span>{updateProgress}%</span>
            </div>
            <div style={{ height: 4, background: "rgba(255,255,255,0.08)", borderRadius: 2, overflow: "hidden" }}>
              <div style={{
                height: "100%", width: `${updateProgress}%`,
                background: "oklch(0.74 0.16 35)",
                borderRadius: 2, transition: "width 0.3s ease",
              }} />
            </div>
          </div>
        )}

        {updateStatus === "done" && (
          <button
            onClick={handleApplyUpdate}
            style={{
              width: "100%", padding: "9px 0",
              background: "oklch(0.78 0.16 150)",
              border: "none", borderRadius: 6,
              color: "#07080c", fontWeight: 700, fontSize: 12,
              cursor: "pointer", letterSpacing: "0.10em",
            }}
          >REINICIAR E APLICAR</button>
        )}

        {updateStatus === "error" && (
          <div style={{ fontSize: 11, color: "oklch(0.7 0.2 25)", textAlign: "center", padding: "4px 0" }}>
            Erro ao baixar. Tente novamente mais tarde.
          </div>
        )}
      </div>
    )}
    </>
  )
}

export default App
