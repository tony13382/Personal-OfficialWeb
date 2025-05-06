from app.builder.basic import WebBuilder
from app.pages.job.y2022_Songla import page as y2022_Songla
from app.pages.job.y2023_NthuOu import page as y2023_NthuOu
from app.pages.job.y2023_NthuIr import page as y2023_NthuIr
from app.pages.job.y2023_Tiic import page as y2023_Tiic
from app.pages.job.y2024_SolwenAi import page as y2024_SolwenAi

jobBuilder = WebBuilder("jobs/")

jobBuilder.addPages(
    [
        y2024_SolwenAi,
        y2023_Tiic,
        y2023_NthuIr,
        y2023_NthuOu,
        y2022_Songla,
    ]
)
