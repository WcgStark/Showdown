import { Icon, CornerTicks } from '../../components'
import { t } from '../../i18n'

/* ── Player banner (top-left / top-right of the draft board) ──────────────── */
const PlayerBanner = ({ side, player, filled, total, active, skips, lang, pfp }) => {
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
        {pfp
          ? <img src={`./pfp/${pfp.split('/').map(encodeURIComponent).join('/')}`} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 20%" }} alt="" />
          : <Icon name="user" size={40} />
        }
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

export default PlayerBanner
