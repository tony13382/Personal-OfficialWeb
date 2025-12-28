/**
 * ImageWithLightbox - Image component with optional Fancybox lightbox
 * React version for use in MDX
 */

interface ImageWithLightboxProps {
  src: string
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

  if (allowPop) {
    return (
      <a href={src} data-fancybox="gallery" className={`mx-auto block ${roundedClass} ${className}`}>
        <img
          src={src}
          className="img-fluid mx-auto"
          alt={alt}
          style={maxWidthStyle}
        />
      </a>
    )
  }

  return (
    <div className={`block mx-auto text-center ${className}`}>
      <img
        src={src}
        className={`img-fluid mx-auto ${roundedClass}`}
        alt={alt}
        style={maxWidthStyle}
      />
    </div>
  )
}
