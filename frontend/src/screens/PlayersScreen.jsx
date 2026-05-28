import { useEffect } from 'react'
import { Atmos, AppBar, Icon, CornerTicks } from '../components'
import { t } from '../i18n'
import { codeLabel } from '../keybinds'

const QUICK_NAMES_FALLBACK = ["ALEX", "RYU", "MIKA", "JIN", "NOVA", "ZED", "KIRA", "OBI"]

const PlayerCard = ({ side, value, setValue, align, quickNames, lang }) => (
  <div className="panel panel-tagged" style={{ position: "relative", padding: 28, display: "flex", flexDirection: "column", justifyContent: "space-between", overflow: "hidden" }}>
    <CornerTicks />
    {/* background portrait */}
    <div style={{
      position: "absolute", inset: 0,
      background:
        `linear-gradient(${align === "right" ? "90deg" : "270deg"}, rgba(7,8,12,0.95) 0%, rgba(7,8,12,0.3) 70%),
         radial-gradient(40% 60% at ${align === "right" ? "80%" : "20%"} 50%, color-mix(in oklab, var(--acc) 24%, transparent), transparent 70%)`,
      pointerEvents: "none",
    }} />
    {/* side label */}
    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", position: "relative" }}>
      <div className="display-x" style={{ fontSize: 16, color: "var(--acc)" }}>
        PLAYER · {side}
      </div>
      <div style={{ fontFamily: "var(--f-mono)", fontSize: 11, color: "var(--ink-3)", letterSpacing: "0.18em" }}>
        SLOT {side === "P1" ? "01" : "02"}
      </div>
    </div>

    {/* input */}
    <div style={{ position: "relative" }}>
      <div style={{ color: "var(--ink-3)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.18em", marginBottom: 8 }}>
        {t('enterCallsign', lang)}
      </div>
      <input
        value={value}
        onChange={e => setValue(e.target.value.slice(0, 14).toUpperCase())}
        placeholder={t('typeName', lang)}
        style={{
          width: "100%",
          background: "transparent", border: 0, borderBottom: "2px solid var(--acc)",
          color: "var(--ink-0)", fontFamily: "var(--f-display)",
          fontSize: 72, fontWeight: 700, letterSpacing: "0.04em",
          padding: "10px 0", outline: "none", textTransform: "uppercase",
        }}
      />
      <div style={{ display: "flex", justifyContent: "space-between", color: "var(--ink-3)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.14em", marginTop: 6 }}>
        <span>{t('maxChars', lang)}</span>
        <span>{value.length} / 14</span>
      </div>
    </div>

    {/* quick names */}
    <div style={{ position: "relative" }}>
      <div className="label" style={{ marginBottom: 10 }}>{t('quickNames', lang)}</div>
      <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
        {(quickNames || QUICK_NAMES_FALLBACK).map(n => (
          <button key={n} className="chip" onClick={() => setValue(n)}>{n}</button>
        ))}
        <button className="chip" onClick={() => setValue("")}>
          <Icon name="cross" size={10} /> CLEAR
        </button>
      </div>
    </div>
  </div>
)

const PlayersScreen = ({ universe, mode, setMode, p1, p2, setP1, setP2, onBack, onStart, quickNames, version, lang, keybinds }) => {
  const resolvedQuickNames = (quickNames && quickNames.length)
    ? quickNames.map(n => n.toUpperCase())
    : QUICK_NAMES_FALLBACK
  const canStart = p1.trim() && p2.trim()

  // Keyboard: back / enter the draft
  useEffect(() => {
    const onKey = e => {
      // don't hijack typing keys while a name field is focused
      const typing = e.target?.tagName === "INPUT" && (e.code.startsWith("Key") || e.code.startsWith("Digit"))
      if (typing) return
      if (e.code === keybinds.back) { e.preventDefault(); onBack() }
      else if (e.code === keybinds.confirm && canStart) { e.preventDefault(); onStart() }
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [keybinds, canStart, onBack, onStart])

  return (
    <div className={`stage acc-${universe.id}`} data-screen-label="02 Players">
      <Atmos particles={false} />
      <AppBar phase="ROSTER" universe={universe} mode={mode} step="02 / 03" version={version} lang={lang} />

      <div style={{ position: "absolute", top: 110, left: 0, right: 0, textAlign: "center" }}>
        <div className="label" style={{ justifyContent: "center", display: "inline-flex" }}>
          {t('step2', lang)}
        </div>
        <h1 className="display" style={{ fontSize: 64, margin: "12px 0 4px", letterSpacing: "0.04em" }}>
          {t('whoDrafting', lang)}
        </h1>
        <div style={{ color: "var(--ink-2)", fontFamily: "var(--f-mono)", fontSize: 13, letterSpacing: "0.18em", textTransform: "uppercase" }}>
          {universe.tag} · {universe.name.toUpperCase()}
        </div>
      </div>

      {/* The match-up */}
      <div style={{
        position: "absolute", top: 280, left: 120, right: 120, height: 460,
        display: "grid", gridTemplateColumns: "1fr 200px 1fr", gap: 28, alignItems: "stretch",
      }}>
        <PlayerCard side="P1" value={p1} setValue={setP1} accent="var(--acc)" align="right" quickNames={resolvedQuickNames} lang={lang} />

        <div style={{ display: "grid", placeItems: "center", position: "relative" }}>
          {/* big VS */}
          <div style={{ position: "relative", textAlign: "center" }}>
            <div style={{
              position: "absolute", inset: -40,
              border: "1px solid var(--line-2)",
              transform: "rotate(45deg)",
              opacity: 0.3,
            }} />
            <div style={{
              position: "absolute", inset: -24,
              border: "1px solid var(--acc-line)",
              transform: "rotate(45deg)",
              boxShadow: "0 0 60px color-mix(in oklab, var(--acc) 35%, transparent)",
            }} />
            <div className="display" style={{
              fontSize: 140, lineHeight: 1, color: "var(--ink-0)",
              textShadow: "0 0 40px color-mix(in oklab, var(--acc) 60%, transparent)",
              fontWeight: 700,
            }}>
              VS
            </div>
          </div>
        </div>

        <PlayerCard side="P2" value={p2} setValue={setP2} accent="var(--acc)" align="left" quickNames={resolvedQuickNames} lang={lang} />
      </div>

      {/* Mode selector */}
      <div style={{
        position: "absolute", left: 120, right: 120, top: 780,
        display: "flex", flexDirection: "column", alignItems: "center", gap: 16,
      }}>
        <span className="label">{t('matchFormat', lang)}</span>
        <div className="panel panel-tagged" style={{ display: "inline-flex", padding: 4, gap: 4 }}>
          {(universe.filters || []).map(f => {
            const on = mode === f.key
            const mainName = f.label.replace(/[^a-zA-ZÀ-ÿ\s(]/g, '').split('(')[0].trim().toUpperCase()
            const descPart = (f.label.match(/\(([^)]+)\)/) || [])[1] || ''
            return (
              <button key={f.key} onClick={() => setMode(f.key)}
                style={{
                  padding: "14px 28px", background: on ? "var(--acc-soft)" : "transparent",
                  border: "1px solid", borderColor: on ? "var(--acc)" : "transparent",
                  color: on ? "var(--ink-0)" : "var(--ink-2)",
                  cursor: "pointer", fontFamily: "var(--f-display)",
                  letterSpacing: "0.14em", textTransform: "uppercase",
                  display: "flex", flexDirection: "column", alignItems: "flex-start", gap: 2,
                  minWidth: 160,
                  boxShadow: on ? "inset 0 0 0 1px color-mix(in oklab, var(--acc) 25%, transparent)" : "none",
                }}>
                <span style={{ fontSize: 14, fontWeight: 700 }}>{mainName}</span>
                <span style={{ fontSize: 10, color: "var(--ink-3)", fontFamily: "var(--f-mono)", letterSpacing: "0.16em" }}>{descPart}</span>
              </button>
            )
          })}
        </div>
      </div>

      {/* Footer */}
      <div style={{
        position: "absolute", bottom: 60, left: 64, right: 64, zIndex: 3,
        display: "flex", justifyContent: "space-between", alignItems: "center",
      }}>
        <button className="btn btn-ghost" onClick={onBack}>
          <Icon name="undo" /> {t('back', lang)}
          <span className="kbd">{codeLabel(keybinds.back)}</span>
        </button>
        <button className="btn btn-primary" onClick={onStart} disabled={!canStart}>
          {t('enterDraft', lang)} <Icon name="arrow" />
          <span className="kbd">{codeLabel(keybinds.confirm)}</span>
        </button>
      </div>
    </div>
  )
}

export default PlayersScreen
