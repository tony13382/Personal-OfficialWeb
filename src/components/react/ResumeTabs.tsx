import { useEffect, useState } from 'react'
import { ArrowSquareOutIcon, DownloadSimpleIcon } from '@phosphor-icons/react'

import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { Button } from '@/components/ui/button'

type ResumeKey = 'general' | 'dev' | 'design'

interface ResumeItem {
  key: ResumeKey
  label: string
  description: string
  driveId: string
}

interface ResumeTabsProps {
  resumes: ResumeItem[]
  defaultKey?: ResumeKey
  openInNewTabLabel: string
  downloadLabel: string
  mobileHint: string
}

const isValidKey = (value: string, keys: string[]): value is ResumeKey =>
  keys.includes(value)

function readInitialKey(defaultKey: ResumeKey, validKeys: string[]): ResumeKey {
  if (typeof window === 'undefined') return defaultKey
  const hash = window.location.hash.replace('#', '')
  return hash && isValidKey(hash, validKeys) ? hash : defaultKey
}

export function ResumeTabs({
  resumes,
  defaultKey = 'general',
  openInNewTabLabel,
  downloadLabel,
  mobileHint,
}: ResumeTabsProps) {
  const validKeys = resumes.map((r) => r.key)
  const [loadedKeys, setLoadedKeys] = useState<Set<ResumeKey>>(
    () => new Set([readInitialKey(defaultKey, validKeys)]),
  )

  const handleChange = (value: string) => {
    if (!isValidKey(value, validKeys)) return
    setLoadedKeys((prev) => {
      if (prev.has(value)) return prev
      const next = new Set(prev)
      next.add(value)
      return next
    })
    history.replaceState(null, '', `#${value}`)
  }

  useEffect(() => {
    const hash = window.location.hash.replace('#', '')
    if (hash && isValidKey(hash, validKeys)) {
      setLoadedKeys((prev) => {
        if (prev.has(hash)) return prev
        const next = new Set(prev)
        next.add(hash)
        return next
      })
    }
  }, [])

  const initialValue = readInitialKey(defaultKey, validKeys)

  return (
    <Tabs
      defaultValue={initialValue}
      onValueChange={handleChange}
      className="w-full"
    >
      <TabsList className="flex w-full justify-start gap-2 border-b border-border">
        {resumes.map((r) => (
          <TabsTrigger key={r.key} value={r.key}>
            {r.label}
          </TabsTrigger>
        ))}
      </TabsList>

      {resumes.map((r) => (
        <TabsContent
          key={r.key}
          value={r.key}
          className="mt-6 flex flex-col gap-4"
        >
          <p className="text-muted-foreground">{r.description}</p>

          <div className="flex flex-wrap gap-3">
            <Button asChild variant="default" size="sm">
              <a
                href={`https://drive.google.com/file/d/${r.driveId}/view`}
                target="_blank"
                rel="noopener noreferrer"
              >
                <ArrowSquareOutIcon weight="bold" />
                {openInNewTabLabel}
              </a>
            </Button>
            <Button asChild variant="outline" size="sm">
              <a
                href={`https://drive.google.com/uc?export=download&id=${r.driveId}`}
                rel="noopener noreferrer"
              >
                <DownloadSimpleIcon weight="bold" />
                {downloadLabel}
              </a>
            </Button>
          </div>

          <p className="text-xs text-muted-foreground md:hidden">{mobileHint}</p>

          {loadedKeys.has(r.key) && (
            <div className="w-full overflow-hidden rounded-lg border border-border bg-muted/30">
              <div className="relative w-full" style={{ aspectRatio: '210 / 297' }}>
                <iframe
                  src={`https://drive.google.com/file/d/${r.driveId}/preview`}
                  title={r.label}
                  loading="lazy"
                  allow="autoplay"
                  className="absolute inset-0 h-full w-full"
                />
              </div>
            </div>
          )}
        </TabsContent>
      ))}
    </Tabs>
  )
}
