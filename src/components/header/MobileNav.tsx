import { useState } from "react";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import { ListIcon } from "@phosphor-icons/react";
import { getMainLinks } from "@/components/header/index";
import { socialLinks } from "@/components/data/social";
import { SearchDialog } from "@/components/search/SearchDialog";
import signUrl from "@/assets/imgs/index/sign.svg?url";
import type { Locale } from "@/i18n";

const menuLabels = {
  "zh-Hant": { menu: "選單", contact: "聯絡方式" },
  en: { menu: "Menu", contact: "Contact" },
} as const;

interface MobileNavProps {
  type?: "main" | "project";
  themeColor?: string;
  locale?: Locale;
}

export function MobileNav({
  type: _type = "main",
  locale = "zh-Hant",
}: MobileNavProps) {
  const [open, setOpen] = useState(false);
  const labels = menuLabels[locale];

  const navLinks = getMainLinks(locale);

  return (
    <Sheet open={open} onOpenChange={setOpen}>
      <SheetTrigger asChild>
        <button
          className="lg:hidden bg-transparent border-0 cursor-pointer text-foreground hover:bg-muted p-4 rounded-full"
          aria-label="Toggle navigation"
        >
          <ListIcon className="size-6" />
        </button>
      </SheetTrigger>
      <SheetContent
        side="right"
        className="w-75 sm:w-100 bg-background flex flex-col px-4 py-6"
      >
        <SheetHeader>
          <SheetTitle className="text-left">{labels.menu}</SheetTitle>
        </SheetHeader>
        <nav className="flex flex-col gap-4 flex-1 min-h-0">
          {/* Search */}
          <div className="px-4 [&_button]:w-full [&_button]:justify-center [&_button]:rounded-lg [&_button]:border [&_button]:border-border [&_button]:py-3">
            <SearchDialog locale={locale} />
          </div>

          {/* Navigation Links */}
          <div className="relative flex-1 flex flex-col gap-2 overflow-y-auto">
            {navLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                onClick={() => setOpen(false)}
                className="flex items-center gap-2 px-4 py-3 text-foreground no-underline text-lg rounded-lg transition-all hover:bg-muted"
              >
                {link.icon}
                <span>{link.label}</span>
              </a>
            ))}
            <span
              role="img"
              aria-label="Liang Chin Lu signature"
              className="absolute bottom-0 right-4 opacity-25 block h-7 mt-2 bg-foreground"
              style={{
                width: "calc(7 * 2286 / 457 * 0.25rem)",
                WebkitMask: `url(${signUrl}) no-repeat center / contain`,
                mask: `url(${signUrl}) no-repeat center / contain`,
              }}
            />
          </div>

          {/* Divider */}
          <div className="border-t border-border my-2"></div>

          {/* Social Links */}
          <p className="px-4 text-sm text-muted-foreground font-medium">
            {labels.contact}
          </p>
          <div className="grid grid-cols-1 gap-2">
            {socialLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                target={link.external ? "_blank" : undefined}
                rel={link.external ? "noopener noreferrer" : undefined}
                onClick={() => setOpen(false)}
                className="flex items-center gap-3 px-4 py-3 text-foreground no-underline text-base rounded-lg transition-all hover:bg-muted"
              >
                {link.icon}
                <span>{link.label}</span>
              </a>
            ))}
          </div>
        </nav>
      </SheetContent>
    </Sheet>
  );
}
