import {
  MusicNotes,
  Tag,
  ListChecks,
  DownloadSimple,
  Brain,
  Waveform,
  ArrowRight,
  GithubLogo,
} from "@phosphor-icons/react";
import type { ReactNode } from "react";
import nextTagsSonglist from "@/assets/imgs/apps/nextags-songlist.png";
import nextTagsTagEditor from "@/assets/imgs/apps/nextags-tageditor.png";
import nextTagsPlaylist from "@/assets/imgs/apps/nextags-playlist.png";
import nextTagsHeroBg from "@/assets/imgs/apps/nextags-hero-bg.avif";

const GITHUB_URL = "https://github.com/tony13382/NexTags";

const screenshots = {
  hero: nextTagsSonglist.src,
  tagEditor: nextTagsTagEditor.src,
  playlist: nextTagsPlaylist.src,
};

interface Feature {
  icon: ReactNode;
  title: string;
  description: string;
}

const features: Feature[] = [
  {
    icon: <MusicNotes size={22} weight="regular" />,
    title: "音樂庫管理",
    description:
      "多條件篩選、即時搜尋，支援 MP3、FLAC、M4A 等主流格式，快速瀏覽你的整個收藏。",
  },
  {
    icon: <Tag size={22} weight="regular" />,
    title: "行內標籤編輯",
    description:
      "支援 20+ metadata 欄位，ID3v2、Vorbis、FLAC 標籤一站搞定，不用再開其他軟體。",
  },
  {
    icon: <ListChecks size={22} weight="regular" />,
    title: "智慧播放清單",
    description:
      "用動態篩選條件跟自動排序建立播放清單，一鍵匯出 M3U 給任何播放器使用。",
  },
  {
    icon: <DownloadSimple size={22} weight="regular" />,
    title: "音樂匯入流程",
    description:
      "上傳、自動轉檔、metadata 編輯、ReplayGain 分析，一條龍完成新音樂入庫。",
  },
  {
    icon: <Brain size={22} weight="regular" />,
    title: "AI 歌詞處理",
    description:
      "Claude API 驅動，自動清理歌詞格式、校正 LRC 時間軸、翻譯歌詞內容。",
  },
  {
    icon: <Waveform size={22} weight="regular" />,
    title: "響度標準化",
    description:
      "ReplayGain 批次分析，確保每首歌的播放音量一致，不用再手動調整音量。",
  },
];

interface Step {
  number: string;
  title: string;
  description: string;
}

const steps: Step[] = [
  {
    number: "01",
    title: "部署 NexTags",
    description:
      "透過 Docker Compose 一鍵啟動，掛載你的音樂資料夾就完成設定。",
  },
  {
    number: "02",
    title: "匯入音樂",
    description:
      "上傳音樂檔案或掃描既有資料夾，系統自動辨識格式並建立資料庫索引。",
  },
  {
    number: "03",
    title: "整理 Metadata",
    description:
      "在瀏覽器裡直接編輯標籤，用 AI 處理歌詞，批次校正專輯資訊。",
  },
  {
    number: "04",
    title: "匯出播放清單",
    description:
      "建立動態播放清單，匯出 M3U 檔案，搭配任何播放器享受你的收藏。",
  },
];

export default function Landing() {
  return (
    <div className="bg-white">
      {/* Hero */}
      <section className="relative overflow-hidden pb-40 md:pb-56">
        {/* Background image */}
        <div
          className="absolute inset-0 bg-cover bg-center bg-no-repeat"
          style={{ backgroundImage: `url('${nextTagsHeroBg.src}')` }}
        />
        {/* Dark overlay for text readability */}
        <div className="absolute inset-0 bg-black/40" />
        {/* Bottom fade to white */}
        <div className="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-white to-transparent" />
        <div className="relative mx-auto max-w-5xl px-6 pt-20 md:pt-32">
          <div className="mx-auto max-w-3xl text-center">
            <h1
              className="mb-6 text-5xl font-bold tracking-tight text-white md:text-7xl"
              style={{ lineHeight: 1.05 }}
            >
              NexTags
            </h1>
            <p
              className="mx-auto mb-10 max-w-2xl text-lg text-slate-300 md:text-xl"
              style={{ lineHeight: 1.7 }}
            >
              整合音樂整理、metadata 編輯跟 AI
              歌詞處理，讓你完全掌控自己的數位音樂收藏。
            </p>
            <div className="flex items-center justify-center gap-3">
              <a
                href={GITHUB_URL}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2.5 rounded-lg bg-white px-5 py-2.5 text-sm font-medium text-slate-900 no-underline transition-colors hover:bg-slate-100"
              >
                <GithubLogo size={18} weight="fill" />
                View on GitHub
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Hero Screenshot — overlaps hero */}
      <section className="relative z-10 -mt-28 px-6 pb-20 md:-mt-40 md:pb-28">
        <div className="mx-auto max-w-5xl">
          <div className="overflow-hidden rounded-2xl border border-white/10 shadow-2xl">
            <img
              src={screenshots.hero}
              alt="NexTags 音樂庫瀏覽介面"
              className="block h-auto w-full"
              loading="eager"
            />
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="border-t border-neutral-100 bg-neutral-50/60">
        <div className="mx-auto max-w-5xl px-6 py-20 md:py-28">
          <div className="mb-14 text-center md:mb-20">
            <p className="mb-3 text-sm font-medium tracking-wide text-neutral-400 uppercase">
              How it works
            </p>
            <h2 className="text-3xl font-semibold tracking-tight text-neutral-900 md:text-4xl">
              四步開始管理你的音樂
            </h2>
          </div>
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {steps.map((step) => (
              <div key={step.number} className="relative">
                <span className="mb-4 block font-semibold text-3xl tabular-nums text-neutral-200">
                  {step.number}
                </span>
                <h3 className="mb-2 text-base font-semibold text-neutral-900">
                  {step.title}
                </h3>
                <p className="text-sm leading-relaxed text-neutral-500">
                  {step.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="border-t border-neutral-100">
        <div className="mx-auto max-w-5xl px-6 py-20 md:py-28">
          <div className="mb-14 text-center md:mb-20">
            <p className="mb-3 text-sm font-medium tracking-wide text-neutral-400 uppercase">
              Features
            </p>
            <h2 className="mb-4 text-3xl font-semibold tracking-tight text-neutral-900 md:text-4xl">
              為音樂收藏打造的管理工具
            </h2>
            <p className="mx-auto max-w-xl text-base text-neutral-500" style={{ lineHeight: 1.7 }}>
              從匯入到播放，每個環節都有對應的功能支援。
            </p>
          </div>
          <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {features.map((feature) => (
              <div
                key={feature.title}
                className="rounded-xl border border-neutral-200 bg-white p-6 transition-colors hover:border-neutral-300"
              >
                <div className="mb-4 flex h-10 w-10 items-center justify-center rounded-lg bg-neutral-100 text-neutral-600">
                  {feature.icon}
                </div>
                <h3 className="mb-2 text-base font-semibold text-neutral-900">
                  {feature.title}
                </h3>
                <p className="text-sm leading-relaxed text-neutral-500">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Screenshot: Tag Editor */}
      <section className="border-t border-neutral-100 bg-neutral-50/60">
        <div className="mx-auto max-w-5xl px-6 py-20 md:py-28">
          <div className="grid items-center gap-12 md:grid-cols-2 md:gap-16">
            <div>
              <p className="mb-3 text-sm font-medium tracking-wide text-neutral-400 uppercase">
                Metadata
              </p>
              <h2 className="mb-4 text-2xl font-semibold tracking-tight text-neutral-900 md:text-3xl">
                直覺的標籤編輯
              </h2>
              <p className="text-base leading-relaxed text-neutral-500">
                在瀏覽器裡直接編輯 20+ 種 metadata
                欄位，支援多種標籤格式。修改完即時寫入檔案，所見即所得。
              </p>
            </div>
            <div className="overflow-hidden rounded-xl border border-neutral-200 shadow-lg shadow-neutral-200/50">
              <img
                src={screenshots.tagEditor}
                alt="NexTags 標籤編輯器"
                className="block h-auto w-full"
                loading="lazy"
                decoding="async"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Screenshot: Playlist */}
      <section className="border-t border-neutral-100">
        <div className="mx-auto max-w-5xl px-6 py-20 md:py-28">
          <div className="grid items-center gap-12 md:grid-cols-2 md:gap-16">
            <div className="order-2 md:order-1">
              <div className="overflow-hidden rounded-xl border border-neutral-200 shadow-lg shadow-neutral-200/50">
                <img
                  src={screenshots.playlist}
                  alt="NexTags 播放清單管理"
                  className="block h-auto w-full"
                  loading="lazy"
                  decoding="async"
                />
              </div>
            </div>
            <div className="order-1 md:order-2">
              <p className="mb-3 text-sm font-medium tracking-wide text-neutral-400 uppercase">
                Playlist
              </p>
              <h2 className="mb-4 text-2xl font-semibold tracking-tight text-neutral-900 md:text-3xl">
                智慧播放清單
              </h2>
              <p className="text-base leading-relaxed text-neutral-500">
                用動態篩選條件自動建立播放清單，支援多種排序邏輯。一鍵匯出
                M3U，直接丟給你慣用的播放器。
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Bottom CTA */}
      <section className="border-t border-neutral-100 bg-neutral-50/60">
        <div className="mx-auto max-w-4xl px-6 py-20 text-center md:py-28">
          <h2 className="mb-4 text-3xl font-semibold tracking-tight text-neutral-900 md:text-4xl">
            開始管理你的音樂
          </h2>
          <p className="mx-auto mb-8 max-w-lg text-base text-neutral-500" style={{ lineHeight: 1.7 }}>
            NexTags 完全開源，透過 Docker 就能在自己的伺服器上部署。
          </p>
          <a
            href={GITHUB_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2.5 rounded-lg bg-neutral-900 px-6 py-3 text-sm font-medium text-white no-underline transition-colors hover:bg-neutral-800"
          >
            <GithubLogo size={18} weight="fill" />
            View on GitHub
            <ArrowRight size={16} weight="bold" />
          </a>
        </div>
      </section>
    </div>
  );
}
