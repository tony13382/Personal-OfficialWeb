import { cn } from "@/lib/utils"
import { formatHighlight } from "@/lib/formatters"
import {
  AcornIcon,
  ChatTeardropTextIcon,
  ClockIcon,
  DatabaseIcon,
  FileArchiveIcon,
  FilePdfIcon,
  FileSqlIcon,
  FileTextIcon,
  FigmaLogoIcon,
  GithubLogoIcon,
  IdentificationBadgeIcon,
  KeyboardIcon,
  LaptopIcon,
  LinkIcon,
  MicrosoftExcelLogoIcon,
  MicrosoftPowerpointLogoIcon,
  MicrosoftWordLogoIcon,
  NumberCircleOneIcon,
  NumberCircleThreeIcon,
  NumberCircleTwoIcon,
  SparkleIcon,
  TextboxIcon,
  WebhooksLogoIcon,
  type Icon,
  FireIcon,
  BroadcastIcon,
  ShareNetworkIcon,
  CardholderIcon,
  CoinVerticalIcon,
  HandCoinsIcon,
  ExportIcon,
  PlaylistIcon,
  PianoKeysIcon,
  MicrophoneIcon,
  PencilIcon,
  ImageIcon,
  HeadphonesIcon,
  FlagIcon,
  TreeStructureIcon,
  ChalkboardTeacherIcon,
  SignatureIcon,
  AddressBookTabsIcon,
  BellRingingIcon,
  EnvelopeOpenIcon
} from "@phosphor-icons/react"

interface IconBlockProps {
  title?: string
  subtitle?: string
  href?: string
  icon?: string | undefined
  className?: string
  iconClassName?: string
}

// Icon mapping - only includes icons actually used in the project
const iconMap: Record<string, Icon> = {
  AcornIcon,
  BroadcastIcon,
  ChatTeardropTextIcon,
  ClockIcon,
  DatabaseIcon,
  FireIcon,
  FileArchiveIcon,
  FilePdfIcon,
  FileSqlIcon,
  FileTextIcon,
  FigmaLogoIcon,
  GithubLogoIcon,
  IdentificationBadgeIcon,
  KeyboardIcon,
  LaptopIcon,
  LinkIcon,
  MicrosoftExcelLogoIcon,
  MicrosoftPowerpointLogoIcon,
  MicrosoftWordLogoIcon,
  NumberCircleOneIcon,
  NumberCircleThreeIcon,
  NumberCircleTwoIcon,
  ShareNetworkIcon,
  SparkleIcon,
  TextboxIcon,
  WebhooksLogoIcon,
  CardholderIcon,
  CoinVerticalIcon,
  HandCoinsIcon,
  ExportIcon,
  PlaylistIcon,
  PianoKeysIcon,
  MicrophoneIcon,
  PencilIcon,
  ImageIcon,
  HeadphonesIcon,
  FlagIcon,
  TreeStructureIcon,
  ChalkboardTeacherIcon,
  SignatureIcon,
  AddressBookTabsIcon,
  BellRingingIcon,
  EnvelopeOpenIcon
}

export function IconBlock({
  title,
  subtitle,
  href,
  icon = undefined,
  className,
  iconClassName
}: IconBlockProps) {
  // Get icon from mapping or use default
  const IconComponent = (icon && iconMap[icon]) || AcornIcon

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
