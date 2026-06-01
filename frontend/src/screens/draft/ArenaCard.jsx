import { CornerTicks } from '../../components'
import { t } from '../../i18n'

/* ── Arena card (top center of the draft board) ──────────────────────────── */
const ARENA_IMG_W = 170  // each reel frame width — matches the wrapper width

const ArenaCard = ({ arena, arenaSpinning, arenaReel, universeId, onRoll, onOpenModal, lang }) => {
  const rolled = !!arena
  const spinning = arenaSpinning

  return (
    <div
      onClick={!rolled && !spinning ? onRoll : (rolled ? onOpenModal : undefined)}
      className="panel"
      style={{
        position: "relative", overflow: "hidden",
        width: "100%", height: "100%",
        background: rolled ? "var(--bg-elev)" : "color-mix(in oklab, var(--acc) 5%, var(--bg-elev))",
        borderColor: "var(--acc-line)",
        cursor: rolled ? "pointer" : (spinning ? "default" : "pointer"),
        display: "flex", flexDirection: "column",
        boxShadow: rolled ? "0 0 20px -6px color-mix(in oklab, var(--acc) 40%, transparent)" : "none",
      }}
    >
      <CornerTicks />

      {/* Not rolled */}
      {!rolled && !spinning && (
        <div style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 4 }}>
          <div style={{ fontFamily: "var(--f-mono)", fontSize: 9, color: "var(--acc)", letterSpacing: "0.22em" }}>
            {t('arenaGacha', lang)}
          </div>
          <div style={{ fontFamily: "var(--f-mono)", fontSize: 8, color: "var(--ink-4)", letterSpacing: "0.14em" }}>
            {t('arenaNotRolled', lang)}
          </div>
        </div>
      )}

      {/* Spinning — loading state before reel is built */}
      {spinning && arenaReel.length === 0 && (
        <div style={{ flex: 1, display: "grid", placeItems: "center", fontFamily: "var(--f-mono)", fontSize: 9, color: "var(--ink-3)", letterSpacing: "0.2em" }}>
          {t('arenaRolling', lang)}
        </div>
      )}

      {/* Spinning — horizontal image reel */}
      {spinning && arenaReel.length > 0 && (
        <>
          {/* fade masks on left and right edges */}
          <div style={{
            position: "absolute", inset: 0, zIndex: 2, pointerEvents: "none",
            background: "linear-gradient(90deg, rgba(7,8,12,0.9) 0%, transparent 18%, transparent 82%, rgba(7,8,12,0.9) 100%)",
          }} />
          {/* scrolling strip */}
          <div style={{
            position: "absolute", top: 0, left: 0, height: "100%",
            display: "flex", flexDirection: "row",
            animation: `arenaReelH 2s cubic-bezier(0.05, 0.85, 0.2, 1) forwards`,
            willChange: "transform",
          }}>
            {arenaReel.map((a, i) => (
              <div key={i} style={{ width: ARENA_IMG_W, height: "100%", flexShrink: 0, position: "relative", overflow: "hidden" }}>
                <img
                  src={`./arena/${universeId}/${encodeURIComponent(a.image)}`}
                  alt={a.name}
                  style={{ width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 40%" }}
                  onError={e => { e.currentTarget.style.display = "none" }}
                />
              </div>
            ))}
          </div>
        </>
      )}

      {/* Rolled: static image + name overlay */}
      {rolled && !spinning && (
        <>
          <img
            src={`./arena/${universeId}/${encodeURIComponent(arena.image)}`}
            alt={arena.name}
            style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 40%" }}
            onError={e => { e.currentTarget.style.display = "none" }}
          />
          <div style={{ position: "absolute", inset: 0, background: "linear-gradient(180deg, transparent 25%, rgba(7,8,12,0.92) 100%)" }} />
          <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, padding: "6px 8px", animation: "popIn 240ms cubic-bezier(.2,.9,.3,1.4)" }}>
            <div style={{ fontFamily: "var(--f-mono)", fontSize: 8, color: "var(--acc)", letterSpacing: "0.2em" }}>
              PT.{arena.part} · {arena.partName.toUpperCase()}
            </div>
            <div className="display" style={{ fontSize: 10, lineHeight: 1.2, color: "var(--ink-0)", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
              {arena.name.toUpperCase()}
            </div>
          </div>
        </>
      )}
    </div>
  )
}

export default ArenaCard
