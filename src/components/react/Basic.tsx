
import { Canva } from './Canva'
import { Youtube } from './Youtube'
import { ImageWithLightbox } from './ImageWithLightbox';
import { IconBlock } from './IconBlock';
import { Fragment } from 'react';

// 將反引號包裹的文字轉換為 highlight span
export const parseTextWithHighlight = (text: string) => {
    const parts = text.split(/(`[^`]+`)/g);
    return parts.map((part, index) => {
        if (part.startsWith('`') && part.endsWith('`')) {
            const content = part.slice(1, -1);
            return <span key={index} className="text-highlight">{content}</span>;
        }
        return <Fragment key={index}>{part}</Fragment>;
    });
};

// 支援的嵌入元件類型
export type EmbedComponent =
    | { type: 'Canva'; src: string; title?: string }
    | { type: "Youtube"; embedUrl: string; className?: string }
    | { type: 'IconBlock'; title?: string; subtitle?: string; href?: string; icon?: string; className?: string; }
    | { type: 'text'; content: string; className?: string }
    | { type: 'image'; src: string; className?: string; allowPop?: boolean }
    | { type: 'hr'; className?: string }
    | { type: 'html'; content: string; className?: string }
    | { type: 'div'; elements: EmbedComponent[]; className?: string }
// 未來可以繼續擴展：
// | { type: 'image-carousel'; images: Array<{src: string, alt: string}> }
// | { type: 'code-block'; code: string; language: string }


export const renderEmbedComponent = (embed: EmbedComponent) => {
    switch (embed.type) {
        case 'Canva':
            return <Canva src={embed.src} title={embed.title} />
        case "Youtube":
            return <div className={embed.className}>
                <Youtube embedUrl={embed.embedUrl} />
            </div>
        case 'IconBlock':
            return <IconBlock title={embed.title} subtitle={embed.subtitle} href={embed.href} icon={embed.icon} className={embed.className} />
        case 'text':
            return <p className={embed.className}>{parseTextWithHighlight(embed.content)}</p>
        case 'image':
            return <ImageWithLightbox src={embed.src} className={embed.className} allowPop={embed.allowPop} />
        case 'hr':
            return <hr className={embed.className} />
        case 'html':
            return <div className={embed.className} dangerouslySetInnerHTML={{ __html: embed.content }} />
        case 'div':
            return <div className={embed.className}>
                {embed.elements && embed.elements.length > 0 && (
                    embed.elements.map((embedItem, index) => (
                        <Fragment key={index}>
                            {renderEmbedComponent(embedItem)}
                        </Fragment>
                    ))
                )}
            </div>
        default:
            return null
    }
}