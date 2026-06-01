import { CornerTicks } from '../../components'
import { t } from '../../i18n'

/* ── Arena detail modal ──────────────────────────────────────────────────── */
const ArenaModal = ({ arena, universeId, onClose, lang }) => (
  <div
    onClick={onClose}
    style={{
      position: "absolute", inset: 0, zIndex: 300,
      background: "rgba(0,0,0,0.92)",
      display: "flex", alignItems: "center", justifyContent: "center",
      cursor: "pointer",
    }}
  >
    <div
      onClick={e => e.stopPropagation()}
      style={{
        width: 860, maxHeight: 720,
        background: "var(--bg-elev)", border: "1px solid var(--acc-line)",
        display: "flex", flexDirection: "column",
        boxShadow: "0 32px 100px rgba(0,0,0,0.95)",
        position: "relative", overflow: "hidden",
        cursor: "default",
      }}
    >
      <CornerTicks />

      {/* Header with image */}
      <div style={{ position: "relative", height: 200, flexShrink: 0, overflow: "hidden", background: "var(--bg-1)" }}>
        <img
          src={`./arena/${universeId}/${encodeURIComponent(arena.image)}`}
          alt={arena.name}
          style={{ width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 40%" }}
          onError={e => { e.currentTarget.style.display = "none" }}
        />
        <div style={{ position: "absolute", inset: 0, background: "linear-gradient(180deg, transparent 30%, rgba(7,8,12,0.98) 100%)" }} />
        <div style={{ position: "absolute", bottom: 20, left: 28, right: 60 }}>
          <div style={{ fontFamily: "var(--f-mono)", fontSize: 10, color: "var(--acc)", letterSpacing: "0.22em", marginBottom: 6 }}>
            {t('arenaPart', lang)} {arena.part} · {arena.partName.toUpperCase()}
          </div>
          <div className="display" style={{ fontSize: 30, lineHeight: 1.1, color: "var(--ink-0)" }}>{arena.name}</div>
          <div style={{ fontFamily: "var(--f-mono)", fontSize: 11, color: "var(--ink-3)", marginTop: 4, letterSpacing: "0.1em" }}>{arena.flavor}</div>
        </div>
        <button onClick={onClose} style={{
          position: "absolute", top: 14, right: 14,
          background: "var(--bg-elev)", border: "1px solid var(--line)",
          color: "var(--ink-2)", cursor: "pointer",
          width: 30, height: 30, borderRadius: "50%",
          display: "grid", placeItems: "center", fontSize: 13,
        }}>✕</button>
      </div>

      {/* Body */}
      <div style={{ overflowY: "auto", padding: "20px 28px 28px", flex: 1 }}>
        {/* 3 columns: conditions | buffs | debuffs */}
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 16, marginBottom: 16 }}>
          {/* Conditions */}
          <div>
            <div style={{ fontFamily: "var(--f-mono)", fontSize: 10, fontWeight: 700, letterSpacing: "0.14em", color: "var(--ink-2)", marginBottom: 10, textTransform: "uppercase" }}>
              {t('arenaConditions', lang)}
            </div>
            <div style={{ display: "flex", flexWrap: "wrap", gap: 5 }}>
              {arena.conditions.map((c, i) => (
                <span key={i} style={{
                  fontFamily: "var(--f-mono)", fontSize: 10, padding: "3px 9px",
                  background: "var(--bg-2)", border: "1px solid var(--line)",
                  color: "var(--ink-2)", letterSpacing: "0.06em",
                }}>{c}</span>
              ))}
            </div>
          </div>

          {/* Buffs */}
          <div>
            <div style={{ fontFamily: "var(--f-mono)", fontSize: 10, fontWeight: 700, letterSpacing: "0.14em", color: "#5a9e2f", marginBottom: 10, textTransform: "uppercase" }}>
              ▲ {t('arenaBuffs', lang)}
            </div>
            <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
              {arena.buffs.map((b, i) => (
                <li key={i} style={{ display: "flex", gap: 6, alignItems: "flex-start", fontSize: 11, color: "var(--ink-2)", padding: "4px 0", borderBottom: "1px solid var(--line-2)", lineHeight: 1.45 }}>
                  <span style={{ color: "#5a9e2f", fontSize: 9, marginTop: 3, flexShrink: 0 }}>▲</span>
                  <span>{b}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Debuffs */}
          <div>
            <div style={{ fontFamily: "var(--f-mono)", fontSize: 10, fontWeight: 700, letterSpacing: "0.14em", color: "#c04040", marginBottom: 10, textTransform: "uppercase" }}>
              ▼ {t('arenaDebuffs', lang)}
            </div>
            <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
              {arena.debuffs.map((d, i) => (
                <li key={i} style={{ display: "flex", gap: 6, alignItems: "flex-start", fontSize: 11, color: "var(--ink-2)", padding: "4px 0", borderBottom: "1px solid var(--line-2)", lineHeight: 1.45 }}>
                  <span style={{ color: "#c04040", fontSize: 9, marginTop: 3, flexShrink: 0 }}>▼</span>
                  <span>{d}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Special event */}
        <div style={{
          background: "color-mix(in oklab, var(--acc) 6%, var(--bg-2))",
          border: "1px solid var(--acc-line)",
          padding: "12px 16px",
          display: "flex", gap: 10, alignItems: "flex-start",
        }}>
          <span style={{ color: "var(--acc)", fontSize: 14, flexShrink: 0, marginTop: 1 }}>⚡</span>
          <div>
            <div style={{ fontFamily: "var(--f-mono)", fontSize: 10, fontWeight: 700, letterSpacing: "0.14em", color: "var(--acc)", marginBottom: 4, textTransform: "uppercase" }}>
              {t('arenaSpecial', lang)}
            </div>
            <div style={{ fontSize: 12, color: "var(--ink-1)", lineHeight: 1.5 }}>{arena.special}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
)

export default ArenaModal
