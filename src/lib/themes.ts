// 主題顏色系統（對應原 Python ThemeColor）
// primary/secondary: 淺色模式；darkPrimary/darkSecondary: 深色模式
// 深色模式使用的是提亮後的色系，在 #1E2023 背景上讀得清楚
export const themes = {
  home: {
    primary: '#7c6e69', secondary: '#49413d',
    darkPrimary: '#B8AAA4', darkSecondary: '#D4C4BD',
  },
  red: {
    primary: '#804C4C', secondary: '#503030',
    darkPrimary: '#D99494', darkSecondary: '#E6B0B0',
  },
  orange: {
    primary: '#805F4C', secondary: '#503C30',
    darkPrimary: '#D9AE94', darkSecondary: '#E6C7B0',
  },
  yellow: {
    primary: '#807E4C', secondary: '#6F6D42',
    darkPrimary: '#D9D594', darkSecondary: '#E6E2B0',
  },
  green: {
    primary: '#4C8077', secondary: '#30504A',
    darkPrimary: '#94D9CC', darkSecondary: '#B0E6DB',
  },
  blue: {
    primary: '#4C6D80', secondary: '#304450',
    darkPrimary: '#94BDD9', darkSecondary: '#B0CFE6',
  },
  purple: {
    primary: '#727196', secondary: '#555474',
    darkPrimary: '#B7B5D9', darkSecondary: '#CECDE6',
  },
  pink: {
    primary: '#804C78', secondary: '#653A5E',
    darkPrimary: '#D994C8', darkSecondary: '#E6B0D8',
  },
  natural: {
    primary: '#555555', secondary: '#2B2B2B',
    darkPrimary: '#A8A8A8', darkSecondary: '#C4C4C4',
  },
} as const

export type ThemeName = keyof typeof themes
