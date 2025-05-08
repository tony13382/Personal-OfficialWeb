from app.builder.basic import WebBuilder
from app.pages.job.y2024_SolwenAi import page as y2024_SolwenAi
from app.pages.job.y2023_Tiic import page as y2023_Tiic
from app.pages.job.y2022_NthuOu import page as y2022_NthuOu
from app.pages.job.y2023_NthuIr import page as y2023_NthuIr
from app.pages.job.y2022_Songla import page as y2022_Songla
from app.pages.job.y2019_CycuEdu import page as y2019_CycuEdu

jobBuilder = WebBuilder("jobs/")

jobBuilder.addPages(
    [
        y2024_SolwenAi,
        y2023_Tiic,
        y2023_NthuIr,
        y2022_NthuOu,
        y2022_Songla,
        y2019_CycuEdu,
    ]
)
