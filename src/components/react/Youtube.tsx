interface YoutubeProps {
  embedUrl: string
  title?: string
}

export function Youtube({ embedUrl, title = "YouTube video player" }: YoutubeProps) {
  return (
    <div className="relative w-full overflow-hidden" style={{ paddingBottom: '56.25%' }}>
      <iframe
        className="absolute top-0 left-0 w-full h-full"
        src={embedUrl}
        title={title}
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      />
    </div>
  )
}
