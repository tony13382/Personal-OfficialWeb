import type { CollectionEntry } from "astro:content";
import { JobDescription } from "@/components/jobs/JobDescription";
import { Badge } from "../ui/badge";

type JobData = CollectionEntry<"jobs">;

interface JobsFallProps {
  jobs: JobData[];
  themes: Record<string, { primary: string; secondary: string }>;
}

const formatDate = (date: Date | null | undefined) => {
  if (!date) return null;
  return date.toLocaleDateString("zh-TW", {
    year: "numeric",
    month: "2-digit",
  });
};

export function JobsFall({ jobs, themes }: JobsFallProps) {
  return (
    <div className="grid grid-cols-1 gap-4">
      {jobs.map((job) => {
        const themeColors = themes[job.data.theme];
        const startDateStr = formatDate(job.data.startDate);
        const endDateStr = job.data.endDate
          ? formatDate(job.data.endDate)
          : "現在";
        const timeStr =
          startDateStr && endDateStr
            ? `${startDateStr} ~ ${endDateStr}`
            : startDateStr || endDateStr || "---";

        return (
          <a
            key={job.slug}
            href={`/jobs/${job.slug}/`}
            className="group flex bg-white rounded-lg border border-muted-background overflow-hidden hover:shadow-xl transition-all duration-300 hover:-translate-y-1"
          >
            <div className="flex-3 flex flex-col p-5 pb-3 gap-4">
              <div className="flex gap-3">
                {job.data.logo && (
                  <div className="flex-shrink-0">
                    <img
                      src={job.data.logo}
                      alt=""
                      className="size-12 mt-0.5 rounded-lg"
                    />
                  </div>
                )}
                <div className="flex-1 grid gap-1 items-center">
                  <div className="flex flex-col md:flex-row justify-left md:items-center gap-1">
                    <p
                      className="text-lg font-bold group-hover:text-opacity-80 transition-colors line-clamp-2"
                    >
                      {job.data.company}
                      {job.data.location && (
                        <span className="text-md font-normal text-muted-foreground">
                          ．{job.data.location}
                        </span>)}
                    </p>

                  </div>
                  <div className="flex flex-col md:flex-row justify-left md:items-center gap-1">
                    <p>
                      {job.data.title}
                      <span className="text-sm font-normal text-muted-foreground">
                        ．{timeStr}
                      </span>
                    </p>
                  </div>
                </div>
              </div>

              {job.data.description && job.data.description.length > 0 && (
                <div className="border-t pt-4">
                  <JobDescription descriptions={job.data.description} />
                </div>
              )}

              {job.data.tags.length > 0 && (<div className="flex gap-2 pb-2">
                {job.data.tags.map((tag: string) => (
                  <Badge key={tag} variant="outline" className="text-xs">
                    {tag}
                  </Badge>
                ))}
              </div>)}
            </div>
          </a>
        );
      })}
    </div>
  );
}
