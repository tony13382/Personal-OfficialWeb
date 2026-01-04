# Bootstrap Icons → Lucide React 圖標遷移指南

## 已完成的遷移

所有 IconBlock 組件已從 Bootstrap Icons 遷移到 Lucide React。

### 遷移的檔案

- ✅ `src/components/react/IconBlock.tsx` - 組件本身
- ✅ `src/layouts/BaseLayout.astro` - 移除 Bootstrap Icons CDN
- ✅ `src/content/projects/mind-reader.mdx` - 更新所有圖標引用
- ✅ `src/content/projects/test-project.mdx` - 更新所有圖標引用

---

## 圖標名稱對照表

### 常用圖標映射

| Bootstrap Icons | Lucide React | 用途 |
|----------------|--------------|------|
| `bi-phone-fill` | `Smartphone` | 手機/移動設備 |
| `bi-github` | `Github` | GitHub 連結 |
| `bi-keyboard` | `Keyboard` | 鍵盤輸入 |
| `bi-hdd-network` / `bi-server` | `Server` | 伺服器/網絡 |
| `bi-line` | `MessageCircle` | Line 或訊息 |
| `bi-arrow-repeat` | `RefreshCw` | 轉換/刷新 |
| `bi-send` | `Send` | 發送 |
| `bi-database-down` | `Database` | 資料庫 |
| `bi-file-earmark-arrow-down` | `FileDown` | 文件下載（預設） |

### 其他常見對照

| Bootstrap Icons | Lucide React | 說明 |
|----------------|--------------|------|
| `bi-envelope` | `Mail` | 郵件 |
| `bi-link-45deg` | `Link` | 連結 |
| `bi-play-circle` | `PlayCircle` | 播放 |
| `bi-calendar` | `Calendar` | 日曆 |
| `bi-clock` | `Clock` | 時鐘 |
| `bi-star` | `Star` | 星星/收藏 |
| `bi-heart` | `Heart` | 喜歡 |
| `bi-image` | `Image` | 圖片 |
| `bi-camera` | `Camera` | 相機 |
| `bi-code` | `Code` | 程式碼 |
| `bi-terminal` | `Terminal` | 終端機 |
| `bi-cloud` | `Cloud` | 雲端 |
| `bi-download` | `Download` | 下載 |
| `bi-upload` | `Upload` | 上傳 |
| `bi-trash` | `Trash2` | 刪除 |
| `bi-pencil` | `Pencil` | 編輯 |
| `bi-check-circle` | `CheckCircle` | 完成 |
| `bi-x-circle` | `XCircle` | 錯誤/取消 |
| `bi-info-circle` | `Info` | 資訊 |
| `bi-exclamation-triangle` | `AlertTriangle` | 警告 |

---

## 如何使用 Lucide 圖標

### 在 MDX 中使用 IconBlock

```mdx
import { IconBlock } from '@/components/react/IconBlock'

<IconBlock
  title="GitHub 專案"
  subtitle="查看原始碼"
  href="https://github.com/username/repo"
  icon="Github"
  client:visible
/>
```

### 查找 Lucide 圖標

訪問 [Lucide Icons 官網](https://lucide.dev/icons/) 瀏覽所有可用圖標。

**重要提示**：
- 圖標名稱使用 **PascalCase**（如 `Github`, `Smartphone`, `MessageCircle`）
- 不是 kebab-case（`github`, `smart-phone`）或 class 名稱（`bi-github`）

### 技術細節

IconBlock 組件使用動態導入：

```tsx
import * as LucideIcons from "lucide-react"

// 動態獲取圖標組件
const IconComponent = (LucideIcons[icon as keyof typeof LucideIcons] as LucideIcon) || LucideIcons.FileDown
```

如果提供的圖標名稱無效，會自動降級到預設圖標 `FileDown`。

---

## 優勢

### 相比 Bootstrap Icons 的改進

1. **更好的 TypeScript 支持** - 完整的類型定義
2. **更小的 Bundle Size** - 只打包實際使用的圖標
3. **React 組件** - 更靈活的 props 和樣式控制
4. **現代化設計** - 更統一的視覺風格
5. **活躍維護** - Lucide 是活躍開發的開源專案

### 性能優化

- **按需加載**：Lucide React 支持 tree-shaking，未使用的圖標不會打包
- **React 整合**：原生 React 組件，無需額外 CSS 文件
- **靈活樣式**：可直接通過 className 控制大小和顏色

---

## 轉換其他專案時的注意事項

當轉換剩餘的 13 個專案時：

1. **檢查 Python 代碼中的圖標**：
   ```python
   # 在 Python 專案中搜尋
   Icon(icon_str="bi-something")
   ```

2. **參考對照表**：使用上面的映射表找到對應的 Lucide 圖標

3. **測試圖標顯示**：
   - 訪問 http://localhost:4321/projects/{slug}/
   - 確認所有圖標正常顯示
   - 檢查大小和顏色是否正確

4. **如果找不到完全對應的圖標**：
   - 訪問 https://lucide.dev/icons/
   - 搜尋類似功能的圖標
   - 選擇最接近的替代品

---

**最後更新**: 2024-12-28
**狀態**: ✅ 完成遷移
