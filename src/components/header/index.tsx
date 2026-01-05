import { MedalIcon, BriefcaseIcon } from '@phosphor-icons/react'

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