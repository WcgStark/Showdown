/* global React, ReactDOM, LobbyScreen, PlayersScreen, DraftScreen, ResultScreen */
const { useState, useEffect, useCallback } = React;

const PORT = 8765;

const App = () => {
  const [screen, setScreen]           = useState("lobby");
  const [config, setConfig]           = useState(null);
  const [selectedId, setSelectedId]   = useState("onepiece");
  const [universeConfig, setUniverseConfig] = useState(null);
  const [p1, setP1]                   = useState("");
  const [p2, setP2]                   = useState("");
  const [mode, setMode]               = useState("draft");
  const [draft, setDraft]             = useState(null);
  const [layout, setLayout]           = useState({ scale: 1, x: 0, y: 0 });

  // ── Responsive layout: scale + center the 1920×1080 stage ────────────────
  useEffect(() => {
    const updateLayout = () => {
      const w = window.innerWidth;
      const h = window.innerHeight;
      const s = Math.min(w / 1920, h / 1080);
      setLayout({ scale: s, x: (w - 1920 * s) / 2, y: (h - 1080 * s) / 2 });
    };
    const onResize = () => requestAnimationFrame(updateLayout);
    updateLayout();
    window.addEventListener("resize", onResize);
    document.addEventListener("fullscreenchange", onResize);
    return () => {
      window.removeEventListener("resize", onResize);
      document.removeEventListener("fullscreenchange", onResize);
    };
  }, []);

  // ── F11 fullscreen toggle ─────────────────────────────────────────────────
  useEffect(() => {
    const onKey = (e) => {
      if (e.key === "F11") {
        e.preventDefault();
        window.pywebview?.api?.toggle_fullscreen();
      }
    };
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, []);

  // ── Wait for pywebview API then load config ───────────────────────────────
  useEffect(() => {
    const loadConfig = async () => {
      const cfg = await window.pywebview.api.get_config();
      setConfig(cfg);

      // Override global UNIVERSES with real data from Python
      window.UNIVERSES = cfg.universes.map(u => ({
        id:        u.id,
        name:      u.name,
        tag:       u.tag,
        codename:  u.name.toUpperCase(),
        accent:    `var(--u-${u.id})`,
        blurb:     "",
        positions: u.positions,
        sample:    u.positions,
      }));
    };

    if (window.pywebview) {
      loadConfig();
    } else {
      window.addEventListener("pywebviewready", loadConfig, { once: true });
    }
  }, []);

  // ── Image URL helper ──────────────────────────────────────────────────────
  const imgUrl = useCallback((charName, ext = "jpeg") => {
    if (!charName || !universeConfig) return null;
    return `http://127.0.0.1:${PORT}/${universeConfig.assetFolder}/${encodeURIComponent(charName)}.${ext}`;
  }, [universeConfig]);

  // ── Universe picker ───────────────────────────────────────────────────────
  const handleSelectUniverse = (universeId) => {
    setSelectedId(universeId);
    const u = config.universes.find(u => u.id === universeId);
    setUniverseConfig(u);
    setMode(u.defaultFilter);
    setScreen("players");
  };

  // ── Start game ────────────────────────────────────────────────────────────
  const handleStartGame = async () => {
    const u = universeConfig;
    const result = await window.pywebview.api.start_match(
      u.id, mode,
      p1 || "Player 1", p2 || "Player 2"
    );
    setDraft(result);
    setScreen("draft");
  };

  // ── Draft actions (call Python, update draft state) ───────────────────────
  const handleGacha = async () => {
    const result = await window.pywebview.api.gacha();
    setDraft(result);
    return result;
  };

  const handleAssign = async (positionName) => {
    const result = await window.pywebview.api.assign(positionName);
    setDraft(result);
  };

  const handleSkip = async () => {
    const result = await window.pywebview.api.skip();
    setDraft(result);
  };

  const handleSwitch = async (posA, posB) => {
    const result = await window.pywebview.api.switch_positions(posA, posB);
    setDraft(result);
  };

  const handleUndo = async () => {
    const result = await window.pywebview.api.undo();
    setDraft(result);
  };

  const handlePass = async () => {
    const result = await window.pywebview.api.pass_turn();
    setDraft(result);
  };

  const handleFinish = () => setScreen("result");

  const handleRestart = async () => {
    await window.pywebview.api.reset();
    setDraft(null);
    setP1("");
    setP2("");
    setScreen("lobby");
  };

  // ── Loading ───────────────────────────────────────────────────────────────
  if (!config) {
    return (
      <div style={{
        position: "fixed", inset: 0, background: "#07080c",
        display: "grid", placeItems: "center",
        fontFamily: "monospace", color: "#5b6076", letterSpacing: "0.28em", fontSize: 13,
      }}>
        LOADING…
      </div>
    );
  }

  const universe = config.universes.find(u => u.id === selectedId) || config.universes[0];

  return (
    <div className="stage-wrap">
      <div className="stage" style={{ transform: `scale(${layout.scale})`, left: layout.x, top: layout.y }}>
        {screen === "lobby" && (
          <LobbyScreen
            onSelect={handleSelectUniverse}
            selectedId={selectedId}
            setSelectedId={setSelectedId}
          />
        )}

        {screen === "players" && universeConfig && (
          <PlayersScreen
            universe={universe}
            mode={mode}
            setMode={setMode}
            p1={p1}
            p2={p2}
            setP1={setP1}
            setP2={setP2}
            onBack={() => setScreen("lobby")}
            onStart={handleStartGame}
            quickNames={config.quickNames}
          />
        )}

        {screen === "draft" && draft && (
          <DraftScreen
            universe={universe}
            p1={p1 || "Player 1"}
            p2={p2 || "Player 2"}
            draft={draft}
            onFinish={handleFinish}
            mode={mode}
            onGacha={handleGacha}
            onAssign={handleAssign}
            onSkip={handleSkip}
            onSwitch={handleSwitch}
            onUndo={handleUndo}
            imgUrl={imgUrl}
            onMenu={handleRestart}
            onPlayers={() => setScreen("players")}
            onPass={handlePass}
          />
        )}

        {screen === "result" && draft && (
          <ResultScreen
            universe={universe}
            p1={p1 || "Player 1"}
            p2={p2 || "Player 2"}
            draft={draft}
            onRestart={handleRestart}
            imgUrl={imgUrl}
          />
        )}
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
