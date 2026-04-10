import type { ImageMetadata } from "astro";
import kitCover from "../assets/imgs/apps/kit/cover.png";
import kitIcon from "../assets/imgs/apps/kit/icon.png";
import nextTagsCover from "../assets/imgs/apps/nexTags/cover.png";
import nextTagsIcon from "../assets/imgs/apps/nexTags/icon.png";
import cloudBioCover from "../assets/imgs/apps/cloudBio/cover.png";
import cloudBioIcon from "../assets/imgs/apps/cloudBio/icon.png";

export interface AppInfo {
  slug: string;
  name: string;
  description: string;
  url: string;
  cover?: ImageMetadata;
  icon?: ImageMetadata;
  projectSlug?: string;
  mode?: "iframe" | "page";
}

export const apps: AppInfo[] = [
  {
    slug: "cloudbio",
    name: "CloudBio・Bio Link 工具",
    description: "Bio 建置工具，支援多模塊與頁面，手機即可輕鬆編輯",
    url: "https://bio.lumakes.com/",
    cover: cloudBioCover,
    icon: cloudBioIcon,
    projectSlug: "cloudbio",
  },
  {
    slug: "kit",
    name: "Kit・書籤管理工具",
    description: "支援多層級資料夾與標籤分類的現代化書籤管理系統",
    url: "https://kit.lumakes.com/intro",
    cover: kitCover,
    icon: kitIcon,
    projectSlug: "kit",
  },
  {
    slug: "nextags",
    name: "NexTags・音樂整理工具",
    description: "多功能音樂管理系統：匯入、修改、智慧播放清單一站完成",
    url: "https://github.com/tony13382/NexTags",
    cover: nextTagsCover,
    icon: nextTagsIcon,
    projectSlug: "nextags",
    mode: "page",
  },
];
