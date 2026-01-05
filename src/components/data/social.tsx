import { EnvelopeIcon, LinkedinLogoIcon, MessengerLogoIcon, InfoIcon, InstagramLogoIcon } from '@phosphor-icons/react'
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
        href: 'https://www.instagram.com/liang_chin_ml/',
        label: 'Instagram',
        icon: <InstagramLogoIcon className="size-5" />,
        external: true,
    },
    {
        href: 'https://www.facebook.com/tony13382/',
        label: 'Facebook',
        icon: <MessengerLogoIcon className="size-5" />,
        external: true,
    },
    {
        href: 'https://portaly.cc/liang_chin_ml',
        label: '更多資料',
        icon: <InfoIcon className="size-5" />,
        external: true,
    },
]