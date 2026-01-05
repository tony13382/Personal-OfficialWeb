import { EnvelopeIcon, LinkedinLogoIcon, InfoIcon, InstagramLogoIcon, GithubLogoIcon, CalendarPlusIcon } from '@phosphor-icons/react'
import { type NavLink } from "@/components/header/index"

export const socialLinks: NavLink[] = [
    {
        href: 'mailto:liangchinlu@gmail.com',
        label: '信箱',
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
        href: 'https://github.com/tony13382',
        label: 'Github',
        icon: <GithubLogoIcon className="size-5" />,
        external: true,
    },
    {
        href: 'https://www.instagram.com/liang_chin_ml/',
        label: 'Instagram',
        icon: <InstagramLogoIcon className="size-5" />,
        external: true,
    },
    {
        href: 'https://calendar.notion.so/meet/liangchin/onehour',
        label: '預約會議',
        icon: <CalendarPlusIcon className="size-5" />,
        external: true,
    },
    // {
    //     href: 'https://www.facebook.com/tony13382/',
    //     label: 'Facebook',
    //     icon: <MessengerLogoIcon className="size-5" />,
    //     external: true,
    // },
    {
        href: 'https://portaly.cc/liang_chin_ml',
        label: '更多資料',
        icon: <InfoIcon className="size-5" />,
        external: true,
    },
]



export function HeaderSocialLinks() {
    return (
        <>
            {socialLinks.map((link) => (
                <a
                    key={link.href}
                    href={link.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-2 px-4 py-2 text-muted-foreground rounded-full transition-all hover:text-foreground hover:bg-muted hover:[&>span]:block"
                >
                    {link.icon}
                    <span className='hidden'>{link.label}</span>
                </a>
            ))}
        </>
    )
}


export function SocialLinksLite() {
    return (
        <>
            {socialLinks.map((link) => (
                <a
                    key={link.href}
                    href={link.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-2 p-3 text-muted-foreground rounded-full transition-all hover:text-foreground hover:bg-muted hover:[&>span]:block"
                >
                    {link.icon}
                </a>
            ))}
        </>
    )
}
