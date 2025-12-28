/**
 * ListDiv - Flexible container with grid/flex/inline layouts
 * React version for use in MDX
 */
import { getSpaceClasses, type SpaceConfig, type GapSize, gapClasses } from '@/lib/spacing'
import type { ReactNode } from 'react'

interface ListDivProps {
  gap?: GapSize
  layout?: 'grid' | 'flex' | 'inline'
  space?: SpaceConfig
  className?: string
  children: ReactNode
}

export function ListDiv({
  gap = 'regular',
  layout = 'grid',
  space,
  className = '',
  children
}: ListDivProps) {
  const displayClass = layout === 'flex'
    ? 'flex flex-wrap'
    : layout === 'inline'
      ? 'inline-flex'
      : 'grid'

  const gapClass = gapClasses[gap]
  const spaceClass = space ? getSpaceClasses(space) : ''

  const classes = [displayClass, gapClass, spaceClass, className].filter(Boolean).join(' ')

  return <div className={classes}>{children}</div>
}
