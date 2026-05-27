let _vol = 0.9

export const setUiVolume = (v) => { _vol = v }

export const playUi = () => {
  try {
    const a = new Audio('./sounds/ui%20sound.mp3')
    a.volume = Math.max(0, Math.min(1, _vol))
    a.play().catch(() => {})
  } catch {}
}

// Global listener — fires for every <button> click anywhere in the app
if (typeof document !== 'undefined') {
  document.addEventListener('mousedown', (e) => {
    if (e.target.closest('button')) playUi()
  }, true)
}
