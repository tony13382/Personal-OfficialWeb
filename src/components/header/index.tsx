import { UserIcon, ArticleIcon, AppWindowIcon, ProjectorScreenChartIcon } from '@phosphor-icons/react'
import type { Locale } from '@/i18n'

export interface NavLink {
    href: string
    label: string
    icon?: React.ReactNode
    external?: boolean
}

const navLabels = {
    'zh-Hant': { about: '關於', articles: '文章', apps: 'APP', projects: '專案' },
    'en': { about: 'About', articles: 'Articles', apps: 'Apps', projects: 'Projects' },
} as const;

export function getMainLinks(locale: Locale = 'zh-Hant'): NavLink[] {
    const labels = navLabels[locale];
    const prefix = locale === 'en' ? '/en' : '';
    return [
        { href: `${prefix}/about/`, label: labels.about, icon: <UserIcon className='size-6 me-1' /> },
        { href: `${prefix}/articles/`, label: labels.articles, icon: <ArticleIcon className='size-6 me-1' /> },
        { href: `${prefix}/apps/`, label: labels.apps, icon: <AppWindowIcon className='size-6 me-1' /> },
        { href: `${prefix}/projects/`, label: labels.projects, icon: <ProjectorScreenChartIcon className='size-6 me-1' /> },
    ];
}

/** @deprecated Use getMainLinks() instead */
export const mainLinks: NavLink[] = getMainLinks('zh-Hant');