/**
 * LinkButton - Button/link component with theme styling
 * React version for use in MDX
 */

interface LinkButtonProps {
  content: string
  href: string
  fill?: boolean
  openInTab?: boolean
  icon?: string
  className?: string
}

export function LinkButton({
  content,
  href,
  fill = false,
  openInTab = false,
  icon = '',
  className = ''
}: LinkButtonProps) {
  const fillClass = fill ? 'btn-theme' : 'btn-outline-theme'
  const target = openInTab ? '_blank' : undefined
  const rel = openInTab ? 'noopener noreferrer' : undefined

  return (
    <a
      href={href}
      target={target}
      rel={rel}
      className={`btn ${fillClass} rounded-full inline-flex items-center gap-2 ${className}`}
    >
      {icon && <i className={`bi ${icon}`}></i>}
      {content}
    </a>
  )
}
