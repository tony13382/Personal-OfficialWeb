import { DownloadSimpleIcon, GithubLogoIcon } from "@phosphor-icons/react"
import { Button } from "../ui/button"



interface ActionLink {
    href: string
    label: string
    icon?: React.ReactNode
}


const actionLinks: ActionLink[] = [
    {
        href: "https://github.com/tony13382",
        label: "Github",
        icon: <GithubLogoIcon className="size-12" />
    },
    {
        href: "https://drive.google.com/file/d/1vN6BVqPXcnAzDVIDNJvWqHbNMjirxx0D/view?usp=sharing",
        label: "下載履歷",
        icon: <DownloadSimpleIcon className="size-12" />
    },

]


export function ActionBtnLinks() {
    return (
        <div className="flex gap-4">
            {actionLinks.map((link) => (
                <a href={link.href} target="_blank">
                    <Button>
                        {link.icon} {link.label}
                    </Button>
                </a>
            ))}
        </div>
    )
}
