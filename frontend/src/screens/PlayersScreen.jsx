import { useState, useEffect, useRef } from 'react'
import { Atmos, AppBar, Icon, CornerTicks } from '../components'
import { t } from '../i18n'
import { codeLabel } from '../keybinds'

const QUICK_NAMES_FALLBACK = ["ALEX", "RYU", "MIKA", "JIN", "NOVA", "ZED", "KIRA", "OBI"]
const IMG_SIZE   = 110   // avatar diameter in the picker grid
const IMG_GAP    = 12    // gap between avatars
const SCROLL_AMT = (IMG_SIZE + IMG_GAP) * 4  // scroll 4 images at a time

const pfpUrl = path =>
  path ? `./pfp/${path.split('/').map(encodeURIComponent).join('/')}` : null

/* ── Arrow button (Crunchyroll style) ───────────────────────────────────── */
const ArrowBtn = ({ dir, onClick }) => (
  <button
    onClick={onClick}
    style={{
      position: "absolute",
      [dir === "left" ? "left" : "right"]: -20,
      top: "50%", transform: "translateY(-50%)",
      width: 38, height: 38, borderRadius: "50%", zIndex: 2,
      background: "var(--bg-elev)", border: "1px solid var(--acc-line)",
      display: "grid", placeItems: "center",
      cursor: "pointer", color: "var(--ink-0)",
      fontSize: 22, lineHeight: 1,
      boxShadow: "0 4px 20px rgba(0,0,0,0.7)",
    }}
  >
    {dir === "left" ? "‹" : "›"}
  </button>
)

/* ── Category row with arrow navigation ─────────────────────────────────── */
const CategoryRow = ({ cat, tempPfp, setTempPfp }) => {
  const scrollRef  = useRef(null)
  const [canLeft,  setCanLeft]  = useState(false)
  const [canRight, setCanRight] = useState(false)

  const sync = () => {
    const el = scrollRef.current
    if (!el) return
    setCanLeft(el.scrollLeft > 4)
    setCanRight(el.scrollLeft < el.scrollWidth - el.clientWidth - 4)
  }

  useEffect(() => {
    sync()
    const timer = setTimeout(sync, 120)
    return () => clearTimeout(timer)
  }, [cat.files.length])

  const scroll = dir => {
    scrollRef.current?.scrollBy({ left: dir * SCROLL_AMT, behavior: "smooth" })
    setTimeout(sync, 380)
  }

  return (
    <div style={{ position: "relative" }}>
      {/* overflow:hidden wrapper hides the scrollbar (paddingBottom trick) */}
      <div style={{ overflow: "hidden" }}>
        <div
          ref={scrollRef}
          onScroll={sync}
          style={{
            display: "flex", gap: IMG_GAP,
            overflowX: "scroll",
            paddingBottom: 20, marginBottom: -20,
          }}
        >
          {cat.files.map(f => {
            const path = cat.name ? `${cat.name}/${f}` : f
            const selected = tempPfp === path
            return (
              <button
                key={path}
                onClick={() => setTempPfp(selected ? null : path)}
                style={{
                  width: IMG_SIZE, height: IMG_SIZE,
                  borderRadius: "50%", overflow: "hidden",
                  border: `2px solid ${selected ? "var(--acc)" : "transparent"}`,
                  padding: 0, cursor: "pointer", flexShrink: 0,
                  background: "var(--bg-1)",
                  outline: selected ? "none" : "1px solid var(--line)",
                  boxShadow: selected
                    ? "0 0 0 2px var(--acc), 0 0 20px -2px color-mix(in oklab, var(--acc) 70%, transparent)"
                    : "none",
                  transition: "border-color 120ms, box-shadow 120ms",
                }}
              >
                <img
                  src={pfpUrl(path)}
                  style={{ width: "100%", height: "100%", objectFit: "cover" }}
                  alt=""
                  onError={e => { e.currentTarget.style.display = "none" }}
                />
              </button>
            )
          })}
        </div>
      </div>

      {canLeft  && <ArrowBtn dir="left"  onClick={() => scroll(-1)} />}
      {canRight && <ArrowBtn dir="right" onClick={() => scroll(1)}  />}
    </div>
  )
}

/* ── Avatar Picker Modal ─────────────────────────────────────────────────── */
const AvatarPickerModal = ({ pfpList, tempPfp, setTempPfp, onCancel, onSave, lang }) => (
  <div style={{
    position: "absolute", inset: 0, zIndex: 300,
    background: "rgba(0,0,0,0.88)",
    display: "flex", alignItems: "center", justifyContent: "center",
  }}>
    <div style={{
      width: 820, maxHeight: 700,
      background: "var(--bg-elev)", border: "1px solid var(--acc-line)",
      display: "flex", flexDirection: "column",
      boxShadow: "0 32px 100px rgba(0,0,0,0.9)",
      position: "relative",
    }}>
      {/* Close */}
      <button
        onClick={onCancel}
        style={{
          position: "absolute", top: 16, right: 16, zIndex: 1,
          background: "none", border: "none", color: "var(--ink-2)", cursor: "pointer",
          fontSize: 18, padding: "4px 8px", lineHeight: 1, fontFamily: "var(--f-display)",
        }}
      >✕</button>

      {/* Header */}
      <div style={{
        padding: "28px 40px 24px", display: "flex", gap: 24, alignItems: "flex-start",
        borderBottom: "1px solid var(--line)", flexShrink: 0,
      }}>
        <div style={{
          width: 88, height: 88, borderRadius: "50%", overflow: "hidden", flexShrink: 0,
          border: `2px solid ${tempPfp ? "var(--acc)" : "var(--line)"}`,
          background: "var(--bg-1)", display: "grid", placeItems: "center",
          boxShadow: tempPfp ? "0 0 24px -4px color-mix(in oklab, var(--acc) 70%, transparent)" : "none",
          transition: "border-color 200ms, box-shadow 200ms",
        }}>
          {tempPfp
            ? <img src={pfpUrl(tempPfp)} style={{ width: "100%", height: "100%", objectFit: "cover" }} alt="" />
            : <Icon name="user" size={36} />
          }
        </div>

        <div style={{ flex: 1 }}>
          <div className="display" style={{ fontSize: 22, letterSpacing: "0.06em", color: "var(--ink-0)" }}>
            {t('avatarTitle', lang)}
          </div>
          <div style={{ color: "var(--ink-3)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.14em", marginTop: 6, lineHeight: 1.5 }}>
            {t('avatarSubtitle', lang)}
          </div>
          <div style={{ display: "flex", gap: 10, marginTop: 18 }}>
            <button className="btn" onClick={onCancel} style={{ height: 40, fontSize: 12, letterSpacing: "0.14em" }}>
              {t('cancel', lang)}
            </button>
            <button className="btn btn-primary" onClick={onSave} style={{ height: 40, fontSize: 12, letterSpacing: "0.14em" }}>
              {t('save', lang)}
            </button>
          </div>
        </div>
      </div>

      {/* Categories */}
      <div style={{ overflowY: "auto", padding: "24px 40px 36px", flex: 1 }}>
        {pfpList && pfpList.length > 0 ? pfpList.map((cat, ci) => (
          <div key={cat.name || `root-${ci}`} style={{ marginBottom: 32 }}>
            {cat.name && (
              <div style={{
                fontFamily: "var(--f-display)", fontSize: 13, fontWeight: 700,
                letterSpacing: "0.12em", color: "var(--ink-1)",
                marginBottom: 14, textTransform: "uppercase",
              }}>
                {cat.name}
              </div>
            )}
            <CategoryRow cat={cat} tempPfp={tempPfp} setTempPfp={setTempPfp} />
          </div>
        )) : (
          <div style={{
            textAlign: "center", padding: "48px 0",
            color: "var(--ink-3)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.18em",
          }}>
            {t('noAvatars', lang)}
          </div>
        )}
      </div>
    </div>
  </div>
)

/* ── Player Card ─────────────────────────────────────────────────────────── */
const PlayerCard = ({ side, value, setValue, align, quickNames, lang, pfp, onOpenPicker, onClearPfp }) => (
  <div className="panel panel-tagged" style={{ position: "relative", padding: 28, display: "flex", flexDirection: "column", justifyContent: "space-between" }}>
    <CornerTicks />
    <div style={{
      position: "absolute", inset: 0,
      background:
        `linear-gradient(${align === "right" ? "90deg" : "270deg"}, rgba(7,8,12,0.95) 0%, rgba(7,8,12,0.3) 70%),
         radial-gradient(40% 60% at ${align === "right" ? "80%" : "20%"} 50%, color-mix(in oklab, var(--acc) 24%, transparent), transparent 70%)`,
      pointerEvents: "none",
    }} />

    {/* side label */}
    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", position: "relative" }}>
      <div className="display-x" style={{ fontSize: 16, color: "var(--acc)" }}>PLAYER · {side}</div>
      <div style={{ fontFamily: "var(--f-mono)", fontSize: 11, color: "var(--ink-3)", letterSpacing: "0.18em" }}>
        SLOT {side === "P1" ? "01" : "02"}
      </div>
    </div>

    {/* avatar selector */}
    <div style={{ position: "relative", display: "flex", alignItems: "center", gap: 18 }}>
      <div style={{ position: "relative", flexShrink: 0 }}>
        <button
          onClick={onOpenPicker}
          style={{
            width: 90, height: 90, borderRadius: "50%", overflow: "hidden",
            border: `2px solid ${pfp ? "var(--acc)" : "var(--line)"}`,
            background: "var(--bg-1)", cursor: "pointer", padding: 0,
            display: "grid", placeItems: "center",
            boxShadow: pfp ? "0 0 22px -4px color-mix(in oklab, var(--acc) 60%, transparent)" : "none",
            transition: "border-color 200ms, box-shadow 200ms",
          }}
        >
          {pfp
            ? <img src={pfpUrl(pfp)} style={{ width: "100%", height: "100%", objectFit: "cover" }} alt="" />
            : <Icon name="user" size={32} />
          }
        </button>
        {pfp && (
          <button
            onClick={onClearPfp}
            style={{
              position: "absolute", top: 0, right: 0,
              width: 22, height: 22, borderRadius: "50%",
              background: "var(--bg-elev)", border: "1px solid var(--line)",
              display: "grid", placeItems: "center", cursor: "pointer", padding: 0,
              fontSize: 11, color: "var(--ink-2)", lineHeight: 1,
            }}
          >✕</button>
        )}
      </div>
      <div style={{ fontFamily: "var(--f-mono)", fontSize: 10, color: "var(--ink-3)", letterSpacing: "0.18em" }}>
        {t('selectAvatar', lang)}
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

/* ── Players Screen ──────────────────────────────────────────────────────── */
const PlayersScreen = ({ universe, mode, setMode, p1, p2, setP1, setP2, onBack, onStart, quickNames, version, lang, keybinds, p1pfp, setP1pfp, p2pfp, setP2pfp, pfpList }) => {
  const resolvedQuickNames = (quickNames && quickNames.length)
    ? quickNames.map(n => n.toUpperCase())
    : QUICK_NAMES_FALLBACK
  const canStart = p1.trim() && p2.trim()

  const [pickerFor, setPickerFor] = useState(null)
  const [tempPfp,   setTempPfp]   = useState(null)

  const openPicker = side => { setPickerFor(side); setTempPfp(side === "p1" ? p1pfp : p2pfp) }
  const closePicker = () => setPickerFor(null)
  const savePicker  = () => {
    if (pickerFor === "p1") setP1pfp(tempPfp)
    else setP2pfp(tempPfp)
    closePicker()
  }

  useEffect(() => {
    const onKey = e => {
      if (pickerFor) return
      const typing = e.target?.tagName === "INPUT" && (e.code.startsWith("Key") || e.code.startsWith("Digit"))
      if (typing) return
      if (e.code === keybinds.back) { e.preventDefault(); onBack() }
      else if (e.code === keybinds.confirm && canStart) { e.preventDefault(); onStart() }
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [keybinds, canStart, onBack, onStart, pickerFor])

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

      <div style={{
        position: "absolute", top: 260, left: 120, right: 120, height: 480,
        display: "grid", gridTemplateColumns: "1fr 200px 1fr", gap: 28, alignItems: "stretch",
      }}>
        <PlayerCard
          side="P1" value={p1} setValue={setP1} align="right" quickNames={resolvedQuickNames} lang={lang}
          pfp={p1pfp} onOpenPicker={() => openPicker("p1")} onClearPfp={() => setP1pfp(null)}
        />
        <div style={{ display: "grid", placeItems: "center", position: "relative" }}>
          <div style={{ position: "relative", textAlign: "center" }}>
            <div style={{ position: "absolute", inset: -40, border: "1px solid var(--line-2)", transform: "rotate(45deg)", opacity: 0.3 }} />
            <div style={{ position: "absolute", inset: -24, border: "1px solid var(--acc-line)", transform: "rotate(45deg)", boxShadow: "0 0 60px color-mix(in oklab, var(--acc) 35%, transparent)" }} />
            <div className="display" style={{ fontSize: 140, lineHeight: 1, color: "var(--ink-0)", textShadow: "0 0 40px color-mix(in oklab, var(--acc) 60%, transparent)", fontWeight: 700 }}>VS</div>
          </div>
        </div>
        <PlayerCard
          side="P2" value={p2} setValue={setP2} align="left" quickNames={resolvedQuickNames} lang={lang}
          pfp={p2pfp} onOpenPicker={() => openPicker("p2")} onClearPfp={() => setP2pfp(null)}
        />
      </div>

      <div style={{ position: "absolute", left: 120, right: 120, top: 780, display: "flex", flexDirection: "column", alignItems: "center", gap: 16 }}>
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

      <div style={{ position: "absolute", bottom: 60, left: 64, right: 64, zIndex: 3, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <button className="btn btn-ghost" onClick={onBack}>
          <Icon name="undo" /> {t('back', lang)}
          <span className="kbd">{codeLabel(keybinds.back)}</span>
        </button>
        <button className="btn btn-primary" onClick={onStart} disabled={!canStart}>
          {t('enterDraft', lang)} <Icon name="arrow" />
          <span className="kbd">{codeLabel(keybinds.confirm)}</span>
        </button>
      </div>

      {pickerFor && (
        <AvatarPickerModal
          pfpList={pfpList}
          tempPfp={tempPfp}
          setTempPfp={setTempPfp}
          onCancel={closePicker}
          onSave={savePicker}
          lang={lang}
        />
      )}
    </div>
  )
}

export default PlayersScreen
