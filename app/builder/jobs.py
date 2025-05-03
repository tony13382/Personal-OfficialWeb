from app.builder.basic import WebBuilder
from app.pages.job import (
    y2022_Songla,
    y2023_NthuOu,
    y2023_NthuIr,
    y2023_Tiic,
    y2024_SolwenAi,
)

jobBuilder = WebBuilder("jobs/")


jobBuilder.addPages(
    [
        y2024_SolwenAi.page,
        y2023_Tiic.page,
        y2023_NthuIr.page,
        y2023_NthuOu.page,
        y2022_Songla.page,
    ]
)
