import type zhHant from "./zh-Hant";

const en: typeof zhHant = {
  // Navigation
  nav: {
    about: "About",
    articles: "Articles",
    apps: "Apps",
    projects: "Projects",
    menu: "Menu",
    contactMethods: "Contact",
  },

  // Header (app/project sub-pages)
  header: {
    intro: "Intro",
    open: "Open",
  },

  // Footer
  footer: {
    products: "Products & Apps",
    links: "Links",
    donate: "Donate",
    connections: "Connections",
    config: "Settings",
    language: "Language",
    knowledgeResources: "Learning Resources",
    bookmarks: "Curated Bookmarks",
    learningLibrary: "Resource Library",
    portalyDonate: "Portaly Sponsor",
    copyright:
      "Copyright \u00a9 2026 LuMakes \u00b7 Liang-Chin Lu. All rights reserved.",
    privacyPolicy: "Privacy Policy",
  },

  // Common
  common: {
    showMore: "Show more",
    showMoreCount: "Show more ({count} total)",
    viewAllArticles: "View all articles",
    viewAllApps: "View all apps",
    backToTop: "Back to top",
    viewProject: "View project",
    now: "Present",
  },

  // Homepage
  index: {
    title:
      "Let Tech Handle the Tedious, Save Your Time for Inspiration \u00b7 LuMakes",
    description:
      "Outsource repetitive work to technology, freeing up space for creative thinking. Liang-Chin Lu's personal brand, sharing workflow strategies, product design, and full-stack development.",
    brand: "LuMakes",
    heroTitle: "Let Tech Handle the Tedious\nSave Your Time for Inspiration",
    heroSubtitle:
      "Outsource repetitive work to technology, freeing up space for creative thinking",
    browseArticles: "Browse Articles",
    aboutMe: "About Me",
    aboutSectionTitle: "I'm Liang-Chin Lu",
    aboutSectionDescription:
      "A full-stack engineer who combines technology with design thinking. LuMakes is my personal brand, documenting how I use tech products and methodologies to streamline life \u2014 outsource the repetitive, keep the creative.",
    articlesSectionTitle: "Articles",
    articlesSectionDescription:
      "Each article focuses on a single topic, covering the reasoning behind my choices and how I integrate tools into my workflow",
    appsSectionTitle: "Self-Built Apps",
    appsSectionDescription: "Small tools I built to solve my own needs",
    projectsSectionTitle: "Projects",
    projectsSectionDescription:
      "Complete records from concept to launch, spanning tech applications, product design, and full-stack development",
  },

  // About page
  about: {
    title:
      "About Liang-Chin Lu \u00b7 Full-Stack Engineer with AI Expertise & Design Thinking \u00b7 LuMakes",
    description:
      "Work experience, awards, and projects by Liang-Chin Lu, founder of LuMakes. AI engineer, product designer, and full-stack developer focused on AI-powered workflows, knowledge management, and creative building.",
    heroTitle: "Full-Stack Engineer with AI Expertise & Design Thinking",
    workExperience: "Work Experience",
    projectWorks: "Projects",
    awards: "Awards",
    noAwards: "No awards recorded yet",
    certifications: "Certifications",
    certificationsCount: "{count} certifications",
    showAllCertifications: "Show all {count}",
  },

  // Articles listing page
  articles: {
    title:
      "Articles \u00b7 Workflow Strategies, Digital Productivity & Dev Notes \u00b7 LuMakes",
    description:
      "Tool recommendations, methodologies, and practical notes on workflow automation, digital productivity, knowledge management, and full-stack development.",
    heading: "Articles",
    subtitle: "Tool recommendations & usage guides by category",
    allLabel: "All",
    showMoreCount: "Show more ({count} articles)",
    noArticles: "No articles published yet",
    noArticlesInCategory: "No articles in this category yet",
    publishedOn: "Published on",
    updatedOn: "Updated on",
    tableOfContents: "Table of Contents",
    youMightLike: "You might also like",
  },

  // Project detail page
  project: {
    statusActive: "Active",
    statusClosed: "Closed",
    statusSwitch: "Handed Off",
    statusPaused: "Paused",
    statusUnknown: "Unknown",
    featured: "Featured",
    awards: "Awards",
    tools: "Tech Stack",
  },

  // Privacy page
  privacy: {
    title: "Privacy Policy \u00b7 LuMakes",
    description:
      "How this website collects data, uses cookies, and implements Google Analytics.",
    heading: "Privacy Policy",
    lastUpdated: "Last updated: {date}",
    intro:
      'Thank you for visiting this website (lumakes.com, hereinafter referred to as "this website"). This policy explains how this website collects, uses, and protects your personal data, as well as your rights. Please read carefully before using this website.',
    section1Title: "1. What Data We Collect",
    section1Intro:
      "This website does not actively ask you to provide personal information. The data collected comes from a third-party analytics tool (Google Analytics 4) and primarily includes:",
    section1Items: [
      "Device information: operating system, browser type, screen resolution, language settings.",
      "Network information: masked IP address, approximate geographic location (country and city level).",
      "Browsing behavior: pages visited, time spent, referring websites, click events.",
      "Cookie identifiers: used to distinguish anonymous visitors and sessions.",
    ],
    section1Note:
      "This website does not actively collect your name, email address, phone number, or other directly identifiable personal information.",
    section2Title: "2. How We Use Your Data",
    section2Intro:
      "The collected data is used solely for the following purposes:",
    section2Items: [
      "Analyzing website traffic and usage patterns to understand what content is helpful to readers.",
      "Diagnosing technical issues and improving page performance and user experience.",
      "Evaluating the reach and effectiveness of content and products (such as articles and app introductions).",
    ],
    section2Note:
      "This website does not use collected data for advertising, nor does it sell or exchange data with third-party marketing entities.",
    section3Title: "3. Third-Party Services",
    section3Intro:
      "This website uses Google Analytics 4 (GA4) for web analytics, provided by Google LLC. GA4 uses cookies and similar technologies to record your visit information. This data is transmitted to Google servers and processed in accordance with Google's privacy policy.",
    section3Cloudflare:
      "This website is hosted on Cloudflare Pages. Cloudflare may log access records for security and service operations purposes. For details, please refer to the",
    section3CloudflareLink: "Cloudflare Privacy Policy",
    section4Title: "4. Cookie Usage",
    section4Intro:
      "This website uses cookies primarily to enable Google Analytics to identify unique visitors and sessions. These cookies do not store directly identifiable personal information.",
    section4Control:
      "You can control or disable cookies through the following methods:",
    section4Items: [
      "Delete existing cookies or block future cookies in your browser settings.",
    ],
    section4GAOptout: "Google Analytics Opt-out Add-on",
    section4GAOptoutSuffix: " to completely disable GA tracking.",
    section5Title: "5. Data Retention",
    section5Content:
      "GA4 retains event data for 14 months by default. After this period, individual user-level data is automatically deleted, and only aggregated statistical reports are retained.",
    section6Title: "6. Your Rights",
    section6Intro:
      "In accordance with Taiwan's Personal Data Protection Act and general international privacy standards, you may exercise the following rights:",
    section6Items: [
      "Inquire and review whether your data has been collected.",
      "Request deletion or cessation of processing your data.",
      "Object to specific data processing activities.",
    ],
    section6Note:
      "To exercise these rights, please submit a request through the contact methods provided below. I will respond within a reasonable timeframe.",
    section7Title: "7. Minors",
    section7Content:
      "This website does not actively collect data from children under 13 years of age (or the equivalent age specified by local law). If such data is found to have been inadvertently collected, it will be deleted immediately.",
    section8Title: "8. Policy Updates",
    section8Content:
      'This policy may be amended in response to legal or service changes. Updated versions will be posted directly on this page with a new "Last Updated" date. We recommend checking back periodically for the latest version.',
    section9Title: "9. Contact",
    section9Content:
      "If you have any questions about this policy or wish to exercise the aforementioned user rights, you can reach me through the contact methods (social links) provided in the page footer.",
  },

  // Down Resume page
  downResume: {
    title: "Download Resume \u00b7 Liang-Chin Lu \u00b7 LuMakes",
    description:
      "Preview and download resumes in general, development, and design versions.",
    heading: "Download Resume",
    subheading: "Liang-Chin Lu \u00b7 LuMakes",
    tabs: {
      general: "General",
      dev: "Development",
      design: "Design",
    },
    descriptions: {
      general:
        "A balanced overview of experience, projects, and core skills for general applications.",
      dev: "Focused on full-stack development, AI engineering, and technical projects.",
      design:
        "Focused on product design, visual systems, and design workflows.",
    },
    openInNewTab: "Open in new tab",
    download: "Download PDF",
    mobileHint:
      'On mobile, tap "Download PDF" for the best reading experience.',
  },
} as const;

export default en;
