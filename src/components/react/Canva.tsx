interface CanvaProps {
  src: string
  title?: string
}

export function Canva({ src, title = "Canva presentation" }: CanvaProps) {
  // 如果最後是 /view 則填充成 /view?embed，如果最後是 /view?embed 則不修改
  const embedSrc = src.endsWith("/view") ? `${src}?embed` : src

  return (
    <div
      style={{
        position: "relative",
        width: "100%",
        height: 0,
        paddingTop: "56.25%", // 16:9 aspect ratio
        paddingBottom: 0,
        overflow: "hidden",
        willChange: "transform",
      }}
    >
      <iframe
        loading="lazy"
        style={{
          position: "absolute",
          width: "calc(100% + 4px)",
          height: "calc(100% + 2px)",
          top: "-1px",
          left: "-2px",
          border: "none",
          padding: 0,
          margin: 0,
        }}
        src={embedSrc}
        allowFullScreen
        allow="fullscreen"
        title={title}
      />
    </div>
  )
}
