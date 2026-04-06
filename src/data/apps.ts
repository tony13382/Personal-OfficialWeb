export interface AppInfo {
    slug: string
    name: string
    description: string
    url: string
    cover?: string
    projectSlug?: string
}

export const apps: AppInfo[] = [
    {
        slug: 'cloudbio',
        name: 'CloudBio',
        description: 'Bio Link 管理工具',
        url: 'https://bio.lumakes.com/',
        cover: '/og/apps-cloudbio.png',
        projectSlug: 'cloudbio',
    },
    {
        slug: 'kit',
        name: 'Kit',
        description: '書籤管理工具',
        url: 'https://kit.lumakes.com/intro',
        cover: '/og/apps-kit.png',
        projectSlug: 'kit',
    },
]
