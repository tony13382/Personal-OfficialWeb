export interface AppInfo {
    slug: string
    name: string
    description: string
    url: string
    cover?: string
    projectSlug?: string
    mode?: 'iframe' | 'page'
}

export const apps: AppInfo[] = [
    {
        slug: 'cloudbio',
        name: 'CloudBio',
        description: 'Bio Link 管理工具',
        url: 'https://bio.lumakes.com/',
        cover: '/og/apps/cloudbio.png',
        projectSlug: 'cloudbio',
    },
    {
        slug: 'kit',
        name: 'Kit',
        description: '書籤管理工具',
        url: 'https://kit.lumakes.com/intro',
        cover: '/og/apps/kit.png',
        projectSlug: 'kit',
    },
    {
        slug: 'nextags',
        name: 'NexTags',
        description: '自架音樂資料庫管理系統',
        url: 'https://github.com/tony13382/NexTags',
        cover: '/og/apps/nextags.png',
        projectSlug: 'nextags',
        mode: 'page',
    },
]
