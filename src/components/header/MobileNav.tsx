import { useState } from 'react'
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet'
import { ListIcon } from '@phosphor-icons/react'
import { mainLinks, socialLinks, type NavLink } from "@/components/header/index"


interface MobileNavProps {
  type?: 'main' | 'project'
  themeColor?: string
}



export function MobileNav({ type = 'main', themeColor }: MobileNavProps) {
  const [open, setOpen] = useState(false)

  const projectLinks: NavLink[] = [{ href: '/', label: '首頁' }]

  const navLinks = type === 'main' ? [...mainLinks] : [...projectLinks]

  return (
    <Sheet open={open} onOpenChange={setOpen}>
      <SheetTrigger asChild>
        <button
          className="lg:hidden bg-transparent border-0 text-gray-900 dark:text-white cursor-pointer  hover:bg-foreground/20 p-4 rounded-full"
          aria-label="Toggle navigation"
        >
          <ListIcon className="size-6" />
        </button>
      </SheetTrigger>
      <SheetContent
        side="right"
        className="w-[300px] sm:w-[400px] bg-background flex flex-col px-4 py-6 rounded-s-2xl"
      >
        <SheetHeader>
          <SheetTitle className="text-left text-gray-900 dark:text-white">
            選單
          </SheetTitle>
        </SheetHeader>
        <nav className="flex flex-col gap-4 flex-1 min-h-0">
          {/* Navigation Links */}
          <div className="flex-1 flex flex-col gap-2 overflow-y-auto">
            {navLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                onClick={() => setOpen(false)}
                className="flex items-center gap-2 px-4 py-3 text-gray-700 dark:text-gray-300 no-underline text-lg rounded-lg transition-all hover:bg-gray-100 dark:hover:bg-gray-800"
              >
                {link.icon}
                <span>{link.label}</span>
              </a>
            ))}
          </div>

          {/* Divider */}
          <div className="border-t border-gray-300 dark:border-gray-700 my-2"></div>

          {/* Social Links */}
          <p className="px-4 text-sm text-gray-500 dark:text-gray-400 font-medium">
            聯絡方式
          </p>
          <div className="grid grid-cols-1 gap-2">
            {socialLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                target={link.external ? '_blank' : undefined}
                rel={link.external ? 'noopener noreferrer' : undefined}
                onClick={() => setOpen(false)}
                className="flex items-center gap-3 px-4 py-3 text-gray-700 dark:text-gray-300 no-underline text-base rounded-lg transition-all hover:bg-gray-100 dark:hover:bg-gray-800"
              >
                {link.icon}
                <span>{link.label}</span>
              </a>
            ))}
          </div>
        </nav>
      </SheetContent>
    </Sheet>
  )
}
