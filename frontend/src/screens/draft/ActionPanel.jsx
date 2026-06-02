import { Icon, CornerTicks } from '../../components'
import { t } from '../../i18n'
import { codeLabel } from '../../keybinds'

/* ── Action button ───────────────────────────────────────────────────────── */
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

/* ── Right action panel (current pick + controls) ────────────────────────── */
const ActionPanel = ({
  universe, draft, spinning, shake, reelChars, onSpin, onSkip, onUndo, onSwitch, onReady,
  ready, imgUrl, onMenu, onPlayers, onPass, onSettings, switchActive, lang, keybinds,
}) => {
  // When a GIF is pulled the whole stage shakes; counter-animate this portrait
  // so the pulled character stays still in the middle of the rattle.
  const cancelShake = shake && draft.currentChar?.ext === "gif"
  const turnLabel = draft.turn === "p1" ? "PLAYER 01" : "PLAYER 02"
  const skipsLeft = draft.turn === "p1" ? draft.skipsP1 : draft.skipsP2
  const myFilled = draft.turn === "p1"
    ? draft.assignments.filter(a => a.p1 !== null).length
    : draft.assignments.filter(a => a.p2 !== null).length
  const totalPositions = draft.assignments.length

  // ARENA mode: block the character gacha until the arena is rolled.
  const arenaPending = draft.arenaEnabled && !draft.arena

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
        <div className={cancelShake ? "shake-cancel" : undefined} style={{ position: "relative", marginTop: 14, height: 280, overflow: "hidden" }}>
          {spinning && reelChars.length > 0 && (
            <div style={{ position: "absolute", inset: 0, background: "linear-gradient(180deg, rgba(7,8,12,1) 0%, transparent 20%, transparent 80%, rgba(7,8,12,1) 100%)", zIndex: 2, pointerEvents: "none" }} />
          )}
          <div style={{ position: "absolute", inset: 0, background: "repeating-linear-gradient(135deg, rgba(255,255,255,0.025) 0 10px, transparent 10px 20px), var(--bg-1)" }} />

          {!spinning && !draft.currentChar && (
            <div style={{ position: "absolute", inset: 0, display: "grid", placeItems: "center", color: arenaPending ? "var(--acc)" : "var(--ink-3)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.2em", textAlign: "center", padding: 20 }}>
              {arenaPending ? (
                <span>⚡ {t('arenaFirst', lang)}</span>
              ) : (
                <>
                  {t('pressGacha', lang)}<br />
                  <span style={{ color: "var(--ink-4)", marginTop: 8, display: "inline-block" }}>{t('noPickActive', lang)}</span>
                </>
              )}
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
          onClick={onSpin} disabled={!!draft.currentChar || spinning || switchActive || arenaPending} fullWidth />
        <ActionBtn icon="skip" label={t('skip', lang)} hint={codeLabel(keybinds.skip)}
          onClick={onSkip} disabled={!draft.currentChar || skipsLeft <= 0 || spinning} />
        <ActionBtn icon="arrow" label={t('pass', lang)} hint={codeLabel(keybinds.pass)}
          onClick={onPass} disabled={!!draft.currentChar || switchActive || spinning || myFilled < totalPositions} />
        <ActionBtn icon="swap" label={t('switch', lang)} hint={codeLabel(keybinds.switch)}
          onClick={onSwitch} disabled={!!draft.currentChar || switchActive || myFilled < 2 || spinning} />
        <ActionBtn icon="undo" label={t('undo', lang)} hint={codeLabel(keybinds.undo)}
          onClick={onUndo} disabled={!draft.undoAvailable || spinning} />
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

export default ActionPanel
