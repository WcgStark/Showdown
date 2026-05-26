/* global React, UNIVERSES, Icon, Atmos, AppBar, ImgPh, CornerTicks */
const { useState, useEffect, useRef, useMemo } = React;

/* ===================================================== */
/* SCREEN 1 — UNIVERSE SELECT (LOBBY)                    */
/* ===================================================== */
const LobbyScreen = ({ onSelect, selectedId, setSelectedId }) => {
  const sel = UNIVERSES.find(u => u.id === selectedId) || UNIVERSES[0];
  return (
    <div className={`stage acc-${sel.id}`} data-screen-label="01 Lobby">
      <Atmos />
      <AppBar phase="LOBBY" />

      {/* Title block */}
      <div style={{
        position: "absolute", top: 110, left: 0, right: 0,
        textAlign: "center", zIndex: 3,
      }}>
        <div className="label" style={{ justifyContent: "center", display: "inline-flex" }}>
          STEP 01 / 03 — SELECT YOUR UNIVERSE
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
        {UNIVERSES.map((u, i) => {
          const active = u.id === sel.id;
          return (
            <UniverseCard
              key={u.id}
              universe={u}
              active={active}
              onHover={() => setSelectedId(u.id)}
              onClick={() => onSelect(u.id)}
              idx={i}
            />
          );
        })}
      </div>

      {/* Footer bar */}
      <div style={{
        position: "absolute", bottom: 60, left: 0, right: 0, zIndex: 3,
        display: "flex", justifyContent: "space-between", alignItems: "center", padding: "0 64px",
      }}>
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          <span className="label">CURRENT SELECTION</span>
          <span className="display" style={{ fontSize: 28, color: "var(--ink-0)" }}>
            {sel.name} <span style={{ color: "var(--ink-3)", fontWeight: 500 }}>/ {sel.codename}</span>
          </span>
        </div>
        <div style={{ display: "flex", gap: 12 }}>
          <button className="btn btn-primary" onClick={() => onSelect(sel.id)}>
            CONFIRM SELECTION <Icon name="arrow" />
            <span className="kbd">ENTER</span>
          </button>
        </div>
      </div>
    </div>
  );
};

const LANDSCAPE = {
  onepiece:   "../assets/landscape/landscape%20onepiece.jpg",
  naruto:     "../assets/landscape/landscape%20naruto.jpg",
  bleach:     "../assets/landscape/landscape%20bleach.jpg",
  invincible: "../assets/landscape/landscape%20invincible.jpg",
};

const UniverseCard = ({ universe, active, onHover, onClick, idx }) => {
  const accStyle = { "--acc": universe.accent };
  const landscapeSrc = LANDSCAPE[universe.id];
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
      {/* gradient overlay */}
      <div style={{
        position: "absolute", inset: 0,
        background:
          `linear-gradient(180deg, rgba(7,8,12,0.35) 0%, rgba(7,8,12,0.5) 50%, rgba(7,8,12,0.95) 100%)`,
      }} />

      {/* big title */}
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
  );
};

/* ===================================================== */
/* SCREEN 2 — PLAYER NAMES                               */
/* ===================================================== */
const QUICK_NAMES = ["ALEX", "RYU", "MIKA", "JIN", "NOVA", "ZED", "KIRA", "OBI"];

const PlayersScreen = ({ universe, mode, setMode, p1, p2, setP1, setP2, onBack, onStart, quickNames }) => {
  const resolvedQuickNames = (quickNames && quickNames.length) ? quickNames.map(n => n.toUpperCase()) : QUICK_NAMES;
  return (
    <div className={`stage acc-${universe.id}`} data-screen-label="02 Players">
      <Atmos particles={false} />
      <AppBar phase="ROSTER" universe={universe} mode={mode} step="02 / 03" />

      <div style={{ position: "absolute", top: 110, left: 0, right: 0, textAlign: "center" }}>
        <div className="label" style={{ justifyContent: "center", display: "inline-flex" }}>
          STEP 02 / 03 — DECLARE COMBATANTS
        </div>
        <h1 className="display" style={{ fontSize: 64, margin: "12px 0 4px", letterSpacing: "0.04em" }}>
          WHO'S DRAFTING?
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
        <PlayerCard side="P1" value={p1} setValue={setP1} accent="var(--acc)" align="right" quickNames={resolvedQuickNames} />

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
            <div style={{ color: "var(--ink-3)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.2em", marginTop: 6 }}>
              BEST OF SIX
            </div>
          </div>
        </div>

        <PlayerCard side="P2" value={p2} setValue={setP2} accent="var(--acc)" align="left" quickNames={resolvedQuickNames} />
      </div>

      {/* Mode selector */}
      <div style={{
        position: "absolute", left: 120, right: 120, top: 780,
        display: "flex", flexDirection: "column", alignItems: "center", gap: 16,
      }}>
        <span className="label">MATCH FORMAT</span>
        <div className="panel panel-tagged" style={{ display: "inline-flex", padding: 4, gap: 4 }}>
          {(universe.filters || []).map(f => {
            const on = mode === f.key;
            const mainName = f.label.replace(/[^a-zA-ZÀ-ÿ\s(]/g, '').split('(')[0].trim().toUpperCase();
            const descPart = (f.label.match(/\(([^)]+)\)/) || [])[1] || '';
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
            );
          })}
        </div>
      </div>

      {/* Footer */}
      <div style={{
        position: "absolute", bottom: 60, left: 64, right: 64, zIndex: 3,
        display: "flex", justifyContent: "space-between", alignItems: "center",
      }}>
        <button className="btn btn-ghost" onClick={onBack}>
          <Icon name="undo" /> BACK
          <span className="kbd">ESC</span>
        </button>
        <button className="btn btn-primary" onClick={onStart} disabled={!p1.trim() || !p2.trim()}>
          ENTER THE DRAFT <Icon name="arrow" />
          <span className="kbd">ENTER</span>
        </button>
      </div>
    </div>
  );
};

const PlayerCard = ({ side, value, setValue, align, quickNames }) => (
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
        ENTER CALLSIGN
      </div>
      <input
        value={value}
        onChange={e => setValue(e.target.value.slice(0, 14).toUpperCase())}
        placeholder="TYPE NAME"
        style={{
          width: "100%",
          background: "transparent", border: 0, borderBottom: "2px solid var(--acc)",
          color: "var(--ink-0)", fontFamily: "var(--f-display)",
          fontSize: 72, fontWeight: 700, letterSpacing: "0.04em",
          padding: "10px 0", outline: "none", textTransform: "uppercase",
        }}
      />
      <div style={{ display: "flex", justifyContent: "space-between", color: "var(--ink-3)", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.14em", marginTop: 6 }}>
        <span>MAX 14 CHARS</span>
        <span>{value.length} / 14</span>
      </div>
    </div>

    {/* quick names */}
    <div style={{ position: "relative" }}>
      <div className="label" style={{ marginBottom: 10 }}>QUICK NAMES</div>
      <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
        {(quickNames || QUICK_NAMES).map(n => (
          <button key={n} className="chip" onClick={() => setValue(n)}>{n}</button>
        ))}
        <button className="chip" onClick={() => setValue("")}>
          <Icon name="cross" size={10} /> CLEAR
        </button>
      </div>
    </div>
  </div>
);

window.LobbyScreen = LobbyScreen;
window.PlayersScreen = PlayersScreen;
