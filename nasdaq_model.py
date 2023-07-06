from pydantic import BaseModel, field_validator


FORMATS = ["json", "xml", "csv"]


class ChartRequest(BaseModel):
    ticker: str
    fmt: str = "json"
    frequency: str
    timeframe: str

    @field_validator("fmt")
    def name_must_contain_space(cls, v):
        if v not in FORMATS:
            raise ValueError(f"must be one of {FORMATS}")
        return v
