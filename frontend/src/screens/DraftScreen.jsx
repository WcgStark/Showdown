import { useState, useEffect, useRef } from 'react'
import { Atmos, AppBar, SettingsModal } from '../components'
import { t } from '../i18n'
import {
  playNumberOne, playYokosoWatashi, playYhwachEntrance, playZankaNTachi,
  playGoldExperience, playKillerQueen, playKingCrimson, playMadeInHeaven,
  playNigerundayo, playYareYareDaze, playZaWarudo,
} from '../sounds'
import HakiOverlay from './draft/HakiOverlay'
import ArenaModal from './draft/ArenaModal'
import ArenaCard from './draft/ArenaCard'
import PlayerBanner from './draft/PlayerBanner'
import SlotColumn from './draft/SlotColumn'
import PositionColumn from './draft/PositionColumn'
import ActionPanel from './draft/ActionPanel'

const CHAR_SFX = {
  // Bleach
  "Ichigo Kurosaki":              playNumberOne,
  "Sousuke Aizen":                playYokosoWatashi,
  "Yhwach":                       playYhwachEntrance,
  "Genryūsai Shigekuni Yamamoto": playZankaNTachi,
  // JoJo
  "Giorno":                       playGoldExperience,
  "Yoshikage Kira":               playKillerQueen,
  "Diavolo":                      playKingCrimson,
  "Pucci":                        playMadeInHeaven,
  "Joseph Joestar":               playNigerundayo,
  "Jotaro Kujo":                  playYareYareDaze,
  "Dio Brando":                   playZaWarudo,
}

// Placeholder names shown on the gacha reel when the real pool is too small.
const REEL_NAMES = [
  "WARRIOR","MAGE","ARCHER","ROGUE","TANK","HEALER",
  "FIGHTER","SCOUT","VANGUARD","STRIKER","SUPPORT","GUARDIAN",
  "LANCER","RANGER","WIZARD","KNIGHT","SHADOW","BERSERKER",
]

/* ===================================================== */
/* SCREEN 3 — DRAFT BOARD                                */
/* ===================================================== */
const DraftScreen = ({
  universe, p1, p2, draft, onFinish, mode,
  onGacha, onAssign, onSkip, onUndo, onSwitch, imgUrl,
  onMenu, onPlayers, onPass, onRollArena, version, uiVolume, sfxVolume, musicVolume, lang,
  onUiVolumeChange, onSfxVolumeChange, onMusicVolumeChange, quality, onQualityChange, onLangChange,
  keybinds, onKeybindsChange, p1pfp, p2pfp,
}) => {
  const positions = universe.positions
  const [settingsOpen, setSettingsOpen] = useState(false)

  const filledP1 = draft.assignments.filter(a => a.p1 !== null).length
  const filledP2 = draft.assignments.filter(a => a.p2 !== null).length
  const totalPicks = filledP1 + filledP2
  const allDone = totalPicks === positions.length * 2

  // ARENA mode: the arena must be rolled before any character gacha is allowed.
  const arenaPending = draft.arenaEnabled && !draft.arena

  const [spinning, setSpinning] = useState(false)
  const [reelChars, setReelChars] = useState([])

  const [hakiActive, setHakiActive] = useState(false)
  const [shake, setShake] = useState(false)
  const shakeTimer = useRef(null)

  const prevSpinning = useRef(false)
  useEffect(() => {
    if (prevSpinning.current && !spinning) {
      if (draft?.currentChar?.ext === "gif") {
        // Any universe: shake the whole screen when a GIF character is pulled.
        setShake(true)
        clearTimeout(shakeTimer.current)
        shakeTimer.current = setTimeout(() => setShake(false), 1300)
        if (universe.id === "onepiece") setHakiActive(true)
      }
      const sfx = CHAR_SFX[draft?.currentChar?.name]
      if (sfx) sfx()
    }
    prevSpinning.current = spinning
  }, [spinning, draft?.currentChar?.ext, draft?.currentChar?.name])

  useEffect(() => () => clearTimeout(shakeTimer.current), [])

  const [switchMode, setSwitchMode] = useState(false)
  const [switchFirst, setSwitchFirst] = useState(null)

  const [arenaSpinning, setArenaSpinning] = useState(false)
  const [arenaReel, setArenaReel]         = useState([])
  const [arenaModalOpen, setArenaModalOpen] = useState(false)

  const spinArena = async () => {
    if (arenaSpinning || draft.arena) return
    setArenaSpinning(true)
    setArenaReel([])
    const result = await onRollArena()
    const resultArena = result?.arena
    const resultName = resultArena?.name ?? "???"
    const allArenas = (universe.arenaList || []).filter(a => a.name !== resultName)
    for (let i = allArenas.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [allArenas[i], allArenas[j]] = [allArenas[j], allArenas[i]]
    }
    const body = Array.from({ length: 10 }, (_, i) => allArenas[i % Math.max(allArenas.length, 1)])
    setArenaReel([...body, resultArena])
    setTimeout(() => {
      setArenaSpinning(false)
      setArenaReel([])
      setArenaModalOpen(true)
    }, 2000)
  }

  const spin = async () => {
    if (draft.currentChar || spinning || arenaPending) return
    setSpinning(true)
    setReelChars([])

    const result = await onGacha()

    const resultName = (result?.currentChar?.name ?? "???").toUpperCase()
    const rawPool = (result?.poolSample && result.poolSample.length > 4)
      ? result.poolSample : REEL_NAMES

    const unique = [...new Set(rawPool.map(n => n.toUpperCase()).filter(n => n !== resultName))]
    for (let i = unique.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [unique[i], unique[j]] = [unique[j], unique[i]]
    }
    const reelBody = Array.from({ length: 29 }, (_, i) => unique[i % Math.max(unique.length, 1)])
    const reel = [...reelBody, resultName]
    setReelChars(reel)

    setTimeout(() => {
      setSpinning(false)
      setReelChars([])
    }, 2400)
  }

  const handleAssign = async posIdx => {
    if (switchMode) {
      const posName = positions[posIdx]
      if (switchFirst === null) {
        setSwitchFirst(posName)
      } else {
        await onSwitch(switchFirst, posName)
        setSwitchMode(false)
        setSwitchFirst(null)
      }
      return
    }
    if (!draft.currentChar) return
    await onAssign(positions[posIdx])
  }

  const handleSwitch = () => {
    const myFilled = draft.turn === "p1" ? filledP1 : filledP2
    if (myFilled < 2) return
    setSwitchMode(true)
    setSwitchFirst(null)
  }

  const handlePass = async () => {
    if (switchMode) {
      setSwitchMode(false)
      setSwitchFirst(null)
    }
    await onPass()
  }

  // ── Keyboard controls (respect the same enable rules as the buttons) ──────
  useEffect(() => {
    const onKey = e => {
      if (e.repeat) return
      const skipsLeft = draft.turn === "p1" ? draft.skipsP1 : draft.skipsP2
      const myFilled  = draft.turn === "p1" ? filledP1 : filledP2

      // Back / Escape: close settings, else cancel an active switch
      if (e.code === keybinds.back) {
        if (settingsOpen) { e.preventDefault(); setSettingsOpen(false) }
        else if (switchMode) { e.preventDefault(); setSwitchMode(false); setSwitchFirst(null) }
        return
      }
      // While settings is open, don't trigger game actions
      if (settingsOpen) return

      if (e.code === keybinds.gacha) {
        if (!draft.currentChar && !spinning && !switchMode && !arenaPending) { e.preventDefault(); spin() }
      } else if (e.code === keybinds.skip) {
        if (draft.currentChar && skipsLeft > 0 && !spinning) { e.preventDefault(); onSkip() }
      } else if (e.code === keybinds.pass) {
        const myFilled = draft.turn === "p1" ? filledP1 : filledP2
        if (!draft.currentChar && !switchMode && !spinning && myFilled >= positions.length) { e.preventDefault(); handlePass() }
      } else if (e.code === keybinds.switch) {
        if (!draft.currentChar && !switchMode && myFilled >= 2 && !spinning) { e.preventDefault(); handleSwitch() }
      } else if (e.code === keybinds.undo) {
        if (draft.undoAvailable && !spinning) { e.preventDefault(); onUndo() }
      } else if (e.code === keybinds.confirm) {
        if (allDone && !spinning) { e.preventDefault(); onFinish() }
      }
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [keybinds, draft, spinning, switchMode, settingsOpen, filledP1, filledP2, allDone])

  return (
    <div className={`stage acc-${universe.id}${shake ? " shake-screen" : ""}`} data-screen-label="03 Draft">
      <Atmos particles={false} grid={true} />
      <AppBar phase="DRAFTING" universe={universe} mode={mode} step={`${totalPicks} / ${positions.length * 2}`} version={version} lang={lang} />

      {switchMode && (
        <div style={{
          position: "absolute", top: 70, left: 0, right: 0, zIndex: 10,
          textAlign: "center",
          fontFamily: "var(--f-mono)", fontSize: 13, letterSpacing: "0.2em",
          color: "var(--acc)", textTransform: "uppercase",
          padding: "10px 0", background: "var(--acc-soft)",
          borderBottom: "1px solid var(--acc-line)",
        }}>
          {switchFirst
            ? t('swapHint2', lang).replace('{slot}', switchFirst)
            : t('swapHint1', lang)}
          <button onClick={() => { setSwitchMode(false); setSwitchFirst(null) }}
            style={{ marginLeft: 24, background: "transparent", border: "1px solid var(--acc-line)", color: "var(--ink-1)", padding: "4px 14px", cursor: "pointer", fontFamily: "var(--f-mono)", fontSize: 11 }}>
            {t('cancel', lang)}
          </button>
        </div>
      )}

      {/* Player banners */}
      <PlayerBanner
        side="left" player={p1} filled={filledP1} total={positions.length}
        active={draft.turn === "p1"} skips={draft.skipsP1} lang={lang} pfp={p1pfp}
      />
      <PlayerBanner
        side="right" player={p2} filled={filledP2} total={positions.length}
        active={draft.turn === "p2"} skips={draft.skipsP2} lang={lang} pfp={p2pfp}
      />

      {/* ARENA CARD — centered in the 196px gap between banners (13px each side) */}
      {draft.arenaEnabled && (
        <div style={{ position: "absolute", top: 80, left: 677, width: 170, height: 120 }}>
          <ArenaCard
            arena={draft.arena}
            arenaSpinning={arenaSpinning}
            arenaReel={arenaReel}
            universeId={universe.id}
            onRoll={spinArena}
            onOpenModal={() => setArenaModalOpen(true)}
            lang={lang}
          />
        </div>
      )}

      {/* MAIN GRID */}
      <div style={{
        position: "absolute",
        top: 220, left: 64, right: 460, bottom: 60,
        display: "grid", gridTemplateColumns: "1fr 280px 1fr", gap: 18,
      }}>
        <SlotColumn
          side="p1" positions={positions} assignments={draft.assignments}
          switchMode={switchMode && draft.turn === "p1"}
          switchFirst={switchFirst}
          onSlotClick={handleAssign}
          imgUrl={imgUrl}
        />
        <PositionColumn
          positions={positions}
          assignments={draft.assignments}
          turn={draft.turn}
          enabled={!!draft.currentChar && !switchMode && !spinning}
          onPick={handleAssign}
          lang={lang}
        />
        <SlotColumn
          side="p2" positions={positions} assignments={draft.assignments}
          switchMode={switchMode && draft.turn === "p2"}
          switchFirst={switchFirst}
          onSlotClick={handleAssign}
          imgUrl={imgUrl}
        />
      </div>

      {/* RIGHT ACTION PANEL */}
      <ActionPanel
        universe={universe}
        draft={draft}
        spinning={spinning}
        shake={shake}
        reelChars={reelChars}
        onSpin={spin}
        onSkip={onSkip}
        onUndo={onUndo}
        onSwitch={handleSwitch}
        onReady={onFinish}
        ready={allDone}
        imgUrl={imgUrl}
        onMenu={onMenu}
        onPlayers={onPlayers}
        onPass={handlePass}
        onSettings={() => setSettingsOpen(true)}
        switchActive={switchMode}
        lang={lang}
        keybinds={keybinds}
      />

      {settingsOpen && (
        <SettingsModal
          uiVolume={uiVolume}
          onUiVolumeChange={onUiVolumeChange}
          sfxVolume={sfxVolume}
          onSfxVolumeChange={onSfxVolumeChange}
          musicVolume={musicVolume}
          onMusicVolumeChange={onMusicVolumeChange}
          quality={quality}
          onQualityChange={onQualityChange}
          lang={lang}
          onLangChange={onLangChange}
          keybinds={keybinds}
          onKeybindsChange={onKeybindsChange}
          onClose={() => setSettingsOpen(false)}
        />
      )}

      {/* Arena detail modal */}
      {arenaModalOpen && draft.arena && (
        <ArenaModal
          arena={draft.arena}
          universeId={universe.id}
          onClose={() => setArenaModalOpen(false)}
          lang={lang}
        />
      )}

      {/* Haki cinematic overlay */}
      {hakiActive && <HakiOverlay sfxVolume={sfxVolume} onComplete={() => setHakiActive(false)} />}
    </div>
  )
}

export default DraftScreen
