import type { Locale } from "@/i18n";

export type IssuerKey = "anthropic" | "coursera" | "google";

export interface Certification {
  name: string;
  issuer: IssuerKey;
  issuedDate: string;
  credentialId?: string;
  credentialUrl?: string;
  skills: {
    "zh-Hant": string[];
    en: string[];
  };
}

export const issuerLabels: Record<IssuerKey, Record<Locale, string>> = {
  anthropic: { "zh-Hant": "Anthropic", en: "Anthropic" },
  coursera: { "zh-Hant": "Coursera", en: "Coursera" },
  google: { "zh-Hant": "Google", en: "Google" },
};

export const issuerOrder: IssuerKey[] = ["anthropic", "coursera", "google"];

export const certifications: Certification[] = [
  {
    name: "Claude Code in Action",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "6m59k2xomurw",
    credentialUrl: "https://verify.skilljar.com/c/6m59k2xomurw",
    skills: {
      "zh-Hant": ["Claude Code", "工作流自動化"],
      en: ["Claude Code", "Workflow Automation"],
    },
  },
  {
    name: "Building with the Claude API",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "d8ammbts6av4",
    credentialUrl: "https://verify.skilljar.com/c/d8ammbts6av4",
    skills: {
      "zh-Hant": ["Claude API", "應用開發"],
      en: ["Claude API", "Application Development"],
    },
  },
  {
    name: "Model Context Protocol: Advanced Topics",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "mbfvdrvi2uhp",
    credentialUrl: "https://verify.skilljar.com/c/mbfvdrvi2uhp",
    skills: {
      "zh-Hant": ["MCP", "AI Agent", "進階開發"],
      en: ["MCP", "AI Agents", "Advanced Development"],
    },
  },
  {
    name: "Introduction to Model Context Protocol",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "cp4bq4f8x8cn",
    credentialUrl: "https://verify.skilljar.com/c/cp4bq4f8x8cn",
    skills: {
      "zh-Hant": ["MCP", "AI Agent"],
      en: ["MCP", "AI Agents"],
    },
  },
  {
    name: "Introduction to subagents",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "pzsmu4qzxw5j",
    credentialUrl: "https://verify.skilljar.com/c/pzsmu4qzxw5j",
    skills: {
      "zh-Hant": ["AI Agent", "Claude Code"],
      en: ["AI Agents", "Claude Code"],
    },
  },
  {
    name: "Introduction to agent skills",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "6zfe3gfa8ec8",
    credentialUrl: "https://verify.skilljar.com/c/6zfe3gfa8ec8",
    skills: {
      "zh-Hant": ["AI Agent", "Claude Code"],
      en: ["AI Agents", "Claude Code"],
    },
  },
  {
    name: "Claude code 101",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "brpfr7iiwbxp",
    credentialUrl: "https://verify.skilljar.com/c/brpfr7iiwbxp",
    skills: {
      "zh-Hant": ["Claude Code"],
      en: ["Claude Code"],
    },
  },
  {
    name: "Claude 101",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "99mwaucjqvzj",
    credentialUrl: "https://verify.skilljar.com/c/99mwaucjqvzj",
    skills: {
      "zh-Hant": ["Claude"],
      en: ["Claude"],
    },
  },
  {
    name: "Introduction to Claude Cowork",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "7vpvci86w9rv",
    credentialUrl: "https://verify.skilljar.com/c/7vpvci86w9rv",
    skills: {
      "zh-Hant": ["Claude", "團隊協作"],
      en: ["Claude", "Team Collaboration"],
    },
  },
  {
    name: "Claude with Google Cloud's Vertex AI",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "zdqiuy8qzn5b",
    credentialUrl: "https://verify.skilljar.com/c/zdqiuy8qzn5b",
    skills: {
      "zh-Hant": ["Claude", "Google Cloud Vertex AI", "雲端部署"],
      en: ["Claude", "Google Cloud Vertex AI", "Cloud Deployment"],
    },
  },
  {
    name: "Claude in Amazon Bedrock",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "pqdeg5tjx4ie",
    credentialUrl: "https://verify.skilljar.com/c/pqdeg5tjx4ie",
    skills: {
      "zh-Hant": ["Claude", "Amazon Bedrock", "雲端部署"],
      en: ["Claude", "Amazon Bedrock", "Cloud Deployment"],
    },
  },
  {
    name: "Teaching the AI Fluency Framework",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "3vobkicvmnvu",
    credentialUrl: "https://verify.skilljar.com/c/3vobkicvmnvu",
    skills: {
      "zh-Hant": ["AI 素養", "教學設計"],
      en: ["AI Fluency", "Teaching"],
    },
  },
  {
    name: "AI Fluency Framework & Foundations",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "prntjdjdrn69",
    credentialUrl: "https://verify.skilljar.com/c/prntjdjdrn69",
    skills: {
      "zh-Hant": ["AI 素養"],
      en: ["AI Fluency"],
    },
  },
  {
    name: "AI Capabilities and Limitations",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "3pdiktek2ted",
    credentialUrl: "https://verify.skilljar.com/c/3pdiktek2ted",
    skills: {
      "zh-Hant": ["AI 素養"],
      en: ["AI Fluency"],
    },
  },
  {
    name: "AI Fluency for educators",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "vnw973jq25px",
    credentialUrl: "https://verify.skilljar.com/c/vnw973jq25px",
    skills: {
      "zh-Hant": ["AI 素養", "教學設計"],
      en: ["AI Fluency", "Teaching"],
    },
  },
  {
    name: "AI Fluency for nonprofits",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "hhdez3n9j452",
    credentialUrl: "https://verify.skilljar.com/c/hhdez3n9j452",
    skills: {
      "zh-Hant": ["AI 素養"],
      en: ["AI Fluency"],
    },
  },
  {
    name: "AI Fluency for students",
    issuer: "anthropic",
    issuedDate: "2026-04",
    credentialId: "9mxzfpwwbx7w",
    credentialUrl: "https://verify.skilljar.com/c/9mxzfpwwbx7w",
    skills: {
      "zh-Hant": ["AI 素養"],
      en: ["AI Fluency"],
    },
  },
  {
    name: "Google Data Analytics Professional Certificate",
    issuer: "coursera",
    issuedDate: "2021-12",
    credentialUrl:
      "https://www.credly.com/badges/a6edfde9-6c3a-442b-8d3f-ef5859e08a62",
    skills: {
      "zh-Hant": ["SQL", "資料分析", "Python", "MySQL"],
      en: ["SQL", "Data Analysis", "Python", "MySQL"],
    },
  },
  {
    name: "IBM: Data Visualization & Dashboard Essentials",
    issuer: "coursera",
    issuedDate: "2021-11",
    credentialUrl:
      "https://www.credly.com/badges/b1cf3e2a-9dd5-47ff-9b60-dc90883d96cc",
    skills: {
      "zh-Hant": ["SQL", "資料分析", "MySQL"],
      en: ["SQL", "Data Analysis", "MySQL"],
    },
  },
  {
    name: "Foundations of User Experience (UX) Design",
    issuer: "google",
    issuedDate: "2021-10",
    credentialUrl:
      "https://coursera.org/share/56efad39de506e876a825074d6e38237",
    skills: {
      "zh-Hant": ["使用者介面設計", "使用者體驗"],
      en: ["UI Design", "UX"],
    },
  },
  {
    name: "大數據分析：商業應用與策略管理",
    issuer: "coursera",
    issuedDate: "2021-09",
    credentialId: "F7PZES7XMUA7",
    credentialUrl:
      "https://coursera.org/share/6aa7167c8cf263f49fe5e4b63a8a093b",
    skills: {
      "zh-Hant": ["資料分析", "商業策略"],
      en: ["Data Analysis", "Business Strategy"],
    },
  },
  {
    name: "Google 基礎行銷資格認證",
    issuer: "google",
    issuedDate: "2021-08",
    credentialId: "49X VTB N46",
    credentialUrl:
      "https://learndigital.withgoogle.com/digitalgarage-tw/validate-certificate-code",
    skills: {
      "zh-Hant": ["行銷", "數位行銷"],
      en: ["Marketing", "Digital Marketing"],
    },
  },
];
