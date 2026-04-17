export type StructuredLocale = "zh-Hant" | "en";

export interface StructuredListItem {
  url: string;
  name: string;
  description?: string;
  image?: string;
  datePublished?: string;
  dateModified?: string;
  dateCreated?: string;
  type?:
    | "Article"
    | "BlogPosting"
    | "CreativeWork"
    | "SoftwareApplication"
    | "WebApplication";
}

export interface BuildItemListOptions {
  name: string;
  description?: string;
  url: string;
  items: StructuredListItem[];
  locale: StructuredLocale;
  authorId?: string;
  siteId?: string;
}

export const toSchemaLang = (locale: StructuredLocale): string =>
  locale === "en" ? "en" : "zh-Hant-TW";

export const absolutize = (siteUrl: string, input: string): string => {
  if (!input) return "";
  if (/^https?:\/\//.test(input)) return input;
  return `${siteUrl}${input.startsWith("/") ? input : `/${input}`}`;
};

export function buildItemListJsonLd(opts: BuildItemListOptions) {
  const inLanguage = toSchemaLang(opts.locale);
  return {
    "@type": "ItemList",
    "@id": `${opts.url}#itemlist`,
    name: opts.name,
    ...(opts.description ? { description: opts.description } : {}),
    url: opts.url,
    inLanguage,
    numberOfItems: opts.items.length,
    ...(opts.siteId ? { isPartOf: { "@id": opts.siteId } } : {}),
    itemListElement: opts.items.map((item, idx) => ({
      "@type": "ListItem",
      position: idx + 1,
      url: item.url,
      item: {
        "@type": item.type ?? "CreativeWork",
        "@id": item.url,
        name: item.name,
        url: item.url,
        inLanguage,
        ...(item.description ? { description: item.description } : {}),
        ...(item.image ? { image: item.image } : {}),
        ...(item.datePublished
          ? { datePublished: item.datePublished }
          : {}),
        ...(item.dateModified ? { dateModified: item.dateModified } : {}),
        ...(item.dateCreated ? { dateCreated: item.dateCreated } : {}),
        ...(opts.authorId && isAuthorBearingType(item.type)
          ? { author: { "@id": opts.authorId } }
          : {}),
      },
    })),
  };
}

function isAuthorBearingType(type?: StructuredListItem["type"]): boolean {
  if (!type) return true;
  return type === "Article" || type === "BlogPosting" || type === "CreativeWork";
}
