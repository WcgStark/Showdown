import { useState } from 'react'
import { Atmos, AppBar, Icon, CornerTicks } from '../components'
import { t } from '../i18n'

const LANDSCAPE = {
  onepiece:   "./landscape/landscape%20onepiece.jpg",
  naruto:     "./landscape/landscape%20naruto.jpg",
  bleach:     "./landscape/landscape%20bleach.jpg",
  invincible: "./landscape/landscape%20invincible.jpg",
}

const UniverseCard = ({ universe, active, onHover, onClick }) => {
  const accStyle = { "--acc": universe.accent }
  const landscapeSrc = LANDSCAPE[universe.id]
  return (
    <div
      onMouseEnter={onHover}
      onClick={onClick}
      className={`panel scanlines ${active ? "ring-on" : ""}`}
      style={{
        ...accStyle,
        position: "relative",
        cursor: "pointer",
        overflow: "hidden",
        transition: "transform 200ms ease",
        transform: active ? "translateY(-4px)" : "none",
      }}
    >
      <CornerTicks />
      {landscapeSrc && (
        <img
          src={landscapeSrc}
          alt=""
          style={{
            position: "absolute", inset: 0,
            width: "100%", height: "100%",
            objectFit: "cover", objectPosition: "center top",
            pointerEvents: "none",
          }}
        />
      )}
      <div style={{
        position: "absolute", inset: 0,
        background:
          `linear-gradient(180deg, rgba(7,8,12,0.35) 0%, rgba(7,8,12,0.5) 50%, rgba(7,8,12,0.95) 100%)`,
      }} />

      <div style={{ position: "absolute", bottom: 28, left: 28, right: 28 }}>
        <div className="display" style={{ fontSize: 56, lineHeight: 0.95, marginBottom: 0 }}>
          {universe.name}
        </div>
        {active && (
          <div style={{
            display: "flex", alignItems: "center", gap: 8, marginTop: 12,
            color: "var(--acc)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.2em",
          }}>
            <span style={{ width: 6, height: 6, background: "var(--acc)", boxShadow: "0 0 8px var(--acc)" }} />
            SELECTED
          </div>
        )}
      </div>
    </div>
  )
}

const SettingsModal = ({ volume, onVolumeChange, quality, onQualityChange, lang, onLangChange, onClose }) => (
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

const LobbyScreen = ({ universes, onSelect, selectedId, setSelectedId, version, volume, onVolumeChange, quality, onQualityChange, lang, onLangChange }) => {
  const [settingsOpen, setSettingsOpen] = useState(false)
  const sel = universes.find(u => u.id === selectedId) || universes[0]
  return (
    <div className={`stage acc-${sel.id}`} data-screen-label="01 Lobby">
      <Atmos />
      <AppBar phase="LOBBY" version={version} />

      {/* Title block */}
      <div style={{
        position: "absolute", top: 110, left: 0, right: 0,
        textAlign: "center", zIndex: 3,
      }}>
        <div className="label" style={{ justifyContent: "center", display: "inline-flex" }}>
          {t('step1', lang)}
        </div>
        <h1 className="display" style={{
          fontSize: 96, lineHeight: 0.95, margin: "16px 0 6px",
          letterSpacing: "0.04em", fontWeight: 700,
          color: "transparent",
          WebkitTextStroke: "1.5px var(--acc)",
          textShadow: "0 0 24px color-mix(in oklab, var(--acc) 50%, transparent)",
        }}>
          SHOWDOWN
        </h1>
      </div>

      {/* Card grid */}
      <div style={{
        position: "absolute", top: 340, left: 120, right: 120, bottom: 200,
        display: "grid", gridTemplateColumns: "1fr 1fr", gridTemplateRows: "1fr 1fr",
        gap: 28, zIndex: 3,
      }}>
        {universes.map(u => (
          <UniverseCard
            key={u.id}
            universe={u}
            active={u.id === sel.id}
            onHover={() => setSelectedId(u.id)}
            onClick={() => onSelect(u.id)}
          />
        ))}
      </div>

      {/* Footer bar */}
      <div style={{
        position: "absolute", bottom: 60, left: 0, right: 0, zIndex: 3,
        display: "flex", justifyContent: "space-between", alignItems: "center", padding: "0 64px",
      }}>
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          <span className="label">{t('currentSelection', lang)}</span>
          <span className="display" style={{ fontSize: 28, color: "var(--ink-0)" }}>
            {sel.name} <span style={{ color: "var(--ink-3)", fontWeight: 500 }}>/ {sel.codename}</span>
          </span>
        </div>
        <div style={{ display: "flex", gap: 12 }}>
          <button className="btn btn-ghost" onClick={() => setSettingsOpen(true)}>
            {t('settings', lang)}
          </button>
          <button className="btn btn-primary" onClick={() => onSelect(sel.id)}>
            {t('confirmSelection', lang)} <Icon name="arrow" />
            <span className="kbd">ENTER</span>
          </button>
        </div>
      </div>

      {settingsOpen && (
        <SettingsModal
          volume={volume}
          onVolumeChange={onVolumeChange}
          quality={quality}
          onQualityChange={onQualityChange}
          lang={lang}
          onLangChange={onLangChange}
          onClose={() => setSettingsOpen(false)}
        />
      )}
    </div>
  )
}

export default LobbyScreen
