import { Accordion, AccordionItem, AccordionTrigger, AccordionContent } from '@/components/ui/accordion'
import { type EmbedComponent, renderEmbedComponent } from './Basic'

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
  firstActive?: boolean
}

export function AccordionBlock({ items, type = 'single', collapsible = true, className = '', firstActive = false }: AccordionBlockProps) {

  const accordionItems = items.map((item) => (
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
  ))

  const accordionClassName = `border rounded-2xl overflow-hidden ${className}`
  const defaultSingleValue = firstActive && items.length > 0 ? items[0].value : undefined

  if (type === 'single') {
    return (
      <Accordion type="single" collapsible={collapsible} defaultValue={defaultSingleValue} className={accordionClassName}>
        {accordionItems}
      </Accordion>
    )
  }

  return (
    <Accordion type="multiple" defaultValue={firstActive && items.length > 0 ? [items[0].value] : []} className={accordionClassName}>
      {accordionItems}
    </Accordion>
  )
}
