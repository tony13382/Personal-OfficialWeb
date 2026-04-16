import type { ImageMetadata } from "astro";
import kitCover from "../assets/imgs/apps/kit/cover.png";
import kitIcon from "../assets/imgs/apps/kit/icon.png";
import nextTagsCover from "../assets/imgs/apps/nexTags/cover.png";
import nextTagsIcon from "../assets/imgs/apps/nexTags/icon.png";
import cloudBioCover from "../assets/imgs/apps/cloudBio/cover.png";
import cloudBioIcon from "../assets/imgs/apps/cloudBio/icon.png";
import stockCalcCover from "../assets/imgs/apps/stockCalc/cover.png";
import stockCalcIcon from "../assets/imgs/apps/stockCalc/icon.png";

export interface AppInfo {
  slug: string;
  name: string;
  nameEn: string;
  description: string;
  descriptionEn: string;
  url: string;
  cover?: ImageMetadata;
  icon?: ImageMetadata;
  projectSlug?: string;
  mode?: "iframe" | "page";
  footerIcon: string;
}

export type Locale = "zh-Hant" | "en";

/** Get the localized name for an app. */
export function getAppName(app: AppInfo, locale: Locale = "zh-Hant"): string {
  return locale === "en" ? app.nameEn : app.name;
}

/** Get the localized description for an app. */
export function getAppDescription(app: AppInfo, locale: Locale = "zh-Hant"): string {
  return locale === "en" ? app.descriptionEn : app.description;
}

export const apps: AppInfo[] = [
  {
    slug: "cloudbio",
    name: "CloudBio・Bio Link 工具",
    nameEn: "CloudBio \u00b7 Bio Link Builder",
    description: "Bio 建置工具，支援多模塊與頁面，手機即可輕鬆編輯",
    descriptionEn: "A bio link builder with multi-module and multi-page support, easily editable on mobile",
    url: "https://bio.lumakes.com/",
    cover: cloudBioCover,
    icon: cloudBioIcon,
    projectSlug: "cloudbio",
    footerIcon: "link",
  },
  {
    slug: "kit",
    name: "Kit・書籤管理工具",
    nameEn: "Kit \u00b7 Bookmark Manager",
    description: "支援多層級資料夾與標籤分類的現代化書籤管理系統",
    descriptionEn: "A modern bookmark management system with multi-level folders and tag-based organization",
    url: "https://kit.lumakes.com/intro",
    cover: kitCover,
    icon: kitIcon,
    projectSlug: "kit",
    footerIcon: "book-bookmark",
  },
  {
    slug: "nextags",
    name: "NexTags・音樂整理工具",
    nameEn: "NexTags \u00b7 Music Organizer",
    description: "多功能音樂管理系統：匯入、修改、智慧播放清單一站完成",
    descriptionEn: "All-in-one music management: import, edit tags, and create smart playlists",
    url: "https://github.com/tony13382/NexTags",
    cover: nextTagsCover,
    icon: nextTagsIcon,
    projectSlug: "nextags",
    mode: "page",
    footerIcon: "playlist",
  },
  {
    slug: "stockcal",
    name: "股票試算小工具",
    nameEn: "Stock Calculator",
    description: "輕鬆好用的股票交易試算工具",
    descriptionEn: "A simple and handy stock trading calculator",
    url: "https://stockcal.lumakes.com/",
    cover: stockCalcCover,
    icon: stockCalcIcon,
    projectSlug: "stock-calc",
    footerIcon: "calculator",
  },
];
