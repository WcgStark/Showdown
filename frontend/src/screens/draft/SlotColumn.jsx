import { Icon } from '../../components'

/* ── Slot column (a player's roster, left or right side) ──────────────────── */
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

export default SlotColumn
