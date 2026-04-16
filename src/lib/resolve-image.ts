import type { ImageMetadata } from 'astro';

const images = import.meta.glob<{ default: ImageMetadata }>(
  '/src/assets/imgs/**/*.{png,jpg,jpeg,webp,svg}',
  { eager: true },
);

/**
 * Resolve a short image path to ImageMetadata.
 *
 * Usage in MDX frontmatter:
 *   cover: imgs/jobs/2024_SolwenAi/cover.png
 *
 * In code:
 *   resolveImage('imgs/jobs/2024_SolwenAi/cover.png')
 */
export function resolveImage(path: string): ImageMetadata {
  const key = `/src/assets/${path}`;
  const entry = images[key];
  if (!entry) {
    throw new Error(
      `Image not found: ${path}\nResolved key: ${key}\nAvailable keys (sample): ${Object.keys(images).slice(0, 5).join(', ')}`,
    );
  }
  return entry.default;
}

/**
 * Resolve string image paths in collection entries to ImageMetadata.
 * Mutates `data.cover`, `data.icon`, `data.logo` in-place so React
 * components receive usable image objects.
 */
export function resolveCollectionImages<T extends { data: Record<string, any> }>(
  entries: T[],
): T[] {
  return entries.map((entry) => {
    const data = { ...entry.data };
    if (typeof data.cover === 'string') data.cover = resolveImage(data.cover);
    if (typeof data.icon === 'string') data.icon = resolveImage(data.icon);
    if (typeof data.logo === 'string') data.logo = resolveImage(data.logo);
    return { ...entry, data };
  });
}
