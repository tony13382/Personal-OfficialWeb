import { defineCollection, z } from 'astro:content'

// 通用 Schema
const LinkButtonSchema = z.object({
  content: z.string(),
  href: z.string(),
  icon: z.string().optional(),
  openInTab: z.boolean().default(true)
})

const ToolSchema = z.object({
  name: z.string(),
  description: z.string()
})

const ScoreSchema = z.object({
  title: z.string(),
  award: z.string(),
  category: z.string().optional()
})

// Projects Collection
const projectsCollection = defineCollection({
  type: 'content',  // MDX 內容
  schema: z.object({
    // 基本資訊
    title: z.string(),
    description: z.string(),
    subdescription: z.string().optional(),

    // 時間與狀態
    startDate: z.coerce.date(),
    endDate: z.coerce.date().optional().nullable(),
    status: z.enum(['active', 'closed', 'paused']).default('active'),

    // 視覺與分類
    theme: z.enum(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'natural', 'home']),
    cover: z.string(),
    pin: z.boolean().default(false),

    // 分類與標籤
    skillTypes: z.array(z.enum(['dev', 'design', 'plan'])).default([]),
    tags: z.array(z.string()).default([]),

    // 關聯資料
    links: z.array(LinkButtonSchema).default([]),
    tools: z.array(ToolSchema).default([]),
    scores: z.array(ScoreSchema).default([]),

    // SEO
    seo: z.object({
      metaTitle: z.string().optional(),
      metaDescription: z.string().optional(),
      ogImage: z.string().optional()
    }).optional()
  })
})

// Jobs Collection
const jobsCollection = defineCollection({
  type: 'content',  // MDX 內容
  schema: z.object({
    // 基本資訊
    title: z.string(),
    company: z.string(),

    // 時間
    startDate: z.coerce.date().optional().nullable(),
    endDate: z.coerce.date().optional().nullable(),

    // 視覺
    theme: z.enum(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'natural', 'home']),
    cover: z.string(),
    logo: z.string().optional(),

    // 工作描述
    description: z.array(z.string()).default([]),

    // SEO
    seo: z.object({
      metaTitle: z.string().optional(),
      metaDescription: z.string().optional(),
      ogImage: z.string().optional()
    }).optional()
  })
})

export const collections = {
  projects: projectsCollection,
  jobs: jobsCollection,
}
