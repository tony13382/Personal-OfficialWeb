import { useState } from 'react'
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet'
import { ListIcon } from '@phosphor-icons/react'
import { mainLinks } from "@/components/header/index"
import { socialLinks } from "@/components/data/social"
import { SearchDialog } from "@/components/search/SearchDialog"
import signUrl from "@/assets/imgs/index/sign.svg?url"


interface MobileNavProps {
  type?: 'main' | 'project'
  themeColor?: string
}



export function MobileNav({ type: _type = 'main' }: MobileNavProps) {
  const [open, setOpen] = useState(false)

  const navLinks = [...mainLinks]

  return (
    <Sheet open={open} onOpenChange={setOpen}>
      <SheetTrigger asChild>
        <button
          className="lg:hidden bg-transparent border-0 cursor-pointer  hover:bg-muted p-4 rounded-full"
          aria-label="Toggle navigation"
        >
          <ListIcon className="size-6" />
        </button>
      </SheetTrigger>
      <SheetContent
        side="right"
        className="w-[300px] sm:w-[400px] bg-background flex flex-col px-4 py-6"
      >
        <SheetHeader>
          <SheetTitle className="text-left">
            選單
          </SheetTitle>
        </SheetHeader>
        <nav className="flex flex-col gap-4 flex-1 min-h-0">
          {/* Search */}
          <div className="px-4 [&_button]:w-full [&_button]:justify-center [&_button]:rounded-lg [&_button]:border [&_button]:border-gray-200 [&_button]:dark:border-gray-700 [&_button]:py-3">
            <SearchDialog />
          </div>

          {/* Navigation Links */}
          <div className="relative flex-1 flex flex-col gap-2 overflow-y-auto">
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
            <img
              src={signUrl}
              alt="Logo"
              className="absolute bottom-0 right-4 opacity-25 text-primary max-h-7 mt-2"
              loading="lazy"
              decoding="async"
            />
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
