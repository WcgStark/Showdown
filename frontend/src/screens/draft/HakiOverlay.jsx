import { useEffect } from 'react'

/* ── Haki cinematic overlay ──────────────────────────────────────────────── */
// Portrait center inside the ActionPanel (right: 64, width: 380) at 1920×1080
const HAKI_OX = 1666 // 1920 - 64 - 380/2
const HAKI_OY = 272  // panel top 80 + padding 18 + label ~20 + marginTop 14 + portrait 280/2

const HakiOverlay = ({ onComplete, sfxVolume = 0.9 }) => {
  useEffect(() => {
    const audio = new Audio(
      "./sfx/one%20piece/Monkey%20D%20Luffy%20Haki%20Sound%20%20One%20Piece.mp3"
    )
    audio.volume = Math.max(0, Math.min(1, sfxVolume))
    audio.play().catch(() => {})
    const t = setTimeout(onComplete, 3600)
    return () => clearTimeout(t)
  }, [])

  const ox = `${HAKI_OX}px`, oy = `${HAKI_OY}px`
  const pctX = (HAKI_OX / 1920 * 100).toFixed(1)
  const pctY = (HAKI_OY / 1080 * 100).toFixed(1)

  return (
    <div style={{ position: "absolute", inset: 0, zIndex: 100, pointerEvents: "none", overflow: "hidden" }}>

      {/* Backdrop darkens the screen but stays transparent over the portrait */}
      <div style={{
        position: "absolute", inset: 0,
        background: `radial-gradient(ellipse 42% 52% at ${pctX}% ${pctY}%, transparent 0%, transparent 28%, rgba(0,0,0,0.92) 80%, rgba(0,0,0,0.97) 100%)`,
        animation: "hakiFlash 3.6s ease-out forwards",
      }} />

      {/* Three red rings expanding from portrait */}
      {[0, 0.28, 0.56].map((delay, i) => (
        <div key={i} style={{
          position: "absolute", left: ox, top: oy,
          width: 180, height: 180, borderRadius: "50%",
          border: "2px solid rgba(225, 0, 0, 0.97)",
          boxShadow: "0 0 32px rgba(220, 0, 0, 0.82), inset 0 0 32px rgba(200, 0, 0, 0.28)",
          transform: "translate(-50%, -50%) scale(0)", opacity: 0,
          animation: `hakiRing 2s ${delay}s cubic-bezier(0.06, 0.82, 0.26, 1) forwards`,
        }} />
      ))}

      {/* Screen-edge red glow + shake */}
      <div style={{
        position: "absolute", inset: 0,
        boxShadow: "inset 0 0 110px rgba(190,0,0,0.48)",
        animation: "hakiShake 0.55s ease-out, hakiFlash 3.6s ease-out forwards",
      }} />
    </div>
  )
}

export default HakiOverlay
