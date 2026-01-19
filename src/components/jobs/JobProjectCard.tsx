import { ArrowUpRightIcon } from "@phosphor-icons/react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card";
import { parseTextWithHighlight } from "../react/Basic";

interface JobProjectCardProps {
    name: string;
    startDate?: string | Date | null;
    endDate?: string | Date | null;
    link?: string;
    descriptions?: string[];
    tags?: string[];
    imageSrc?: string;
    imageAlt?: string;
}

const formatDateValue = (value?: string | Date | null) => {
    if (!value) return null;
    if (typeof value === "string") return value;
    return value.toLocaleDateString("zh-TW", {
        year: "numeric",
        month: "2-digit",
    });
};

const formatDateRange = (
    startDate?: string | Date | null,
    endDate?: string | Date | null
) => {
    const startLabel = formatDateValue(startDate);
    let endLabel = formatDateValue(endDate);

    if (!endLabel && startLabel && endDate == null) {
        endLabel = "現在";
    }

    if (startLabel && endLabel) return `${startLabel} ~ ${endLabel}`;
    return startLabel || endLabel || null;
};

export const JobProjectCard = ({
    name,
    startDate,
    endDate,
    link,
    descriptions = [],
    tags = [],
    imageSrc,
    imageAlt,
}: JobProjectCardProps) => {
    const timeStr = formatDateRange(startDate, endDate);

    return (
        <Card>
            {imageSrc && (
                <CardHeader>
                    <img src={imageSrc} alt={imageAlt || name} className="img-fluid" />
                </CardHeader>
            )}
            <CardContent className="space-y-4">
                <div className="flex items-start justify-between gap-3">
                    <p className="text-2xl font-bold text-foreground">{name}</p>
                </div>
                <hr />
                {timeStr && <p className="text-muted-foreground">{timeStr}</p>}
                {descriptions.length > 0 && (
                    <ul className="space-y-2 list-disc ps-5">
                        {descriptions.map((desc, index) => {
                            const isHeading = desc.startsWith("## ");
                            const content = isHeading ? desc.replace(/^##\s+/, "") : desc;
                            return (
                                <li
                                    key={index}
                                    className={
                                        isHeading
                                            ? "font-bold text-foreground list-none pt-1.5 -ms-5"
                                            : undefined
                                    }
                                >
                                    {parseTextWithHighlight(content)}
                                </li>
                            );
                        })}
                    </ul>
                )}
                {link && (
                    <Button variant="outline" asChild>
                        <a href={link} className="flex items-center gap-1.5 mt-3">
                            <ArrowUpRightIcon className="size-4" />
                            查看專案
                        </a>
                    </Button>
                )}
            </CardContent>
            {tags.length > 0 && (
                <CardFooter className="flex flex-wrap gap-2">
                    {tags.map((tag, index) => {
                        const label = tag.trim().startsWith("#")
                            ? tag.trim()
                            : `# ${tag.trim()}`;
                        return (
                            <Badge key={index} variant="secondary">
                                {label}
                            </Badge>
                        );
                    })}
                </CardFooter>
            )}
        </Card>
    );
};
