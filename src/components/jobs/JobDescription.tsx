import { parseTextWithHighlight } from "../react/Basic";

interface JobDescriptionProps {
  descriptions: string[];
}

export const JobDescription = ({ descriptions }: JobDescriptionProps) => {
  return (
    <div className="flex flex-col gap-3">
      {descriptions.map((desc, index) => (
        <p key={index} className="flex-1 text-foreground text-sm">
          {parseTextWithHighlight(desc || "")}
        </p>
      ))}
    </div>
  );
};
