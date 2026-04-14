import { useState, useEffect, useRef, useCallback, useMemo } from "react";
import * as Dialog from "@radix-ui/react-dialog";
import { MagnifyingGlass, X, ArrowRight } from "@phosphor-icons/react";

interface SearchResult {
  url: string;
  meta?: { title?: string; image?: string; type?: string };
  excerpt?: string;
}

interface Pagefind {
  debouncedSearch: (
    query: string
  ) => Promise<{ results: { data: () => Promise<SearchResult> }[] } | null>;
}

const TYPE_ORDER = ["文章", "專案", "經歷"];

function resolveType(result: SearchResult): string {
  const url = result.url || "";
  if (url.startsWith("/articles/")) return "文章";
  if (url.startsWith("/projects/")) return "專案";
  if (url.startsWith("/jobs/")) return "經歷";
  if (url.startsWith("/apps/")) return "APP";
  return "其他";
}

export function SearchDialog() {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [activeIndex, setActiveIndex] = useState(-1);
  const pagefindRef = useRef<Pagefind | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const listRef = useRef<HTMLUListElement>(null);

  // Group results by type (based on URL path)
  const grouped = useMemo(() => {
    const groups: { type: string; items: SearchResult[] }[] = [];
    const map = new Map<string, SearchResult[]>();

    for (const r of results) {
      const type = resolveType(r);
      if (!map.has(type)) map.set(type, []);
      map.get(type)!.push(r);
    }

    // Sort by defined order
    const sorted = [...map.entries()].sort(([a], [b]) => {
      const ia = TYPE_ORDER.indexOf(a);
      const ib = TYPE_ORDER.indexOf(b);
      return (ia === -1 ? 99 : ia) - (ib === -1 ? 99 : ib);
    });

    for (const [type, items] of sorted) {
      groups.push({ type, items });
    }

    return groups;
  }, [results]);

  // Flat list for keyboard navigation
  const flatResults = useMemo(() => {
    return grouped.flatMap((g) => g.items);
  }, [grouped]);

  // Load pagefind on first open
  useEffect(() => {
    if (!open) return;
    async function load() {
      if (!pagefindRef.current) {
        try {
          const path = "/pagefind/pagefind.js";
          pagefindRef.current = await import(/* @vite-ignore */ path);
        } catch {
          // Index not available (dev mode without prior build)
        }
      }
    }
    load();
  }, [open]);

  // Search on query change
  useEffect(() => {
    if (!query.trim()) {
      setResults([]);
      setLoading(false);
      return;
    }

    let cancelled = false;
    setLoading(true);

    async function search() {
      if (!pagefindRef.current) return;
      const response = await pagefindRef.current.debouncedSearch(query);
      if (cancelled) return;
      if (response) {
        const data = await Promise.all(
          response.results.slice(0, 12).map((r) => r.data())
        );
        if (!cancelled) {
          setResults(data);
          setActiveIndex(-1);
        }
      }
      if (!cancelled) setLoading(false);
    }

    search();
    return () => {
      cancelled = true;
    };
  }, [query]);

  // Keyboard shortcut: Cmd/Ctrl + K
  useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault();
        setOpen((prev) => !prev);
      }
    }
    document.addEventListener("keydown", onKeyDown);
    return () => document.removeEventListener("keydown", onKeyDown);
  }, []);

  // Scroll active item into view
  useEffect(() => {
    if (activeIndex >= 0 && listRef.current) {
      const items = listRef.current.querySelectorAll("[data-search-item]");
      const item = items[activeIndex] as HTMLElement;
      item?.scrollIntoView({ block: "nearest" });
    }
  }, [activeIndex]);

  const handleOpenChange = useCallback((value: boolean) => {
    setOpen(value);
    if (!value) {
      setQuery("");
      setResults([]);
    }
  }, []);

  return (
    <Dialog.Root open={open} onOpenChange={handleOpenChange}>
      <Dialog.Trigger asChild>
        <button
          className="flex items-center gap-2 px-3 py-2 text-muted-foreground rounded-full transition-all hover:bg-muted cursor-pointer bg-transparent border-0"
          aria-label="搜尋"
          title="搜尋"
        >
          <MagnifyingGlass className="size-5" />
          <span className="hidden md:inline text-sm">搜尋</span>
          <kbd className="hidden md:inline-flex items-center gap-0.5 px-1.5 py-0.5 text-[10px] font-mono text-muted-foreground bg-muted border border-border rounded-full">
            ⌘ K
          </kbd>
        </button>
      </Dialog.Trigger>

      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 z-50 bg-black/50 backdrop-blur-sm animate-[fade-in_150ms]" />
        <Dialog.Content className="fixed z-50 top-[15vh] inset-x-0 mx-auto w-[calc(100%-2rem)] max-w-lg bg-background rounded-2xl shadow-2xl overflow-hidden animate-[slide-up_200ms_ease-out]">
          <Dialog.Title className="sr-only">搜尋</Dialog.Title>

          {/* Search Input */}
          <div className="flex items-center gap-3 px-4 border-b">
            <MagnifyingGlass className="size-5 text-muted-foreground flex-shrink-0" />
            <input
              ref={inputRef}
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "ArrowDown") {
                  e.preventDefault();
                  setActiveIndex((prev) =>
                    prev < flatResults.length - 1 ? prev + 1 : 0
                  );
                } else if (e.key === "ArrowUp") {
                  e.preventDefault();
                  setActiveIndex((prev) =>
                    prev > 0 ? prev - 1 : flatResults.length - 1
                  );
                } else if (e.key === "Enter" && !e.nativeEvent.isComposing && activeIndex >= 0 && flatResults[activeIndex]) {
                  e.preventDefault();
                  handleOpenChange(false);
                  window.location.href = flatResults[activeIndex].url;
                }
              }}
              placeholder="搜尋全站內容..."
              className="flex-1 py-4 text-base bg-transparent border-0 outline-none placeholder:text-muted-foreground"
              autoFocus
            />
            {query && (
              <button
                onClick={() => {
                  setQuery("");
                  inputRef.current?.focus();
                }}
                className="p-1 text-muted-foreground hover:text-foreground cursor-pointer bg-transparent border-0"
              >
                <X className="size-4" />
              </button>
            )}
          </div>

          {/* Results */}
          <div className="max-h-[50vh] overflow-y-auto">
            {!query.trim() && (
              <div className="px-4 py-8 text-center text-sm text-muted-foreground">
                輸入關鍵字搜尋全站內容
              </div>
            )}

            {query.trim() && loading && (
              <div className="px-4 py-8 text-center text-sm text-muted-foreground">
                搜尋中...
              </div>
            )}

            {query.trim() && !loading && results.length === 0 && (
              <div className="px-4 py-8 text-center text-sm text-muted-foreground">
                找不到相關結果
              </div>
            )}

            {grouped.length > 0 && (
              <ul ref={listRef} className="py-2 list-none !m-0 !p-0">
                {grouped.map((group) => {
                  return (
                    <li key={group.type} className="list-none">
                      <div className="px-4 pt-3 pb-1">
                        <span className="text-[11px] font-semibold uppercase tracking-wider text-muted-foreground">
                          {group.type}
                        </span>
                      </div>
                      {group.items.map((result) => {
                        const flatIdx = flatResults.indexOf(result);
                        return (
                          <a
                            key={result.url}
                            data-search-item
                            href={result.url}
                            className={`flex items-start gap-3 px-4 py-3 no-underline text-foreground transition-colors group ${activeIndex === flatIdx ? "bg-muted" : "hover:bg-muted/50"}`}
                            onClick={() => handleOpenChange(false)}
                            onMouseEnter={() => setActiveIndex(flatIdx)}
                          >
                            <div className="flex-1 min-w-0">
                              <p className="font-medium text-sm truncate">
                                {result.meta?.title || "無標題"}
                              </p>
                              {result.excerpt && (
                                <p
                                  className="text-xs text-muted-foreground mt-1 line-clamp-2 [&_mark]:bg-yellow-100 [&_mark]:text-yellow-900 dark:[&_mark]:bg-yellow-900/40 dark:[&_mark]:text-yellow-100 [&_mark]:rounded-sm [&_mark]:px-0.5"
                                  dangerouslySetInnerHTML={{
                                    __html: result.excerpt,
                                  }}
                                />
                              )}
                            </div>
                            <ArrowRight className="size-4 text-muted-foreground/50 group-hover:text-muted-foreground mt-0.5 flex-shrink-0 transition-colors" />
                          </a>
                        );
                      })}
                    </li>
                  );
                })}
              </ul>
            )}
          </div>

          {/* Footer */}
          <div className="flex items-center justify-between px-4 py-2 border-t text-[11px] text-muted-foreground bg-muted/50">
            <span className="flex items-center gap-2">
              <span>
                <kbd className="px-1 py-0.5 bg-muted border border-border rounded text-[10px] font-mono">
                  ESC
                </kbd>{" "}
                關閉
              </span>
              <span>
                <kbd className="px-1 py-0.5 bg-muted border border-border rounded text-[10px] font-mono">
                  ↑↓
                </kbd>{" "}
                選擇
              </span>
              <span>
                <kbd className="px-1 py-0.5 bg-muted border border-border rounded text-[10px] font-mono">
                  ↵
                </kbd>{" "}
                開啟
              </span>
            </span>
            <span>Pagefind</span>
          </div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
