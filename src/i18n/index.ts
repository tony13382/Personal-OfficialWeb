import zhHant from './zh-Hant';
import en from './en';

export type Locale = 'zh-Hant' | 'en';
export type Translations = typeof zhHant;

const translations: Record<Locale, Translations> = {
  'zh-Hant': zhHant,
  en,
};

/**
 * Extract locale from URL pathname.
 * /en/about/ → 'en', /about/ → 'zh-Hant'
 */
export function getLangFromUrl(url: URL): Locale {
  const [, lang] = url.pathname.split('/');
  if (lang === 'en') return 'en';
  return 'zh-Hant';
}

/**
 * Get the translation object for a given locale.
 */
export function useTranslations(lang: Locale): Translations {
  return translations[lang];
}

/**
 * Convert a path to its localised version.
 * getLocalePath('/about/', 'en') → '/en/about/'
 * getLocalePath('/en/about/', 'zh-Hant') → '/about/'
 */
export function getLocalePath(path: string, lang: Locale): string {
  // Strip existing /en/ prefix if present
  const stripped = path.replace(/^\/en(\/|$)/, '/');

  if (lang === 'zh-Hant') return stripped || '/';
  return `/en${stripped === '/' ? '/' : stripped}`;
}

/**
 * Get the HTML lang attribute value for a locale.
 */
export function getHtmlLang(lang: Locale): string {
  return lang === 'zh-Hant' ? 'zh-Hant-TW' : 'en';
}

/**
 * Get the alternate locale (for language switcher).
 */
export function getAlternateLocale(lang: Locale): Locale {
  return lang === 'zh-Hant' ? 'en' : 'zh-Hant';
}

/**
 * Get display label for a locale.
 */
export function getLocaleLabel(lang: Locale): string {
  return lang === 'zh-Hant' ? '中文' : 'EN';
}

/**
 * Filter a content collection by locale prefix in slug.
 * Entries in `zh-Hant/foo` match locale 'zh-Hant', `en/foo` match 'en'.
 * Returns entries with the locale prefix stripped from the slug.
 */
export function filterByLocale<T extends { slug: string }>(
  entries: T[],
  lang: Locale,
): (T & { slug: string })[] {
  const prefix = `${lang.toLowerCase()}/`;
  return entries
    .filter((e) => e.slug.toLowerCase().startsWith(prefix))
    .map((e) => ({ ...e, slug: e.slug.slice(prefix.length) }));
}
