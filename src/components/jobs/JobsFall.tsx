import type { CollectionEntry } from "astro:content";
import { JobDescription } from "@/components/jobs/JobDescription";

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
            className="group flex bg-white rounded-lg border border-gray-200 overflow-hidden hover:shadow-xl transition-all duration-300 hover:-translate-y-1"
          >
            <div className="flex-3 flex flex-col p-5 pb-3">
              <div className="flex gap-3 mb-3">
                {job.data.logo && (
                  <div className="flex-shrink-0">
                    <img
                      src={job.data.logo}
                      alt=""
                      className="size-16 mt-0.5 rounded-lg"
                    />
                  </div>
                )}
                <div className="flex-1 grid gap-2">
                  <h3
                    className="text-xl font-bold group-hover:text-opacity-80 transition-colors line-clamp-2"
                    style={{ color: themeColors.primary }}
                  >
                    {job.data.title}
                  </h3>
                  <p
                    className="text-sm font-semibold text-foreground"
                    dangerouslySetInnerHTML={{ __html: job.data.company }}
                  />
                  <p className="text-xs text-muted-foreground">{timeStr}</p>
                </div>
              </div>

              {job.data.description && job.data.description.length > 0 && (
                <div className="pt-4 border-t">
                  <JobDescription descriptions={job.data.description} />
                </div>
              )}
            </div>
          </a>
        );
      })}
    </div>
  );
}
