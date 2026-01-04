/**
 * HtmlCarousel - Generic carousel for any HTML content
 * React version of Python HtmlCarousel component
 * Features: autoplay, dot indicators, navigation buttons
 */
import { useState, useCallback, useEffect } from 'react'
import useEmblaCarousel from 'embla-carousel-react'
import Autoplay from 'embla-carousel-autoplay'
import { CaretLeft, CaretRight } from '@phosphor-icons/react'
import type { ReactNode } from 'react'

interface HtmlCarouselProps {
  blocks: ReactNode[]
  autoplaySpeed?: number
  className?: string
}

export function HtmlCarousel({
  blocks,
  autoplaySpeed = 3000,
  className = ''
}: HtmlCarouselProps) {
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
    <div className={`mt-3 mb-5 ${className}`}>
      {/* Carousel viewport */}
      <div className="relative">
        <div className="overflow-hidden" ref={emblaRef}>
          <div className="flex">
            {blocks.map((block, index) => (
              <div key={index} className="flex-[0_0_100%] min-w-0">
                {block}
              </div>
            ))}
          </div>
        </div>

        {/* Navigation buttons */}
        {blocks.length > 1 && (
          <>
            <button
              onClick={scrollPrev}
              disabled={!canScrollPrev}
              className="absolute left-2 top-1/2 -translate-y-1/2 bg-white/80 hover:bg-white disabled:opacity-30 rounded-full p-2 shadow-lg transition-all z-10"
              aria-label="Previous slide"
              title="Previous slide"
            >
              <CaretLeft className="w-6 h-6" />
            </button>
            <button
              onClick={scrollNext}
              disabled={!canScrollNext}
              className="absolute right-2 top-1/2 -translate-y-1/2 bg-white/80 hover:bg-white disabled:opacity-30 rounded-full p-2 shadow-lg transition-all z-10"
              aria-label="Next slide"
              title="Next slide"
            >
              <CaretRight className="w-6 h-6" />
            </button>
          </>
        )}
      </div>

      {/* Dot indicators */}
      {blocks.length > 1 && (
        <div className="flex justify-center gap-2 mt-4">
          {blocks.map((_, index) => (
            <button
              key={index}
              onClick={() => scrollTo(index)}
              className={`w-3 h-3 rounded-full transition-all ${
                index === selectedIndex
                  ? 'bg-[var(--theme-primary,var(--color-primary))] scale-125'
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
