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

const sfx  = (path) => `./sfx/${path}`
const ui   = (path) => `./ui/${path}`
const enc  = (s)    => s.split('/').map(encodeURIComponent).join('/')

export const playUi = () => {
  try {
    const a = new Audio(ui(enc('ui sound.mp3')))
    a.volume = clamp(_uiVol)
    a.play().catch(() => {})
  } catch {}
}

export const playUiHover = () => {
  try {
    const a = new Audio(ui(enc('ui hover.mp3')))
    a.volume = clamp(_uiVol)
    a.play().catch(() => {})
  } catch {}
}

export const playNumberOne = () => {
  try {
    const a = new Audio(sfx(enc('bleach/Number One - Bankai - Shiro Sagisu.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playYokosoWatashi = () => {
  try {
    const a = new Audio(sfx(enc('bleach/Yokoso watashi no soul society.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playYhwachEntrance = () => {
  try {
    const a = new Audio(sfx(enc('bleach/Yhwach Entrance Theme.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playZankaNTachi = () => {
  try {
    const a = new Audio(sfx(enc('bleach/Zanka no Tachi.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playGoldExperience = () => {
  try {
    const a = new Audio(sfx(enc('jojo/Gold Experience Requiem.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playKillerQueen = () => {
  try {
    const a = new Audio(sfx(enc('jojo/Killer Queen.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playKingCrimson = () => {
  try {
    const a = new Audio(sfx(enc('jojo/King Crimson.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playMadeInHeaven = () => {
  try {
    const a = new Audio(sfx(enc('jojo/Made in Heaven.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playNigerundayo = () => {
  try {
    const a = new Audio(sfx(enc('jojo/Nigerundayo.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playYareYareDaze = () => {
  try {
    const a = new Audio(sfx(enc('jojo/Yare Yare Daze.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playZaWarudo = () => {
  try {
    const a = new Audio(sfx(enc('jojo/Za Warudo.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playGojoRyoiki = () => {
  try {
    const a = new Audio(sfx(enc('jujutsu/Gojo - Ryoiki tenkai.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playSukunaRyoiki = () => {
  try {
    const a = new Audio(sfx(enc('jujutsu/Sukuna - Ryoiki tenkai.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playHigurumaRyoiki = () => {
  try {
    const a = new Audio(sfx(enc('jujutsu/Higuruma - Ryoiki tenkai.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playMegumiRyoiki = () => {
  try {
    const a = new Audio(sfx(enc('jujutsu/Megumi - Ryoiki tenkai.mp3')))
    a.volume = clamp(_sfxVol)
    a.play().catch(() => {})
  } catch {}
}

export const playYutaRika = () => {
  try {
    const a = new Audio(sfx(enc('jujutsu/Yuta - Rika.mp3')))
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
