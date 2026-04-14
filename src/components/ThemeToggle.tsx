import { useEffect, useState } from "react";
import { SunIcon, MoonIcon, MonitorIcon } from "@phosphor-icons/react";

type Theme = "light" | "dark" | "system";

const STORAGE_KEY = "theme";

function applyTheme(theme: Theme) {
  const root = document.documentElement;
  const isDark =
    theme === "dark" ||
    (theme === "system" &&
      window.matchMedia("(prefers-color-scheme: dark)").matches);
  root.classList.toggle("dark", isDark);
}

export default function ThemeToggle() {
  const [theme, setTheme] = useState<Theme>("system");

  useEffect(() => {
    const stored = (localStorage.getItem(STORAGE_KEY) as Theme | null) ?? "system";
    setTheme(stored);
  }, []);

  useEffect(() => {
    const media = window.matchMedia("(prefers-color-scheme: dark)");
    const onChange = () => {
      if ((localStorage.getItem(STORAGE_KEY) as Theme | null) === "system" || !localStorage.getItem(STORAGE_KEY)) {
        applyTheme("system");
      }
    };
    media.addEventListener("change", onChange);
    return () => media.removeEventListener("change", onChange);
  }, []);

  const select = (next: Theme) => {
    setTheme(next);
    if (next === "system") {
      localStorage.removeItem(STORAGE_KEY);
    } else {
      localStorage.setItem(STORAGE_KEY, next);
    }
    applyTheme(next);
  };

  const options: { value: Theme; label: string; Icon: typeof SunIcon }[] = [
    { value: "light", label: "淺色", Icon: SunIcon },
    { value: "system", label: "系統", Icon: MonitorIcon },
    { value: "dark", label: "深色", Icon: MoonIcon },
  ];

  return (
    <div
      role="radiogroup"
      aria-label="主題切換"
      className="inline-flex items-center gap-0.5 rounded-full border border-border bg-muted p-0.5"
    >
      {options.map(({ value, label, Icon }) => {
        const active = theme === value;
        return (
          <button
            key={value}
            type="button"
            role="radio"
            aria-checked={active}
            aria-label={label}
            title={label}
            onClick={() => select(value)}
            className={`flex size-8 items-center justify-center rounded-full transition-colors cursor-pointer ${
              active
                ? "bg-background text-foreground shadow-sm"
                : "text-muted-foreground hover:text-foreground"
            }`}
          >
            <Icon className="size-4" weight={active ? "fill" : "regular"} />
          </button>
        );
      })}
    </div>
  );
}
