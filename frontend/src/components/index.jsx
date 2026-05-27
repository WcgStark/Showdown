import { useState, useEffect, useRef, useMemo } from 'react'
import { t } from '../i18n'

/* ============ ICONS (simple, line) ============ */
export const Icon = ({ name, size = 16 }) => {
  const paths = {
    dice: <g><rect x="3" y="3" width="18" height="18" rx="3" /><circle cx="8" cy="8" r="1.2" fill="currentColor" /><circle cx="16" cy="16" r="1.2" fill="currentColor" /><circle cx="12" cy="12" r="1.2" fill="currentColor" /></g>,
    skip: <g><path d="M5 5l8 7-8 7V5z" /><path d="M16 5v14" /></g>,
    swap: <g><path d="M4 7h13M14 4l3 3-3 3" /><path d="M20 17H7M10 14l-3 3 3 3" /></g>,
    undo: <g><path d="M9 7L3 13l6 6" /><path d="M3 13h12a6 6 0 0 1 0 12" /></g>,
    check: <g><path d="M4 12l5 5L20 6" /></g>,
    arrow: <g><path d="M5 12h14M13 6l6 6-6 6" /></g>,
    play: <g><path d="M6 4l14 8L6 20V4z" fill="currentColor" stroke="none" /></g>,
    bolt: <g><path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z" /></g>,
    grid: <g><rect x="3" y="3" width="7" height="7" /><rect x="14" y="3" width="7" height="7" /><rect x="3" y="14" width="7" height="7" /><rect x="14" y="14" width="7" height="7" /></g>,
    user: <g><circle cx="12" cy="8" r="4" /><path d="M4 21c0-4 4-7 8-7s8 3 8 7" /></g>,
    crown: <g><path d="M3 7l4 5 5-7 5 7 4-5v11H3V7z" /></g>,
    timer: <g><circle cx="12" cy="13" r="8" /><path d="M12 8v5l3 2M9 3h6" /></g>,
    target: <g><circle cx="12" cy="12" r="9" /><circle cx="12" cy="12" r="5" /><circle cx="12" cy="12" r="1.3" fill="currentColor" /></g>,
    cross: <g><path d="M6 6l12 12M18 6L6 18" /></g>,
    gear: <g><circle cx="12" cy="12" r="3" /><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" /></g>,
  }
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="square">
      {paths[name] || null}
    </svg>
  )
}

/* ============ Particles ============ */
export const Particles = ({ count = 30 }) => {
  const seeds = useMemo(() => (
    Array.from({ length: count }).map((_, i) => ({
      left: (i * 137.5) % 100,
      top: (i * 53.7 + 30) % 100,
      delay: (i * 0.61) % 18,
      size: 1 + ((i * 7) % 4),
    }))
  ), [count])
  return (
    <div className="particles">
      {seeds.map((p, i) => (
        <span key={i} className="p" style={{
          left: `${p.left}%`, top: `${p.top}%`,
          animationDelay: `-${p.delay}s`,
          width: p.size, height: p.size,
        }} />
      ))}
    </div>
  )
}

/* ============ Background atmosphere ============ */
export const Atmos = ({ glow = true, grid = true, particles = true }) => (
  <>
    {glow && <div className="bg-glow" />}
    {grid && <div className="bg-grid" />}
    {particles && <Particles />}
    <div className="bg-noise" />
    <div className="bg-vignette" />
  </>
)

/* ============ AppBar ============ */
export const AppBar = ({ phase = "LOBBY", universe, mode, step, version }) => (
  <div className="appbar">
    <div className="brand">
      <div className="mark" />
      <span>SHOWDOWN</span>
      <span style={{ color: "var(--ink-3)", letterSpacing: "0.18em", fontWeight: 500, fontSize: 11, marginLeft: 6 }}>
        / Draft v.{version || "?"}
      </span>
    </div>
    <div className="meta">
      <div><span style={{ color: "var(--ink-3)" }}>PHASE</span> <b>{phase}</b></div>
      {universe && <div><span style={{ color: "var(--ink-3)" }}>UNIVERSE</span> <b>{universe.tag}</b></div>}
      {mode && <div><span style={{ color: "var(--ink-3)" }}>MODE</span> <b>{mode}</b></div>}
      {step && <div><span style={{ color: "var(--ink-3)" }}>STEP</span> <b>{step}</b></div>}
    </div>
  </div>
)

/* ============ Image Placeholder ============ */
export const ImgPh = ({ label = "PORTRAIT", aspect = "3 / 4", style }) => (
  <div className="imgph" style={{ aspectRatio: aspect, ...style }}>
    <div className="tag">{label}</div>
    <svg className="crosshair" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1">
      <path d="M12 2v6M12 16v6M2 12h6M16 12h6" />
      <circle cx="12" cy="12" r="3" />
    </svg>
  </div>
)

/* ============ Settings modal (shared) ============ */
export const SettingsModal = ({ volume, onVolumeChange, quality, onQualityChange, lang, onLangChange, onClose }) => (
  <div
    onClick={onClose}
    style={{
      position: "absolute", inset: 0, zIndex: 50,
      background: "rgba(7,8,12,0.85)", backdropFilter: "blur(8px)",
      display: "flex", alignItems: "center", justifyContent: "center",
    }}
  >
    <div
      onClick={e => e.stopPropagation()}
      style={{
        width: 480,
        background: "var(--bg-1)",
        border: "1px solid var(--line-2)",
        borderRadius: 16,
        padding: "36px 40px",
        maxHeight: "90vh",
        overflowY: "auto",
      }}
    >
      {/* Header */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 32 }}>
        <div>
          <div style={{ fontFamily: "var(--f-mono)", fontSize: 10, color: "var(--ink-3)", letterSpacing: "0.2em", marginBottom: 4 }}>
            {t('configuration', lang)}
          </div>
          <div className="display" style={{ fontSize: 32, letterSpacing: "0.06em" }}>{t('settings', lang)}</div>
        </div>
        <button
          onClick={onClose}
          style={{
            background: "var(--bg-glass)", border: "1px solid var(--line)",
            color: "var(--ink-2)", cursor: "pointer",
            width: 36, height: 36, borderRadius: 8,
            fontFamily: "var(--f-mono)", fontSize: 18, lineHeight: 1,
          }}
        >×</button>
      </div>

      {/* Volume */}
      <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="square" style={{ color: "var(--ink-2)" }}>
              <path d="M11 5L6 9H2v6h4l5 4V5z"/>
              <path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
              <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
            </svg>
            <span style={{ fontFamily: "var(--f-mono)", fontSize: 11, color: "var(--ink-2)", letterSpacing: "0.16em" }}>
              {t('audioVolume', lang)}
            </span>
          </div>
          <span style={{ fontFamily: "var(--f-mono)", fontSize: 13, color: "var(--ink-0)", letterSpacing: "0.08em", minWidth: 40, textAlign: "right" }}>
            {Math.round(volume * 100)}%
          </span>
        </div>

        <input
          type="range" min="0" max="1" step="0.05"
          value={volume}
          onChange={e => onVolumeChange(parseFloat(e.target.value))}
          style={{ width: "100%", accentColor: "var(--acc)", cursor: "pointer", height: 4 }}
        />

        <div style={{ display: "flex", justifyContent: "space-between" }}>
          <span style={{ fontFamily: "var(--f-mono)", fontSize: 9, color: "var(--ink-4)", letterSpacing: "0.12em" }}>{t('mute', lang)}</span>
          <span style={{ fontFamily: "var(--f-mono)", fontSize: 9, color: "var(--ink-4)", letterSpacing: "0.12em" }}>{t('max', lang)}</span>
        </div>
      </div>

      {/* Divider */}
      <div style={{ height: 1, background: "var(--line-2)", margin: "28px 0" }} />

      {/* Quality */}
      <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="square" style={{ color: "var(--ink-2)" }}>
            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
          </svg>
          <span style={{ fontFamily: "var(--f-mono)", fontSize: 11, color: "var(--ink-2)", letterSpacing: "0.16em" }}>
            {t('quality', lang)}
          </span>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
          {[
            { id: "rtx",    label: "RTX",    descKey: "rtxDesc"    },
            { id: "potato", label: "POTATO", descKey: "potatoDesc" },
          ].map(opt => (
            <button
              key={opt.id}
              onClick={() => onQualityChange(opt.id)}
              style={{
                padding: "12px 16px",
                background: quality === opt.id ? "color-mix(in oklab, var(--acc) 18%, transparent)" : "var(--bg-glass)",
                border: `1px solid ${quality === opt.id ? "var(--acc)" : "var(--line-2)"}`,
                borderRadius: 8, cursor: "pointer", textAlign: "left", transition: "all 120ms ease",
              }}
            >
              <div style={{ fontFamily: "var(--f-display)", fontWeight: 700, fontSize: 14, color: quality === opt.id ? "var(--acc)" : "var(--ink-1)", letterSpacing: "0.12em", marginBottom: 4 }}>
                {opt.label}
              </div>
              <div style={{ fontFamily: "var(--f-mono)", fontSize: 10, color: "var(--ink-3)", letterSpacing: "0.08em" }}>
                {t(opt.descKey, lang)}
              </div>
            </button>
          ))}
        </div>
      </div>

      {/* Divider */}
      <div style={{ height: 1, background: "var(--line-2)", margin: "28px 0" }} />

      {/* Language */}
      <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="square" style={{ color: "var(--ink-2)" }}>
            <circle cx="12" cy="12" r="10" />
            <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
          </svg>
          <span style={{ fontFamily: "var(--f-mono)", fontSize: 11, color: "var(--ink-2)", letterSpacing: "0.16em" }}>
            {t('language', lang)}
          </span>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
          {[
            { id: "en", labelKey: "langEn", descKey: "langEnDesc" },
            { id: "pt", labelKey: "langPt", descKey: "langPtDesc" },
          ].map(opt => (
            <button
              key={opt.id}
              onClick={() => onLangChange(opt.id)}
              style={{
                padding: "12px 16px",
                background: lang === opt.id ? "color-mix(in oklab, var(--acc) 18%, transparent)" : "var(--bg-glass)",
                border: `1px solid ${lang === opt.id ? "var(--acc)" : "var(--line-2)"}`,
                borderRadius: 8, cursor: "pointer", textAlign: "left", transition: "all 120ms ease",
              }}
            >
              <div style={{ fontFamily: "var(--f-display)", fontWeight: 700, fontSize: 14, color: lang === opt.id ? "var(--acc)" : "var(--ink-1)", letterSpacing: "0.12em", marginBottom: 4 }}>
                {t(opt.labelKey, lang)}
              </div>
              <div style={{ fontFamily: "var(--f-mono)", fontSize: 10, color: "var(--ink-3)", letterSpacing: "0.08em" }}>
                {t(opt.descKey, lang)}
              </div>
            </button>
          ))}
        </div>
      </div>
    </div>
  </div>
)

/* ============ Corner tick marks ============ */
export const CornerTicks = ({ color = "var(--acc)" }) => (
  <>
    {["tl","tr","bl","br"].map(c => (
      <span key={c} style={{
        position: "absolute",
        width: 12, height: 12,
        borderColor: color,
        borderStyle: "solid",
        borderWidth: 0,
        ...(c[0] === "t" ? { top: -1, borderTopWidth: 1 } : { bottom: -1, borderBottomWidth: 1 }),
        ...(c[1] === "l" ? { left: -1, borderLeftWidth: 1 } : { right: -1, borderRightWidth: 1 }),
        pointerEvents: "none",
      }} />
    ))}
  </>
)
