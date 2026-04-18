import { DownloadSimpleIcon, GithubLogoIcon } from "@phosphor-icons/react"
import { Button } from "../ui/button"



interface ActionLink {
    href: string
    label: string
    icon?: React.ReactNode
    external?: boolean
}


function getActionLinks(): ActionLink[] {
    const en = typeof window !== 'undefined' && window.location.pathname.startsWith('/en/')
    return [
        {
            href: "https://github.com/tony13382",
            label: "Github",
            icon: <GithubLogoIcon className="size-12" />,
            external: true,
        },
        {
            href: en ? "/en/down-resume" : "/down-resume",
            label: en ? "Resume" : "下載履歷",
            icon: <DownloadSimpleIcon className="size-12" />,
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
                        {...(link.external ? { target: "_blank", rel: "noreferrer" } : {})}
                    >
                        {link.icon} {link.label}
                    </a>
                </Button>
            ))}
        </div>
    )
}
