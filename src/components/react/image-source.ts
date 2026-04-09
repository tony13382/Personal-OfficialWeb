import type { ImageMetadata } from "astro";

export type ImageSource = string | ImageMetadata;

export const getImageSrc = (source: ImageSource) =>
  typeof source === "string" ? source : source.src;
