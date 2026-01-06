import { useState, useEffect } from "react"
import { SocialLinksLite } from "../data/social"
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
            className="mt-8 transition-all duration-300 pb-4 hidden lg:flex  justify-center"
        >
            <CardContent className="gap-6 items-center pt-3 pb-2">
                <div
                    className="h-4 w-10 my-2 border rounded-full bg-[var(--theme-primary-10)] inset-shadow-sm"
                >
                </div>
                <img
                    src="/assets/imgs/index/myHead.webp"
                    alt={`${profileData.name}的頭像`}
                    className="size-32 rounded-full overflow-hidden"
                />
                <div className="grid gap-3">
                    <p
                        className="text-xl md:text-2xl text-center text-foreground font-bold"
                    >
                        {profileData.name}
                    </p>
                    <p className="text-muted-foreground text-center">
                        {profileData.jobTitle}
                    </p>
                </div>
                <ActionBtnLinks />
                <div>
                    <div className="flex px-1 flex-wrap justify-center">
                        <SocialLinksLite />
                    </div>
                </div>
            </CardContent>
        </Card>
    )
}

export function ProfileCardTigger() {
    return (
        <button
            id="profile-modal-btn"
            className="floatbtn fixed bottom-28 right-6 size-16 md:bottom-30 md:right-8 rounded-full bg-[var(--theme-primary)] text-background flex items-center justify-center shadow-[0_4px_12px_rgba(0,0,0,0.15)] opacity-0 invisible transition-all duration-300 ease-in-out z-40 cursor-pointer hover:bg-[var(--theme-secondary)] hover:-translate-y-1 hover:shadow-[0_6px_16px_rgba(0,0,0,0.2)] active:-translate-y-0.5 lg:hidden"
            title="通知我"
        >
            <img
                src="/assets/imgs/index/myHead.webp"
                alt={`${profileData.name}的頭像`}
                className="size-16 rounded-full overflow-hidden"
            />
        </button>
    )
}



export function ProfileCardModal() {
    const [isOpen, setIsOpen] = useState(false)

    useEffect(() => {
        const handleEscape = (e: KeyboardEvent) => {
            if (e.key === "Escape" && isOpen) {
                setIsOpen(false)
            }
        }

        if (isOpen) {
            document.body.style.overflow = "hidden"
            document.addEventListener("keydown", handleEscape)
        } else {
            document.body.style.overflow = ""
        }

        return () => {
            document.removeEventListener("keydown", handleEscape)
            document.body.style.overflow = ""
        }
    }, [isOpen])

    useEffect(() => {
        const openBtn = document.getElementById("profile-modal-btn")

        const handleOpen = () => {
            setIsOpen(true)
        }

        openBtn?.addEventListener("click", handleOpen)

        return () => {
            openBtn?.removeEventListener("click", handleOpen)
        }
    }, [])

    if (!isOpen) return null

    return (
        <div
            className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4 animate-[fadeIn_0.2s_ease-out]"
            onClick={() => setIsOpen(false)}
        >
            <div
                className="flex flex-col items-center gap-6 max-w-md w-full"
                onClick={(e) => e.stopPropagation()}
            >
                {/* ProfileCard */}
                <div className="animate-[slideUp_0.3s_ease-out]">
                    <Card className="mt-8 transition-all duration-300 pb-4 inline-flex">
                        <CardContent className="gap-6 items-center pt-3 pb-2">
                            <div className="h-4 w-10 my-2 border rounded-full bg-black/50" />
                            <img
                                src="/assets/imgs/index/myHead.webp"
                                alt={`${profileData.name}的頭像`}
                                className="size-32 rounded-full overflow-hidden"
                            />
                            <div className="">
                                <p className="text-xl md:text-2xl text-center text-foreground font-bold mb-3">
                                    {profileData.name}
                                </p>
                                <p className="text-muted-foreground text-center mb-3">
                                    {profileData.jobTitle}
                                </p>
                            </div>
                            <ActionBtnLinks />
                            <div>
                                <div className="flex px-1">
                                    <SocialLinksLite />
                                </div>
                            </div>
                        </CardContent>
                    </Card>
                </div>

                {/* Close Button */}
                <button
                    onClick={() => setIsOpen(false)}
                    className="w-14 h-14 rounded-full bg-white text-gray-800 flex items-center justify-center shadow-lg hover:bg-gray-100 transition-all duration-200 hover:scale-110 active:scale-95"
                    aria-label="關閉"
                    title="關閉"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-8 w-8"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        strokeWidth="2"
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M6 18L18 6M6 6l12 12"
                        />
                    </svg>
                </button>
            </div>

            <style>{`
                @keyframes fadeIn {
                    from {
                        opacity: 0;
                    }
                    to {
                        opacity: 1;
                    }
                }
                @keyframes slideUp {
                    from {
                        opacity: 0;
                        transform: translateY(20px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
            `}</style>
        </div>
    )
}