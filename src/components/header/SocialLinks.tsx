import { socialLinks } from './index'

export function SocialLinks() {
  return (
    <>
      {socialLinks.map((link) => (
        <a
          key={link.href}
          href={link.href}
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center gap-2 px-4 py-2 text-muted-foreground rounded-full transition-all hover:text-foreground hover:bg-muted"
        >
          {link.icon}
          <span>{link.label}</span>
        </a>
      ))}
    </>
  )
}
