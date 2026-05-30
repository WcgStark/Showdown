import { useState, useEffect, useRef } from 'react'
import { Atmos, AppBar, Icon, CornerTicks, SettingsModal } from '../components'
import { t } from '../i18n'
import { codeLabel } from '../keybinds'
import { playNumberOne, playYokosoWatashi, playYhwachEntrance } from '../sounds'

const CHAR_SFX = {
  "Ichigo Kurosaki": playNumberOne,
  "Sousuke Aizen":   playYokosoWatashi,
  "Yhwach":          playYhwachEntrance,
}

/* ── Haki effect ─────────────────────────────────────────────────── */
// Portrait center inside the ActionPanel (right: 64, width: 380) at 1920×1080
const HAKI_OX = 1666 // 1920 - 64 - 380/2
const HAKI_OY = 272  // panel top 80 + padding 18 + label ~20 + marginTop 14 + portrait 280/2

const HakiOverlay = ({ onComplete, sfxVolume = 0.9 }) => {
  useEffect(() => {
    const audio = new Audio(
      "./sounds/Monkey%20D%20Luffy%20Haki%20Sound%20%20One%20Piece.mp3"
    )
    audio.volume = Math.max(0, Math.min(1, sfxVolume))
    audio.play().catch(() => {})
    const t = setTimeout(onComplete, 3600)
    return () => clearTimeout(t)
  }, [])

  const ox = `${HAKI_OX}px`, oy = `${HAKI_OY}px`
  const pctX = (HAKI_OX / 1920 * 100).toFixed(1)
  const pctY = (HAKI_OY / 1080 * 100).toFixed(1)

  return (
    <div style={{ position: "absolute", inset: 0, zIndex: 100, pointerEvents: "none", overflow: "hidden" }}>

      {/* Backdrop darkens the screen but stays transparent over the portrait */}
      <div style={{
        position: "absolute", inset: 0,
        background: `radial-gradient(ellipse 42% 52% at ${pctX}% ${pctY}%, transparent 0%, transparent 28%, rgba(0,0,0,0.92) 80%, rgba(0,0,0,0.97) 100%)`,
        animation: "hakiFlash 3.6s ease-out forwards",
      }} />

      {/* Three red rings expanding from portrait */}
      {[0, 0.28, 0.56].map((delay, i) => (
        <div key={i} style={{
          position: "absolute", left: ox, top: oy,
          width: 180, height: 180, borderRadius: "50%",
          border: "2px solid rgba(225, 0, 0, 0.97)",
          boxShadow: "0 0 32px rgba(220, 0, 0, 0.82), inset 0 0 32px rgba(200, 0, 0, 0.28)",
          transform: "translate(-50%, -50%) scale(0)", opacity: 0,
          animation: `hakiRing 2s ${delay}s cubic-bezier(0.06, 0.82, 0.26, 1) forwards`,
        }} />
      ))}

      {/* Screen-edge red glow + shake */}
      <div style={{
        position: "absolute", inset: 0,
        boxShadow: "inset 0 0 110px rgba(190,0,0,0.48)",
        animation: "hakiShake 0.55s ease-out, hakiFlash 3.6s ease-out forwards",
      }} />
    </div>
  )
}

/* ===================================================== */
/* SCREEN 3 — DRAFT BOARD                                */
/* ===================================================== */

const REEL_NAMES = [
  "WARRIOR","MAGE","ARCHER","ROGUE","TANK","HEALER",
  "FIGHTER","SCOUT","VANGUARD","STRIKER","SUPPORT","GUARDIAN",
  "LANCER","RANGER","WIZARD","KNIGHT","SHADOW","BERSERKER",
]

/* ----- Player banner ----- */
const PlayerBanner = ({ side, player, filled, total, active, skips, lang }) => {
  const isLeft = side === "left"
  return (
    <div style={{
      position: "absolute", top: 80, [isLeft ? "left" : "right"]: isLeft ? 64 : 460, width: 600,
      height: 120,
      display: "flex", alignItems: "center", gap: 18,
      flexDirection: isLeft ? "row" : "row-reverse",
    }}>
      <div className="panel" style={{
        width: 100, height: 100, position: "relative", display: "grid", placeItems: "center",
        background: active ? "color-mix(in oklab, var(--acc) 18%, var(--bg-elev))" : "var(--bg-elev)",
        borderColor: active ? "var(--acc)" : "var(--line)",
        boxShadow: active ? "0 0 32px -4px color-mix(in oklab, var(--acc) 60%, transparent)" : "none",
      }}>
        <CornerTicks color={active ? "var(--acc)" : "var(--line-2)"} />
        <Icon name="user" size={40} />
        {active && (
          <div style={{
            position: "absolute", bottom: -8, [isLeft ? "left" : "right"]: -8,
            background: "var(--acc)", color: "#000",
            fontFamily: "var(--f-display)", fontSize: 10, padding: "3px 8px",
            letterSpacing: "0.18em", fontWeight: 700,
            boxShadow: "0 0 16px var(--acc)",
          }}>ON CLOCK</div>
        )}
      </div>

      <div style={{ flex: 1, textAlign: isLeft ? "left" : "right", display: "flex", flexDirection: "column", gap: 6 }}>
        <div className="display-x" style={{ fontSize: 12, color: active ? "var(--acc)" : "var(--ink-3)" }}>
          PLAYER {isLeft ? "01" : "02"} · {active ? t('drafting', lang) : t('standby', lang)}
        </div>
        <div className="display" style={{ fontSize: 40, lineHeight: 1, letterSpacing: "0.04em" }}>
          {player || (isLeft ? "PLAYER ONE" : "PLAYER TWO")}
        </div>
        <div style={{ display: "flex", gap: 4, justifyContent: isLeft ? "flex-start" : "flex-end" }}>
          {Array.from({ length: total }).map((_, i) => (
            <span key={i} style={{
              width: 26, height: 4,
              background: i < filled ? "var(--acc)" : "var(--line-2)",
              boxShadow: i < filled ? "0 0 8px var(--acc)" : "none",
            }} />
          ))}
        </div>
      </div>

      <div style={{ textAlign: isLeft ? "right" : "left", display: "flex", flexDirection: "column", gap: 2 }}>
        <span style={{ color: "var(--ink-3)", fontFamily: "var(--f-mono)", fontSize: 10, letterSpacing: "0.18em" }}>{t('skipsWord', lang)}</span>
        <span className="display" style={{ fontSize: 32, color: "var(--ink-0)" }}>
          {skips}<span style={{ color: "var(--ink-3)", fontSize: 18 }}>/1</span>
        </span>
      </div>
    </div>
  )
}

/* ----- Slot Column ----- */
const SlotColumn = ({ side, positions, assignments, switchMode, switchFirst, onSlotClick, imgUrl }) => (
  <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
    {positions.map((pos, i) => {
      const assigned = assignments[i][side]
      const isFirstSelected = switchMode && switchFirst === pos
      const clickable = switchMode && assigned
      return (
        <div
          key={i}
          onClick={() => clickable ? onSlotClick(i) : undefined}
          style={{
            flex: 1,
            display: "flex", flexDirection: side === "p1" ? "row" : "row-reverse",
            alignItems: "stretch", position: "relative",
            background: isFirstSelected
              ? "color-mix(in oklab, var(--acc) 25%, var(--bg-elev))"
              : assigned ? "var(--bg-elev)" : "transparent",
            border: "1px solid",
            borderColor: isFirstSelected ? "var(--acc)"
              : clickable ? "var(--acc-line)"
              : assigned ? "var(--acc-line)" : "var(--line)",
            borderStyle: assigned ? "solid" : "dashed",
            cursor: clickable ? "pointer" : "default",
            boxShadow: isFirstSelected ? "0 0 20px -4px color-mix(in oklab, var(--acc) 60%, transparent)" : "none",
          }}
        >
          {/* Fixed-size image cell */}
          <div style={{
            width: 90, minWidth: 90, flexShrink: 0,
            position: "relative", overflow: "hidden",
            background: "var(--bg-3)",
          }}>
            {assigned && imgUrl ? (
              <img
                src={imgUrl(assigned.name, assigned.ext)}
                alt={assigned.name}
                style={{
                  position: "absolute", inset: 0,
                  width: "100%", height: "100%",
                  objectFit: "cover",
                  objectPosition: "50% 15%",
                }}
                onError={e => { e.currentTarget.style.display = "none" }}
              />
            ) : (
              <div style={{ position: "absolute", inset: 0, display: "grid", placeItems: "center", color: "var(--ink-4)" }}>
                <Icon name="user" size={28} />
              </div>
            )}
          </div>
          <div style={{
            flex: 1, padding: "12px 16px", display: "flex", flexDirection: "column",
            justifyContent: "center", textAlign: side === "p1" ? "left" : "right",
          }}>
            <span style={{ fontFamily: "var(--f-mono)", fontSize: 10, letterSpacing: "0.18em", color: assigned ? "var(--acc)" : "var(--ink-3)" }}>
              {String(i + 1).padStart(2, "0")} · {pos.toUpperCase()}
            </span>
            <span className="display" style={{ fontSize: 22, marginTop: 2, color: assigned ? "var(--ink-0)" : "var(--ink-4)" }}>
              {assigned ? assigned.name : "— EMPTY —"}
            </span>
          </div>
        </div>
      )
    })}
  </div>
)

/* ----- Position column (center / drop targets) ----- */
const PositionColumn = ({ positions, assignments, turn, enabled, onPick, lang }) => (
  <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
    {positions.map((pos, i) => {
      const alreadyForTurn = assignments[i][turn] !== null
      const open = enabled && !alreadyForTurn
      return (
        <button
          key={i}
          disabled={!open}
          onClick={() => onPick(i)}
          className="panel"
          style={{
            flex: 1, position: "relative",
            background: open ? "var(--acc-soft)" : "var(--bg-glass)",
            borderColor: open ? "var(--acc)" : "var(--line)",
            color: "var(--ink-0)", cursor: open ? "pointer" : "not-allowed",
            display: "grid", placeItems: "center",
            fontFamily: "var(--f-display)", fontSize: 20, fontWeight: 700,
            letterSpacing: "0.08em", textTransform: "uppercase",
            transition: "transform 80ms ease",
            boxShadow: open ? "0 0 28px -8px color-mix(in oklab, var(--acc) 60%, transparent)" : "none",
          }}
          onMouseDown={e => open && (e.currentTarget.style.transform = "scale(0.99)")}
          onMouseUp={e => (e.currentTarget.style.transform = "scale(1)")}
          onMouseLeave={e => (e.currentTarget.style.transform = "scale(1)")}
        >
          {open && (
            <>
              <span style={{ position: "absolute", top: 6, left: 8, fontSize: 10, fontFamily: "var(--f-mono)", color: "var(--acc)", letterSpacing: "0.2em" }}>{t('drop', lang)}</span>
              <span style={{ position: "absolute", top: 6, right: 8, fontSize: 10, fontFamily: "var(--f-mono)", color: "var(--acc)", letterSpacing: "0.2em" }}>{String(i + 1).padStart(2, "0")}</span>
            </>
          )}
          <span style={{ color: alreadyForTurn ? "var(--ink-4)" : (open ? "var(--ink-0)" : "var(--ink-2)") }}>{pos}</span>
          <span style={{ position: "absolute", bottom: 6, fontSize: 10, fontFamily: "var(--f-mono)", color: "var(--ink-3)", letterSpacing: "0.18em" }}>
            {assignments[i].p1 ? "P1" : "·"} <span style={{ color: "var(--ink-4)" }}>/</span> {assignments[i].p2 ? "P2" : "·"}
          </span>
        </button>
      )
    })}
  </div>
)

/* ----- Action button ----- */
const ActionBtn = ({ icon, label, hint, onClick, disabled, primary, fullWidth }) => (
  <button
    onClick={onClick}
    disabled={disabled}
    className={primary ? "btn btn-primary" : "btn"}
    style={{ height: 56, gridColumn: fullWidth ? "span 2" : "auto", flexDirection: "column", gap: 4, padding: 0 }}
  >
    <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
      <Icon name={icon} size={16} />
      <span>{label}</span>
    </div>
    <span style={{ fontSize: 9, color: "var(--ink-3)", fontFamily: "var(--f-mono)", letterSpacing: "0.18em" }}>[ {hint} ]</span>
  </button>
)

/* ----- Right action panel ----- */
const ActionPanel = ({
  universe, draft, spinning, reelChars, onSpin, onSkip, onUndo, onSwitch, onReady,
  ready, imgUrl, onMenu, onPlayers, onPass, onSettings, switchActive, lang, keybinds,
}) => {
  const turnLabel = draft.turn === "p1" ? "PLAYER 01" : "PLAYER 02"
  const skipsLeft = draft.turn === "p1" ? draft.skipsP1 : draft.skipsP2
  const myFilled = draft.turn === "p1"
    ? draft.assignments.filter(a => a.p1 !== null).length
    : draft.assignments.filter(a => a.p2 !== null).length
  const totalPositions = draft.assignments.length

  return (
    <div style={{ position: "absolute", top: 80, right: 64, bottom: 60, width: 380, display: "flex", flexDirection: "column", gap: 14 }}>
      {/* Current pick / Gacha reveal */}
      <div className="panel panel-tagged scanlines" style={{
        padding: 18, position: "relative", height: 460,
        background: "linear-gradient(180deg, color-mix(in oklab, var(--acc) 8%, var(--bg-elev)), var(--bg-elev))",
        borderColor: "var(--acc-line)",
      }}>
        <CornerTicks />
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <span className="label">{t('currentPick', lang)}</span>
          <span style={{ fontFamily: "var(--f-mono)", fontSize: 10, color: "var(--acc)", letterSpacing: "0.2em" }}>
            {draft.turn === "p1" ? "↩ FOR P1" : "FOR P2 ↪"}
          </span>
        </div>

        {/* Portrait area */}
        <div style={{ position: "relative", marginTop: 14, height: 280, overflow: "hidden" }}>
          {spinning && reelChars.length > 0 && (
            <div style={{ position: "absolute", inset: 0, background: "linear-gradient(180deg, rgba(7,8,12,1) 0%, transparent 20%, transparent 80%, rgba(7,8,12,1) 100%)", zIndex: 2, pointerEvents: "none" }} />
          )}
          <div style={{ position: "absolute", inset: 0, background: "repeating-linear-gradient(135deg, rgba(255,255,255,0.025) 0 10px, transparent 10px 20px), var(--bg-1)" }} />

          {!spinning && !draft.currentChar && (
            <div style={{ position: "absolute", inset: 0, display: "grid", placeItems: "center", color: "var(--ink-3)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.2em", textAlign: "center", padding: 20 }}>
              {t('pressGacha', lang)}<br />
              <span style={{ color: "var(--ink-4)", marginTop: 8, display: "inline-block" }}>{t('noPickActive', lang)}</span>
            </div>
          )}

          {spinning && reelChars.length === 0 && (
            <div style={{ position: "absolute", inset: 0, display: "grid", placeItems: "center", color: "var(--ink-2)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.2em" }}>
              {t('rolling', lang)}
            </div>
          )}

          {spinning && reelChars.length > 0 && (
            <div style={{
              position: "absolute", left: 0, right: 0, top: 0,
              display: "flex", flexDirection: "column", alignItems: "center",
              animation: "reelSpin 2.4s cubic-bezier(0.05, 0.85, 0.2, 1) forwards",
              willChange: "transform",
            }}>
              {reelChars.map((n, i) => (
                <div key={i} className="display" style={{
                  fontSize: 22, lineHeight: "60px", height: 60,
                  color: i === reelChars.length - 1 ? "var(--acc)" : "var(--ink-1)",
                  textShadow: i === reelChars.length - 1 ? "0 0 24px var(--acc)" : "none",
                  whiteSpace: "nowrap",
                }}>{n}</div>
              ))}
            </div>
          )}

          {!spinning && draft.currentChar && (
            <div style={{ position: "absolute", inset: 0, display: "flex", flexDirection: "column" }}>
              {imgUrl && (
                <img
                  src={imgUrl(draft.currentChar.name, draft.currentChar.ext)}
                  alt={draft.currentChar.name}
                  style={{ flex: 1, width: "100%", objectFit: "cover", objectPosition: "50% 10%" }}
                  onError={e => { e.currentTarget.style.display = "none" }}
                />
              )}
              <div style={{ position: "absolute", inset: 0, background: "linear-gradient(180deg, transparent 55%, rgba(7,8,12,0.95))" }} />
              <div style={{ position: "absolute", bottom: 14, left: 14, right: 14, animation: "popIn 240ms cubic-bezier(.2,.9,.3,1.4)" }}>
                <div className="display-x" style={{ fontSize: 11, color: "var(--acc)" }}>PULLED · {universe.tag}</div>
                <div className="display" style={{ fontSize: 26, lineHeight: 1.05, marginTop: 2 }}>
                  {draft.currentChar.name.toUpperCase()}
                </div>
              </div>
            </div>
          )}

          <div style={{
            position: "absolute", left: -4, right: -4, top: "50%", height: 50, marginTop: -25,
            border: "1px solid var(--acc)", opacity: (spinning && reelChars.length > 0) ? 0.6 : 0, pointerEvents: "none",
            boxShadow: "0 0 18px color-mix(in oklab, var(--acc) 50%, transparent)",
          }} />
        </div>

        <div style={{ marginTop: 14, display: "flex", justifyContent: "space-between", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.14em" }}>
          <div>
            <div style={{ color: "var(--ink-3)" }}>{t('turn', lang)}</div>
            <div style={{ color: "var(--ink-0)", fontWeight: 600 }}>{turnLabel}</div>
          </div>
          <div>
            <div style={{ color: "var(--ink-3)" }}>{t('skipsLeft', lang)}</div>
            <div style={{ color: "var(--ink-0)", fontWeight: 600 }}>{skipsLeft} / 1</div>
          </div>
          <div>
            <div style={{ color: "var(--ink-3)" }}>{t('picks', lang)}</div>
            <div style={{ color: "var(--ink-0)", fontWeight: 600 }}>{draft.history.length} / {totalPositions * 2}</div>
          </div>
        </div>
      </div>

      {/* Action buttons */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
        <ActionBtn icon="dice" label={t('gacha', lang)} hint={codeLabel(keybinds.gacha)} primary
          onClick={onSpin} disabled={!!draft.currentChar || spinning || switchActive} fullWidth />
        <ActionBtn icon="skip" label={t('skip', lang)} hint={codeLabel(keybinds.skip)}
          onClick={onSkip} disabled={!draft.currentChar || skipsLeft <= 0} />
        <ActionBtn icon="arrow" label={t('pass', lang)} hint={codeLabel(keybinds.pass)}
          onClick={onPass} disabled={!!draft.currentChar || switchActive} />
        <ActionBtn icon="swap" label={t('switch', lang)} hint={codeLabel(keybinds.switch)}
          onClick={onSwitch} disabled={!!draft.currentChar || switchActive || myFilled < 2} />
        <ActionBtn icon="undo" label={t('undo', lang)} hint={codeLabel(keybinds.undo)}
          onClick={onUndo} disabled={!draft.undoAvailable} />
      </div>

      <button
        className="btn btn-primary"
        disabled={!ready}
        onClick={onReady}
        style={{ height: 64, fontSize: 16 }}
      >
        <Icon name="check" size={18} /> {t('readyLock', lang)}
        <span className="kbd">{codeLabel(keybinds.confirm)}</span>
      </button>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 8 }}>
        <button className="btn btn-ghost" onClick={onPlayers} style={{ height: 42, fontSize: 11 }}>
          <Icon name="user" size={14} /> {t('players', lang)}
        </button>
        <button className="btn btn-ghost" onClick={onSettings} style={{ height: 42, fontSize: 11 }}>
          <Icon name="gear" size={14} /> {t('settings', lang)}
        </button>
        <button className="btn btn-ghost" onClick={onMenu} style={{ height: 42, fontSize: 11 }}>
          <Icon name="undo" size={14} /> {t('menu', lang)}
        </button>
      </div>

    </div>
  )
}

/* ===================================================== */
/* SCREEN 3 — DRAFT BOARD (main export)                  */
/* ===================================================== */
const DraftScreen = ({
  universe, p1, p2, draft, onFinish, mode,
  onGacha, onAssign, onSkip, onUndo, onSwitch, imgUrl,
  onMenu, onPlayers, onPass, version, uiVolume, sfxVolume, musicVolume, lang,
  onUiVolumeChange, onSfxVolumeChange, onMusicVolumeChange, quality, onQualityChange, onLangChange,
  keybinds, onKeybindsChange,
}) => {
  const positions = universe.positions
  const [settingsOpen, setSettingsOpen] = useState(false)

  const filledP1 = draft.assignments.filter(a => a.p1 !== null).length
  const filledP2 = draft.assignments.filter(a => a.p2 !== null).length
  const totalPicks = filledP1 + filledP2
  const allDone = totalPicks === positions.length * 2

  const [spinning, setSpinning] = useState(false)
  const [reelChars, setReelChars] = useState([])

  const [hakiActive, setHakiActive] = useState(false)

  const prevSpinning = useRef(false)
  useEffect(() => {
    if (prevSpinning.current && !spinning) {
      if (draft?.currentChar?.ext === "gif" && universe.id === "onepiece") {
        setHakiActive(true)
      }
      const sfx = CHAR_SFX[draft?.currentChar?.name]
      if (sfx) sfx()
    }
    prevSpinning.current = spinning
  }, [spinning, draft?.currentChar?.ext, draft?.currentChar?.name])

  const [switchMode, setSwitchMode] = useState(false)
  const [switchFirst, setSwitchFirst] = useState(null)

  const spin = async () => {
    if (draft.currentChar || spinning) return
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
        if (!draft.currentChar && !spinning && !switchMode) { e.preventDefault(); spin() }
      } else if (e.code === keybinds.skip) {
        if (draft.currentChar && skipsLeft > 0) { e.preventDefault(); onSkip() }
      } else if (e.code === keybinds.pass) {
        if (!draft.currentChar && !switchMode) { e.preventDefault(); handlePass() }
      } else if (e.code === keybinds.switch) {
        if (!draft.currentChar && !switchMode && myFilled >= 2) { e.preventDefault(); handleSwitch() }
      } else if (e.code === keybinds.undo) {
        if (draft.undoAvailable) { e.preventDefault(); onUndo() }
      } else if (e.code === keybinds.confirm) {
        if (allDone) { e.preventDefault(); onFinish() }
      }
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [keybinds, draft, spinning, switchMode, settingsOpen, filledP1, filledP2, allDone])

  return (
    <div className={`stage acc-${universe.id}`} data-screen-label="03 Draft">
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
        active={draft.turn === "p1"} skips={draft.skipsP1} lang={lang}
      />
      <PlayerBanner
        side="right" player={p2} filled={filledP2} total={positions.length}
        active={draft.turn === "p2"} skips={draft.skipsP2} lang={lang}
      />

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
          enabled={!!draft.currentChar && !switchMode}
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

      {/* Haki cinematic overlay */}
      {hakiActive && <HakiOverlay sfxVolume={sfxVolume} onComplete={() => setHakiActive(false)} />}
    </div>
  )
}

export default DraftScreen
