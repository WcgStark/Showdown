// Three independent audio channels — UI clicks, SFX (haki etc), and Music.
// Volumes are module-level so play() reads them live (no captured-stale value).

let _uiVol    = 0.9
let _sfxVol   = 0.9
let _musicVol = 0.5

let _music = null
let _musicSrc = null

const clamp = (v) => Math.max(0, Math.min(1, v))

export const setUiVolume    = (v) => { _uiVol    = v }
export const setSfxVolume   = (v) => { _sfxVol   = v }
export const setMusicVolume = (v) => {
  _musicVol = v
  if (_music) _music.volume = clamp(v)
}

export const getUiVolume    = () => _uiVol
export const getSfxVolume   = () => _sfxVol
export const getMusicVolume = () => _musicVol

export const playUi = () => {
  try {
    const a = new Audio('./sounds/ui%20sound.mp3')
    a.volume = clamp(_uiVol)
    a.play().catch(() => {})
  } catch {}
}

export const playUiHover = () => {
  try {
    const a = new Audio('./sounds/ui%20hover.mp3')
    a.volume = clamp(_uiVol)
    a.play().catch(() => {})
  } catch {}
}

export const playNumberOne = () => {
  try {
    const a = new Audio('./sounds/Number%20One%20-%20Bankai%20-%20Shiro%20Sagisu.mp3')
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playYokosoWatashi = () => {
  try {
    const a = new Audio('./sounds/Yokoso%20watashi%20no%20soul%20society.mp3')
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playYhwachEntrance = () => {
  try {
    const a = new Audio('./sounds/Yhwach%20Entrance%20Theme.mp3')
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playMusic = (urls) => {
  if (!urls || urls.length === 0) { stopMusic(); return }
  const url = urls[Math.floor(Math.random() * urls.length)]
  if (_music && _musicSrc === url) return
  stopMusic()
  try {
    _music = new Audio(encodeURI(url))
    _music.volume = clamp(_musicVol)
    _music.loop = true
    _music.play().catch(() => {})
    _musicSrc = url
  } catch {}
}

export const stopMusic = () => {
  if (_music) {
    try { _music.pause() } catch {}
    _music.src = ''
    _music = null
  }
  _musicSrc = null
}

// Global listener — fires for every <button> click anywhere in the app
if (typeof document !== 'undefined') {
  document.addEventListener('mousedown', (e) => {
    if (e.target.closest('button')) playUi()
  }, true)
}
