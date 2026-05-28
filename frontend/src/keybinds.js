// Keybinding model — uses KeyboardEvent.code (layout-independent) so remapping
// and on-screen labels stay consistent regardless of keyboard layout.

export const DEFAULT_KEYBINDS = {
  confirm: "Enter",
  back:    "Escape",
  gacha:   "Space",
  skip:    "KeyS",
  pass:    "KeyP",
  switch:  "KeyW",
  undo:    "KeyZ",
}

// Order + i18n label key for the Settings list.
export const KEYBIND_ACTIONS = [
  { id: "confirm", labelKey: "kbConfirm" },
  { id: "back",    labelKey: "kbBack" },
  { id: "gacha",   labelKey: "kbGacha" },
  { id: "skip",    labelKey: "kbSkip" },
  { id: "pass",    labelKey: "kbPass" },
  { id: "switch",  labelKey: "kbSwitch" },
  { id: "undo",    labelKey: "kbUndo" },
]

const SPECIAL = {
  Space:        "SPACE",
  Enter:        "ENTER",
  NumpadEnter:  "ENTER",
  Escape:       "ESC",
  ArrowUp:      "↑",
  ArrowDown:    "↓",
  ArrowLeft:    "←",
  ArrowRight:   "→",
  Backspace:    "⌫",
  Tab:          "TAB",
  ShiftLeft:    "SHIFT",
  ShiftRight:   "SHIFT",
  ControlLeft:  "CTRL",
  ControlRight: "CTRL",
  AltLeft:      "ALT",
  AltRight:     "ALT",
}

// KeyboardEvent.code -> short label shown on buttons / settings.
export const codeLabel = (code) => {
  if (!code) return "—"
  if (SPECIAL[code]) return SPECIAL[code]
  if (code.startsWith("Key"))    return code.slice(3)
  if (code.startsWith("Digit"))  return code.slice(5)
  if (code.startsWith("Numpad")) return "N" + code.slice(6)
  return code.toUpperCase()
}

// Load merged keybinds from localStorage (falling back to defaults).
export const loadKeybinds = () => {
  try {
    return { ...DEFAULT_KEYBINDS, ...JSON.parse(localStorage.getItem("hakiKeybinds") || "{}") }
  } catch {
    return { ...DEFAULT_KEYBINDS }
  }
}
