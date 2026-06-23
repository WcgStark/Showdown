import { useState, useEffect } from 'react'
import { Atmos, AppBar, Icon, CornerTicks, SettingsModal } from '../components'
import { t } from '../i18n'
import { codeLabel } from '../keybinds'
import { playUi, playUiHover } from '../sounds'

const LANDSCAPE = {
  onepiece:   "./landscape/landscape%20onepiece.jpg",
  naruto:     "./landscape/landscape%20naruto.jpg",
  bleach:     "./landscape/landscape%20bleach.jpg",
  invincible: "./landscape/landscape%20invincible.jpg",
  jojo:       "./landscape/landscape%20jojo.jpg",
  jujutsu:    "./landscape/landscape%20jujutsu.jpg",
  dragonball: "./landscape/landscape%20dragonball.jpg",
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

const PAGE_SIZE = 6

const LobbyScreen =({ universes, onSelect, selectedId, setSelectedId, version, uiVolume, onUiVolumeChange, sfxVolume, onSfxVolumeChange, musicVolume, onMusicVolumeChange, quality, onQualityChange, lang, onLangChange, keybinds, onKeybindsChange }) => {
  const [settingsOpen, setSettingsOpen] = useState(false)
  const [page, setPage] = useState(0)
  const sel = universes.find(u => u.id === selectedId) || universes[0]

  const pageCount = Math.max(1, Math.ceil(universes.length / PAGE_SIZE))
  const safePage = Math.min(page, pageCount - 1)
  const visible = universes.slice(safePage * PAGE_SIZE, safePage * PAGE_SIZE + PAGE_SIZE)
  // When paginated, keep the full 3×2 page layout so a lone card (e.g. Dragon
  // Ball on its own page) sits in the top-left slot at the same size as the
  // others, instead of stretching to fill the whole grid.
  const cols = pageCount > 1 ? 3 : (universes.length <= 4 ? 2 : 3)
  const rows = pageCount > 1 ? Math.ceil(PAGE_SIZE / cols) : Math.ceil(universes.length / cols)

  // Returns true if the page actually changed. Does NOT play the UI sound: a
  // global mousedown listener (sounds.js) already fires playUi() for every
  // <button> click, so the arrow buttons would double up. Keyboard nav plays it
  // explicitly below.
  const goPage = delta => {
    const next = Math.min(Math.max(safePage + delta, 0), pageCount - 1)
    if (next !== safePage) { setPage(next); return true }
    return false
  }

  // Preload every landscape so flipping pages shows images instantly (no decode
  // flash on remount).
  useEffect(() => {
    Object.values(LANDSCAPE).forEach(src => { const img = new Image(); img.src = src })
  }, [])

  // Keyboard: confirm selection / close settings / page nav
  useEffect(() => {
    const onKey = e => {
      if (settingsOpen) {
        if (e.code === keybinds.back) { e.preventDefault(); setSettingsOpen(false) }
        return
      }
      if (e.code === keybinds.confirm) { e.preventDefault(); onSelect(sel.id) }
      else if (e.code === "ArrowRight") { e.preventDefault(); if (goPage(1)) playUi() }
      else if (e.code === "ArrowLeft") { e.preventDefault(); if (goPage(-1)) playUi() }
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [settingsOpen, keybinds, sel.id, onSelect, safePage, pageCount])

  return (
    <div className={`stage acc-${sel.id}`} data-screen-label="01 Lobby">
      <Atmos />
      <AppBar phase="LOBBY" version={version} lang={lang} />

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

      {/* Card grid — paginated, 6 per page (kept at a fixed 3×2 layout) */}
      <div style={{
        position: "absolute", top: 340, left: 120, right: 120, bottom: 200,
        display: "grid",
        gridTemplateColumns: `repeat(${cols}, 1fr)`,
        gridTemplateRows: `repeat(${rows}, 1fr)`,
        gap: 28, zIndex: 3,
      }}>
        {visible.map(u => (
          <UniverseCard
            key={u.id}
            universe={u}
            active={u.id === sel.id}
            onHover={() => { playUiHover(); setSelectedId(u.id) }}
            onClick={() => { playUi(); onSelect(u.id) }}
          />
        ))}
      </div>

      {/* Page navigation arrows */}
      {pageCount > 1 && (
        <>
          {safePage > 0 && (
            <button
              className="btn btn-ghost"
              onMouseEnter={playUiHover}
              onClick={() => goPage(-1)}
              aria-label="Previous page"
              style={{
                position: "absolute", left: 36, top: "52%", transform: "translateY(-50%)",
                zIndex: 4, width: 56, height: 56, borderRadius: "50%",
                display: "grid", placeItems: "center", padding: 0,
              }}
            >
              <span style={{ transform: "rotate(180deg)", display: "inline-flex" }}>
                <Icon name="arrow" size={22} />
              </span>
            </button>
          )}
          {safePage < pageCount - 1 && (
            <button
              className="btn btn-ghost"
              onMouseEnter={playUiHover}
              onClick={() => goPage(1)}
              aria-label="Next page"
              style={{
                position: "absolute", right: 36, top: "52%", transform: "translateY(-50%)",
                zIndex: 4, width: 56, height: 56, borderRadius: "50%",
                display: "grid", placeItems: "center", padding: 0,
              }}
            >
              <Icon name="arrow" size={22} />
            </button>
          )}
          {/* Page dots */}
          <div style={{
            position: "absolute", bottom: 150, left: 0, right: 0, zIndex: 4,
            display: "flex", justifyContent: "center", gap: 10,
          }}>
            {Array.from({ length: pageCount }).map((_, i) => (
              <span
                key={i}
                onClick={() => { playUi(); setPage(i) }}
                style={{
                  width: 8, height: 8, borderRadius: "50%", cursor: "pointer",
                  background: i === safePage ? "var(--acc)" : "var(--ink-3)",
                  boxShadow: i === safePage ? "0 0 8px var(--acc)" : "none",
                  transition: "background 150ms ease",
                }}
              />
            ))}
          </div>
        </>
      )}

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
            <span className="kbd">{codeLabel(keybinds.confirm)}</span>
          </button>
        </div>
      </div>

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
    </div>
  )
}

export default LobbyScreen
