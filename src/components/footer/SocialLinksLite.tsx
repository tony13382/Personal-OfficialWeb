import { socialLinks } from '@/components/data/social'

export function SocialLinks() {
    return (
        <>
            {socialLinks.map((link) => (
                <a
                    key={link.href}
                    href={link.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-2 p-3 text-muted-foreground rounded-full transition-all hover:text-foreground hover:bg-muted hover:[&>span]:block"
                >
                    {link.icon}
                </a>
            ))}
        </>
    )
}
