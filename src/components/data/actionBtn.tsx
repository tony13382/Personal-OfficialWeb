import { DownloadSimpleIcon, GithubLogoIcon } from "@phosphor-icons/react"
import { Button } from "../ui/button"



interface ActionLink {
    href: string
    label: string
    icon?: React.ReactNode
}


function getActionLinks(): ActionLink[] {
    const en = typeof window !== 'undefined' && window.location.pathname.startsWith('/en/')
    return [
        {
            href: "https://github.com/tony13382",
            label: "Github",
            icon: <GithubLogoIcon className="size-12" />
        },
        {
            href: "https://drive.google.com/file/d/1vN6BVqPXcnAzDVIDNJvWqHbNMjirxx0D/view?usp=sharing",
            label: en ? "Resume" : "下載履歷",
            icon: <DownloadSimpleIcon className="size-12" />
        },
    ]
}


export function ActionBtnLinks() {
    const links = getActionLinks()
    return (
        <div className="flex gap-3">
            {links.map((link) => (
                <Button key={link.href} asChild>
                    <a
                        href={link.href}
                        target="_blank"
                        rel="noreferrer"
                    >
                        {link.icon} {link.label}
                    </a>
                </Button>
            ))}
        </div>
    )
}
