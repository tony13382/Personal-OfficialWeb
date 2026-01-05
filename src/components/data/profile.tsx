import { SocialLinks } from "../footer/SocialLinksLite"
import { Card, CardContent } from "../ui/card"
import { ActionBtnLinks } from "./actionBtn"

interface ProfileData {
    name: string
    jobTitle: string
}


export const profileData: ProfileData = {
    name: "呂亮進",
    jobTitle: "AI 工程師、產品設計師、全端開發者"
}


export function ProfileCard() {
    return (
        <Card
            className="mt-8 transition-all duration-300 pb-4 hidden lg:inline-flex"
        >
            <CardContent className="gap-6 items-center pt-3 pb-4">
                <div
                    className="h-4 w-10 my-2 border rounded-full bg-[var(--theme-primary-10)] inset-shadow-sm"
                >
                </div>
                <img
                    src="/assets/imgs/index/myHead.webp"
                    alt={`${profileData.name}的頭像`}
                    className="size-32 rounded-full overflow-hidden"
                />
                <div className="">
                    <p
                        className="text-xl md:text-2xl text-center text-foreground font-bold mb-3"
                    >
                        {profileData.name}
                    </p>
                    <p className="text-muted-foreground text-center mb-3">
                        {profileData.jobTitle}
                    </p>
                </div>
                <ActionBtnLinks />
                <div>
                    <div className="flex px-1">
                        <SocialLinks />
                    </div>
                </div>
            </CardContent>
        </Card>
    )
}