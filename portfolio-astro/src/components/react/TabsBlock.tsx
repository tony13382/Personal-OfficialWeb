import { Tabs, TabsList, TabsTrigger, TabsContent } from '@/components/ui/tabs'
import { Card, CardContent } from '@/components/ui/card'

interface TabData {
  value: string
  label: string
  title: string
  description?: string
  listItems?: string[]
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
            {tab.listItems && (
              <ul className="list-disc pl-6 space-y-1">
                {tab.listItems.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
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
