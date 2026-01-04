import { EnvelopeIcon, FacebookLogoIcon, LinkedinLogoIcon, LaptopIcon, MedalIcon, BriefcaseIcon, MessengerLogoIcon } from '@phosphor-icons/react'

export interface NavLink {
    href: string
    label: string
    icon?: React.ReactNode
    external?: boolean
}

export const mainLinks: NavLink[] = [
    // { href: '/projects/', label: '所有作品', icon: <LaptopIcon className='size-8 me-2' /> },
    { href: '/awards/', label: '得獎紀錄', icon: <MedalIcon className='size-8 me-2' /> },
    { href: '/jobs/', label: '經驗', icon: <BriefcaseIcon className='size-8 me-2' /> },
]

export const socialLinks: NavLink[] = [
    {
        href: 'mailto:liangchinlu@gmail.com',
        label: '信箱',
        icon: <EnvelopeIcon className="size-5" />,
        external: true,
    },
    {
        href: 'https://www.facebook.com/tony13382/',
        label: 'Facebook',
        icon: <MessengerLogoIcon className="size-5" />,
        external: true,
    },
    {
        href: 'https://www.linkedin.com/in/liang-chin-lu/',
        label: 'LinkedIn',
        icon: <LinkedinLogoIcon className="size-5" />,
        external: true,
    },
]