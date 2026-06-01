import { t } from '../../i18n'

/* ── Position column (center / drop targets) ──────────────────────────────── */
const PositionColumn = ({ positions, assignments, turn, enabled, onPick, lang }) => (
  <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
    {positions.map((pos, i) => {
      const alreadyForTurn = assignments[i][turn] !== null
      const open = enabled && !alreadyForTurn
      return (
        <button
          key={i}
          disabled={!open}
          onClick={() => onPick(i)}
          className="panel"
          style={{
            flex: 1, position: "relative",
            background: open ? "var(--acc-soft)" : "var(--bg-glass)",
            borderColor: open ? "var(--acc)" : "var(--line)",
            color: "var(--ink-0)", cursor: open ? "pointer" : "not-allowed",
            display: "grid", placeItems: "center",
            fontFamily: "var(--f-display)", fontSize: 20, fontWeight: 700,
            letterSpacing: "0.08em", textTransform: "uppercase",
            transition: "transform 80ms ease",
            boxShadow: open ? "0 0 28px -8px color-mix(in oklab, var(--acc) 60%, transparent)" : "none",
          }}
          onMouseDown={e => open && (e.currentTarget.style.transform = "scale(0.99)")}
          onMouseUp={e => (e.currentTarget.style.transform = "scale(1)")}
          onMouseLeave={e => (e.currentTarget.style.transform = "scale(1)")}
        >
          {open && (
            <>
              <span style={{ position: "absolute", top: 6, left: 8, fontSize: 10, fontFamily: "var(--f-mono)", color: "var(--acc)", letterSpacing: "0.2em" }}>{t('drop', lang)}</span>
              <span style={{ position: "absolute", top: 6, right: 8, fontSize: 10, fontFamily: "var(--f-mono)", color: "var(--acc)", letterSpacing: "0.2em" }}>{String(i + 1).padStart(2, "0")}</span>
            </>
          )}
          <span style={{ color: alreadyForTurn ? "var(--ink-4)" : (open ? "var(--ink-0)" : "var(--ink-2)") }}>{pos}</span>
          <span style={{ position: "absolute", bottom: 6, fontSize: 10, fontFamily: "var(--f-mono)", color: "var(--ink-3)", letterSpacing: "0.18em" }}>
            {assignments[i].p1 ? "P1" : "·"} <span style={{ color: "var(--ink-4)" }}>/</span> {assignments[i].p2 ? "P2" : "·"}
          </span>
        </button>
      )
    })}
  </div>
)

export default PositionColumn
