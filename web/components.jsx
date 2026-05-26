/* global React */
const { useState, useEffect, useRef, useMemo } = React;

/* ============ UNIVERSE CATALOG ============ */
const UNIVERSES = [
  {
    id: "onepiece",
    name: "Pirate Crew",
    codename: "GRAND LINE",
    tag: "ONE PIECE",
    accent: "var(--u-onepiece)",
    blurb: "Captains, navigators, gunners and dreamers chasing a horizon that keeps moving.",
    positions: ["Captain", "First Mate", "Navigator", "Sharpshooter", "Cook", "Doctor"],
    sample: ["The Captain", "The Swordsman", "The Navigator", "The Sniper", "The Cook", "The Surgeon"],
  },
  {
    id: "naruto",
    name: "Shinobi Cell",
    codename: "HIDDEN LEAF",
    tag: "NARUTO",
    accent: "var(--u-naruto)",
    blurb: "Three-man cells with a sensei. Jutsu, doctrine, and a lot of borrowed chakra.",
    positions: ["Sensei", "Front Line", "Mid Range", "Support", "Tactician", "Specialist"],
    sample: ["The Sensei", "The Hothead", "The Genius", "The Medic", "The Strategist", "The Sealer"],
  },
  {
    id: "bleach",
    name: "Soul Division",
    codename: "GOTEI",
    tag: "BLEACH",
    accent: "var(--u-bleach)",
    blurb: "Captains and lieutenants of a death-touched military caste. Discipline meets spectacle.",
    positions: ["Captain", "Lieutenant", "Bankai User", "Kido Master", "Hollow Specialist", "Scout"],
    sample: ["The Captain", "The Lieutenant", "The Prodigy", "The Kido User", "The Hunter", "The Scout"],
  },
  {
    id: "invincible",
    name: "Hero Roster",
    codename: "VILTRUM",
    tag: "INVINCIBLE",
    accent: "var(--u-invincible)",
    blurb: "Flying bricks, super-geniuses, and the people they can never quite save in time.",
    positions: ["Leader", "Powerhouse", "Speedster", "Tech", "Ranged", "Wildcard"],
    sample: ["The Leader", "The Bruiser", "The Speedster", "The Engineer", "The Marksman", "The Wildcard"],
  },
];

/* ============ ICONS (simple, line) ============ */
const Icon = ({ name, size = 16 }) => {
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
  };
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="square">
      {paths[name] || null}
    </svg>
  );
};

/* ============ Particles ============ */
const Particles = ({ count = 30 }) => {
  const seeds = useMemo(() => (
    Array.from({ length: count }).map((_, i) => ({
      left: (i * 137.5) % 100,
      top: (i * 53.7 + 30) % 100,
      delay: (i * 0.61) % 18,
      size: 1 + ((i * 7) % 4),
    }))
  ), [count]);
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
  );
};

/* ============ Background atmosphere ============ */
const Atmos = ({ glow = true, grid = true, particles = true }) => (
  <>
    {glow && <div className="bg-glow" />}
    {grid && <div className="bg-grid" />}
    {particles && <Particles />}
    <div className="bg-noise" />
    <div className="bg-vignette" />
  </>
);

/* ============ AppBar ============ */
const AppBar = ({ phase = "LOBBY", universe, mode, step }) => (
  <div className="appbar">
    <div className="brand">
      <div className="mark" />
      <span>SHOWDOWN</span>
      <span style={{ color: "var(--ink-3)", letterSpacing: "0.18em", fontWeight: 500, fontSize: 11, marginLeft: 6 }}>
        / Draft v.2.1
      </span>
    </div>
    <div className="meta">
      <div><span style={{ color: "var(--ink-3)" }}>PHASE</span> <b>{phase}</b></div>
      {universe && <div><span style={{ color: "var(--ink-3)" }}>UNIVERSE</span> <b>{universe.tag}</b></div>}
      {mode && <div><span style={{ color: "var(--ink-3)" }}>MODE</span> <b>{mode}</b></div>}
      {step && <div><span style={{ color: "var(--ink-3)" }}>STEP</span> <b>{step}</b></div>}
    </div>
  </div>
);

/* ============ Image Placeholder ============ */
const ImgPh = ({ label = "PORTRAIT", aspect = "3 / 4", style }) => (
  <div className="imgph" style={{ aspectRatio: aspect, ...style }}>
    <div className="tag">{label}</div>
    <svg className="crosshair" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1">
      <path d="M12 2v6M12 16v6M2 12h6M16 12h6" />
      <circle cx="12" cy="12" r="3" />
    </svg>
  </div>
);

/* Section corner tick marks */
const CornerTicks = ({ color = "var(--acc)" }) => (
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
);

Object.assign(window, { UNIVERSES, Icon, Particles, Atmos, AppBar, ImgPh, CornerTicks });
