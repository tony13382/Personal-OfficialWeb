import { useEffect, useState, useRef } from 'react'
import { Badge } from '@/components/ui/badge'
import { ArrowDownIcon, AtomIcon, CaretDoubleRightIcon, ChartLineUpIcon, ClockUserIcon, DatabaseIcon, FigmaLogoIcon, GlobeHemisphereEastIcon, ListMagnifyingGlassIcon, PlugsIcon, RocketLaunchIcon, SquaresFourIcon, StarIcon, WechatLogoIcon } from '@phosphor-icons/react'
import { Card, CardContent, CardHeader } from '../ui/card'
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '../ui/tooltip'

type SkillType = 'dev' | 'design' | 'plan'

interface ProjectData {
  slug: string
  data: {
    title: string
    description: string
    cover: string
    startDate: Date
    endDate?: Date | null
    pin: boolean
    theme: string
    skillTypes: SkillType[]
    tags: string[]
  }
}

interface ProjectsFallProps {
  projects: ProjectData[]
  themes: Record<string, { primary: string; secondary: string }>
}

const filterLabels = {
  dev: '開發',
  design: '設計',
  plan: '企劃'
}

const filterDescriptions: Record<string, React.ReactNode> = {
  dev: (
    <div className='grid grid-cols-1 md:grid-cols-2 gap-4 pb-4 border-b mb-4'>
      <Card className='flex flex-col col-span-1 shadow-none md:grayscale hover:grayscale-0 hover:[&>div>div>div>.mid-btn]:bg-cyan-600 hover:[&>div>div>div>div>.animate-circle]:opacity-75'>
        <CardHeader className='p-6 pb-0'>
          <p className='text-center text-foreground text-xl font-bold'>Core System & Data Flow</p>
          <p className='text-center text-muted-foreground text-md'>有豐富的 API 開發經驗，熟悉各類資料庫</p>
        </CardHeader>
        <CardContent className='flex-1 items-center justify-center'>
          <div className='relative'>
            {/* Backend & Logic Section */}
            <div className='flex-1 flex items-end relative z-10'>
              <div className='inline-flex flex-col p-4 pt-3 my-4 mx-auto space-y-4 rounded-xl bg-muted'>
                <p className='text-center text-muted-foreground'>Backend & Logic</p>
                <TooltipProvider>
                  <div className='flex flex-wrap justify-center gap-4'>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Python.png" alt="Python" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Python</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/FastAPI.png" alt="FastAPI" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>FastAPI</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Supabase.png" alt="Supabase" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Supabase</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/NodeJs.png" alt="NodeJs" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>NodeJs</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Golang.png" alt="Golang" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Golang</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Php.png" alt="Php" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Php</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/RubyOnrRils.png" alt="RubyOnrRils" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Ruby On Rils</p>
                      </TooltipContent>
                    </Tooltip>
                  </div>
                </TooltipProvider>
              </div>
            </div>

            {/* Center Icon with Connecting Lines */}
            <div className='flex items-center justify-center relative my-4'>
              {/* Outer Circle Border with Continuous Animation */}
              <div className='absolute inset-0 flex items-center justify-center'>
                <div className='animate-circle w-40 h-40 shrink-0 rounded-full border-2 border-muted-foreground/20 animate-ping opacity-0 z-0'></div>
              </div>

              {/* Inner Circle with Icon */}
              <div className='mid-btn relative inline-flex items-center gap-2 p-4 rounded-full bg-cyan-600 md:bg-foreground/70 text-muted z-10'>
                <PlugsIcon className='size-6' /> API Server
              </div>
            </div>

            {/* Data Store Section */}
            <div className='flex-1 flex items-start relative z-10'>
              <div className='inline-flex flex-col p-4 pt-3 my-4 mx-auto space-y-4 rounded-xl bg-muted'>
                <p className='text-center text-muted-foreground'>Data Store</p>
                <TooltipProvider>
                  <div className='flex flex-wrap justify-center gap-4'>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/PostgreSQL.png" alt="PostgreSQL" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>PostgreSQL</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/MongoDB.png" alt="MongoDB" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>MongoDB</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Firebase.png" alt="Firebase" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Firebase</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/SQLite.png" alt="SQLite" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>SQLite</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Redis.png" alt="Redis" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Redis</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Cloudflare.png" alt="Cloudflare" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Cloudflare</p>
                      </TooltipContent>
                    </Tooltip>
                  </div>
                </TooltipProvider>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
      <Card className='flex flex-col col-span-1 shadow-none md:grayscale hover:grayscale-0 hover:[&>div>div>div>.mid-btn]:bg-pink-600 hover:[&>div>div>div>div>.animate-circle]:opacity-75'>
        <CardHeader className='p-6 pb-0'>
          <p className='text-center text-foreground text-xl font-bold'>Frontend</p>
          <p className='text-center text-muted-foreground text-md'>有大量靜態與 React SPA 的開發經驗</p>
        </CardHeader>
        <CardContent className='flex-1 items-center justify-center'>
          <div className='relative flex flex-col h-full'>
            {/* Backend & Logic Section */}
            <div className='flex-1 flex items-end relative z-10'>
              <div className='inline-flex flex-col p-4 pt-3 my-4 mx-auto space-y-4 rounded-xl bg-muted'>
                <p className='text-center text-muted-foreground'>Framework</p>
                <TooltipProvider>
                  <div className='flex flex-wrap justify-center gap-4'>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/React.png" alt="React" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>React</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/ReactRouter.png" alt="ReactRouter" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>React Router</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/NextJs.png" alt="NextJs" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>NextJs</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/JavaServerPage.png" alt="JavaServerPage" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Java Page (Tomcat)</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Astro.png" alt="Astro" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Astro</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Remix.png" alt="Remix" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Remix</p>
                      </TooltipContent>
                    </Tooltip>
                  </div>
                </TooltipProvider>
              </div>
            </div>

            {/* Center Icon with Connecting Lines */}
            <div className='flex items-center justify-center relative my-4'>
              {/* Outer Circle Border with Continuous Animation */}
              <div className='animate-circle absolute inset-0 flex items-center justify-center'>
                <div className='animate-circle w-40 h-40 shrink-0 rounded-full border-2 border-muted-foreground/20 animate-ping opacity-0 z-0'></div>
              </div>

              {/* Inner Circle with Icon */}
              <div className='mid-btn relative inline-flex items-center gap-2 p-4 rounded-full bg-pink-600 md:bg-foreground/70 text-muted z-10'>
                <GlobeHemisphereEastIcon className='size-6' /> Web UI
              </div>
            </div>

            {/* Data Store Section */}
            <div className='flex-1 flex items-start relative z-10'>
              <div className='inline-flex flex-col p-4 pt-3 my-4 mx-auto space-y-4 rounded-xl bg-muted'>
                <p className='text-center text-muted-foreground'>Tools</p>
                <TooltipProvider>
                  <div className='flex flex-wrap justify-center gap-4'>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Vite.png" alt="Vite" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Vite</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Tailwind.png" alt="Tailwind" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Tailwind CSS</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/ShadcnUi.png" alt="ShadcnUi" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Shadcn UI Kit</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Bootstrap.png" alt="Bootstrap" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Bootstrap</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Streamlit.png" alt="Streamlit" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Streamlit</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Java.png" alt="Java" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Java</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Flutter.png" alt="Flutter" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Flutter</p>
                      </TooltipContent>
                    </Tooltip>
                  </div>
                </TooltipProvider>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
      <Card className='flex flex-col col-span-1 md:col-span-2 shadow-none md:grayscale hover:grayscale-0 hover:[&>div>div>div>.mid-btn]:bg-indigo-600 hover:[&>div>div>div>div>.animate-circle]:opacity-75'>
        <CardHeader className='p-6 pb-0'>
          <p className='text-center text-foreground text-xl font-bold'>Deploy</p>
          <p className='text-center text-muted-foreground text-md'>具 Docker Compose 封装、Cloudflare Worker 部屬經驗</p>
        </CardHeader>
        <CardContent className='flex-1 items-center justify-center'>
          <div className='relative flex flex-col md:flex-row md:gap-8'>
            {/* Backend & Logic Section */}
            <div className='flex-1 flex items-end relative z-10'>
              <div className='inline-flex flex-col p-4 pt-3 my-4 mx-auto space-y-4 rounded-xl bg-muted'>
                <p className='text-center text-muted-foreground'>Platform</p>
                <TooltipProvider>
                  <div className='flex flex-wrap justify-center gap-4'>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Cloudflare.png" alt="Cloudflare" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Cloudflare Worker</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Linode.png" alt="Linode" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Linode</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/AWS.png" alt="AWS" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>AWS</p>
                      </TooltipContent>
                    </Tooltip>
                  </div>
                </TooltipProvider>
              </div>
            </div>

            {/* Center Icon with Connecting Lines */}
            <div className='flex items-center justify-center relative my-4'>
              {/* Outer Circle Border with Continuous Animation */}
              <div className='absolute inset-0 flex items-center justify-center'>
                <div className='animate-circle w-40 h-40 shrink-0 rounded-full border-2 border-muted-foreground/20 animate-ping opacity-0 z-0'></div>
              </div>

              {/* Inner Circle with Icon */}
              <div className='mid-btn relative inline-flex items-center gap-2 p-4 rounded-full bg-indigo-600 md:bg-foreground/70 text-muted z-10'>
                <RocketLaunchIcon className='size-6' /> Deploy
              </div>
            </div>

            {/* Data Store Section */}
            <div className='flex-1 flex items-start relative z-10'>
              <div className='inline-flex flex-col p-4 pt-3 my-4 mx-auto space-y-4 rounded-xl bg-muted'>
                <p className='text-center text-muted-foreground'>Tools</p>
                <TooltipProvider>
                  <div className='flex flex-wrap justify-center gap-4'>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Docker.png" alt="Docker" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Docker</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/GithubAction.png" alt="GithubAction" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Github Action</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/AppScript.png" alt="AppScript" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>AppScript</p>
                      </TooltipContent>
                    </Tooltip>
                  </div>
                </TooltipProvider>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  ),
  design: (
    <div className='grid grid-cols-1 md:grid-cols-2 gap-4 pb-4 border-b mb-4'>
      <Card className='flex flex-col col-span-1 shadow-none md:grayscale hover:grayscale-0 hover:[&>div>div>div>.mid-btn]:bg-cyan-600 hover:[&>div>div>div>div>.animate-circle]:opacity-75'>
        <CardHeader className='p-6 pb-0'>
          <p className='text-center text-foreground text-xl font-bold'>資料視覺化</p>
          <p className='text-center text-muted-foreground text-md'>將原始數據轉化為引人入勝的故事</p>
        </CardHeader>
        <CardContent className='flex-1'>
          <div className='flex flex-col items-center justify-center'>
            <div className='inline-flex flex-col p-4 pt-3 my-4 mx-auto space-y-4 rounded-xl bg-muted'>
              <p className='text-center text-muted-foreground'>資料整理與前處理</p>
              <TooltipProvider>
                <div className='flex flex-wrap justify-center gap-4'>
                  <Tooltip>
                    <TooltipTrigger asChild>
                      <img src="/assets/imgs/appIcons/Python.png" alt="Python" className='size-14' />
                    </TooltipTrigger>
                    <TooltipContent>
                      <p>Python</p>
                    </TooltipContent>
                  </Tooltip>
                  <Tooltip>
                    <TooltipTrigger asChild>
                      <img src="/assets/imgs/appIcons/R.png" alt="R" className='size-14' />
                    </TooltipTrigger>
                    <TooltipContent>
                      <p>R</p>
                    </TooltipContent>
                  </Tooltip>
                  <Tooltip>
                    <TooltipTrigger asChild>
                      <img src="/assets/imgs/appIcons/Excel.png" alt="Excel" className='size-14' />
                    </TooltipTrigger>
                    <TooltipContent>
                      <p>Excel</p>
                    </TooltipContent>
                  </Tooltip>
                  <Tooltip>
                    <TooltipTrigger asChild>
                      <img src="/assets/imgs/appIcons/GoogleSheet.png" alt="GoogleSheet" className='size-14' />
                    </TooltipTrigger>
                    <TooltipContent>
                      <p>Google Sheet</p>
                    </TooltipContent>
                  </Tooltip>
                </div>
              </TooltipProvider>
            </div>
            <ArrowDownIcon className='size-8 text-muted-foreground' />
            <div className='grid grid-cols-1 md:grid-cols-2 gap-4'>
              <div className='inline-flex flex-col p-4 pt-3 my-4 mx-auto space-y-4 rounded-xl bg-muted'>
                <p className='text-center text-muted-foreground'>簡報</p>
                <TooltipProvider>
                  <div className='flex flex-wrap justify-center gap-4'>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Canva.png" alt="Canva" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Canva</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Powerpoint.png" alt="Powerpoint" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Powerpoint</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/GoogleSlide.png" alt="GoogleSlide" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Google Slides</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Figma.png" alt="Figma" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Figma Slides</p>
                      </TooltipContent>
                    </Tooltip>
                  </div>
                </TooltipProvider>
              </div>
              <div className='inline-flex flex-col p-4 pt-3 my-4 mx-auto space-y-4 rounded-xl bg-muted'>
                <p className='text-center text-muted-foreground'>儀表板</p>
                <TooltipProvider>
                  <div className='flex flex-wrap justify-center gap-4'>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/PoewrBI.png" alt="PoewrBI" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>PoewrBI</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/GoogleLookerStudio.png" alt="GoogleLookerStudio" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>Looker Studio</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Excel.png" alt="Excel" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>IBM Cognos</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/IbmCognos.png" alt="IbmCognos" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>IBM Cognos</p>
                      </TooltipContent>
                    </Tooltip>
                    <Tooltip>
                      <TooltipTrigger asChild>
                        <img src="/assets/imgs/appIcons/Ggplot2.png" alt="Ggplot2" className='size-14' />
                      </TooltipTrigger>
                      <TooltipContent>
                        <p>GGPlot 2</p>
                      </TooltipContent>
                    </Tooltip>
                  </div>
                </TooltipProvider>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
      <Card className='flex flex-col col-span-1 shadow-none md:grayscale hover:grayscale-0'>
        <CardHeader className='p-6 pb-0'>
          <p className='text-center text-foreground text-xl font-bold'>UX / UI 設計</p>
          <p className='text-center text-muted-foreground text-md'>從抽象洞察到極致完美的體驗</p>
        </CardHeader>
        <CardContent className='flex-1 items-center justify-center'>
          <div className='grid gap-6'>
            <div className='flex items-center justify-center gap-4'>
              <div className='p-4 rounded-full bg-orange-50 text-orange-600'>
                <WechatLogoIcon className='size-8' />
              </div>
              <div className='flex-1'>
                <p className='font-bold'>洞見與訪談</p>
                <p className='text-muted-foreground'>用戶研究、Personas</p>
              </div>
            </div>
            <div className='flex items-center justify-center gap-4'>
              <div className='p-4 rounded-full bg-sky-50 text-sky-600'>
                <ListMagnifyingGlassIcon className='size-8' />
              </div>
              <div className='flex-1'>
                <p className='font-bold'>流程與作業流程</p>
                <p className='text-muted-foreground'>用戶旅程、使用者流程分析</p>
              </div>
            </div>
            <div className='flex items-center justify-center gap-4'>
              <div className='p-4 rounded-full bg-teal-50 text-teal-600'>
                <AtomIcon className='size-8' />
              </div>
              <div className='flex-1'>
                <p className='font-bold'>原子設計</p>
                <p className='text-muted-foreground'>線框圖、元件、設計系統</p>
              </div>
            </div>
            <div className='flex items-center justify-center gap-4'>
              <div className='p-4 rounded-full bg-rose-50 text-rose-500'>
                <FigmaLogoIcon className='size-8' />
              </div>
              <div className='flex-1'>
                <p className='font-bold'>Figma</p>
                <p className='text-muted-foreground'>介面繪製、原型設計</p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  ),
  plan: (
    <div className='grid grid-cols-1 md:grid-cols-2 gap-4 pb-4 border-b mb-4'>
      <Card className='flex flex-col col-span-1 shadow-none md:grayscale hover:grayscale-0 hover:[&>div>div>div>.mid-btn]:bg-cyan-600 hover:[&>div>div>div>div>.animate-circle]:opacity-75'>
        <CardHeader className='p-6 border-b'>
          <p className='text-center text-foreground text-xl font-bold'>報告</p>
          <p className='text-center text-muted-foreground text-md'>聚焦新創與 AI 科技產業發展</p>
        </CardHeader>
        <CardContent className='flex-1 justify-center pb-0'>
          <div className='relative'>
            {/* 四个类别 */}
            <div className='grid grid-cols-4 gap-6 pt-1'>
              <div className='flex flex-col items-center gap-3'>
                <div className='p-4 rounded-full bg-orange-500 text-background'>
                  <ChartLineUpIcon className='size-8' />
                </div>
                <p className='text-sm text-muted-foreground text-center'>市場分析</p>
              </div>
              <div className='flex flex-col items-center gap-3'>
                <div className='p-4 rounded-full bg-green-600 text-background'>
                  <ClockUserIcon className='size-8' />
                </div>
                <p className='text-sm text-muted-foreground text-center'>生產力管理</p>
              </div>
              <div className='flex flex-col items-center gap-3'>
                <div className='p-4 rounded-full bg-pink-400 text-background'>
                  <SquaresFourIcon className='size-8' />
                </div>
                <p className='text-sm text-muted-foreground text-center'>工具教學</p>
              </div>
              <div className='flex flex-col items-center gap-3'>
                <div className='p-4 rounded-full bg-cyan-600 text-background'>
                  <DatabaseIcon className='size-8' />
                </div>
                <p className='text-sm text-muted-foreground text-center'>資料洞察</p>
              </div>
            </div>

            {/* 连接线条 - SVG 弧形 */}
            <div className='relative h-24 mt-6'>
              <svg className='absolute inset-0 w-full h-full' viewBox='0 0 400 96' preserveAspectRatio='none'>
                {/* 左边第一条：垂直线 + 弧形转角向右 + 横线到中心 */}
                <path
                  d='M 50 0 L 50 24 Q 50 40, 66 40 L 184 40'
                  fill='none'
                  stroke='currentColor'
                  strokeWidth='1.5'
                  className='text-border'
                />

                {/* 左中第二条：垂直线 + 弧形转角向右 + 横线汇入中心 */}
                <path
                  d='M 150 0 L 150 24 Q 150 40, 166 40 L 184 40'
                  fill='none'
                  stroke='currentColor'
                  strokeWidth='1.5'
                  className='text-border'
                />

                {/* 右中第三条：垂直线 + 弧形转角向左 + 横线汇入中心 */}
                <path
                  d='M 250 0 L 250 24 Q 250 40, 234 40 L 216 40'
                  fill='none'
                  stroke='currentColor'
                  strokeWidth='1.5'
                  className='text-border'
                />

                {/* 右边第四条：垂直线 + 弧形转角向左 + 横线到中心 */}
                <path
                  d='M 350 0 L 350 24 Q 350 40, 334 40 L 216 40'
                  fill='none'
                  stroke='currentColor'
                  strokeWidth='1.5'
                  className='text-border'
                />

                {/* 中心横线连接左右 */}
                <path
                  d='M 184 40 L 216 40'
                  fill='none'
                  stroke='currentColor'
                  strokeWidth='1.5'
                  className='text-border'
                />

                {/* 中心向下的弧形转角 + 垂直线 */}
                <path
                  d='M 200 40 Q 200 56, 200 56 L 200 96'
                  fill='none'
                  stroke='currentColor'
                  strokeWidth='1.5'
                  className='text-border'
                />
              </svg>

              {/* 中心焦点 - 使用HTML元素保持正圆 */}
              <div className='absolute left-1/2 -translate-x-1/2' style={{ top: 'calc(40 / 96 * 100%)' }}>
                {/* 扩散动画圆 */}
                <div className='absolute -translate-x-1/2 -translate-y-1/2 w-4 h-4 rounded-full bg-border opacity-75 animate-ping'></div>
                {/* 实心圆 */}
                <div className='absolute -translate-x-1/2 -translate-y-1/2 w-2 h-2 rounded-full bg-border'></div>
              </div>
            </div>

            {/* 底部内容框 */}
            <div className='relative rounded-t-2xl border-1 border-b-0 border-border bg-background p-6'>
              <div className='flex items-center justify-center gap-4'>
                <div className='p-3 rounded-xl bg-muted'>
                  <TooltipProvider>
                    <div className='flex gap-4'>
                      <Tooltip>
                        <TooltipTrigger asChild>
                          <img src="/assets/imgs/appIcons/GoogleDocs.png" alt="GoogleDocs" className='size-14' />
                        </TooltipTrigger>
                        <TooltipContent>
                          <p>Google Docs</p>
                        </TooltipContent>
                      </Tooltip>
                      <Tooltip>
                        <TooltipTrigger asChild>
                          <img src="/assets/imgs/appIcons/Notion.png" alt="Notion" className='size-14' />
                        </TooltipTrigger>
                        <TooltipContent>
                          <p>Notion</p>
                        </TooltipContent>
                      </Tooltip>
                      <Tooltip>
                        <TooltipTrigger asChild>
                          <img src="/assets/imgs/appIcons/Wordpress.png" alt="Wordpress" className='size-14' />
                        </TooltipTrigger>
                        <TooltipContent>
                          <p>Wordpress</p>
                        </TooltipContent>
                      </Tooltip>
                      <Tooltip>
                        <TooltipTrigger asChild>
                          <img src="/assets/imgs/appIcons/GoogleAnalytics.png" alt="GoogleAnalytics" className='size-14' />
                        </TooltipTrigger>
                        <TooltipContent>
                          <p>Google Analytics</p>
                        </TooltipContent>
                      </Tooltip>
                    </div>
                  </TooltipProvider>
                </div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
      <Card className='flex flex-col col-span-1 shadow-none md:grayscale hover:grayscale-0 md:hover:[&>div>div>.browser-frame]:shadow-xl'>
        <CardHeader className='p-6'>
          <p className='text-center text-foreground text-xl font-bold'>知識共享</p>
          <p className='text-center text-muted-foreground text-md'>開放資料教學與資源共享</p>
        </CardHeader>
        <CardContent className='flex-1 justify-center p-0'>
          {/* Browser Window with Grid Background */}
          <div className='relative w-full h-full min-h-80 overflow-hidden border border-gray-200'
            style={{
              backgroundImage: `
                repeating-linear-gradient(0deg, transparent, transparent 19px, #e5e7eb 19px, #e5e7eb 20px),
                repeating-linear-gradient(90deg, transparent, transparent 19px, #e5e7eb 19px, #e5e7eb 20px)
              `,
              backgroundColor: '#f9fafb'
            }}>
            {/* Browser Window */}
            <div className='browser-frame shadow-xl md:shadow-none absolute inset-4 bg-white rounded-lg overflow-hidden'>
              {/* Browser Title Bar */}
              <div className='flex items-center gap-2 px-4 py-3 bg-gray-100 border-b border-gray-200'>
                <div className='flex gap-2'>
                  <div className='w-3 h-3 rounded-full bg-red-500'></div>
                  <div className='w-3 h-3 rounded-full bg-yellow-500'></div>
                  <div className='w-3 h-3 rounded-full bg-green-500'></div>
                </div>
              </div>

              {/* Browser Content */}
              <div className='p-2 flex items-center justify-center gap-6 h-[calc(100%-56px)]'>
                <div className='inline-flex flex-col items-center gap-2'>
                  <div className='p-2 border rounded-xl'>
                    <img src="/assets/imgs/appIcons/Notion.png" alt="Notion" className='size-14' />
                  </div>
                  <p className='text-muted-foreground text-center'>學習資源共享</p>
                </div>
                <CaretDoubleRightIcon className='size-12 text-border animate-pulse' />
                <div className='inline-flex flex-col items-center gap-2'>
                  <div className='p-1 border rounded-xl'>
                    <img src="/assets/imgs/appIcons/Instagram.png" alt="Instagram" className='size-16' />
                  </div>
                  <p className='text-muted-foreground text-center'>知識輸出</p>
                </div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

export function ProjectsFall({ projects, themes }: ProjectsFallProps) {
  const [activeSection, setActiveSection] = useState<SkillType>('dev')
  const sectionRefs = useRef<Record<SkillType, HTMLElement | null>>({
    dev: null,
    design: null,
    plan: null
  })

  useEffect(() => {
    const observerOptions = {
      root: null,
      rootMargin: '-20% 0px -60% 0px',
      threshold: 0
    }

    const observerCallback = (entries: IntersectionObserverEntry[]) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const sectionId = entry.target.getAttribute('data-section') as SkillType
          if (sectionId) {
            setActiveSection(sectionId)
          }
        }
      })
    }

    const observer = new IntersectionObserver(observerCallback, observerOptions)

    Object.values(sectionRefs.current).forEach((section) => {
      if (section) observer.observe(section)
    })

    return () => observer.disconnect()
  }, [])

  const scrollToSection = (filter: SkillType) => {
    const section = sectionRefs.current[filter]
    if (section) {
      const offset = 100
      const elementPosition = section.getBoundingClientRect().top
      const offsetPosition = elementPosition + window.pageYOffset - offset

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      })
    }
  }

  const filterProjects = (filter: SkillType) => {
    return projects.filter(project =>
      project.data.skillTypes.includes(filter)
    )
  }

  const renderProjectCard = (project: ProjectData) => {
    const themeColors = themes[project.data.theme]

    return (
      <a
        key={project.slug}
        href={`/projects/${project.slug}/`}
        className="group flex flex-col bg-white rounded-lg border border-gray-200 overflow-hidden hover:shadow-xl transition-all duration-300 hover:-translate-y-1"
      >
        {/* Cover Image */}
        <div className="relative h-auto overflow-hidden bg-gray-100">
          <img
            src={project.data.cover}
            alt={project.data.title}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
          />
          {project.data.pin && (
            <div
              className="absolute top-3 right-3"
              style={{ color: themeColors.secondary }}
            >
              <StarIcon className="size-4" weight="fill" />
            </div>
          )}
          <div
            className="absolute bottom-0 left-0 right-0 h-1"
            style={{ backgroundColor: themeColors.primary }}
          />
        </div>

        {/* Content */}
        <div className="flex-1 flex flex-col p-5 pb-3">
          {/* Date */}
          <p className="text-xs text-gray-400 mb-2">
            {project.data.startDate.toLocaleDateString('zh-TW', {
              year: 'numeric',
              month: '2-digit',
            })}
            {project.data.endDate
              ? ` - ${project.data.endDate.toLocaleDateString('zh-TW', { year: 'numeric', month: '2-digit' })}`
              : ' - 現在'}
          </p>
          <h3
            className="text-xl font-bold mb-2 group-hover:text-opacity-80 transition-colors line-clamp-2"
            style={{ color: themeColors.primary }}
          >
            {project.data.title}
          </h3>

          <p className="flex-1 text-gray-600 text-sm mb-4">
            {project.data.description}
          </p>

          {/* Tags */}
          <div className="flex flex-wrap gap-2 my-1">
            {project.data.tags.map((tag: string) => (
              <Badge key={tag} variant="secondary" className="text-xs">
                {tag}
              </Badge>
            ))}
          </div>
        </div>
      </a>
    )
  }

  return (
    <div className="w-full">
      {/* Sticky Navigation */}
      <nav className="sticky top-20 z-20 bg-white/80 backdrop-blur-sm rounded-full mb-8 -mx-2 px-8">
        <div className="flex gap-6 py-4">
          {(Object.entries(filterLabels) as [SkillType, string][]).map(([filter, label]) => (
            <button
              key={filter}
              onClick={() => scrollToSection(filter)}
              className={`text-lg font-medium transition-colors relative pb-1 ${activeSection === filter
                ? 'text-foreground'
                : 'text-muted-foreground hover:text-foreground'
                }`}
            >
              {label}
              {activeSection === filter && (
                <span className="absolute bottom-0 left-0 right-0 h-0.5 bg-foreground rounded-full" />
              )}
            </button>
          ))}
        </div>
      </nav>

      {/* Sections */}
      <div className="space-y-12">
        {(Object.entries(filterLabels) as [SkillType, string][]).map(([filter, label]) => {
          const filteredProjects = filterProjects(filter)

          return (
            <section
              key={filter}
              ref={(el) => { sectionRefs.current[filter] = el }}
              data-section={filter}
              className="space-y-6 scroll-mt-32"
            >
              {/* Section Title */}
              <h3 className="text-2xl font-bold text-foreground">{label}</h3>

              {/* Description */}
              {filterDescriptions[filter]}

              {/* Projects Grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {filteredProjects.map(renderProjectCard)}
              </div>

              {/* Empty State */}
              {filteredProjects.length === 0 && (
                <div className="text-center py-12 text-gray-500">
                  目前沒有相關專案
                </div>
              )}
            </section>
          )
        })}
      </div>
    </div>
  )
}
