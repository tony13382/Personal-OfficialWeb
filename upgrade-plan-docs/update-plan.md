# 作品集網站重構計劃 - Astro + shadcn/ui

## 📋 專案概述

### 重構目標
- 從 Python 靜態生成器遷移到 Astro
- 使用 MDX 管理內容（Markdown + React 組件）
- 整合 shadcn/ui 構建現代化 UI
- 保持完美的 SEO 優化
- 提升開發體驗與維護性

### 技術選型
- **框架**: Astro (SSG)
- **UI 組件**: shadcn/ui (React)
- **內容格式**: MDX (Markdown + JSX)
- **樣式**: Tailwind CSS
- **類型安全**: TypeScript + Zod
- **部署**: Netlify (保持現有方式)

---

## 🏗️ 項目架構

```
portfolio/                           # 新項目根目錄
├── src/
│   ├── content/
│   │   ├── config.ts                # Content Collections 配置（類型定義）
│   │   ├── projects/
│   │   │   ├── mind-reader.mdx      # MDX 格式的專案
│   │   │   ├── panda-chinese.mdx
│   │   │   ├── soeasy-edu-ai.mdx
│   │   │   └── ... (共 14 個專案)
│   │   ├── jobs/
│   │   │   ├── 2024-solwen-ai.mdx
│   │   │   ├── 2023-tiic.mdx
│   │   │   ├── 2022-tiic-intern.mdx
│   │   │   └── ... (共 7 個工作經驗)
│   │   └── skills/
│   │       ├── develope.mdx
│   │       ├── design.mdx
│   │       ├── plan.mdx
│   │       └── other.mdx
│   ├── components/
│   │   ├── ui/                      # shadcn React 組件
│   │   │   ├── card.tsx
│   │   │   ├── badge.tsx
│   │   │   ├── accordion.tsx
│   │   │   ├── button.tsx
│   │   │   └── ... (其他 shadcn 組件)
│   │   ├── react/                   # 自定義 React 組件（互動式）
│   │   │   ├── ProjectCard.tsx
│   │   │   ├── JobCard.tsx
│   │   │   ├── SkillGroup.tsx
│   │   │   ├── Youtube.tsx
│   │   │   ├── IconBlock.tsx
│   │   │   └── ImageCarousel.tsx
│   │   └── astro/                   # Astro 組件（靜態，0 JS）
│   │       ├── Navbar.astro
│   │       ├── Footer.astro
│   │       └── Hero.astro
│   ├── layouts/
│   │   ├── BaseLayout.astro         # 基礎佈局（含 SEO meta tags）
│   │   ├── ProjectLayout.astro      # 專案詳情佈局
│   │   └── JobLayout.astro          # 工作經驗佈局
│   ├── pages/
│   │   ├── index.astro              # 首頁
│   │   ├── projects/
│   │   │   ├── index.astro          # 專案列表頁
│   │   │   └── [slug].astro         # 專案詳情（動態路由）
│   │   ├── jobs/
│   │   │   ├── index.astro          # 工作經驗列表
│   │   │   └── [slug].astro         # 工作詳情
│   │   ├── skills/
│   │   │   └── [slug].astro         # 技能詳情
│   │   └── awards.astro             # 獎項頁面
│   ├── styles/
│   │   └── global.css               # Tailwind + 自定義樣式
│   └── lib/
│       ├── themes.ts                # 主題顏色系統
│       ├── utils.ts                 # 工具函數（cn helper）
│       └── constants.ts             # 常量定義
├── public/
│   └── assets/                      # 靜態資源（複製現有的）
│       ├── imgs/
│       ├── stylesheets/
│       └── favicon.png
├── migration/                       # 遷移腳本
│   └── convert_to_mdx.py            # Python → MDX 轉換器
├── astro.config.mjs                 # Astro 配置
├── tailwind.config.mjs              # Tailwind 配置
├── tsconfig.json                    # TypeScript 配置
└── package.json
```

---

## 📄 Content Collections Schema

### `src/content/config.ts`

```typescript
import { defineCollection, z } from 'astro:content'

// ========== 通用 Schema ==========

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

// ========== Projects Collection ==========

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
    skillTypes: z.array(z.string()).default([]),
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

// ========== Jobs Collection ==========

const jobsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),                 // 職位名稱
    jobName: z.string(),                // 公司名稱
    startDate: z.coerce.date(),
    endDate: z.coerce.date().optional().nullable(),
    theme: z.enum(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'natural', 'home']),
    cover: z.string(),
    description: z.array(z.string()).default([]),  // 職位描述列表
    tags: z.array(z.string()).default([])
  })
})

// ========== Skills Collection ==========

const skillsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    theme: z.enum(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'natural', 'home']),
    icon: z.string(),                   // Bootstrap Icons class
    order: z.number().default(0)        // 排序順序
  })
})

export const collections = {
  projects: projectsCollection,
  jobs: jobsCollection,
  skills: skillsCollection
}
```

**優勢**:
- ✅ TypeScript 自動生成類型
- ✅ 構建時內容驗證
- ✅ 編輯器自動補全
- ✅ Zod 提供運行時檢查

---

## 📝 MDX 內容範例

### `src/content/projects/mind-reader.mdx`

```mdx
---
title: MindReader 與你心譯相通
description: 透過文本分析技術微調用戶輸入文本，經由技術精準的表達出文字中所包含的情感和意思，減少生活上的誤會。
subdescription: 擔任：CTO, Product Designer<br>負責：軟體架構設計、產品介面設計、資料庫設計、軟體開發、技術管理
startDate: 2019-11-01
endDate: 2020-12-31
status: closed
theme: orange
cover: /assets/imgs/projects/mindReader/cover.png
pin: true
skillTypes: [pin, dev, design, analysis]
tags: [介面設計, 產品規劃, UX 優化, API 開發, NLP, Azure]
links:
  - content: 專案網址
    href: https://github.com/tony13382/MindReader-MVP
    icon: bi-github
    openInTab: true
scores:
  - title: 2021 大專校院資訊應用服務創新競賽
    award: 佳作
    category: 資訊應用組
  - title: 2021 大專校院資訊應用服務創新競賽
    award: 第三名
    category: Azure 雲端組
  - title: 中原大學資管系 110 學年度資訊管理畢業專題競賽
    award: 第一名
  - title: 109 學年度中原大學資管系資訊管理專題初賽
    award: 第二名
  - title: 110 年中原大學高教深耕學生解決企業問題研究團隊計畫
    award: 佳作
tools:
  - name: Figma
    description: UI 設計與產品原型設計
  - name: Bootstrap V5.0
    description: 前端元件套件
  - name: Azure LUIS
    description: NLP 自然語言處理、文字意圖分析
  - name: Firebase
    description: NoSQL 資料庫設計與串接
  - name: Flask
    description: API 伺服器開發
  - name: Django
    description: LineBot 伺服器開發
  - name: Jieba
    description: NLP 中文斷詞與字典訓練
  - name: OpenCC
    description: 簡繁轉換文字處理
seo:
  metaTitle: MindReader 與你心譯相通 - 呂亮進的專案作品
  metaDescription: 透過 NLP 技術打造的智慧聊天輔助系統，獲得 2021 大專校院資訊應用服務創新競賽佳作
  ogImage: /assets/imgs/projects/mindReader/cover.png
---

import { Card, CardHeader, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Youtube } from '@/components/react/Youtube'
import { IconBlock } from '@/components/react/IconBlock'

## 專案介紹

<Card className="my-6">
  <CardHeader>
    <Youtube embedUrl="https://www.youtube.com/embed/VzLFWFRzGh8" client:visible />
  </CardHeader>
  <CardContent>
    相信使用過通訊軟體的人都曾遇到過這些問題：說話詞不達意和因感受不到對方情緒而造成誤會，這是因為每個人對訊息文字的解讀都有所不同，嚴重時甚至會導致人際關係上的破裂。為了解決以上這些問題，我們想出了一種輔助聊天的應用程式。它能幫助人們精準的表達出文字中所包含的情感和意思，從而減少誤會的發生，讓文字變得更有溫度，就算隔著螢幕，也能感覺像是面對面談話一般。
  </CardContent>
</Card>

## 產品優勢

<div className="space-y-6">
  <div>
    <Badge variant="default" className="mb-2 font-bold">客製化對話情境</Badge>
    <p className="text-gray-700">為聊天對象設定角色定位並打造出專屬於你的客製化說話情境。希望能藉此系統為使用者雙方都帶來舒適的聊天體驗，不會因為是透過文字傳遞訊息而有所誤會甚至是產生衝突，解決文字訊息中無法確切傳遞出情感的問題。</p>
  </div>

  <div>
    <Badge variant="default" className="mb-2 font-bold">聊天話題不間斷</Badge>
    <p className="text-gray-700">為了讓使用者能將話題不斷地延續下去，系統能透過過往的聊天紀錄去分析用戶間有所共鳴的話題，並結合當下的時事推薦給你。除了共鳴的話題之外，系統也會推薦各種不同領域的熱門話題，並附上一段開頭語句，讓你成為話題高手，聊天不間斷。</p>
  </div>

  <div>
    <Badge variant="default" className="mb-2 font-bold">個人化智慧提醒</Badge>
    <p className="text-gray-700">人們常需要將已經安排好的行程再次手動輸入到手機行事曆中，費時又費力，利用系統的功能一鍵加入，便利又快速。智慧提醒能在最即時和適當的時間推播個人化的資訊，如:本日行程、天氣、股市的波動等等。讓MindReader替你安排好，使你輕鬆沒煩惱，成為你專屬的智慧秘書。</p>
  </div>
</div>

## 產品架構

<Card className="my-6">
  <CardContent className="pt-6">
    ![MindReader 系統架構](/assets/imgs/projects/mindReader/systemFrame.png)
  </CardContent>
</Card>

## 設計理念

<Card className="my-6">
  <CardContent className="pt-6">
    <h3 className="text-xl font-bold mb-4">介面設計貼近原生鍵盤體驗，唯一記得的事就是`輸入`</h3>

    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
      <IconBlock
        title="Figma 原型展示連結"
        subtitle="Figma"
        href="https://www.figma.com/proto/Tk1mSaUpLrBxUdHbHQvtQd/%5B2021-MR%5D-APP-Design?page-id=0%3A1&node-id=58%3A3277&viewport=241%2C48%2C0.14&scaling=scale-down&starting-point-node-id=58%3A3277&show-proto-sidebar=1"
        icon="bi-phone-fill"
        client:visible
      />
      <IconBlock
        title="MVP 網頁"
        subtitle="GitHub"
        href="https://github.com/tony13382/MindReader-MVP/"
        icon="bi-github"
        client:visible
      />
    </div>
  </CardContent>
</Card>

## 輸入文本轉換流程

<Card className="my-6">
  <CardHeader>
    ![API Flow](/assets/imgs/projects/mindReader/apiFlow%20(1).jpg)
  </CardHeader>
  <CardContent>
    <div className="space-y-4">
      <IconBlock title="用戶輸入（鍵盤攔截）" icon="bi-keyboard" />
      <IconBlock title="鍵盤利用 Web APIs 將文字傳送至 MindReader Core" icon="bi-hdd-network" />
      <IconBlock title="Line Bot 抓取用戶 ID" icon="bi-line" />
      <IconBlock title="根據 ID 與文字進行轉換" icon="bi-arrow-repeat" />
      <IconBlock title="傳送轉譯後文字" icon="bi-send" />
      <IconBlock title="接收使用者以外的回饋文字" icon="bi-hdd-network" />
      <IconBlock title="錄入資料進行評分" icon="bi-database-down" />
    </div>
  </CardContent>
</Card>
```

**說明**:
- Frontmatter (---...---) 包含所有結構化數據
- 內容使用標準 Markdown 語法
- 可以直接導入和使用 React 組件
- `client:visible` 指令表示該組件在可見時才載入 JS（Islands Architecture）

---

## 🎨 shadcn/ui 整合方案

### 安裝步驟

```bash
# 1. 創建 Astro 項目
npm create astro@latest portfolio
cd portfolio

# 2. 安裝必要整合
npx astro add react
npx astro add tailwind

# 3. 安裝 shadcn 相關依賴
npm install class-variance-authority clsx tailwind-merge
npm install lucide-react

# 4. 安裝其他依賴
npm install @radix-ui/react-accordion
npm install @radix-ui/react-slot
npm install tailwindcss-animate
```

### Tailwind 配置

**`tailwind.config.mjs`**

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ["class"],
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        // ... shadcn 標準顏色
      },
      // 你的主題顏色系統
      themeColors: {
        red: { primary: '#804C4C', secondary: '#503030' },
        orange: { primary: '#805F4C', secondary: '#503C30' },
        yellow: { primary: '#807E4C', secondary: '#6F6D42' },
        green: { primary: '#4C8077', secondary: '#30504A' },
        blue: { primary: '#4C6D80', secondary: '#304450' },
        purple: { primary: '#727196', secondary: '#555474' },
        pink: { primary: '#804C78', secondary: '#653A5E' },
        natural: { primary: '#555555', secondary: '#2B2B2B' },
        home: { primary: '#7c6e69', secondary: '#49413d' }
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}
```

### 工具函數

**`src/lib/utils.ts`**

```typescript
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

### shadcn 組件範例

**`src/components/ui/card.tsx`**

```tsx
import * as React from "react"
import { cn } from "@/lib/utils"

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-lg border bg-card text-card-foreground shadow-sm",
      className
    )}
    {...props}
  />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
  <h3
    ref={ref}
    className={cn(
      "text-2xl font-semibold leading-none tracking-tight",
      className
    )}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
  <p
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex items-center p-6 pt-0", className)}
    {...props}
  />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }
```

**需要手動添加的 shadcn 組件**:
- Card
- Badge
- Button
- Accordion
- Tabs
- Dialog
- Separator

---

## 🔄 內容遷移策略

### 自動轉換腳本

**`migration/convert_to_mdx.py`**

```python
"""
Python 內容轉 MDX 腳本
用法: python migration/convert_to_mdx.py
"""

import os
import sys
import yaml
from pathlib import Path
from datetime import datetime

# 添加 app 目錄到路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.pages.project import allProjects
from app.pages.job import allJobs
from app.pages.skill import allSkills


def get_theme_name(color_set):
    """從顏色元組推斷主題名稱"""
    theme_map = {
        ("#7c6e69", "#49413d"): "home",
        ("#804C4C", "#503030"): "red",
        ("#805F4C", "#503C30"): "orange",
        ("#807E4C", "#6F6D42"): "yellow",
        ("#4C8077", "#30504A"): "green",
        ("#4C6D80", "#304450"): "blue",
        ("#727196", "#555474"): "purple",
        ("#804C78", "#653A5E"): "pink",
        ("#555555", "#2B2B2B"): "natural",
    }
    return theme_map.get(color_set, "natural")


def convert_date(date_str):
    """轉換日期格式 2024/08 -> 2024-08-01"""
    if date_str is None:
        return None
    try:
        parts = date_str.split('/')
        if len(parts) == 2:
            return f"{parts[0]}-{parts[1]}-01"
        return date_str
    except:
        return None


def convert_project_to_mdx(project):
    """將 ProjectPage 轉換為 MDX"""

    # Frontmatter
    frontmatter = {
        'title': project.title,
        'description': project.description,
        'subdescription': getattr(project, 'subdescription', ''),
        'startDate': convert_date(project.startdate),
        'endDate': convert_date(project.enddate),
        'status': project.status,
        'theme': get_theme_name(project.colorSet),
        'cover': project.cover,
        'pin': project.pin,
        'skillTypes': project.skill_types,
        'tags': project.tags,
    }

    # Links
    if hasattr(project, 'description_links') and project.description_links:
        frontmatter['links'] = [
            {
                'content': link.content,
                'href': link.href,
                'icon': getattr(link, 'icon', ''),
                'openInTab': getattr(link, 'open_in_tab', True)
            }
            for link in project.description_links
        ]

    # Tools
    if project.tools:
        frontmatter['tools'] = [
            {'name': tool.title, 'description': tool.subtitle}
            for tool in project.tools
        ]

    # Scores
    if project.scores:
        frontmatter['scores'] = [
            {
                'title': score.title,
                'award': score.subtitle,
                'category': getattr(score, 'tag', '')
            }
            for score in project.scores
        ]

    # 生成 MDX
    mdx = f"""---
{yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False)}---

import {{ Card, CardHeader, CardContent }} from '@/components/ui/card'
import {{ Badge }} from '@/components/ui/badge'

## 專案內容

此內容需要手動從 Python children 轉換。

<!-- TODO: 手動轉換以下內容 -->
<!-- children 數量: {len(project.children) if hasattr(project, 'children') else 0} -->
"""

    return mdx


def convert_job_to_mdx(job):
    """將 JobPage 轉換為 MDX"""

    frontmatter = {
        'title': job.title,
        'jobName': job.job_name,
        'startDate': convert_date(job.startdate),
        'endDate': convert_date(job.enddate),
        'theme': get_theme_name(job.colorSet),
        'cover': job.cover,
        'description': job.description.items if hasattr(job.description, 'items') else [],
    }

    mdx = f"""---
{yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False)}---

import {{ Card, CardHeader, CardContent }} from '@/components/ui/card'
import {{ Badge }} from '@/components/ui/badge'

## 工作內容

此內容需要手動從 Python children 轉換。

<!-- TODO: 手動轉換專案卡片 -->
"""

    return mdx


def main():
    """主函數"""
    output_dir = Path('migration/output')
    output_dir.mkdir(exist_ok=True)

    # 轉換專案
    projects_dir = output_dir / 'projects'
    projects_dir.mkdir(exist_ok=True)

    print("轉換專案...")
    for project in allProjects:
        slug = project.prefix
        mdx_content = convert_project_to_mdx(project)
        output_file = projects_dir / f"{slug}.mdx"
        output_file.write_text(mdx_content, encoding='utf-8')
        print(f"  ✓ {slug}.mdx")

    # 轉換工作經驗
    jobs_dir = output_dir / 'jobs'
    jobs_dir.mkdir(exist_ok=True)

    print("\n轉換工作經驗...")
    for job in allJobs:
        slug = job.prefix
        mdx_content = convert_job_to_mdx(job)
        output_file = jobs_dir / f"{slug}.mdx"
        output_file.write_text(mdx_content, encoding='utf-8')
        print(f"  ✓ {slug}.mdx")

    print(f"\n✅ 轉換完成！輸出目錄: {output_dir}")
    print("\n⚠️  注意: 需要手動轉換內容中的 children 部分")


if __name__ == '__main__':
    main()
```

### 手動調整指南

自動轉換腳本會生成基礎的 frontmatter，但以下內容需要手動轉換：

1. **Card 組件內容** - 從 Python `Card()` 轉為 MDX `<Card>`
2. **圖片輪播** - `UiImageCarousel` → React 組件
3. **YouTube 嵌入** - `Youtube()` → `<Youtube client:visible>`
4. **IconBlock 列表** - 轉為 React 組件

---

## 📱 頁面實現範例

### `src/pages/projects/[slug].astro`

```astro
---
import { getCollection, getEntry } from 'astro:content'
import BaseLayout from '@/layouts/BaseLayout.astro'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { themes } from '@/lib/themes'

// 生成靜態路徑
export async function getStaticPaths() {
  const projects = await getCollection('projects')
  return projects.map(p => ({
    params: { slug: p.slug },
    props: { project: p }
  }))
}

const { project } = Astro.props
const { Content } = await project.render()

// SEO
const seo = {
  title: project.data.seo?.metaTitle || `${project.data.title} | 呂亮進`,
  description: project.data.seo?.metaDescription || project.data.description,
  ogImage: project.data.seo?.ogImage || project.data.cover
}

// 主題顏色
const themeColors = themes[project.data.theme]
---

<BaseLayout
  title={seo.title}
  description={seo.description}
  ogImage={seo.ogImage}
>
  <!-- 動態 CSS 變量 -->
  <style define:vars={{ themeColor: themeColors.primary, secondColor: themeColors.secondary }}>
    :root {
      --theme-primary: var(--themeColor);
      --theme-secondary: var(--secondColor);
    }
  </style>

  <div class="container mx-auto px-4 py-8 max-w-5xl">
    <!-- 頁首 -->
    <header class="mb-8">
      <!-- 返回按鈕 -->
      <a href="/projects" class="inline-flex items-center text-sm text-gray-600 hover:text-gray-900 mb-4">
        <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        返回專案列表
      </a>

      <!-- 標題 -->
      <h1 class="text-4xl md:text-5xl font-bold mb-4" style={`color: ${themeColors.primary}`}>
        {project.data.title}
      </h1>

      <!-- 副標題 -->
      {project.data.subdescription && (
        <p class="text-lg text-gray-600 mb-4" set:html={project.data.subdescription} />
      )}

      <!-- 時間與狀態 -->
      <div class="flex items-center gap-4 text-sm text-gray-500 mb-4">
        <span>
          {project.data.startDate.toLocaleDateString('zh-TW', { year: 'numeric', month: '2-digit' })}
          {project.data.endDate
            ? ` - ${project.data.endDate.toLocaleDateString('zh-TW', { year: 'numeric', month: '2-digit' })}`
            : ' - 現在'
          }
        </span>
        <span class="px-2 py-1 rounded-full bg-gray-100 text-gray-700">
          {project.data.status === 'active' ? '進行中' : project.data.status === 'closed' ? '已結束' : '暫停'}
        </span>
        {project.data.pin && (
          <span class="px-2 py-1 rounded-full bg-yellow-100 text-yellow-700">精選</span>
        )}
      </div>

      <!-- 標籤 -->
      <div class="flex flex-wrap gap-2 mb-6">
        {project.data.tags.map((tag: string) => (
          <Badge variant="secondary">{tag}</Badge>
        ))}
      </div>

      <!-- 連結按鈕 -->
      {project.data.links && project.data.links.length > 0 && (
        <div class="flex flex-wrap gap-3">
          {project.data.links.map((link: any) => (
            <Button asChild variant="default">
              <a href={link.href} target={link.openInTab ? '_blank' : '_self'} rel="noopener noreferrer">
                {link.icon && <i class={`${link.icon} mr-2`}></i>}
                {link.content}
              </a>
            </Button>
          ))}
        </div>
      )}
    </header>

    <!-- MDX 內容 -->
    <article class="prose prose-lg max-w-none prose-headings:text-gray-900 prose-a:text-blue-600">
      <Content />
    </article>

    <!-- 使用工具 -->
    {project.data.tools && project.data.tools.length > 0 && (
      <section class="mt-16 pt-8 border-t">
        <h2 class="text-3xl font-bold mb-6">使用工具</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          {project.data.tools.map((tool: any) => (
            <div class="border rounded-lg p-4 hover:shadow-md transition-shadow">
              <h3 class="font-bold text-lg mb-1">{tool.name}</h3>
              <p class="text-sm text-gray-600">{tool.description}</p>
            </div>
          ))}
        </div>
      </section>
    )}

    <!-- 獎項 -->
    {project.data.scores && project.data.scores.length > 0 && (
      <section class="mt-12">
        <h2 class="text-3xl font-bold mb-6">獲獎紀錄</h2>
        <div class="space-y-4">
          {project.data.scores.map((score: any) => (
            <div class="border-l-4 border-yellow-500 pl-4 py-2">
              <h3 class="font-bold">{score.title}</h3>
              <p class="text-gray-600">
                {score.award}
                {score.category && ` · ${score.category}`}
              </p>
            </div>
          ))}
        </div>
      </section>
    )}
  </div>
</BaseLayout>
```

### `src/layouts/BaseLayout.astro`

```astro
---
import '@/styles/global.css'

interface Props {
  title: string
  description: string
  ogImage?: string
}

const { title, description, ogImage = '/assets/MetaTagCover.png' } = Astro.props
const canonicalURL = new URL(Astro.url.pathname, Astro.site)
---

<!doctype html>
<html lang="zh-Hant-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO -->
    <title>{title}</title>
    <meta name="description" content={description}>
    <link rel="canonical" href={canonicalURL}>

    <!-- Open Graph -->
    <meta property="og:url" content={canonicalURL}>
    <meta property="og:type" content="website">
    <meta property="og:title" content={title}>
    <meta property="og:description" content={description}>
    <meta property="og:image" content={new URL(ogImage, Astro.site)}>
    <meta property="og:image:alt" content={title}>
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <!-- Favicon -->
    <link rel="icon" type="image/png" href="/assets/favicon.png">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100;400;700&display=swap" rel="stylesheet">

    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-165132NHTH"></script>
    <script is:inline>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-165132NHTH');
    </script>
</head>
<body>
    <slot />
</body>
</html>
```

---

## 🚀 實施步驟（4 週計劃）

### 第 1 週：環境設置與基礎架構

**目標**: 完成 Astro 項目初始化和基礎配置

#### Day 1-2: 項目初始化
```bash
# 創建新項目
npm create astro@latest portfolio
cd portfolio

# 安裝整合
npx astro add react
npx astro add tailwind

# 安裝依賴
npm install class-variance-authority clsx tailwind-merge lucide-react
npm install @radix-ui/react-accordion @radix-ui/react-slot
npm install tailwindcss-animate
```

**交付物**:
- ✅ Astro 項目運行成功
- ✅ Tailwind 配置完成
- ✅ TypeScript 配置完成

#### Day 3-4: shadcn/ui 設置
- 手動添加 shadcn 組件（Card, Badge, Button, Accordion）
- 創建 `src/lib/utils.ts`
- 測試組件渲染

**交付物**:
- ✅ 5-8 個 shadcn 組件可用
- ✅ 組件示例頁面

#### Day 5-7: Content Collections 配置
- 創建 `src/content/config.ts`
- 定義 Projects, Jobs, Skills schema
- 創建測試 MDX 文件

**交付物**:
- ✅ Content Collections 配置完成
- ✅ TypeScript 類型自動生成
- ✅ 至少 1 個測試 MDX 文件可渲染

---

### 第 2 週：內容遷移

**目標**: 將所有 Python 內容轉換為 MDX

#### Day 8-10: 自動轉換
```bash
# 運行轉換腳本
python migration/convert_to_mdx.py
```

**任務**:
- 運行自動轉換腳本
- 生成 frontmatter
- 複製圖片資源到 `public/assets/`

**交付物**:
- ✅ 14 個專案 MDX（帶 frontmatter）
- ✅ 7 個工作 MDX
- ✅ 4 個技能 MDX
- ✅ 圖片資源已複製

#### Day 11-14: 手動調整
**任務**:
- 轉換 Card 內容
- 調整圖片路徑
- 處理特殊組件（YouTube, Carousel, IconBlock）
- 測試每個頁面

**優先順序**:
1. 先完成 3 個精選專案（pin: true）
2. 再完成其他專案
3. 最後完成 Jobs 和 Skills

**交付物**:
- ✅ 至少 5 個完整的專案 MDX
- ✅ 所有頁面可正常渲染

---

### 第 3 週：頁面與組件開發

**目標**: 完成所有頁面佈局和自定義組件

#### Day 15-17: 頁面開發
**任務**:
- 實現 `[slug].astro` 動態路由（Projects, Jobs, Skills）
- 實現首頁 `index.astro`
- 實現列表頁（Projects Index, Jobs Index）
- 實現 Navbar 和 Footer

**交付物**:
- ✅ 所有頁面路由正常
- ✅ 導航和頁腳完成
- ✅ SEO meta tags 正確

#### Day 18-21: 自定義組件
**任務**:
- 實現 `Youtube.tsx` (React)
- 實現 `IconBlock.tsx` (React)
- 實現 `ImageCarousel.tsx` (React)
- 整合主題系統（`src/lib/themes.ts`）

**交付物**:
- ✅ 所有自定義組件完成
- ✅ Islands Architecture 正確配置（client:visible）
- ✅ 主題顏色動態應用

---

### 第 4 週：優化與部署

**目標**: 性能優化、SEO 完善、部署上線

#### Day 22-24: SEO 與性能優化
**任務**:
- 生成 `sitemap.xml`
- 生成 `robots.txt`
- 優化圖片（使用 Astro Image）
- 實現 lazy loading
- Core Web Vitals 測試

**交付物**:
- ✅ Lighthouse 分數 > 95
- ✅ SEO 分數 100
- ✅ 所有圖片優化

#### Day 25-26: 測試
**任務**:
- 跨瀏覽器測試
- 響應式測試（Mobile, Tablet, Desktop）
- 所有連結檢查
- 內容校對

**交付物**:
- ✅ 所有頁面在 Chrome, Safari, Firefox 正常
- ✅ 移動端體驗良好
- ✅ 無 404 連結

#### Day 27-28: 部署
**任務**:
- Netlify 配置
- 環境變數設置
- 構建測試
- DNS 設置（如需要）

**部署配置** (`netlify.toml`):
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/404"
  status = 404
```

**交付物**:
- ✅ 網站成功部署到 Netlify
- ✅ 所有頁面可訪問
- ✅ Analytics 正常運作

---

## 📊 技術對比總結

### 現有 Python 方案 vs Astro 方案

| 項目 | Python 方案 | Astro 方案 | 改進 |
|------|------------|-----------|------|
| **開發體驗** | 手動刷新 | 熱重載 | ⬆️ 大幅提升 |
| **內容管理** | Python 代碼 | MDX 文件 | ⬆️ 更直觀 |
| **類型安全** | 部分 Pydantic | 完整 TypeScript | ⬆️ 更強 |
| **UI 組件** | 自定義 Bootstrap | shadcn/ui | ⬆️ 更現代 |
| **首次加載** | ~80KB CSS | ~30KB JS+CSS | ⬆️ 性能提升 |
| **SEO** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ➡️ 相同 |
| **構建時間** | ~2s | ~5-8s | ⬇️ 稍慢 |
| **學習曲線** | 低（Python） | 中（React/Astro） | ⬇️ 需學習 |

### 為什麼選擇 Astro

1. ✅ **Islands Architecture**: 靜態內容零 JS，互動組件按需加載
2. ✅ **MDX 原生支持**: 內容即代碼，Git 友好
3. ✅ **Content Collections**: 類型安全的內容管理
4. ✅ **shadcn/ui**: 現代化、可定制的 UI 組件
5. ✅ **SEO 完美**: 構建時預渲染，和現有方案一樣好
6. ✅ **未來可擴展**: 需要時可添加 CMS

---

## 💰 成本估算

### 開發時間
- **初期設置**: 1 週（40 小時）
- **內容遷移**: 1 週（40 小時）
- **組件開發**: 1 週（40 小時）
- **優化部署**: 1 週（40 小時）
- **總計**: 4 週（160 小時）

### 運行成本
- **託管**: Netlify 免費方案（100GB 帶寬）
- **域名**: 現有
- **總成本**: $0/月

### 維護成本
- **內容更新**: 編輯 MDX 文件（5-10 分鐘/篇）
- **組件更新**: 類似 React 開發
- **依賴更新**: 每月檢查一次

---

## 🎯 成功指標

### 性能指標
- ✅ Lighthouse Performance > 95
- ✅ First Contentful Paint < 1.2s
- ✅ Time to Interactive < 2.5s
- ✅ Cumulative Layout Shift < 0.1

### SEO 指標
- ✅ Lighthouse SEO = 100
- ✅ 所有頁面有完整 meta tags
- ✅ sitemap.xml 自動生成
- ✅ 社交分享卡片正常

### 開發體驗
- ✅ 熱重載 < 200ms
- ✅ TypeScript 自動補全
- ✅ 編輯 MDX 即時預覽
- ✅ 構建錯誤清晰提示

---

## 📚 參考資源

### 官方文檔
- [Astro 文檔](https://docs.astro.build/)
- [shadcn/ui 文檔](https://ui.shadcn.com/)
- [MDX 文檔](https://mdxjs.com/)
- [Tailwind CSS](https://tailwindcss.com/)

### 學習資源
- [Astro Content Collections 指南](https://docs.astro.build/en/guides/content-collections/)
- [Islands Architecture 概念](https://docs.astro.build/en/concepts/islands/)
- [shadcn/ui 在 Astro 中的使用](https://ui.shadcn.com/docs/installation/astro)

### 社區
- [Astro Discord](https://astro.build/chat)
- [GitHub Discussions](https://github.com/withastro/astro/discussions)

---

## 🚀 下一步行動

### 立即開始

1. **創建新分支**
   ```bash
   git checkout -b refactor/astro-migration
   ```

2. **初始化 Astro 項目**（在新目錄）
   ```bash
   npm create astro@latest portfolio-new
   cd portfolio-new
   ```

3. **運行轉換腳本**
   ```bash
   python migration/convert_to_mdx.py
   ```

4. **手動完成第一個頁面**（以 MindReader 為例）
   - 確保 MDX 正確渲染
   - 驗證 SEO meta tags
   - 測試主題顏色

5. **決定是否繼續**
   - 如果第一個頁面效果滿意，繼續完成其他頁面
   - 如果需要調整，修改方案後再繼續

---

## ✅ 檢查清單

### 開發前
- [ ] 確認 Node.js 版本 >= 18
- [ ] 確認 Python 版本 >= 3.10
- [ ] 備份現有網站
- [ ] 閱讀 Astro 和 shadcn 文檔

### 第 1 週
- [ ] Astro 項目初始化
- [ ] shadcn 組件設置
- [ ] Content Collections 配置
- [ ] 至少 1 個測試頁面運行

### 第 2 週
- [ ] 所有內容轉換為 MDX
- [ ] 圖片資源複製
- [ ] 至少 5 個頁面完成

### 第 3 週
- [ ] 所有頁面路由完成
- [ ] 自定義組件開發
- [ ] 主題系統整合

### 第 4 週
- [ ] SEO 優化完成
- [ ] 性能測試通過
- [ ] 部署到 Netlify
- [ ] 所有功能測試通過

---

## 📝 備註

### 風險管理
1. **時間超支**: 預留 20% 緩衝時間
2. **技術難點**: 遇到問題立即查文檔或詢問社區
3. **內容遺失**: 保留原 Python 代碼直到完全遷移完成

### 回滾計劃
如果遷移過程中遇到重大問題：
1. 原網站繼續運行（不影響線上服務）
2. Astro 項目在獨立分支開發
3. 可隨時回到 Python 方案

### 漸進遷移
也可以採用漸進式遷移：
1. 先遷移 3-5 個精選專案
2. 部署到子目錄（example.com/new）
3. 驗證效果後再全量遷移

---

**準備好開始了嗎？我可以立即幫你執行以下任一步驟：**

1. 創建 Astro 項目腳手架
2. 編寫並執行 Python → MDX 轉換腳本
3. 設置第一個完整的 MDX 頁面（MindReader）
4. 配置 shadcn/ui 組件

請告訴我你想從哪裡開始！
