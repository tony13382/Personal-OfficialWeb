/**
 * Text - Typography component with highlighting and auto-ID generation
 * React version for use in MDX
 */
import { formatHighlight } from '@/lib/formatters'

interface TextProps {
  content: string
  tag?: 'h2' | 'h3' | 'h4' | 'p' | 'span'
  bold?: boolean
  center?: boolean
  pillType?: boolean
  className?: string
}

export function Text({
  content,
  tag = 'p',
  bold = false,
  center = false,
  pillType = false,
  className = ''
}: TextProps) {
  const isHeading = ['h2', 'h3', 'h4'].includes(tag)

  // Generate ID for headings (for anchor links)
  const id = isHeading
    ? content.replace(/\s+/g, '_').replace(/`/g, '')
    : undefined

  const classes = [
    'm-0 p-0',
    bold && 'font-bold',
    center && 'text-center',
    className
  ].filter(Boolean).join(' ')

  // Apply backtick highlighting
  const formattedContent = formatHighlight(content)

  const Element = tag as keyof React.JSX.IntrinsicElements

  if (pillType) {
    return (
      <span
        className={`badge bg-[var(--theme-primary)] text-white rounded-full overflow-hidden text-base ${classes}`}
        id={id}
      >
        <Element className="m-0 p-0" dangerouslySetInnerHTML={{ __html: formattedContent }} />
      </span>
    )
  }

  return (
    <Element
      className={classes}
      id={id}
      dangerouslySetInnerHTML={{ __html: formattedContent }}
    />
  )
}
