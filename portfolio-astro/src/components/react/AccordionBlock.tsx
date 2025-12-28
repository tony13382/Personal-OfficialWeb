import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from '@/components/ui/accordion'
import { Canva } from './Canva'
import { Youtube } from './Youtube'

// 支援的嵌入元件類型
export type EmbedComponent =
  | { type: 'canva'; src: string; title?: string }
  | { type: 'youtube'; embedUrl: string; className?: string }
  | { type: 'text'; content: string; className?: string }
  | { type: 'image'; content: string; className?: string }
// 未來可以繼續擴展：
// | { type: 'image-carousel'; images: Array<{src: string, alt: string}> }
// | { type: 'code-block'; code: string; language: string }

export interface AccordionItemData {
  value: string
  trigger: string
  content?: string
  description?: string  // 可選的描述文字
  embed?: EmbedComponent[]  // 可選的嵌入元件
  contentClassName?: string
}

interface AccordionBlockProps {
  items: AccordionItemData[]
  type?: 'single' | 'multiple'
  collapsible?: boolean
  className?: string
}

export function AccordionBlock({ items, type = 'single', collapsible = true, className = '' }: AccordionBlockProps) {
  const renderEmbedComponent = (embed: EmbedComponent) => {
    switch (embed.type) {
      case 'canva':
        return <Canva src={embed.src} title={embed.title} />
      case 'youtube':
        return <div className={embed.className}>
          <Youtube embedUrl={embed.embedUrl} />
        </div>
      case 'text':
        return <p className={embed.className}>{embed.type}</p>
      default:
        return null
    }
  }

  return (
    <Accordion type={type} collapsible={collapsible} className={`border rounded-2xl overflow-hidden ${className}`}>
      {items.map((item) => (
        <AccordionItem key={item.value} value={item.value}>
          <AccordionTrigger>{item.trigger}</AccordionTrigger>
          <AccordionContent className={item.contentClassName}>
            {item.description && <p className="">{item.description}</p>}
            {item.embed && item.embed.length > 0 && (
              <div className="space-y-4">
                {item.embed.map((embedItem, index) => (
                  <div key={index}>
                    {renderEmbedComponent(embedItem)}
                  </div>
                ))}
              </div>
            )}
            {!item.description && !item.embed && item.content}
          </AccordionContent>
        </AccordionItem>
      ))}
    </Accordion>
  )
}
