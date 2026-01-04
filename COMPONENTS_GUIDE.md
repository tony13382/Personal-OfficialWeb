# React Components Guide

This guide documents the newly migrated React components from the Python `elements.py` system.

## Overview

All 11 missing components have been successfully converted from Python to React, providing full feature parity with the original system while being fully usable in MDX files.

---

## Project Structure

```
portfolio-astro/src/
├── components/
│   ├── react/               # React components
│   │   ├── AccordionBlock.tsx   # Existing
│   │   ├── Canva.tsx            # Existing
│   │   ├── IconBlock.tsx        # Existing
│   │   ├── ImageCarousel.tsx    # Existing
│   │   ├── TabsBlock.tsx        # Existing
│   │   ├── Youtube.tsx          # Existing
│   │   ├── Columns.tsx          # New - Layout
│   │   ├── Div.tsx              # New - Layout
│   │   ├── DivBar.tsx           # New - Layout
│   │   ├── ListDiv.tsx          # New - Layout
│   │   ├── Text.tsx             # New - Content
│   │   ├── ListStr.tsx          # New - Content
│   │   ├── Html.tsx             # New - Content
│   │   ├── Score.tsx            # New - Content
│   │   ├── Tool.tsx             # New - Content
│   │   ├── ImageWithLightbox.tsx # New - Media
│   │   └── LinkButton.tsx       # New - Media
│   └── ui/                  # shadcn/ui components
│       └── ...
├── lib/
│   ├── spacing.ts           # GapSet/SpaceSet utilities
│   └── formatters.ts        # Text formatting utilities
└── styles/
    └── global.css           # Custom CSS classes
```

---

## Component Reference

All components are React components designed for use in MDX files. Remember to add `client:load` or `client:visible` directives when using them.

### Layout Components

#### **Columns**

Responsive grid system (Bootstrap → Tailwind conversion)

```mdx
import { Columns } from '@/components/react/Columns'

<Columns cols={3} gap="regular" client:load>
  <div>Column 1</div>
  <div>Column 2</div>
  <div>Column 3</div>
</Columns>
```

**Props:**
- `cols?: 1 | 2 | 3 | 4 | 6 | 12` - Number of columns
- `gap?: GapSize | number` - Gap between items
- `className?: string`
- `children: ReactNode`

---

#### **Div**

Simple wrapper with margin controls

```mdx
import { Div } from '@/components/react/Div'

<Div mt={4} mb={2} client:load>
  <p>Content with margins</p>
</Div>
```

**Props:**
- `mt?: number` - Margin top
- `mb?: number` - Margin bottom
- `ms?: number` - Margin start
- `me?: number` - Margin end
- `className?: string`
- `children: ReactNode`

---

#### **DivBar**

Horizontal divider with spacing

```mdx
import { DivBar } from '@/components/react/DivBar'

<DivBar space="regular" opacity={0.15} client:load />
```

**Props:**
- `space?: 'nano' | 'mini' | 'regular' | 'wide'`
- `opacity?: number`
- `className?: string`

---

#### **ListDiv**

Flexible container with grid/flex/inline layouts

```mdx
import { ListDiv } from '@/components/react/ListDiv'

<ListDiv layout="flex" gap="regular" client:load>
  <div>Item 1</div>
  <div>Item 2</div>
</ListDiv>
```

**Props:**
- `layout?: 'grid' | 'flex' | 'inline'`
- `gap?: GapSize`
- `space?: SpaceConfig`
- `className?: string`
- `children: ReactNode`

---

### Content Components

#### **Text**

Typography component with backtick highlighting

```mdx
import { Text } from '@/components/react/Text'

<Text content="This is `highlighted` text" tag="h2" bold client:load />
```

**Props:**
- `content: string` - Text with optional backtick highlighting
- `tag?: 'h2' | 'h3' | 'h4' | 'p' | 'span'`
- `bold?: boolean`
- `center?: boolean`
- `pillType?: boolean`
- `className?: string`

---

#### **ListStr**

Unordered list with text formatting

```mdx
import { ListStr } from '@/components/react/ListStr'

<ListStr items={[
  "First item with `highlight`",
  "Second item",
]} client:load />
```

**Props:**
- `items: string[]`
- `className?: string`

---

#### **Html**

Raw HTML passthrough component

```mdx
import { Html } from '@/components/react/Html'

<Html code="<div>Custom HTML</div>" client:load />
```

**Props:**
- `code: string`

---

#### **Score**

Award/score display card

```mdx
import { Score } from '@/components/react/Score'

<Score name="Best Award" score="1st Place" group="Category" client:load />
```

**Props:**
- `name: string`
- `score: string`
- `group?: string`
- `className?: string`

---

#### **Tool**

Two-column tool description

```mdx
import { Tool } from '@/components/react/Tool'

<Tool name="Frontend" action="React, TypeScript" client:load />
```

**Props:**
- `name: string`
- `action: string`
- `className?: string`

---

### Media Components

#### **ImageWithLightbox**

Image with optional Fancybox lightbox

```mdx
import { ImageWithLightbox } from '@/components/react/ImageWithLightbox'

<ImageWithLightbox
  src="/path/to/image.jpg"
  alt="Description"
  allowPop
  rounded
  client:load
/>
```

**Props:**
- `src: string`
- `alt?: string`
- `allowPop?: boolean` - Enable lightbox
- `maxWidth?: number`
- `rounded?: boolean`
- `className?: string`

---

#### **LinkButton**

Button/link with theme styling

```mdx
import { LinkButton } from '@/components/react/LinkButton'

<LinkButton
  content="View Demo"
  href="/demo"
  fill
  icon="bi-arrow-right"
  client:load
/>
```

**Props:**
- `content: string`
- `href: string`
- `fill?: boolean`
- `openInTab?: boolean`
- `icon?: string`
- `className?: string`

---

## Usage Example in MDX

```mdx
---
title: My Project
description: Project description
---

import { Columns, Div, DivBar, Text, ListStr, Score, Tool } from '@/components/react'
import { ImageWithLightbox, LinkButton } from '@/components/react'

<Div mt={4} mb={6} client:load>
  <Text content="My Awesome `Project`" tag="h2" bold center client:load />
</Div>

<DivBar space="wide" client:load />

<Columns cols={3} gap="regular" client:load>
  <ImageWithLightbox src="/img1.jpg" alt="Screenshot" allowPop rounded client:load />
  <ImageWithLightbox src="/img2.jpg" alt="Screenshot" allowPop rounded client:load />
  <ImageWithLightbox src="/img3.jpg" alt="Screenshot" allowPop rounded client:load />
</Columns>

<DivBar space="regular" client:load />

<Text content="Key Features" tag="h3" bold client:load />
<ListStr items={[
  "Real-time data sync",
  "Responsive with `Tailwind CSS`",
  "Type-safe `TypeScript`",
]} client:load />

<DivBar space="regular" client:load />

<Columns cols={3} gap="regular" client:load>
  <Score name="Design Award" score="Gold" group="UI/UX" client:load />
  <Score name="Innovation" score="1st Place" client:load />
  <Score name="User Choice" score="4.8/5.0" client:load />
</Columns>

<DivBar space="wide" client:load />

<Columns cols={2} gap="small" client:load>
  <Tool name="Frontend" action="React, TypeScript, Tailwind" client:load />
  <Tool name="Backend" action="Python, FastAPI" client:load />
</Columns>

<DivBar space="wide" client:load />

<LinkButton content="View Demo" href="/demo" fill icon="bi-arrow-right" client:load />
```

---

## Migration from Python

### Component Mapping

| Python Class | React Component | Status |
|--------------|----------------|--------|
| `Columns` | `Columns.tsx` | ✅ Created |
| `Div` | `Div.tsx` | ✅ Created |
| `DivBar` | `DivBar.tsx` | ✅ Created |
| `ListDiv` | `ListDiv.tsx` | ✅ Created |
| `Text` | `Text.tsx` | ✅ Created |
| `ListStr` | `ListStr.tsx` | ✅ Created |
| `Html` | `Html.tsx` | ✅ Created |
| `Score` | `Score.tsx` | ✅ Created |
| `Tool` | `Tool.tsx` | ✅ Created |
| `Image` | `ImageWithLightbox.tsx` | ✅ Created |
| `LinkButton` | `LinkButton.tsx` | ✅ Created |
| `Card` | `Card` (shadcn/ui) | ✅ Already exists |
| `AccordionBlock` | `AccordionBlock.tsx` | ✅ Already exists |
| `Tab` | `TabsBlock.tsx` | ✅ Already exists |
| `Canva` | `Canva.tsx` | ✅ Already exists |
| `Youtube` | `Youtube.tsx` | ✅ Already exists |
| `IconBlock` | `IconBlock.tsx` | ✅ Already exists |
| `ImageCarousel` | `ImageCarousel.tsx` | ✅ Already exists |

### Props Naming

| Python | React |
|--------|-------|
| `fontsize` | `tag` |
| `allow_pop` | `allowPop` |
| `open_in_tab` | `openInTab` |
| `pill_type` | `pillType` |

### Bootstrap → Tailwind Classes

| Bootstrap | Tailwind |
|-----------|----------|
| `d-grid` | `grid` |
| `d-flex` | `flex` |
| `fw-bold` | `font-bold` |
| `text-center` | `text-center` |
| `rounded-pill` | `rounded-full` |
| `col-12 col-md-6` | `grid-cols-1 md:grid-cols-2` |

---

## Best Practices

1. **Always use path aliases**: Import with `@/components/react/...`
2. **Client directives required**: Always add `client:load` or `client:visible` in MDX
3. **Type safety**: All components have TypeScript interfaces
4. **Accessibility**: Use proper `alt` text for images
5. **Theme colors**: Use CSS variables (`var(--theme-primary)`)
6. **Responsive design**: Use responsive props like `cols` in Columns

---

## Client Directives

When using React components in MDX, you must specify how they should be hydrated:

- `client:load` - Load immediately on page load
- `client:visible` - Load when component enters viewport
- `client:idle` - Load after page is idle
- `client:only="react"` - Only render on client (skip SSR)

**Example:**
```mdx
<Text content="Hello `World`" tag="h2" client:load />
```

---

**Migration Complete**: All 11 components successfully converted to React! 🎉

## Summary

✅ **11 React Components** - Fully compatible with MDX
✅ **Type-safe** - Full TypeScript support
✅ **Bootstrap → Tailwind** - Modern CSS framework
✅ **Fancybox Integration** - Image lightbox ready
✅ **Responsive Grid** - Mobile-first design
✅ **Text Highlighting** - Backtick syntax support
