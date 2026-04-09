/**
 * ImageWithLightbox - Image component with optional Fancybox lightbox
 * React version for use in MDX
 */
import type { ImageSource } from "./image-source"
import { getImageSrc } from "./image-source"

interface ImageWithLightboxProps {
  src: ImageSource
  alt?: string
  allowPop?: boolean
  maxWidth?: number
  rounded?: boolean
  className?: string
}

export function ImageWithLightbox({
  src,
  alt = '',
  allowPop = false,
  maxWidth,
  rounded = false,
  className = ''
}: ImageWithLightboxProps) {
  const roundedClass = rounded ? 'rounded-inline-basic' : ''
  const maxWidthStyle = maxWidth ? { width: '100%', maxWidth: `${maxWidth}px` } : undefined
  const imageSrc = getImageSrc(src)

  if (allowPop) {
    return (
      <a href={imageSrc} data-fancybox="gallery" aria-label={alt || '檢視大圖'} className={`mx-auto block ${roundedClass} ${className}`}>
        <img
          src={imageSrc}
          className="img-fluid mx-auto"
          alt={alt}
          style={maxWidthStyle}
          loading="lazy"
          decoding="async"
        />
      </a>
    )
  }

  return (
    <div className={`block mx-auto text-center ${className}`}>
      <img
        src={imageSrc}
        className={`img-fluid mx-auto ${roundedClass}`}
        alt={alt}
        style={maxWidthStyle}
        loading="lazy"
        decoding="async"
      />
    </div>
  )
}
