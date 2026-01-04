// 主題顏色系統（對應原 Python ThemeColor）
export const themes = {
  home: { primary: '#7c6e69', secondary: '#49413d' },
  red: { primary: '#804C4C', secondary: '#503030' },
  orange: { primary: '#805F4C', secondary: '#503C30' },
  yellow: { primary: '#807E4C', secondary: '#6F6D42' },
  green: { primary: '#4C8077', secondary: '#30504A' },
  blue: { primary: '#4C6D80', secondary: '#304450' },
  purple: { primary: '#727196', secondary: '#555474' },
  pink: { primary: '#804C78', secondary: '#653A5E' },
  natural: { primary: '#555555', secondary: '#2B2B2B' },
} as const

export type ThemeName = keyof typeof themes
