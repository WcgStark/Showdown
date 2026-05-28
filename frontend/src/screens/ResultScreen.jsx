import { Atmos, AppBar, Icon, CornerTicks } from '../components'
import { t } from '../i18n'

const TeamSheet = ({ side, player, draft, universe, align, imgUrl, lang }) => (
  <div className="panel panel-tagged scanlines" style={{ position: "relative", padding: 20, overflow: "hidden" }}>
    <CornerTicks />
    <div style={{
      position: "absolute", inset: 0,
      background: `linear-gradient(${align === "left" ? "90deg" : "270deg"}, color-mix(in oklab, var(--acc) 14%, transparent) 0%, transparent 60%)`,
      pointerEvents: "none",
    }} />

    <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end", position: "relative", marginBottom: 14 }}>
      <div>
        <div className="display-x" style={{ fontSize: 12, color: "var(--acc)" }}>PLAYER · {side === "p1" ? "01" : "02"}</div>
        <div className="display" style={{ fontSize: 44, lineHeight: 1, marginTop: 2, letterSpacing: "0.04em" }}>{player}</div>
      </div>
      <div style={{ textAlign: "right", fontFamily: "var(--f-mono)", fontSize: 11, letterSpacing: "0.18em", color: "var(--ink-3)" }}>
        <div>{universe.tag}</div>
        <div style={{ color: "var(--acc)" }}>{universe.positions.length} {t('slots', lang)}</div>
      </div>
    </div>

    <div className="sep" style={{ marginBottom: 14 }} />

    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
      {universe.positions.map((pos, i) => {
        const a = draft.assignments[i][side]
        return (
          <div key={i} className="panel" style={{
            position: "relative", padding: 0, display: "flex",
            borderColor: a ? "var(--acc-line)" : "var(--line)",
            background: "var(--bg-2)", minHeight: 120,
          }}>
            <div style={{ width: 80, minWidth: 80, flexShrink: 0, position: "relative", overflow: "hidden" }}>
              {a && imgUrl ? (
                <img
                  src={imgUrl(a.name, a.ext)}
                  alt={a.name}
                  style={{
                    position: "absolute", inset: 0,
                    width: "100%", height: "100%",
                    objectFit: "cover", objectPosition: "50% 15%",
                  }}
                  onError={e => { e.currentTarget.style.display = "none" }}
                />
              ) : (
                <div style={{ position: "absolute", inset: 0, display: "grid", placeItems: "center", color: "var(--ink-4)" }}>
                  <Icon name="user" size={24} />
                </div>
              )}
            </div>
            <div style={{ flex: 1, padding: "10px 12px", display: "flex", flexDirection: "column", gap: 4, justifyContent: "center" }}>
              <span style={{ fontFamily: "var(--f-mono)", fontSize: 10, color: "var(--acc)", letterSpacing: "0.18em" }}>
                #{String(i + 1).padStart(2, "0")} · {pos.toUpperCase()}
              </span>
              <span className="display" style={{ fontSize: 18, lineHeight: 1.1, letterSpacing: "0.02em", color: a ? "var(--ink-0)" : "var(--ink-4)" }}>
                {a ? a.name : t('undrafted', lang)}
              </span>
            </div>
          </div>
        )
      })}
    </div>
  </div>
)

const ResultScreen = ({ universe, p1, p2, draft, onRestart, imgUrl, version, lang }) => (
  <div className={`stage acc-${universe.id}`} data-screen-label="04 Result">
    <Atmos particles={true} />
    <AppBar phase="ROSTER LOCKED" universe={universe} mode={t('matchReady', lang)} step="03 / 03" version={version} lang={lang} />

    <div style={{ position: "absolute", top: 100, left: 0, right: 0, textAlign: "center" }}>
      <div className="label" style={{ justifyContent: "center", display: "inline-flex" }}>
        {t('draftComplete', lang)}
      </div>
      <h1 className="display" style={{ fontSize: 76, margin: "10px 0 4px", letterSpacing: "0.04em" }}>
        {t('rosterWord', lang)} <span style={{ color: "var(--acc)", textShadow: "0 0 32px color-mix(in oklab, var(--acc) 70%, transparent)" }}>{t('lockedWord', lang)}</span>
      </h1>
      <div style={{ color: "var(--ink-2)", fontFamily: "var(--f-mono)", fontSize: 12, letterSpacing: "0.18em", textTransform: "uppercase" }}>
        {t('noWinner', lang)}
      </div>
    </div>

    <div style={{
      position: "absolute", top: 280, left: 64, right: 64, bottom: 140,
      display: "grid", gridTemplateColumns: "1fr 60px 1fr", gap: 16, alignItems: "stretch",
    }}>
      <TeamSheet side="p1" player={p1 || "PLAYER ONE"} draft={draft} universe={universe} align="left" imgUrl={imgUrl} lang={lang} />

      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 16 }}>
        <div style={{ flex: 1, width: 1, background: "linear-gradient(180deg, transparent, var(--line-2), transparent)" }} />
        <div className="display" style={{ fontSize: 56, lineHeight: 1, color: "var(--ink-0)", textShadow: "0 0 30px color-mix(in oklab, var(--acc) 60%, transparent)" }}>VS</div>
        <div style={{ flex: 1, width: 1, background: "linear-gradient(180deg, transparent, var(--line-2), transparent)" }} />
      </div>

      <TeamSheet side="p2" player={p2 || "PLAYER TWO"} draft={draft} universe={universe} align="right" imgUrl={imgUrl} lang={lang} />
    </div>

    <div style={{ position: "absolute", bottom: 60, left: 0, right: 0, zIndex: 3, display: "flex", justifyContent: "center", gap: 12 }}>
      <button className="btn btn-primary" onClick={onRestart}>
        <Icon name="undo" /> {t('newDraft', lang)}
      </button>
    </div>
  </div>
)

export default ResultScreen
