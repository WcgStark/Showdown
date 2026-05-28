// Two independent audio channels — UI clicks vs SFX (haki, future per-universe
// effects). Each volume is a module-level value updated from App via setters,
// and exposed via getters so components mount-time captures still see live
// updates (since the value is read at play() time).

let _uiVol  = 0.9
let _sfxVol = 0.9

export const setUiVolume  = (v) => { _uiVol  = v }
export const setSfxVolume = (v) => { _sfxVol = v }

export const getUiVolume  = () => _uiVol
export const getSfxVolume = () => _sfxVol

const clamp = (v) => Math.max(0, Math.min(1, v))

export const playUi = () => {
  try {
    const a = new Audio('./sounds/ui%20sound.mp3')
    a.volume = clamp(_uiVol)
    a.play().catch(() => {})
  } catch {}
}

// Global listener — fires for every <button> click anywhere in the app
if (typeof document !== 'undefined') {
  document.addEventListener('mousedown', (e) => {
    if (e.target.closest('button')) playUi()
  }, true)
}
