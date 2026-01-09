import { Tabs, TabsList, TabsTrigger, TabsContent } from '@/components/ui/tabs'

import { renderEmbedComponent, type EmbedComponent } from './Basic'

interface TabData {
  value: string
  label: string
  title: string
  description?: string
  embed?: EmbedComponent[]  // 可選的嵌入元件
  code?: string
}

interface TabsBlockProps {
  tabs: TabData[]
  defaultValue?: string
  className?: string
}

export function TabsBlock({ tabs, defaultValue, className = '' }: TabsBlockProps) {
  return (
    <Tabs defaultValue={defaultValue || tabs[0]?.value} className={className}>
      <TabsList>
        {tabs.map((tab) => (
          <TabsTrigger key={tab.value} value={tab.value}>
            {tab.label}
          </TabsTrigger>
        ))}
      </TabsList>
      {tabs.map((tab) => (
        <TabsContent key={tab.value} value={tab.value} className="mt-4">
          <div>
            <h4 className="font-bold mb-2">{tab.title}</h4>
            {tab.description && <p>{tab.description}</p>}
            {tab.embed && tab.embed.length > 0 && (
              <div className="space-y-4">
                {tab.embed.map((embedItem, index) => (
                  <div key={index}>
                    {renderEmbedComponent(embedItem)}
                  </div>
                ))}
              </div>
            )}
            {tab.code && (
              <pre className="bg-gray-100 p-4 rounded-lg overflow-x-auto">
                {tab.code}
              </pre>
            )}
          </div>
        </TabsContent>
      ))}
    </Tabs>
  )
}
