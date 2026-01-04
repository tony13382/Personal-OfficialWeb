/**
 * Spacing Utilities - Mirrors Python's GapSet and SpaceSet
 * Converts spacing configurations to Tailwind CSS classes
 */

/**
 * Gap size options matching Python GapSet
 */
export type GapSize = 'nano' | 'small' | 'regular' | 'large'

/**
 * Maps gap sizes to Tailwind gap classes
 * nano: gap-0 (0px)
 * small: gap-1 (0.25rem / 4px)
 * regular: gap-2 (0.5rem / 8px)
 * large: gap-4 (1rem / 16px)
 */
export const gapClasses: Record<GapSize, string> = {
  nano: 'gap-0',
  small: 'gap-1',
  regular: 'gap-2',
  large: 'gap-4',
}

/**
 * Spacing configuration interface matching Python SpaceSet
 * Supports margin (m) and padding (p) with directional variants
 */
export interface SpaceConfig {
  // Margin properties
  m?: number    // margin (all sides)
  mx?: number   // margin-left + margin-right
  my?: number   // margin-top + margin-bottom
  mt?: number   // margin-top
  mb?: number   // margin-bottom
  ms?: number   // margin-start (left in LTR)
  me?: number   // margin-end (right in LTR)

  // Padding properties
  p?: number    // padding (all sides)
  px?: number   // padding-left + padding-right
  py?: number   // padding-top + padding-bottom
  pt?: number   // padding-top
  pb?: number   // padding-bottom
  ps?: number   // padding-start (left in LTR)
  pe?: number   // padding-end (right in LTR)
}

/**
 * Converts SpaceConfig object to Tailwind spacing classes
 *
 * @param config - Object with spacing properties
 * @returns Space-separated string of Tailwind classes
 *
 * @example
 * getSpaceClasses({ mt: 2, mb: 3, px: 4 })
 * // Returns: "mt-2 mb-3 px-4"
 */
export function getSpaceClasses(config: SpaceConfig): string {
  const classes: string[] = []

  // Margin classes
  if (config.m !== undefined) classes.push(`m-${config.m}`)
  if (config.mx !== undefined) classes.push(`mx-${config.mx}`)
  if (config.my !== undefined) classes.push(`my-${config.my}`)
  if (config.mt !== undefined) classes.push(`mt-${config.mt}`)
  if (config.mb !== undefined) classes.push(`mb-${config.mb}`)
  if (config.ms !== undefined) classes.push(`ms-${config.ms}`)
  if (config.me !== undefined) classes.push(`me-${config.me}`)

  // Padding classes
  if (config.p !== undefined) classes.push(`p-${config.p}`)
  if (config.px !== undefined) classes.push(`px-${config.px}`)
  if (config.py !== undefined) classes.push(`py-${config.py}`)
  if (config.pt !== undefined) classes.push(`pt-${config.pt}`)
  if (config.pb !== undefined) classes.push(`pb-${config.pb}`)
  if (config.ps !== undefined) classes.push(`ps-${config.ps}`)
  if (config.pe !== undefined) classes.push(`pe-${config.pe}`)

  return classes.join(' ')
}

/**
 * Helper to get gap class from size
 *
 * @param size - Gap size (nano, small, regular, large)
 * @returns Tailwind gap class
 *
 * @example
 * getGapClass('regular') // Returns: "gap-2"
 */
export function getGapClass(size: GapSize): string {
  return gapClasses[size]
}
