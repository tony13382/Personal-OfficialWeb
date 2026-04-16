import { EnvelopeIcon, LinkedinLogoIcon, InfoIcon, InstagramLogoIcon, CalendarPlusIcon } from '@phosphor-icons/react'
import { type NavLink } from "@/components/header/index"

function isEn() {
  return typeof window !== 'undefined' && window.location.pathname.startsWith('/en/')
}

export function getSocialLinks(): NavLink[] {
  const en = isEn()
  return [
    {
      href: 'mailto:liangchinlu@gmail.com',
      label: en ? 'Email' : '信箱',
      icon: <EnvelopeIcon className="size-5" />,
      external: true,
    },
    {
      href: 'https://www.linkedin.com/in/liang-chin-lu/',
      label: 'LinkedIn',
      icon: <LinkedinLogoIcon className="size-5" />,
      external: true,
    },
    {
      href: 'https://www.instagram.com/liang_chin_ml/',
      label: 'Instagram',
      icon: <InstagramLogoIcon className="size-5" />,
      external: true,
    },
    {
      href: 'https://calendar.notion.so/meet/liangchin/short',
      label: en ? 'Book a Meeting' : '預約會議',
      icon: <CalendarPlusIcon className="size-5" />,
      external: true,
    },
    {
      href: 'https://bio.lumakes.com/liang',
      label: en ? 'More Info' : '更多資料',
      icon: <InfoIcon className="size-5" />,
      external: true,
    },
  ]
}

/** @deprecated Use getSocialLinks() */
export const socialLinks = getSocialLinks()



export function HeaderSocialLinks() {
  const links = getSocialLinks()
  return (
    <>
      {links.map((link) => (
        <a
          key={link.href}
          href={link.href}
          target="_blank"
          rel="noopener noreferrer"
          aria-label={link.label}
          className="flex items-center gap-2 px-4 py-2 text-muted-foreground rounded-full transition-all hover:text-foreground hover:bg-muted hover:[&>span]:inline whitespace-nowrap"
        >
          {link.icon}
          <span className='hidden'>{link.label}</span>
        </a>
      ))}
    </>
  )
}


export function SocialLinksLite() {
  const links = getSocialLinks()
  return (
    <>
      {links.map((link) => (
        <a
          key={link.href}
          href={link.href}
          target="_blank"
          rel="noopener noreferrer"
          aria-label={link.label}
          className="flex items-center gap-2 p-3 text-muted-foreground rounded-full transition-all hover:text-foreground hover:bg-muted hover:[&>span]:block"
        >
          {link.icon}
        </a>
      ))}
    </>
  )
}
