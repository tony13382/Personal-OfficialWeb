/**
 * Tool - Two-column tool description component
 * React version for use in MDX
 */
import { Text } from './Text'
import { ListDiv } from './ListDiv'

interface ToolProps {
  name: string
  action: string
  className?: string
}

export function Tool({ name, action, className = '' }: ToolProps) {
  return (
    <div className={`col-span-12 sm:col-span-6 ${className}`}>
      <ListDiv gap="nano">
        <Text content={name} bold />
        <Text content={action} />
      </ListDiv>
    </div>
  )
}
