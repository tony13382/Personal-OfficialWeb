import { BriefcaseIcon, MegaphoneIcon } from '@phosphor-icons/react'

export interface NavLink {
    href: string
    label: string
    icon?: React.ReactNode
    external?: boolean
}

export const mainLinks: NavLink[] = [
    { href: '/experience/', label: '經歷', icon: <BriefcaseIcon className='size-6 me-1' /> },
    { href: '/toolbox/', label: '分享專欄', icon: <MegaphoneIcon className='size-6 me-1' /> },
]