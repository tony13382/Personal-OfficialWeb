# CLAUDE.md

## 專案概覽

個人官方網站，使用 Astro 5 + React + Tailwind CSS v4 建構。部署在 Cloudflare Pages。

## 技術棧

- **框架**：Astro 5（SSG）+ React（互動元件）
- **樣式**：Tailwind CSS v4（透過 @tailwindcss/vite 整合）
- **UI 元件**：shadcn/ui + Radix UI
- **圖示**：Phosphor Icons + Lucide React
- **內容**：MDX（文章、專案、經歷）
- **部署**：Cloudflare Pages
- **圖片**：Astro Image（Sharp，quality: 90）

## 常用指令

```bash
npm run dev      # 啟動開發伺服器
npm run build    # 建構正式版本
npm run preview  # 預覽建構結果
```

## 專案結構

```
src/
├── content/          # MDX 內容
│   ├── articles/     # 文章（雙語）
│   │   ├── zh-Hant/  # 中文版
│   │   └── en/       # 英文版
│   ├── projects/     # 專案頁面
│   └── jobs/         # 經歷頁面
├── pages/            # Astro 頁面路由
├── components/       # React + Astro 元件
├── layouts/          # 頁面佈局
├── assets/imgs/      # 圖片資源（由 Astro Image 處理）
└── styles/           # 全域樣式
public/
└── og/               # OG Cover 圖片（不經過 Astro Image 處理）
```

## 文章創作流程（雙語）

文章內容放在 `src/content/articles/zh-Hant/` 跟 `src/content/articles/en/`，採用「中文先行」的三階段流程：

1. **方向確認與大綱討論** — 決定主題、文章類型、H2 結構、slug 命名
2. **中文內容撰寫與打磨** — 只處理 `zh-Hant/` 版本，反覆修改到滿意為止
3. **英文版本翻譯** — 中文定稿後，才建立 `en/` 版本

原則：在中文版本尚未定稿前，不建立英文版本。這樣迭代時只需修改一份檔案，避免雙語同步維護的負擔。

### 修改既有文章時的 updatedDate 提醒

當對**已經發佈**的文章做內容層級的修改時，應該主動詢問使用者要不要在 frontmatter 加上或更新 `updatedDate: YYYY-MM-DD`（中英版本要一起更新）。

判斷原則：

- **要提醒更新 `updatedDate`**：工具換版本、流程步驟改掉、結論或推薦調整、補上重要遺漏、補新章節
- **不用提醒**：錯字、標點、排版、內部連結修正、純翻譯校對、描述文案微調

排序一律照 `date`（發佈日），`updatedDate` 不影響排序，只是「這篇最近有維護」的信號——文章卡片會在 `updatedDate` 位於近 60 天內時顯示「已更新」徽章（見 `ArticleCard.astro`）。

## 分享專欄（Toolbox）寫作指引

### 定位

目標讀者是廣泛的科技愛好者。核心價值是讓讀者帶走「工具 + 方法」的組合。

### 每篇文章必須回答三個問題

1. **用什麼工具** — 工具本身的介紹
2. **為什麼選它** — 選擇的理由跟比較過的替代方案
3. **怎麼搭配使用** — 工具之間的串接方式、具體的工作流程

### 寫作風格

- 第一人稱、口語化，像在跟朋友分享經驗
- 用「跟」不用「與」
- 不用 emoji
- 交代選擇脈絡：「因為我同時在用 A 跟 B，所以...」
- 方法論搭配具體操作步驟跟提示詞範例

### MDX 特殊元件

- **Pricing Tag**：`<span class="pricing-tag">免費</span>`（綠）、`.paid`（橘）、`.freemium`（藍）
- **Callout**：`<div class="callout info">...</div>`（藍）、`.warning`（粉）
- **Code Title**：`<p class="code-title">檔案名稱</p>`
- **Official Link（大按鈕）**：`<a href="..." target="_blank" class="official-link">文字</a>`，只用在獨立一行的 CTA，不要嵌在句子裡
- **行內連結**：用一般 Markdown 連結語法 `[文字](url)`，用在段落內文中的超連結

#### 連結樣式選用原則（重要）

- **文本較多的行內連結 → 一律用 Markdown 連結 `[文字](url)`**，不要用 `class="official-link"` 的大按鈕
- **外連按鈕用小的就好**，只有獨立成行的 CTA、引導使用者點擊前往的明確入口才用大按鈕
- 段落中提到其他文章、外部資源、工具名稱的連結，全部都用 Markdown 行內連結，不要把大按鈕塞在句子中間，會破壞閱讀節奏

### Commit 規範

使用 `/commit-generate` skill 來產生 commit message。不加 Co-Authored-By。

## 注意事項

- toolbox 頁面的 inline code 樣式是程式碼風格（灰底紅字），其他頁面是 highlight 風格（主題色底線）
- H2 區塊會被 JS 拆成獨立卡片，每個 H2 是一張卡片
- TOC 連結使用 replaceState 避免污染瀏覽器歷史
- 圖片品質設定為 90（astro.config.mjs）
- `.gitignore` 已排除 `design/` 跟 `*.ttf`
