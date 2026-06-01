import { useState, useEffect } from 'react'

// State that mirrors itself to localStorage. `initial` may be a value or a
// lazy initializer; it's only used when the key isn't set yet. `parse` turns
// the stored string back into a value, `serialize` does the reverse, and
// `onChange` runs a side effect (e.g. pushing a volume into the audio engine)
// whenever the value changes.
export function usePersistedState(
  key,
  initial,
  { parse, serialize, onChange } = {},
) {
  const [value, setValue] = useState(() => {
    const raw = localStorage.getItem(key)
    if (raw === null) return typeof initial === 'function' ? initial() : initial
    return parse ? parse(raw) : raw
  })

  useEffect(() => {
    localStorage.setItem(key, serialize ? serialize(value) : value)
    onChange?.(value)
  }, [value])

  return [value, setValue]
}
