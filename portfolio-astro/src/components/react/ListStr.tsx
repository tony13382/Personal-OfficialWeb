/**
 * ListStr - Unordered list with text formatting
 * React version for use in MDX
 */
import { formatHighlight } from '@/lib/formatters'

interface ListStrProps {
  items: string[]
  className?: string
}

export function ListStr({ items, className = '' }: ListStrProps) {
  const classes = ['ps-3 m-0 leading-loose', className].filter(Boolean).join(' ')

  return (
    <ul className={classes}>
      {items.map((item, index) => (
        <li key={index} dangerouslySetInnerHTML={{ __html: formatHighlight(item) }} />
      ))}
    </ul>
  )
}
