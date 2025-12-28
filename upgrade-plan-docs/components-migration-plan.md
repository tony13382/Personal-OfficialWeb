# 組件遷移計劃 - Python Elements → Astro/React

## 📊 組件清單與分類

根據 `app/elements.py` 分析，共有 **20 個自定義組件**，按互動性分類：

### 🟦 靜態組件（Astro 實現，0 JS）
| 原組件 | 新實現方式 | 優先級 |
|--------|-----------|--------|
| `DivBar` | Tailwind `<hr>` | ⭐⭐⭐⭐⭐ |
| `Html` | Astro `<Fragment set:html>` | ⭐⭐⭐⭐⭐ |
| `Image` | Astro `<Image>` + Fancybox | ⭐⭐⭐⭐⭐ |
| `ListStr` | 標準 `<ul>` + Tailwind | ⭐⭐⭐⭐⭐ |
| `Text` | 標準 HTML + Tailwind | ⭐⭐⭐⭐⭐ |
| `LinkButton` | shadcn `Button` | ⭐⭐⭐⭐ |
| `Div` | Tailwind utility classes | ⭐⭐⭐⭐ |
| `Columns` | Tailwind Grid/Flex | ⭐⭐⭐⭐ |
| `ListDiv` | Tailwind Flex | ⭐⭐⭐⭐ |
| `Score` | 自定義 Astro 組件 | ⭐⭐⭐ |
| `Tool` | 自定義 Astro 組件 | ⭐⭐⭐ |

### 🟩 互動組件（React + shadcn/ui）
| 原組件 | 新實現方式 | shadcn 替代 | 優先級 |
|--------|-----------|------------|--------|
| `Card` | shadcn `Card` | ✅ 完全替代 | ⭐⭐⭐⭐⭐ |
| `AccordionBlock` | shadcn `Accordion` | ✅ 完全替代 | ⭐⭐⭐⭐⭐ |
| `Tab` | shadcn `Tabs` | ✅ 完全替代 | ⭐⭐⭐⭐ |
| `IconBlock` | 自定義 React | ❌ 需自定義 | ⭐⭐⭐⭐ |
| `Youtube` | React 組件 | ❌ 需自定義 | ⭐⭐⭐⭐ |
| `Canva` | React 組件 | ❌ 需自定義 | ⭐⭐⭐ |

### 🟨 複雜互動組件（需第三方庫）
| 原組件 | 新實現方式 | 建議庫 | 優先級 |
|--------|-----------|-------|--------|
| `ImageCarousel` | React 組件 | Embla Carousel | ⭐⭐⭐⭐ |
| `UiImageCarousel` | React 組件 | Embla Carousel | ⭐⭐⭐⭐ |
| `HtmlCarousel` | React 組件 | Embla Carousel | ⭐⭐⭐ |

---

## 🔧 詳細遷移方案

### 1. DivBar（分隔線）

**原實現**:
```python
DivBar(space="regular", opacity=0.15)
```

**新實現（Astro）**:
```astro
<!-- src/components/astro/DivBar.astro -->
---
interface Props {
  space?: 'nano' | 'mini' | 'regular' | 'wide'
  opacity?: number
}

const { space = 'regular', opacity = 0.15 } = Astro.props

const spaceClass = {
  nano: 'my-0',
  mini: 'my-1',
  regular: 'my-2',
  wide: 'my-3'
}[space]
---

<hr class={spaceClass} style={`opacity: ${opacity}`} />
```

**使用**:
```mdx
import { DivBar } from '@/components/astro/DivBar.astro'

<DivBar space="regular" />
```

---

### 2. Card（卡片）

**原實現**:
```python
Card(
    header=Image(...),
    body=[Text(...), ListStr(...)],
    footer=[LinkButton(...)],
    body_gap=GapSet("large")
)
```

**新實現（shadcn Card）**:
```tsx
// 直接使用 shadcn Card
import { Card, CardHeader, CardContent, CardFooter } from '@/components/ui/card'

<Card>
  <CardHeader>
    <img src="..." alt="..." />
  </CardHeader>
  <CardContent className="space-y-4">
    <p>內容...</p>
    <ul>...</ul>
  </CardContent>
  <CardFooter>
    <Button>...</Button>
  </CardFooter>
</Card>
```

**優勢**:
- ✅ shadcn 原生組件，樣式一致
- ✅ 支持所有 Tailwind classes
- ✅ 比原組件更靈活

---

### 3. AccordionBlock（折疊面板）

**原實現**:
```python
AccordionBlock(
    items=[
        AccordionItem(
            title="標題",
            items=[Text(...), Image(...)],
            expanded=True
        )
    ]
)
```

**新實現（shadcn Accordion）**:
```tsx
// src/components/react/AccordionBlock.tsx
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"

interface AccordionBlockProps {
  items: Array<{
    title: string
    content: React.ReactNode
    defaultOpen?: boolean
  }>
}

export function AccordionBlock({ items }: AccordionBlockProps) {
  return (
    <Accordion type="single" collapsible defaultValue={items.find(i => i.defaultOpen)?.title}>
      {items.map((item, index) => (
        <AccordionItem key={index} value={item.title}>
          <AccordionTrigger>{item.title}</AccordionTrigger>
          <AccordionContent>
            {item.content}
          </AccordionContent>
        </AccordionItem>
      ))}
    </Accordion>
  )
}
```

**MDX 使用**:
```mdx
import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from '@/components/ui/accordion'

<Accordion type="single" collapsible>
  <AccordionItem value="item-1">
    <AccordionTrigger>產品架構</AccordionTrigger>
    <AccordionContent>
      ![架構圖](/assets/...)
    </AccordionContent>
  </AccordionItem>
</Accordion>
```

---

### 4. IconBlock（圖標卡片）

**原實現**:
```python
IconBlock(
    title="Figma 原型展示連結",
    subtitle="Figma",
    src="https://...",
    icon="bi-phone-fill"
)
```

**新實現（自定義 React）**:
```tsx
// src/components/react/IconBlock.tsx
import { cn } from "@/lib/utils"

interface IconBlockProps {
  title?: string
  subtitle?: string
  href?: string
  icon?: string
  className?: string
}

export function IconBlock({
  title,
  subtitle,
  href,
  icon = "bi-file-earmark-arrow-down",
  className
}: IconBlockProps) {
  const content = (
    <div className={cn(
      "flex items-center gap-4 p-4 border rounded-lg",
      href && "hover:shadow-md transition-shadow cursor-pointer",
      className
    )}>
      <div
        className="flex items-center justify-center w-14 h-14 rounded-lg text-white text-2xl"
        style={{ backgroundColor: 'var(--theme-primary)' }}
      >
        <i className={`bi ${icon}`}></i>
      </div>
      <div className="flex-1">
        {title && <p className="font-bold m-0">{title}</p>}
        {subtitle && <p className="text-sm text-gray-500 m-0">{subtitle}</p>}
      </div>
    </div>
  )

  if (href) {
    return (
      <a href={href} target="_blank" rel="noopener noreferrer" className="no-underline">
        {content}
      </a>
    )
  }

  return content
}
```

**MDX 使用**:
```mdx
import { IconBlock } from '@/components/react/IconBlock'

<IconBlock
  title="Figma 原型展示連結"
  subtitle="Figma"
  href="https://..."
  icon="bi-phone-fill"
  client:visible
/>
```

---

### 5. Image（圖片 + Fancybox）

**原實現**:
```python
Image(
    src="/assets/imgs/...",
    alt="描述",
    allow_pop=True,
    max_width=800,
    rounded=True
)
```

**新實現（Astro Image + Fancybox）**:
```astro
<!-- src/components/astro/OptimizedImage.astro -->
---
import { Image } from 'astro:assets'

interface Props {
  src: string
  alt: string
  allowPop?: boolean
  maxWidth?: number
  rounded?: boolean
  class?: string
}

const { src, alt, allowPop = false, maxWidth, rounded = false, class: className } = Astro.props

const roundedClass = rounded ? 'rounded-lg' : ''
const maxWidthStyle = maxWidth ? `max-width: ${maxWidth}px` : ''
---

{allowPop ? (
  <a href={src} data-fancybox="gallery" class:list={['block mx-auto', roundedClass]}>
    <img
      src={src}
      alt={alt}
      class:list={['w-full mx-auto', roundedClass, className]}
      style={maxWidthStyle}
      loading="lazy"
    />
  </a>
) : (
  <div class="block mx-auto text-center">
    <img
      src={src}
      alt={alt}
      class:list={['w-full mx-auto', roundedClass, className]}
      style={maxWidthStyle}
      loading="lazy"
    />
  </div>
)}
```

**MDX 使用**:
```mdx
import { OptimizedImage } from '@/components/astro/OptimizedImage.astro'

![產品架構](/assets/imgs/projects/mindReader/systemFrame.png)

<!-- 或使用組件 -->
<OptimizedImage
  src="/assets/imgs/..."
  alt="描述"
  allowPop={true}
  rounded={true}
/>
```

**Fancybox 設置**:
```astro
<!-- src/layouts/BaseLayout.astro -->
<head>
  <!-- ... -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.css" />
</head>
<body>
  <!-- ... -->
  <script src="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.umd.js"></script>
  <script is:inline>
    Fancybox.bind("[data-fancybox]", {
      // 配置選項
    });
  </script>
</body>
```

---

### 6. Youtube（YouTube 嵌入）

**原實現**:
```python
Youtube("https://www.youtube.com/embed/VzLFWFRzGh8")
```

**新實現（React 組件）**:
```tsx
// src/components/react/Youtube.tsx
interface YoutubeProps {
  embedUrl: string
  title?: string
}

export function Youtube({ embedUrl, title = "YouTube video player" }: YoutubeProps) {
  return (
    <div className="relative w-full" style={{ paddingBottom: '56.25%' }}>
      <iframe
        className="absolute top-0 left-0 w-full h-full rounded-lg"
        src={embedUrl}
        title={title}
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      />
    </div>
  )
}
```

**MDX 使用**:
```mdx
import { Youtube } from '@/components/react/Youtube'

<Youtube
  embedUrl="https://www.youtube.com/embed/VzLFWFRzGh8"
  client:visible
/>
```

---

### 7. ImageCarousel（圖片輪播）

**原實現**:
```python
UiImageCarousel([
    "/assets/imgs/projects/mindReader/keybroad01.png",
    "/assets/imgs/projects/mindReader/keybroad02.png",
    "/assets/imgs/projects/mindReader/keybroad03.png",
])
```

**新實現（Embla Carousel）**:
```tsx
// src/components/react/ImageCarousel.tsx
import { useEffect } from 'react'
import useEmblaCarousel from 'embla-carousel-react'
import Autoplay from 'embla-carousel-autoplay'

interface ImageCarouselProps {
  images: string[]
  allowPop?: boolean
}

export function ImageCarousel({ images, allowPop = false }: ImageCarouselProps) {
  const [emblaRef, emblaApi] = useEmblaCarousel(
    { loop: true },
    [Autoplay({ delay: 3000 })]
  )

  return (
    <div className="overflow-hidden rounded-lg" ref={emblaRef}>
      <div className="flex">
        {images.map((src, index) => (
          <div key={index} className="flex-[0_0_100%] min-w-0">
            {allowPop ? (
              <a href={src} data-fancybox="carousel">
                <img src={src} alt={`Slide ${index + 1}`} className="w-full" />
              </a>
            ) : (
              <img src={src} alt={`Slide ${index + 1}`} className="w-full" />
            )}
          </div>
        ))}
      </div>
    </div>
  )
}
```

**安裝依賴**:
```bash
npm install embla-carousel-react embla-carousel-autoplay
```

**MDX 使用**:
```mdx
import { ImageCarousel } from '@/components/react/ImageCarousel'

<ImageCarousel
  images={[
    "/assets/imgs/projects/mindReader/keybroad01.png",
    "/assets/imgs/projects/mindReader/keybroad02.png",
    "/assets/imgs/projects/mindReader/keybroad03.png"
  ]}
  allowPop={true}
  client:visible
/>
```

---

### 8. Text（文本/標題）

**原實現**:
```python
Text("產品優勢", "h3", bold=True)
Text("描述內容", "p")
Text("# 標籤", "span", pill_type=True)
```

**新實現（Astro 組件）**:
```astro
<!-- src/components/astro/Text.astro -->
---
interface Props {
  content: string
  as?: 'h2' | 'h3' | 'h4' | 'p' | 'span'
  bold?: boolean
  center?: boolean
  pill?: boolean
  class?: string
}

const {
  content,
  as: Tag = 'p',
  bold = false,
  center = false,
  pill = false,
  class: className
} = Astro.props

// 處理 `code` 高亮語法
const processedContent = content.replace(/`([^`]+)`/g, '<span class="text-highlight">$1</span>')

const classes = [
  bold && 'font-bold',
  center && 'text-center',
  pill && 'badge bg-theme-soft text-dark rounded-full px-3 py-1',
  className
].filter(Boolean).join(' ')

const id = ['h2', 'h3', 'h4'].includes(Tag)
  ? content.replace(/\s+/g, '_').replace(/`/g, '')
  : undefined
---

<Tag class={classes} id={id} set:html={processedContent} />
```

**Tailwind 配置（高亮樣式）**:
```css
/* src/styles/global.css */
.text-highlight {
  @apply bg-yellow-100 px-1 rounded;
}
```

**MDX 使用**:
```mdx
## 產品優勢

這是一段包含 `高亮文本` 的描述。

<!-- 或使用組件 -->
import { Text } from '@/components/astro/Text.astro'

<Text content="產品優勢" as="h3" bold={true} />
```

---

### 9. Tab（標籤頁）

**原實現**:
```python
Tab(data=[
    TabItem(title="前端", content="..."),
    TabItem(title="後端", content="...")
])
```

**新實現（shadcn Tabs）**:
```tsx
// 直接使用 shadcn Tabs
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

<Tabs defaultValue="frontend">
  <TabsList>
    <TabsTrigger value="frontend">前端</TabsTrigger>
    <TabsTrigger value="backend">後端</TabsTrigger>
  </TabsList>
  <TabsContent value="frontend">
    前端內容...
  </TabsContent>
  <TabsContent value="backend">
    後端內容...
  </TabsContent>
</Tabs>
```

---

### 10. ListStr（無序列表）

**原實現**:
```python
ListStr([
    "第一項",
    "第二項包含`高亮文本`",
    "第三項"
])
```

**新實現（標準 HTML + Tailwind）**:
```astro
<!-- src/components/astro/ListStr.astro -->
---
interface Props {
  items: string[]
  class?: string
}

const { items, class: className } = Astro.props

function processText(text: string) {
  return text.replace(/`([^`]+)`/g, '<span class="text-highlight">$1</span>')
}
---

<ul class:list={['ps-3 m-0 leading-relaxed', className]}>
  {items.map(item => (
    <li set:html={processText(item)} />
  ))}
</ul>
```

**MDX 使用**:
```mdx
<!-- 標準 Markdown -->
- 第一項
- 第二項包含 `高亮文本`
- 第三項

<!-- 或使用組件 -->
import { ListStr } from '@/components/astro/ListStr.astro'

<ListStr items={[
  "第一項",
  "第二項包含 `高亮文本`",
  "第三項"
]} />
```

---

### 11. Canva（Canva 嵌入）

**原實現**:
```python
Canva(src="https://www.canva.com/.../view")
```

**新實現（React 組件）**:
```tsx
// src/components/react/Canva.tsx
interface CanvaProps {
  src: string
}

export function Canva({ src }: CanvaProps) {
  // 自動添加 ?embed 參數
  const embedSrc = src.endsWith('/view') ? `${src}?embed` : src

  return (
    <div
      className="relative w-full overflow-hidden rounded-lg shadow-md"
      style={{
        paddingTop: '56.24%',
        paddingBottom: 0
      }}
    >
      <iframe
        loading="lazy"
        className="absolute top-0 left-0 w-full h-full border-0"
        src={embedSrc}
        allowFullScreen
      />
    </div>
  )
}
```

**MDX 使用**:
```mdx
import { Canva } from '@/components/react/Canva'

<Canva
  src="https://www.canva.com/.../view"
  client:load
/>
```

---

### 12. Score（獎項展示）

**原實現**:
```python
Score("2021 大專校院資訊應用服務創新競賽", "佳作", "資訊應用組")
```

**新實現（Astro 組件）**:
```astro
<!-- src/components/astro/Score.astro -->
---
interface Props {
  name: string
  score: string
  group?: string
}

const { name, score, group } = Astro.props
---

<div class="p-4 border-l-4 border-yellow-500">
  <p class="text-sm text-gray-600 mb-1">
    {name}
    {group && <span> · {group}</span>}
  </p>
  <p class="text-2xl font-bold text-theme m-0">{score}</p>
</div>
```

**MDX 使用**:
```mdx
import { Score } from '@/components/astro/Score.astro'

<div class="space-y-4">
  <Score
    name="2021 大專校院資訊應用服務創新競賽"
    score="佳作"
    group="資訊應用組"
  />
  <Score
    name="中原大學資管系畢業專題競賽"
    score="第一名"
  />
</div>
```

---

## 📦 必要的依賴安裝

```bash
# shadcn/ui 核心
npm install class-variance-authority clsx tailwind-merge
npm install lucide-react

# Radix UI（shadcn 依賴）
npm install @radix-ui/react-accordion
npm install @radix-ui/react-tabs
npm install @radix-ui/react-slot

# Carousel
npm install embla-carousel-react embla-carousel-autoplay

# Tailwind 插件
npm install tailwindcss-animate

# Fancybox（CDN 或 npm）
# 建議使用 CDN
```

---

## 🎨 Tailwind 配置增強

```javascript
// tailwind.config.mjs
export default {
  theme: {
    extend: {
      // 主題顏色（動態注入）
      colors: {
        'theme-primary': 'var(--theme-primary)',
        'theme-secondary': 'var(--theme-secondary)',
        'theme-soft': 'var(--theme-soft)',
      },
      // 字體
      fontFamily: {
        sans: ['Noto Sans TC', 'sans-serif'],
        emoji: ['Noto Emoji', 'sans-serif'],
        logo: ['Playwrite HR Lijeva', 'cursive'],
      },
      // 圓角（對應 Bootstrap）
      borderRadius: {
        'inline-basic': '0.5rem',
      },
      // 行高
      lineHeight: {
        'relaxed': '1.75',
      }
    }
  }
}
```

---

## 🔄 組件對照表

### 完全由 shadcn/ui 替代
| Python 組件 | shadcn 組件 | 改進 |
|------------|------------|------|
| `Card` | `Card, CardHeader, CardContent, CardFooter` | ✅ 更靈活 |
| `AccordionBlock` | `Accordion, AccordionItem` | ✅ 更好的動畫 |
| `Tab` | `Tabs, TabsList, TabsTrigger` | ✅ 更現代 |
| `LinkButton` | `Button` | ✅ 更多變體 |

### 簡化為 Tailwind
| Python 組件 | Tailwind 替代 | 改進 |
|------------|--------------|------|
| `DivBar` | `<hr class="my-2">` | ✅ 更簡潔 |
| `Div` | `<div class="mt-4">` | ✅ 直接使用 utility |
| `Columns` | `<div class="grid grid-cols-2">` | ✅ 更強大 |
| `ListDiv` | `<div class="flex gap-4">` | ✅ 更直觀 |

### 需自定義實現
| Python 組件 | 新實現 | 難度 |
|------------|--------|------|
| `IconBlock` | React 組件 | ⭐⭐ |
| `Youtube` | React 組件 | ⭐ |
| `Canva` | React 組件 | ⭐ |
| `ImageCarousel` | Embla Carousel | ⭐⭐⭐ |
| `Score` | Astro 組件 | ⭐ |
| `Tool` | Astro 組件 | ⭐ |

---

## 🚀 實施優先級

### 第 1 優先（立即實現）
1. ✅ **Card** - shadcn Card（最常用）
2. ✅ **Text** - Astro 組件 + Markdown
3. ✅ **Image** - Astro Image + Fancybox
4. ✅ **ListStr** - 標準 `<ul>`
5. ✅ **DivBar** - `<hr>`

### 第 2 優先（第一批內容需要）
6. ✅ **Youtube** - React 組件
7. ✅ **IconBlock** - React 組件
8. ✅ **AccordionBlock** - shadcn Accordion
9. ✅ **LinkButton** - shadcn Button
10. ✅ **ImageCarousel** - Embla

### 第 3 優先（特殊頁面需要）
11. ✅ **Tab** - shadcn Tabs
12. ✅ **Score** - Astro 組件
13. ✅ **Tool** - Astro 組件
14. ✅ **Canva** - React 組件

---

## 💡 遷移策略建議

### 策略 1：漸進式替換
```mdx
<!-- 第一版：使用 Markdown -->
## 產品優勢

- 客製化對話情境
- 聊天話題不間斷

<!-- 第二版：混合使用組件 -->
<Card>
  <CardHeader>
    <h3>產品優勢</h3>
  </CardHeader>
  <CardContent>
    <ul>
      <li>客製化對話情境</li>
      <li>聊天話題不間斷</li>
    </ul>
  </CardContent>
</Card>
```

### 策略 2：組件別名
```typescript
// src/components/index.ts
// 為了兼容性，提供別名
export { Card as PyCard } from '@/components/ui/card'
export { Accordion as PyAccordion } from '@/components/ui/accordion'
```

### 策略 3：自動轉換腳本增強
```python
# migration/convert_elements.py
def convert_card(card):
    """將 Python Card 轉換為 MDX Card"""
    mdx = "<Card>\n"

    if card.header:
        mdx += "  <CardHeader>\n"
        mdx += convert_element(card.header)
        mdx += "  </CardHeader>\n"

    if card.body:
        gap_class = get_gap_class(card.body_gap)
        mdx += f"  <CardContent className=\"{gap_class}\">\n"
        for item in card.body:
            mdx += "    " + convert_element(item) + "\n"
        mdx += "  </CardContent>\n"

    mdx += "</Card>\n"
    return mdx
```

---

## 📋 組件開發檢查清單

### 每個組件完成時需確認：
- [ ] TypeScript 類型定義完整
- [ ] 支持 className 屬性（可擴展樣式）
- [ ] 響應式設計（Mobile First）
- [ ] 無障礙性（ARIA 屬性）
- [ ] 性能優化（lazy loading、client:visible）
- [ ] 文檔說明（Props、使用範例）

### 互動組件額外檢查：
- [ ] 正確使用 Islands（client:visible / client:load）
- [ ] 避免不必要的 hydration
- [ ] 事件處理器優化
- [ ] 狀態管理合理

---

## 🎯 成功指標

### 代碼質量
- ✅ TypeScript 類型覆蓋率 100%
- ✅ 組件可重用性高
- ✅ 樣式一致性（shadcn + Tailwind）

### 性能指標
- ✅ 首次加載 JS < 30KB（靜態頁面）
- ✅ 互動組件按需加載
- ✅ 圖片自動 lazy loading

### 開發體驗
- ✅ MDX 中可直接使用組件
- ✅ 編輯器自動補全
- ✅ 熱重載 < 200ms

---

## 🔗 參考資源

- [shadcn/ui Components](https://ui.shadcn.com/docs/components)
- [Embla Carousel](https://www.embla-carousel.com/)
- [Fancybox Documentation](https://fancyapps.com/fancybox/)
- [Astro Islands](https://docs.astro.build/en/concepts/islands/)
- [Tailwind CSS](https://tailwindcss.com/docs)

---

**準備好開始實現了嗎？我建議按照以下順序：**

1. **設置 shadcn/ui** - 安裝 Card, Accordion, Tabs, Button
2. **實現 5 個核心組件** - Text, Image, ListStr, DivBar, Youtube
3. **實現 IconBlock** - 自定義 React 組件
4. **實現 ImageCarousel** - 集成 Embla Carousel
5. **測試第一個完整頁面** - 以 MindReader 為例

你想從哪一步開始？
