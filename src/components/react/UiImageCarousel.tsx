/**
 * UiImageCarousel - Image carousel with autoplay and dots
 * React version of Python UiImageCarousel component
 * Features: autoplay, dot indicators, Fancybox lightbox, navigation buttons
 */
import { useState, useCallback, useEffect, useId } from 'react'
import useEmblaCarousel from 'embla-carousel-react'
import Autoplay from 'embla-carousel-autoplay'
import { CaretLeftIcon, CaretRightIcon } from '@phosphor-icons/react'

interface UiImage {
  image: string
  desc?: string
  title?: string
}

interface UiImageCarouselProps {
  images: (string | UiImage)[]
  autoplaySpeed?: number
  alignBody?: 'top' | 'center' | 'bottom'

  className?: string
  galleryId?: string
  allowPop?: boolean
}

const alignBodyClasses = {
  top: 'items-start',
  center: 'items-center',
  bottom: 'items-end'
}

export function UiImageCarousel({
  images,
  autoplaySpeed = 3000,
  alignBody = 'top',
  className = '',
  galleryId,
  allowPop = true
}: UiImageCarouselProps) {
  const uniqueId = useId()
  const fancyboxGalleryId = galleryId || `gallery-${uniqueId}`
  const [emblaRef, emblaApi] = useEmblaCarousel(
    { loop: true },
    [Autoplay({ delay: autoplaySpeed, stopOnInteraction: false })]
  )

  const [selectedIndex, setSelectedIndex] = useState(0)
  const [canScrollPrev, setCanScrollPrev] = useState(false)
  const [canScrollNext, setCanScrollNext] = useState(false)

  const scrollPrev = useCallback(() => {
    if (emblaApi) emblaApi.scrollPrev()
  }, [emblaApi])

  const scrollNext = useCallback(() => {
    if (emblaApi) emblaApi.scrollNext()
  }, [emblaApi])

  const scrollTo = useCallback((index: number) => {
    if (emblaApi) emblaApi.scrollTo(index)
  }, [emblaApi])

  const onSelect = useCallback(() => {
    if (!emblaApi) return
    setSelectedIndex(emblaApi.selectedScrollSnap())
    setCanScrollPrev(emblaApi.canScrollPrev())
    setCanScrollNext(emblaApi.canScrollNext())
  }, [emblaApi])

  useEffect(() => {
    if (!emblaApi) return
    onSelect()
    emblaApi.on('select', onSelect)
    emblaApi.on('reInit', onSelect)
  }, [emblaApi, onSelect])

  return (
    <div className={`${className ? className : "mt-5 mb-5"}`}>
      {/* Carousel viewport */}
      <div className="relative">
        <div className="overflow-hidden" ref={emblaRef}>
          <div className={`flex ${alignBodyClasses[alignBody]}`}>
            {images.map((item, index) => {
              const imageUrl = typeof item === 'string' ? item : item.image
              const imageDesc = typeof item === 'string' ? `` : item.desc
              const imageTitle = typeof item === 'string' ? `` : item.title

              const content = (
                <>
                  {imageTitle && (<p className='text-center mb-4 text-xl text-foreground font-bold'>
                    {imageTitle}
                  </p>)}
                  <img
                    src={imageUrl}
                    alt={imageDesc ? imageDesc : `Slide ${index}`}
                    className="w-full h-auto object-contain rounded-inline-basic"
                  />
                  {imageDesc && (<p className='text-center mt-4 text-muted-foreground whitespace-pre-line'>
                    {imageDesc}
                  </p>)}
                </>
              )

              return (
                <div key={index} className="flex-[0_0_80%] min-w-0 px-8">
                  {allowPop ? (
                    <a href={imageUrl} data-fancybox={fancyboxGalleryId} className='my-auto'>
                      {content}
                    </a>
                  ) : (
                    <div className='my-auto'>
                      {content}
                    </div>
                  )}
                </div>
              )
            })}
          </div>
        </div>

        {/* Navigation buttons */}
        {images.length > 1 && (
          <>
            <button
              onClick={scrollPrev}
              disabled={!canScrollPrev}
              className="absolute left-4 top-1/2 -translate-y-1/2 bg-white/80 hover:bg-white disabled:opacity-30 rounded-full p-2 shadow-lg transition-all z-10"
              aria-label="Previous slide"
              title="Previous slide"
            >
              <CaretLeftIcon className="w-6 h-6" />
            </button>
            <button
              onClick={scrollNext}
              disabled={!canScrollNext}
              className="absolute right-4 top-1/2 -translate-y-1/2 bg-white/80 hover:bg-white disabled:opacity-30 rounded-full p-2 shadow-lg transition-all z-10"
              aria-label="Next slide"
              title="Next slide"
            >
              <CaretRightIcon className="w-6 h-6" />
            </button>
          </>
        )}
      </div>

      {/* Dot indicators */}
      {images.length > 1 && (
        <div className="flex justify-center gap-2 mt-4">
          {images.map((_, index) => (
            <button
              key={index}
              onClick={() => scrollTo(index)}
              className={`w-2 h-2 rounded-full transition-all ${index === selectedIndex
                ? 'bg-[var(--theme-primary,var(--color-primary))]'
                : 'bg-gray-300 hover:bg-gray-400'
                }`}
              aria-label={`Go to slide ${index + 1}`}
              title={`Go to slide ${index + 1}`}
            />
          ))}
        </div>
      )}
    </div>
  )
}
