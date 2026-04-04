import { UserIcon, MegaphoneIcon } from '@phosphor-icons/react'

export interface NavLink {
    href: string
    label: string
    icon?: React.ReactNode
    external?: boolean
}

export const mainLinks: NavLink[] = [
    { href: '/about/', label: '關於', icon: <UserIcon className='size-6 me-1' /> },
    { href: '/articles/', label: '文章', icon: <MegaphoneIcon className='size-6 me-1' /> },
]