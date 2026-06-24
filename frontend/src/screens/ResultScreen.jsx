import { useState, useEffect, useMemo, useRef } from 'react'
import { Atmos, AppBar, Icon } from '../components'
import { t } from '../i18n'

const cap = s => s.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
const r0 = n => Math.round(n)
const RED = "oklch(0.72 0.19 25)"

// Show the most signature tags first (so domain/heal never get cut off).
const TAG_ORDER = [
  "anti_domain", "domain_counter", "domain", "heal", "revive", "sustain", "ace",
  "manipulation", "lockdown", "aoe", "burst", "bruiser", "tank", "guard",
  "durability", "leadership", "buff", "debuff", "recon", "versatility",
  "utility", "betrayal", "sabotage",
]
const orderTags = tags => [...tags].sort((a, b) => {
  const ia = TAG_ORDER.indexOf(a), ib = TAG_ORDER.indexOf(b)
  return (ia < 0 ? 99 : ia) - (ib < 0 ? 99 : ib)
})

const TagRow = ({ tags, align }) => (
  <div style={{ display: "flex", gap: 4, flexWrap: "wrap", justifyContent: align === "left" ? "flex-end" : "flex-start" }}>
    {orderTags(tags).slice(0, 5).map((tag, i) => (
      <span key={i} style={{ fontFamily: "var(--f-mono)", fontSize: 8.5, letterSpacing: "0.06em", color: "var(--ink-2)", background: "var(--bg-2)", border: "1px solid var(--line)", borderRadius: 4, padding: "1px 5px" }}>
        {cap(tag)}
      </span>
    ))}
  </div>
)

// ── Compact settled row (one side) ───────────────────────────────────────────
const Cell = ({ e, align, extMap, imgUrl }) => {
  if (!e) return <div style={{ flex: 1 }} />
  const left = align === "left"
  const toEnemy = e.defects
  const arrow = toEnemy ? (left ? "→" : "←") : null
  return (
    <div style={{ flex: 1, display: "flex", gap: 10, alignItems: "center", flexDirection: left ? "row-reverse" : "row", textAlign: left ? "right" : "left", minWidth: 0 }}>
      <div style={{ display: "flex", alignItems: "center", gap: 5, minWidth: 92, padding: "0 4px", justifyContent: left ? "flex-start" : "flex-end" }}>
        {!left && arrow && <span style={{ fontSize: 17, color: RED }}>{arrow}</span>}
        <span className="display" style={{ fontSize: 23, lineHeight: 1, color: toEnemy ? RED : "var(--acc)", textShadow: `0 0 16px color-mix(in oklab, ${toEnemy ? RED : "var(--acc)"} 45%, transparent)` }}>{r0(e.score)}</span>
        {left && arrow && <span style={{ fontSize: 17, color: RED }}>{arrow}</span>}
      </div>
      <div style={{ width: 42, minWidth: 42, height: 42, borderRadius: 7, overflow: "hidden", position: "relative", border: "1px solid var(--line)", background: "var(--bg-2)" }}>
        <img src={imgUrl(e.char, extMap[e.char] || "jpeg")} alt="" style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 15%" }} onError={ev => { ev.currentTarget.style.display = "none" }} />
      </div>
      <div style={{ minWidth: 0, flex: 1, display: "flex", flexDirection: "column", gap: 3 }}>
        <span className="display" style={{ fontSize: 15, lineHeight: 1, color: "var(--ink-0)", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>{e.char}</span>
        <div style={{ display: "flex", gap: 4, flexWrap: "wrap", justifyContent: left ? "flex-end" : "flex-start" }}>
          {toEnemy && <span style={{ fontFamily: "var(--f-mono)", fontSize: 8.5, letterSpacing: "0.1em", color: RED, border: "1px solid oklch(0.5 0.15 25)", borderRadius: 4, padding: "1px 5px" }}>TRAIDOR → {e.role.toUpperCase()}</span>}
          <TagRow tags={e.tags} align={align} />
        </div>
      </div>
    </div>
  )
}

// ── Big spotlight portrait (one side) ────────────────────────────────────────
const Portrait = ({ e, side, on, extMap, imgUrl }) => {
  if (!e) return <div style={{ width: 200 }} />
  const left = side === "left"
  const toEnemy = e.defects
  return (
    <div style={{
      display: "flex", flexDirection: "column", alignItems: "center", gap: 10, width: 220,
      opacity: on ? 1 : 0, transform: on ? "translateX(0)" : `translateX(${left ? -50 : 50}px)`,
      transition: "opacity .5s ease, transform .55s cubic-bezier(.2,.8,.2,1)",
    }}>
      <div style={{ width: 172, height: 186, borderRadius: 14, overflow: "hidden", position: "relative", border: `2px solid ${toEnemy ? RED : "var(--acc-line)"}`, boxShadow: `0 0 46px color-mix(in oklab, ${toEnemy ? RED : "var(--acc)"} 32%, transparent)`, background: "var(--bg-2)" }}>
        <img src={imgUrl(e.char, extMap[e.char] || "jpeg")} alt="" style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 12%" }} onError={ev => { ev.currentTarget.style.display = "none" }} />
      </div>
      <div className="display" style={{ fontSize: 21, lineHeight: 1.05, color: "var(--ink-0)", textAlign: "center", maxWidth: 220 }}>{e.char}</div>
      {toEnemy && <span style={{ fontFamily: "var(--f-mono)", fontSize: 9.5, letterSpacing: "0.1em", color: RED, border: `1px solid oklch(0.5 0.15 25)`, borderRadius: 4, padding: "2px 7px", whiteSpace: "nowrap" }}>TRAIDOR → {e.role.toUpperCase()}</span>}
      <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
        {toEnemy && <span style={{ fontSize: 24, color: RED }}>{left ? "→" : "←"}</span>}
        <span className="display" style={{ fontSize: 46, lineHeight: 1, color: toEnemy ? RED : "var(--acc)", textShadow: `0 0 34px color-mix(in oklab, ${toEnemy ? RED : "var(--acc)"} 65%, transparent)`, transform: on ? "scale(1)" : "scale(0.5)", transition: "transform .5s cubic-bezier(.2,1.4,.4,1) .15s" }}>{r0(e.score)}</span>
      </div>
    </div>
  )
}

const Spotlight = ({ row, p1, p2, extMap, imgUrl }) => {
  const [on, setOn] = useState(false)
  useEffect(() => { const id = requestAnimationFrame(() => setOn(true)); return () => cancelAnimationFrame(id) }, [])
  return (
    <div style={{ position: "absolute", top: 150, left: 0, right: 0, height: 372, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 12, pointerEvents: "none" }}>
      <div style={{ position: "absolute", inset: "-30px 18% 0", background: "radial-gradient(ellipse at center, color-mix(in oklab, var(--acc) 12%, transparent), transparent 72%)" }} />
      <div className="display" style={{ fontSize: 58, letterSpacing: "0.1em", color: "var(--acc)", textShadow: "0 0 44px color-mix(in oklab, var(--acc) 70%, transparent)", opacity: on ? 1 : 0, transform: on ? "translateY(0)" : "translateY(-18px)", transition: "all .5s ease" }}>
        {row.position.toUpperCase()}
      </div>
      <div style={{ display: "flex", alignItems: "center", gap: 44 }}>
        <Portrait e={row.p1} side="left" on={on} extMap={extMap} imgUrl={imgUrl} />
        <div className="display" style={{ fontSize: 36, color: "var(--ink-1)", opacity: on ? 0.9 : 0, transition: "opacity .6s ease .2s" }}>VS</div>
        <Portrait e={row.p2} side="right" on={on} extMap={extMap} imgUrl={imgUrl} />
      </div>
    </div>
  )
}

const Counter = ({ name, value, lead }) => (
  <div style={{ textAlign: "center" }}>
    <div className="display-x" style={{ fontSize: 11, color: "var(--acc)", letterSpacing: "0.2em" }}>{name}</div>
    <div className="display" style={{ fontSize: 60, lineHeight: 1, marginTop: 2, color: lead ? "var(--acc)" : "var(--ink-1)", textShadow: lead ? "0 0 36px color-mix(in oklab, var(--acc) 75%, transparent)" : "none", transition: "color 0.4s" }}>{value}</div>
  </div>
)

// ── Fallback roster (universes with no power profiles) ───────────────────────
const RosterList = ({ side, player, draft, universe, align, imgUrl, lang }) => (
  <div className="panel panel-tagged scanlines" style={{ position: "relative", padding: 20, overflow: "hidden" }}>
    <div style={{ position: "absolute", inset: 0, background: `linear-gradient(${align === "left" ? "90deg" : "270deg"}, color-mix(in oklab, var(--acc) 14%, transparent) 0%, transparent 60%)`, pointerEvents: "none" }} />
    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end", marginBottom: 14 }}>
      <div>
        <div className="display-x" style={{ fontSize: 12, color: "var(--acc)" }}>PLAYER · {side === "p1" ? "01" : "02"}</div>
        <div className="display" style={{ fontSize: 44, lineHeight: 1, marginTop: 2 }}>{player}</div>
      </div>
    </div>
    <div className="sep" style={{ marginBottom: 14 }} />
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
      {universe.positions.map((pos, i) => {
        const a = draft.assignments[i][side]
        return (
          <div key={i} className="panel" style={{ display: "flex", padding: 0, background: "var(--bg-2)", minHeight: 110, borderColor: a ? "var(--acc-line)" : "var(--line)" }}>
            <div style={{ width: 76, minWidth: 76, position: "relative", overflow: "hidden" }}>
              {a && <img src={imgUrl(a.name, a.ext)} alt="" style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 15%" }} onError={e => { e.currentTarget.style.display = "none" }} />}
            </div>
            <div style={{ flex: 1, padding: "8px 10px", display: "flex", flexDirection: "column", justifyContent: "center", gap: 3 }}>
              <span style={{ fontFamily: "var(--f-mono)", fontSize: 10, color: "var(--acc)", letterSpacing: "0.16em" }}>#{String(i + 1).padStart(2, "0")} · {pos.toUpperCase()}</span>
              <span className="display" style={{ fontSize: 17, color: a ? "var(--ink-0)" : "var(--ink-4)" }}>{a ? a.name : t('undrafted', lang)}</span>
            </div>
          </div>
        )
      })}
    </div>
  </div>
)

// Who wins this single position, and by how much (defectors count for the
// other side, mirroring the running-total rule).
const laneOutcome = row => {
  let a = 0, b = 0
  if (row.p1) row.p1.defects ? (b += row.p1.score) : (a += row.p1.score)
  if (row.p2) row.p2.defects ? (a += row.p2.score) : (b += row.p2.score)
  const delta = r0(Math.abs(a - b))
  const side = a === b ? "tie" : a > b ? "p1" : "p2"
  return { side, delta }
}

const AbilityNote = ({ e, align }) => {
  const left = align === "left"
  const abilities = e?.abilities || []
  return (
    <div style={{ flex: 1, minWidth: 0, display: "flex", flexDirection: "column", gap: 3, textAlign: left ? "right" : "left" }}>
      {abilities.length === 0 ? (
        <span style={{ fontFamily: "var(--f-mono)", fontSize: 9.5, color: "var(--ink-4)", letterSpacing: "0.1em" }}>—</span>
      ) : abilities.slice(0, 3).map((txt, i) => (
        <span key={i} style={{ fontSize: 10.5, lineHeight: 1.3, color: "var(--ink-2)" }}>{txt}</span>
      ))}
    </div>
  )
}

// One settled position. Hover enlarges the row and reveals the individual
// battle readout (lane winner + each fighter's visible abilities).
const SettledRow = ({ row, p1, p2, extMap, imgUrl, lang }) => {
  const [hover, setHover] = useState(false)
  const { side, delta } = laneOutcome(row)
  const isTie = side === "tie"
  const winColor = isTie ? "var(--ink-2)" : "var(--acc)"
  const winName = side === "p1" ? (p1 || "PLAYER ONE")
    : side === "p2" ? (p2 || "PLAYER TWO")
    : t('evenMatch', lang)
  return (
    <div
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        borderRadius: 9, background: "var(--bg-1)",
        border: `1px solid ${hover ? "var(--acc-line)" : "var(--line)"}`,
        boxShadow: hover ? "0 8px 30px color-mix(in oklab, var(--acc) 24%, transparent)" : "none",
        transform: hover ? "scale(1.02)" : "scale(1)",
        position: "relative", zIndex: hover ? 6 : 1,
        transition: "transform .2s cubic-bezier(.2,.8,.2,1), box-shadow .2s ease, border-color .2s ease",
        animation: "popIn .4s ease",
      }}
    >
      <div style={{ display: "grid", gridTemplateColumns: "1fr 128px 1fr", alignItems: "center", gap: 12, padding: "6px 14px" }}>
        <Cell e={row.p1} align="left" extMap={extMap} imgUrl={imgUrl} />
        <div style={{ textAlign: "center" }}>
          <div style={{ fontFamily: "var(--f-mono)", fontSize: 10.5, letterSpacing: "0.16em", color: "var(--ink-3)", textTransform: "uppercase" }}>{row.position}</div>
          <div style={{
            marginTop: 3, fontFamily: "var(--f-mono)", fontSize: 9.5, letterSpacing: "0.08em",
            color: winColor, whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis",
            opacity: hover ? 1 : 0, transition: "opacity .2s ease",
          }}>
            {isTie ? t('evenMatch', lang) : `▲ ${winName} +${delta}`}
          </div>
        </div>
        <Cell e={row.p2} align="right" extMap={extMap} imgUrl={imgUrl} />
      </div>
      {/* Individual-battle readout — revealed on hover */}
      <div style={{ maxHeight: hover ? 170 : 0, overflow: "hidden", transition: "max-height .25s ease" }}>
        <div className="sep" style={{ margin: "0 14px" }} />
        <div style={{ display: "grid", gridTemplateColumns: "1fr 128px 1fr", gap: 12, padding: "8px 14px 10px", alignItems: "start" }}>
          <AbilityNote e={row.p1} align="left" />
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 2 }}>
            <span className="display" style={{ fontSize: 22, lineHeight: 1, color: winColor }}>{isTie ? "=" : `+${delta}`}</span>
            <span style={{ fontFamily: "var(--f-mono)", fontSize: 8.5, letterSpacing: "0.14em", color: "var(--ink-3)", textTransform: "uppercase", textAlign: "center" }}>{winName}</span>
          </div>
          <AbilityNote e={row.p2} align="right" />
        </div>
      </div>
    </div>
  )
}

const ResultScreen = ({ universe, p1, p2, draft, onMenu, onPlayers, imgUrl, version, lang }) => {
  const [analysis, setAnalysis] = useState(null)
  const [presented, setPresented] = useState(0)   // positions settled into the list
  const [done, setDone] = useState(false)
  const timer = useRef(null)

  useEffect(() => {
    let alive = true
    ;(async () => {
      try { const res = await window.pywebview?.api?.analyze(); if (alive) setAnalysis(res) }
      catch { /* best-effort */ }
    })()
    return () => { alive = false }
  }, [])

  // Drive the spotlight → list sequence.
  useEffect(() => {
    if (!analysis?.available) return
    const n = analysis.rows.length
    setPresented(0); setDone(false)
    let i = 0
    timer.current = setInterval(() => {
      i += 1; setPresented(i)
      if (i >= n) { clearInterval(timer.current); setDone(true) }
    }, 1850)
    return () => clearInterval(timer.current)
  }, [analysis])

  const skip = () => {
    if (!analysis?.available || done) return
    clearInterval(timer.current)
    setPresented(analysis.rows.length)
    setDone(true)
  }

  const extMap = useMemo(() => {
    const m = {}
    draft.assignments.forEach(a => { if (a.p1) m[a.p1.name] = a.p1.ext; if (a.p2) m[a.p2.name] = a.p2.ext })
    return m
  }, [draft])

  // Running totals over settled rows (defectors credited to the other side).
  const running = useMemo(() => {
    let a = 0, b = 0
    if (analysis?.available) {
      for (let i = 0; i < presented; i++) {
        const row = analysis.rows[i]
        if (row.p1) (row.p1.defects ? (b += row.p1.score) : (a += row.p1.score))
        if (row.p2) (row.p2.defects ? (a += row.p2.score) : (b += row.p2.score))
      }
    }
    return { a, b }
  }, [analysis, presented])

  const hasAnalysis = analysis?.available

  // ── Fallback (no profiles for this universe) ───────────────────────────────
  if (analysis && !hasAnalysis) {
    return (
      <div className={`stage acc-${universe.id}`} data-screen-label="04 Result">
        <Atmos particles={true} />
        <AppBar phase="ROSTER LOCKED" universe={universe} mode={t('matchReady', lang)} step="03 / 03" version={version} lang={lang} />
        <div style={{ position: "absolute", top: 100, left: 0, right: 0, textAlign: "center" }}>
          <div className="label" style={{ justifyContent: "center", display: "inline-flex" }}>{t('draftComplete', lang)}</div>
          <h1 className="display" style={{ fontSize: 76, margin: "10px 0 4px" }}>{t('rosterWord', lang)} <span style={{ color: "var(--acc)" }}>{t('lockedWord', lang)}</span></h1>
          <div style={{ color: "var(--ink-2)", fontFamily: "var(--f-mono)", fontSize: 12, letterSpacing: "0.18em", textTransform: "uppercase" }}>{t('noWinner', lang)}</div>
        </div>
        <div style={{ position: "absolute", top: 280, left: 64, right: 64, bottom: 140, display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
          <RosterList side="p1" player={p1 || "PLAYER ONE"} draft={draft} universe={universe} align="left" imgUrl={imgUrl} lang={lang} />
          <RosterList side="p2" player={p2 || "PLAYER TWO"} draft={draft} universe={universe} align="right" imgUrl={imgUrl} lang={lang} />
        </div>
        <div style={{ position: "absolute", bottom: 60, left: 0, right: 0, display: "flex", justifyContent: "center", gap: 12 }}>
          <button className="btn" onClick={onMenu}><Icon name="grid" /> {t('menu', lang)}</button>
          <button className="btn btn-primary" onClick={onPlayers}><Icon name="user" /> {t('players', lang)}</button>
        </div>
      </div>
    )
  }

  const p1Val = r0(running.a + (done ? analysis.p1.bonus : 0))
  const p2Val = r0(running.b + (done ? analysis.p2.bonus : 0))
  const winner = done ? analysis.verdict : null
  const winnerName = winner === "p1" ? (p1 || "PLAYER ONE") : winner === "p2" ? (p2 || "PLAYER TWO") : null

  return (
    <div className={`stage acc-${universe.id}`} data-screen-label="04 Result" onClick={skip} style={{ cursor: hasAnalysis && !done ? "pointer" : "default" }}>
      <Atmos particles={true} />
      <AppBar phase="ROSTER LOCKED" universe={universe} mode={t('battleAnalysis', lang)} step="03 / 03" version={version} lang={lang} />

      {/* Scoreboard */}
      <div style={{ position: "absolute", top: 88, left: 64, right: 64, display: "grid", gridTemplateColumns: "1fr auto 1fr", alignItems: "center", gap: 24 }}>
        <Counter name={p1 || "PLAYER ONE"} value={p1Val} lead={winner === "p1"} />
        <div style={{ textAlign: "center" }}>
          <div className="display-x" style={{ fontSize: 10, color: "var(--ink-3)", letterSpacing: "0.24em" }}>{t('battleAnalysis', lang)}</div>
          <div className="display" style={{ fontSize: 28, color: "var(--ink-0)", lineHeight: 1.1 }}>VS</div>
        </div>
        <Counter name={p2 || "PLAYER TWO"} value={p2Val} lead={winner === "p2"} />
      </div>

      {/* Hero: spotlight while presenting, winner banner when done */}
      {hasAnalysis && !done && presented < analysis.rows.length && (
        <Spotlight key={presented} row={analysis.rows[presented]} p1={p1} p2={p2} extMap={extMap} imgUrl={imgUrl} />
      )}
      {done && (
        <div style={{ position: "absolute", top: 172, left: 0, right: 0, height: 356, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 10 }}>
          {winner === "tie" ? (
            <div className="display" style={{ fontSize: 56, color: "var(--ink-1)" }}>{t('evenMatch', lang)}</div>
          ) : (
            <>
              <div className="display-x" style={{ fontSize: 13, letterSpacing: "0.3em", color: "var(--ink-3)" }}>{t('edgeWord', lang)}</div>
              <div className="display" style={{ fontSize: 80, lineHeight: 1, color: "var(--acc)", textShadow: "0 0 50px color-mix(in oklab, var(--acc) 70%, transparent)" }}>{winnerName}</div>
              <div className="display" style={{ fontSize: 26, color: "var(--ink-2)" }}>+{Math.abs(analysis.margin).toFixed(0)}</div>
            </>
          )}
        </div>
      )}

      {/* Settled list */}
      <div style={{ position: "absolute", top: 540, left: 64, right: 64, bottom: 150, display: "flex", flexDirection: "column", gap: 6 }}>
        {hasAnalysis && analysis.rows.slice(0, presented).map((row, i) => (
          <SettledRow key={i} row={row} p1={p1} p2={p2} extMap={extMap} imgUrl={imgUrl} lang={lang} />
        ))}
      </div>

      <div style={{ position: "absolute", bottom: 56, left: 0, right: 0, display: "flex", justifyContent: "center", gap: 12 }}>
        <button className="btn" onClick={e => { e.stopPropagation(); onMenu() }}><Icon name="grid" /> {t('menu', lang)}</button>
        <button className="btn btn-primary" onClick={e => { e.stopPropagation(); onPlayers() }}><Icon name="user" /> {t('players', lang)}</button>
      </div>
    </div>
  )
}

export default ResultScreen
