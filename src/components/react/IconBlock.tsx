import { cn } from "@/lib/utils"
import * as PhosphorIcons from "@phosphor-icons/react"
import { formatHighlight } from "@/lib/formatters"

interface IconBlockProps {
  title?: string
  subtitle?: string
  href?: string
  icon?: string | undefined
  className?: string
  iconClassName?: string
}

export function IconBlock({
  title,
  subtitle,
  href,
  icon = undefined,
  className,
  iconClassName
}: IconBlockProps) {
  // Dynamically get the Phosphor icon component
  const IconComponent = (icon && PhosphorIcons[icon as keyof typeof PhosphorIcons] as PhosphorIcons.Icon) || PhosphorIcons.AcornIcon

  const content = (
    <div className={cn(
      "flex items-center gap-3 p-2 border rounded-lg transition-shadow",
      href && "hover:shadow-md cursor-pointer hover:border-[var(--theme-primary)]",
      className
    )}
    >
      {icon && (<div
        className="flex items-center justify-center size-12 rounded-lg text-white flex-shrink-0"
        style={{ backgroundColor: 'var(--theme-primary)' }}
      >
        <IconComponent className={`size-6 ${iconClassName}`} />
      </div>)}
      <div className="flex-1 min-w-0">
        {title && <p className="font-bold m-0 break-words" dangerouslySetInnerHTML={{ __html: formatHighlight(title) }} />}
        {subtitle && <p className="text-sm text-gray-500 m-0 break-words" dangerouslySetInnerHTML={{ __html: formatHighlight(subtitle) }} />}
      </div>
    </div>
  )

  if (href) {
    return (
      <a href={href} target="_blank" rel="noopener noreferrer" className="no-underline text-inherit">
        {content}
      </a>
    )
  }

  return content
}
