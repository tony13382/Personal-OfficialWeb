/**
 * Score - Award/score display card
 * React version for use in MDX
 */

interface ScoreProps {
  name: string
  score: string
  group?: string
  className?: string
}

export function Score({ name, score, group, className = '' }: ScoreProps) {
  return (
    <div className={`grid px-1 ${className}`}>
      <div className="p-2">
        <ul className="list-none border-0">
          <li className="px-0 border-b border-border pb-4">
            <p className="m-0 text-sm">
              {name}
              {group && (
                <>
                  ・<span className="inline-block">{group}</span>
                </>
              )}
            </p>
            <p className="m-0 pt-1 font-bold text-2xl" style={{ color: 'var(--theme-primary, var(--color-primary))' }}>
              {score}
            </p>
          </li>
        </ul>
      </div>
    </div>
  )
}
