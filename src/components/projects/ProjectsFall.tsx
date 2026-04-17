import { useEffect, useState, useRef } from "react";
import type { CollectionEntry } from "astro:content";
import { Badge } from "@/components/ui/badge";
import {
  CaretDownIcon,
  CaretUpIcon,
  PauseIcon,
  PlayIcon,
  StarIcon,
  ArrowRightIcon,
} from "@phosphor-icons/react";
import { Card } from "../ui/card";
import { Button } from "../ui/button";
import { getImageSrc, type ImageSource } from "../react/image-source";
import backendSkillImg from "@/assets/imgs/projects/_skills/backend-skill.png";
import frontendSkillImg from "@/assets/imgs/projects/_skills/frontend-skill.png";
import deploySkillImg from "@/assets/imgs/projects/_skills/deploy-skill.png";
import datadesignSkillImg from "@/assets/imgs/projects/_skills/datadesign-skill.png";
import uxSkillImg from "@/assets/imgs/projects/_skills/ux-skill.png";
import figmaSkillImg from "@/assets/imgs/projects/_skills/figma-skill.png";

type SkillType = "dev" | "design";
type ProjectData = CollectionEntry<"projects">;

type SupportedLocale = "zh-Hant" | "en";

interface ProjectsFallProps {
  projects: ProjectData[];
  themes: Record<
    string,
    {
      primary: string;
      secondary: string;
      darkPrimary: string;
      darkSecondary: string;
    }
  >;
  compact?: boolean;
  pathPrefix?: string;
  locale?: SupportedLocale;
}

const i18nLabels = {
  "zh-Hant": {
    filterLabels: { dev: "開發", design: "設計" },
    collapse: "收起",
    viewMore: (n: number) => `查看更多 (${n} 個專案)`,
    noProjects: "目前沒有相關專案",
    carouselPause: "暫停輪播",
    carouselPlay: "繼續輪播",
    carouselNext: "下一項",
    devTabs: [
      {
        key: "backend",
        label: "後端 API",
        title: "有豐富的 API 開發經驗，具各類資料庫架構設計技能",
        body: {
          kind: "tags",
          groups: [
            {
              label: "後端框架包含：",
              tags: ["FastAPI · Python", "Go", "Express · NodeJS"],
            },
            {
              label: "資料庫涵蓋：",
              tags: [
                "PostgreSQL",
                "Cloudflare D1",
                "Supabase",
                "Firebase",
                "MongoDB",
                "Redis",
              ],
            },
          ],
        },
      },
      {
        key: "frontend",
        label: "前端 SPA",
        title: "開發大量 React SPA 的應用經驗",
        body: {
          kind: "tags",
          groups: [
            {
              label: "前端框架包含：",
              tags: ["React Router · Remix", "NextJS", "Astro"],
            },
            {
              label: "偏好工具庫：",
              tags: [
                "Vite",
                "Streamlit · Python",
                "TailwindCSS",
                "shadcn UI",
                "Recharts",
                "Flutter · 跨平台應用",
              ],
            },
          ],
        },
      },
      {
        key: "deploy",
        label: "自動部署",
        title: "自動部署管理、自動化工作",
        body: {
          kind: "tags",
          groups: [
            {
              label: "平台:",
              tags: ["Cloudflare Worker", "Linode", "AWS"],
            },
            {
              label: "偏好工具庫：",
              tags: ["Docker Compose", "Github Action", "n8n", "APP Script"],
            },
          ],
        },
      },
    ],
    designTabs: [
      {
        key: "info-design",
        label: "資訊設計",
        title: "理解問題透過數據分析並結合平面設計傳達資訊",
        body: {
          kind: "tags",
          groups: [
            {
              label: "資料整理與前處理：",
              tags: ["Excel", "Google Sheet", "Pandas · PY"],
            },
            {
              label: "儀表板：",
              tags: ["Looker Studio", "PowerBI", "IBM Cognos", "ggplot2 · PY"],
            },
            {
              label: "簡報：",
              tags: ["Canva", "Powerpoint · 精通母片"],
            },
          ],
        },
      },
      {
        key: "ux-flow",
        label: "UX 規劃",
        title: "結合量化與質化數據，探索最佳服務體驗",
        body: {
          kind: "comparison",
          columns: [
            {
              label: "質化・深入觀察",
              method: "用戶訪談",
              detail: "分析用戶意圖與想達成的目標",
            },
            {
              label: "量化・整體趨勢",
              method: "問卷表單",
              detail: "大批量蒐集行為與偏好資料",
            },
          ],
          summary: "整合質化深入觀察與量化整體趨勢，做服務體驗的通盤規劃",
        },
      },
      {
        key: "ui-proto",
        label: "UI 原型製作",
        title: "從介面規劃到高互動原型的完整設計能力",
        body: {
          kind: "features",
          items: [
            {
              index: "01",
              title: "介面規劃",
              description:
                "根據使用者流程（User Flow）及商業目標，規劃出最舒適的使用者介面，讓用戶能快速上手。",
            },
            {
              index: "02",
              title: "Figma 專業應用",
              description:
                "熟悉企業大量使用的 Figma，特別針對原子元件（Atomic Design）與企業色彩系統進行配置。",
            },
            {
              index: "03",
              title: "高互動性 MVP 製作",
              description:
                "憑藉 Figma 原型製作能力與開發經驗，不論用 Figma 或開發方式，都能快速做出高互動性的 MVP 原型。",
            },
          ],
        },
      },
    ],
    now: "現在",
  },
  en: {
    filterLabels: { dev: "Development", design: "Design" },
    collapse: "Collapse",
    viewMore: (n: number) => `View more (${n} projects)`,
    noProjects: "No related projects yet",
    carouselPause: "Pause carousel",
    carouselPlay: "Resume carousel",
    carouselNext: "Next tab",
    devTabs: [
      {
        key: "backend",
        label: "Backend API",
        title:
          "Extensive API development experience across diverse database architectures",
        body: {
          kind: "tags",
          groups: [
            {
              label: "Backend frameworks:",
              tags: ["FastAPI · Python", "Go", "Express · NodeJS"],
            },
            {
              label: "Databases:",
              tags: [
                "PostgreSQL",
                "Cloudflare D1",
                "Supabase",
                "Firebase",
                "MongoDB",
                "Redis",
              ],
            },
          ],
        },
      },
      {
        key: "frontend",
        label: "Frontend SPA",
        title: "Extensive experience building React SPA applications",
        body: {
          kind: "tags",
          groups: [
            {
              label: "Frontend frameworks:",
              tags: ["React Router · Remix", "NextJS", "Astro"],
            },
            {
              label: "Preferred toolkit:",
              tags: [
                "Vite",
                "Streamlit · Python",
                "TailwindCSS",
                "shadcn UI",
                "Recharts",
                "Flutter · Cross-platform",
              ],
            },
          ],
        },
      },
      {
        key: "deploy",
        label: "Auto Deploy",
        title: "Automated deployment & workflow automation",
        body: {
          kind: "tags",
          groups: [
            {
              label: "Platforms:",
              tags: ["Cloudflare Worker", "Linode", "AWS"],
            },
            {
              label: "Preferred toolkit:",
              tags: ["Docker Compose", "Github Action", "n8n", "APP Script"],
            },
          ],
        },
      },
    ],
    designTabs: [
      {
        key: "info-design",
        label: "Information Design",
        title:
          "Understanding problems through data analysis and communicating insights through visual design",
        body: {
          kind: "tags",
          groups: [
            {
              label: "Data preparation:",
              tags: ["Excel", "Google Sheet", "Pandas · PY"],
            },
            {
              label: "Dashboards:",
              tags: ["Looker Studio", "PowerBI", "IBM Cognos", "ggplot2 · PY"],
            },
            {
              label: "Presentations:",
              tags: ["Canva", "Powerpoint · Template mastery"],
            },
          ],
        },
      },
      {
        key: "ux-flow",
        label: "UX Planning",
        title:
          "Blending qualitative and quantitative data to explore the best service experience",
        body: {
          kind: "comparison",
          columns: [
            {
              label: "Qualitative · Depth",
              method: "User Interviews",
              detail: "Uncover user intent and goals",
            },
            {
              label: "Quantitative · Trends",
              method: "Surveys",
              detail: "Collect broad behavioral and preference data",
            },
          ],
          summary:
            "Combining qualitative depth with quantitative trends to plan the full service experience",
        },
      },
      {
        key: "ui-proto",
        label: "UI Prototyping",
        title:
          "From interface planning to high-fidelity interactive prototypes",
        body: {
          kind: "features",
          items: [
            {
              index: "01",
              title: "Interface Planning",
              description:
                "Shape intuitive UIs grounded in user flows and business goals so users can get up to speed quickly.",
            },
            {
              index: "02",
              title: "Figma Expertise",
              description:
                "Fluent in Figma as used across enterprises, with a focus on atomic components and enterprise color systems.",
            },
            {
              index: "03",
              title: "High-interactivity MVPs",
              description:
                "Combining Figma prototyping with development experience to quickly build highly interactive MVP prototypes.",
            },
          ],
        },
      },
    ],
    now: "Present",
  },
} as const;

const skillTabImages: Record<string, ImageSource> = {
  backend: backendSkillImg,
  frontend: frontendSkillImg,
  deploy: deploySkillImg,
  "info-design": datadesignSkillImg,
  "ux-flow": uxSkillImg,
  "ui-proto": figmaSkillImg,
};

type SkillTabData =
  | (typeof i18nLabels)[SupportedLocale]["devTabs"][number]
  | (typeof i18nLabels)[SupportedLocale]["designTabs"][number];

type SkillTabBody = SkillTabData["body"];

const SKILL_CAROUSEL_ROTATION_MS = 5000;
const SKILL_CAROUSEL_TICK_MS = 50;

function SkillTabBodyRenderer({ body }: { body: SkillTabBody }) {
  if (body.kind === "tags") {
    return (
      <div className="space-y-5">
        {body.groups.map((group, gi) => (
          <div key={gi}>
            <p className="text-sm text-foreground mb-3">{group.label}</p>
            <div className="flex flex-wrap gap-2">
              {group.tags.map((tag) => (
                <span
                  key={tag}
                  className="px-3 py-1 rounded-full bg-muted border-foreground text-sm text-foreground"
                >
                  {tag}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    );
  }

  if (body.kind === "comparison") {
    return (
      <div className="space-y-4">
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          {body.columns.map((col, ci) => (
            <div
              key={ci}
              className="rounded-xl border border-border p-4 space-y-2"
            >
              <p className="text-xs font-semibold text-muted-foreground tracking-wide uppercase">
                {col.label}
              </p>
              <p className="text-base font-bold text-foreground">
                {col.method}
              </p>
              <p className="text-sm text-muted-foreground leading-relaxed">
                {col.detail}
              </p>
            </div>
          ))}
        </div>
        <div className="rounded-xl bg-muted px-4 py-3 text-sm text-foreground leading-relaxed">
          {body.summary}
        </div>
      </div>
    );
  }

  if (body.kind === "features") {
    return (
      <div className="space-y-5">
        {body.items.map((item) => (
          <div key={item.index} className="flex gap-4">
            <div className="shrink-0 w-8 text-muted-foreground/60 font-bold text-lg leading-tight">
              {item.index}
            </div>
            <div className="flex-1 space-y-1">
              <p className="font-bold text-foreground">{item.title}</p>
              <p className="text-sm text-muted-foreground leading-relaxed">
                {item.description}
              </p>
            </div>
          </div>
        ))}
      </div>
    );
  }

  return null;
}

function SkillCarousel({
  tabs,
  pauseLabel,
  playLabel,
  nextLabel,
}: {
  tabs: readonly SkillTabData[];
  pauseLabel: string;
  playLabel: string;
  nextLabel: string;
}) {
  const [activeIndex, setActiveIndex] = useState(0);
  const [isPaused, setIsPaused] = useState(false);
  const [isHovered, setIsHovered] = useState(false);
  const [progress, setProgress] = useState(0);
  const touchStartRef = useRef<{ x: number; y: number } | null>(null);

  const rotationSuspended = isPaused || isHovered;

  useEffect(() => {
    if (rotationSuspended) return;
    let elapsed = 0;
    const interval = setInterval(() => {
      elapsed += SKILL_CAROUSEL_TICK_MS;
      if (elapsed >= SKILL_CAROUSEL_ROTATION_MS) {
        setActiveIndex((i) => (i + 1) % tabs.length);
        elapsed = 0;
      }
      setProgress((elapsed / SKILL_CAROUSEL_ROTATION_MS) * 100);
    }, SKILL_CAROUSEL_TICK_MS);
    return () => clearInterval(interval);
  }, [rotationSuspended, tabs.length, activeIndex]);

  const handleTabClick = (i: number) => {
    setActiveIndex(i);
    setProgress(0);
  };

  const handleNext = () => {
    setActiveIndex((i) => (i + 1) % tabs.length);
    setProgress(0);
  };

  const togglePause = () => setIsPaused((p) => !p);

  // Horizontal swipe beyond this much (px) triggers a tab switch. Vertical
  // dominance short-circuits so page scroll gestures aren't hijacked.
  const SWIPE_THRESHOLD_PX = 48;

  const handleTouchStart = (e: React.TouchEvent) => {
    const t = e.touches[0];
    touchStartRef.current = { x: t.clientX, y: t.clientY };
    setIsHovered(true);
  };

  const handleTouchEnd = (e: React.TouchEvent) => {
    const start = touchStartRef.current;
    touchStartRef.current = null;
    setIsHovered(false);
    if (!start) return;
    const t = e.changedTouches[0];
    const dx = t.clientX - start.x;
    const dy = t.clientY - start.y;
    if (Math.abs(dx) <= SWIPE_THRESHOLD_PX) return;
    if (Math.abs(dy) >= Math.abs(dx)) return;
    setActiveIndex((i) =>
      dx < 0 ? (i + 1) % tabs.length : (i - 1 + tabs.length) % tabs.length,
    );
    setProgress(0);
  };

  const handleTouchCancel = () => {
    touchStartRef.current = null;
    setIsHovered(false);
  };

  const toggleAriaLabel = isPaused ? playLabel : pauseLabel;

  return (
    <Card
      className="shadow-none overflow-hidden gap-0 touch-pan-y"
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      onTouchStart={handleTouchStart}
      onTouchEnd={handleTouchEnd}
      onTouchCancel={handleTouchCancel}
    >
      <div className="flex items-center justify-between gap-4 px-6 pt-5 pb-4">
        <div className="flex items-center gap-4 sm:gap-6 md:gap-8 flex-wrap">
          {tabs.map((tab, i) => (
            <button
              key={tab.key}
              type="button"
              onClick={() => handleTabClick(i)}
              className={`sm:text-xl font-bold transition-colors cursor-pointer ${i === activeIndex
                ? "text-foreground"
                : "hidden md:block text-muted-foreground/60 hover:text-muted-foreground"
                }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
        <div className="flex -mt-1 gap-3">
          <button
            type="button"
            onClick={togglePause}
            aria-label={toggleAriaLabel}
            title={toggleAriaLabel}
            className="p-2 shrink-0 text-foreground border rounded-full transition-opacity opacity-50 hover:opacity-60 cursor-pointer"
          >
            {isPaused ? (
              <PlayIcon className="size-4" weight="fill" />
            ) : (
              <PauseIcon className="size-4" weight="fill" />
            )}
          </button>
          <button
            type="button"
            onClick={handleNext}
            aria-label={nextLabel}
            title={nextLabel}
            className="md:hidden p-2 shrink-0 text-foreground border rounded-full transition-opacity opacity-50 hover:opacity-60 cursor-pointer"
          >
            <ArrowRightIcon className="size-4" />
          </button>
        </div>
      </div>

      <button
        type="button"
        onClick={togglePause}
        aria-label={toggleAriaLabel}
        className="block relative h-0.5 w-full bg-border cursor-pointer focus:outline-none"
      >
        <div
          className="absolute left-0 top-0 h-full bg-foreground"
          style={{ width: `${progress}%` }}
        />
      </button>

      <div className="overflow-hidden">
        <div
          className="flex transition-transform duration-500 ease-out"
          style={{ transform: `translateX(-${activeIndex * 100}%)` }}
        >
          {tabs.map((tab, i) => (
            <div
              key={tab.key}
              aria-hidden={i !== activeIndex}
              className="w-full shrink-0 grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-10 p-6 md:p-8"
            >
              <div className="flex items-center justify-center order-1 md:order-none">
                <img
                  src={getImageSrc(skillTabImages[tab.key])}
                  alt={tab.label}
                  width={512}
                  height={512}
                  loading="lazy"
                  decoding="async"
                  className="w-full max-w-80 h-auto"
                />
              </div>
              <div className="flex flex-col justify-center gap-5 order-2 md:order-none">
                <p className="text-xl font-bold leading-snug">{tab.title}</p>
                <SkillTabBodyRenderer body={tab.body} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </Card>
  );
}

const getFilterDescriptions = (
  t: (typeof i18nLabels)[SupportedLocale],
): Record<string, React.ReactNode> => ({
  dev: (
    <div className="pb-4 border-b mb-4">
      <SkillCarousel
        tabs={t.devTabs}
        pauseLabel={t.carouselPause}
        playLabel={t.carouselPlay}
        nextLabel={t.carouselNext}
      />
    </div>
  ),
  design: (
    <div className="pb-4 border-b mb-4">
      <SkillCarousel
        tabs={t.designTabs}
        pauseLabel={t.carouselPause}
        playLabel={t.carouselPlay}
        nextLabel={t.carouselNext}
      />
    </div>
  ),
});

export function ProjectsFall({
  projects,
  themes,
  compact = false,
  pathPrefix = "",
  locale = "zh-Hant",
}: ProjectsFallProps) {
  const t = i18nLabels[locale];
  const filterLabels = t.filterLabels;
  const [activeSection, setActiveSection] = useState<SkillType>("dev");
  const [expandedSections, setExpandedSections] = useState<
    Record<SkillType, boolean>
  >({
    dev: false,
    design: false,
  });
  const sectionRefs = useRef<Record<SkillType, HTMLElement | null>>({
    dev: null,
    design: null,
  });

  useEffect(() => {
    const observerOptions = {
      root: null,
      rootMargin: "-20% 0px -60% 0px",
      threshold: 0,
    };

    const observerCallback = (entries: IntersectionObserverEntry[]) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const sectionId = entry.target.getAttribute(
            "data-section",
          ) as SkillType;
          if (sectionId) {
            setActiveSection(sectionId);
          }
        }
      });
    };

    const observer = new IntersectionObserver(
      observerCallback,
      observerOptions,
    );

    Object.values(sectionRefs.current).forEach((section) => {
      if (section) observer.observe(section);
    });

    return () => observer.disconnect();
  }, []);

  const scrollToSection = (filter: SkillType) => {
    const section = sectionRefs.current[filter];
    if (section) {
      const offset = 100;
      const elementPosition = section.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - offset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth",
      });
    }
  };

  const toggleSection = (filter: SkillType) => {
    setExpandedSections((prev) => ({
      ...prev,
      [filter]: !prev[filter],
    }));
  };

  const filterProjects = (filter: SkillType) => {
    return projects.filter((project) =>
      project.data.skillTypes.includes(filter),
    );
  };

  const getDisplayProjects = (filter: SkillType) => {
    const filtered = filterProjects(filter);
    const isExpanded = expandedSections[filter];
    return isExpanded ? filtered : filtered.slice(0, 6);
  };

  const renderProjectCard = (project: ProjectData) => {
    const themeColors = themes[project.data.theme];

    return (
      <a
        key={project.slug}
        href={`${pathPrefix}/projects/${project.slug}/`}
        data-card-theme
        className="group flex flex-col bg-card rounded-lg border border-border overflow-hidden hover:shadow-xl transition-all duration-300 hover:-translate-y-1"
        style={
          {
            "--card-primary-light": themeColors.primary,
            "--card-primary-dark": themeColors.darkPrimary,
            "--card-secondary-light": themeColors.secondary,
            "--card-secondary-dark": themeColors.darkSecondary,
          } as React.CSSProperties
        }
      >
        {/* Cover Image */}
        <div className="relative h-auto overflow-hidden bg-muted">
          <img
            src={getImageSrc(project.data.cover)}
            alt={project.data.title}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
            loading="lazy"
            decoding="async"
          />
          {project.data.pin && (
            <div
              className="absolute top-3 right-3"
              style={{ color: "var(--card-secondary)" }}
            >
              <StarIcon className="size-4" weight="fill" />
            </div>
          )}
          <div
            className="absolute bottom-0 left-0 right-0 h-1"
            style={{ backgroundColor: "var(--card-primary)" }}
          />
        </div>

        {/* Content */}
        <div className="flex-1 flex flex-col p-5 pb-3">
          {/* Date */}
          <p className="text-xs text-muted-foreground mb-2">
            {project.data.startDate.toLocaleDateString(
              locale === "en" ? "en-US" : "zh-TW",
              {
                year: "numeric",
                month: "2-digit",
              },
            )}
            {project.data.endDate
              ? ` - ${project.data.endDate.toLocaleDateString(locale === "en" ? "en-US" : "zh-TW", { year: "numeric", month: "2-digit" })}`
              : ` - ${t.now}`}
          </p>
          <h3
            className="text-xl font-bold mb-2 group-hover:text-opacity-80 transition-colors line-clamp-2"
            style={{ color: "var(--card-primary)" }}
          >
            {project.data.title}
          </h3>

          <p className="flex-1 text-muted-foreground text-sm mb-4">
            {project.data.description}
          </p>

          {/* Tags */}
          <div className="flex flex-wrap gap-2 my-1">
            {project.data.tags.map((tag: string) => (
              <Badge key={tag} variant="outline" className="text-xs">
                {tag}
              </Badge>
            ))}
          </div>
        </div>
      </a>
    );
  };

  return (
    <div className="w-full">
      {/* Sticky Navigation */}
      <nav className="sticky top-18 z-20 bg-background/80 backdrop-blur-sm rounded-xl mb-8 -mx-4 px-8">
        <div className="flex gap-6 py-4">
          {(Object.entries(filterLabels) as [SkillType, string][]).map(
            ([filter, label]) => (
              <button
                key={filter}
                onClick={() => scrollToSection(filter)}
                className={`text-lg font-medium transition-colors relative pb-1 ${activeSection === filter
                  ? "text-foreground"
                  : "text-muted-foreground hover:text-foreground"
                  }`}
              >
                {label}
                {activeSection === filter && (
                  <span className="absolute bottom-0 left-0 right-0 h-0.5 bg-foreground rounded-full" />
                )}
              </button>
            ),
          )}
        </div>
      </nav>

      {/* Sections */}
      <div className="space-y-12">
        {(Object.entries(filterLabels) as [SkillType, string][]).map(
          ([filter, label]) => {
            const filteredProjects = filterProjects(filter);
            const displayProjects = getDisplayProjects(filter);
            const hasMore = filteredProjects.length > 6;
            const isExpanded = expandedSections[filter];

            return (
              <section
                key={filter}
                ref={(el) => {
                  sectionRefs.current[filter] = el;
                }}
                data-section={filter}
                className="space-y-6 scroll-mt-32"
              >
                {/* Section Title */}
                <h3 className="text-2xl font-bold text-foreground">{label}</h3>

                {/* Description */}
                {!compact && getFilterDescriptions(t)[filter]}

                {/* Projects Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {displayProjects.map(renderProjectCard)}
                </div>

                {/* View More Button */}
                {hasMore && (
                  <div className="flex justify-center pt-4">
                    <Button
                      onClick={() => toggleSection(filter)}
                      variant="outline"
                    >
                      {isExpanded ? (
                        <>
                          {t.collapse}
                          <CaretUpIcon className="size-6" />
                        </>
                      ) : (
                        <>
                          {t.viewMore(filteredProjects.length - 6)}
                          <CaretDownIcon className="size-6" />
                        </>
                      )}
                    </Button>
                  </div>
                )}

                {/* Empty State */}
                {filteredProjects.length === 0 && (
                  <div className="text-center py-12 text-muted-foreground">
                    {t.noProjects}
                  </div>
                )}
              </section>
            );
          },
        )}
      </div>
    </div>
  );
}
