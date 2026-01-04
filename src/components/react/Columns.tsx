/**
 * Columns - Responsive grid system
 * React version for use in MDX
 */
import { getGapClass, type GapSize } from '@/lib/spacing'
import type { ReactNode } from 'react'

interface ColumnsProps {
  gap?: GapSize | number
  cols?: 1 | 2 | 3 | 4 | 6 | 12
  className?: string
  children: ReactNode
}

export function Columns({
  gap = 0,
  cols = 1,
  className = '',
  children
}: ColumnsProps) {
  // Convert gap to class
  const gapClass = typeof gap === 'string'
    ? getGapClass(gap as GapSize)
    : gap > 0
      ? `gap-${gap}`
      : 'gap-0'

  // Map columns to Tailwind grid classes
  const colsClassMap: Record<number, string> = {
    1: 'grid-cols-1',
    2: 'grid-cols-1 md:grid-cols-2',
    3: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3',
    4: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-4',
    6: 'grid-cols-2 md:grid-cols-3 lg:grid-cols-6',
    12: 'grid-cols-12',
  }

  const colsClass = colsClassMap[cols] || 'grid-cols-1'

  const classes = ['grid', colsClass, gapClass, className].filter(Boolean).join(' ')

  return <div className={classes}>{children}</div>
}
