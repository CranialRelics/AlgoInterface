from pydantic import BaseModel, field_validator


FORMATS = ["json", "xml", "csv"]
EXPECTED_LENGTHS = [4, 2, 2]


class ChartRequest(BaseModel):
    database_code: str = "WIKI"
    ticker: str  # labeled "dataset_code on nasdaq site"
    fmt: str = "json"
    start_date: str  # 2014-01-01
    end_date: str  # ToDo: make these proper date fmt
    frequency: str
    timeframe: str

    @field_validator("fmt")
    def name_must_contain_space(cls, v):
        if v not in FORMATS:
            raise ValueError(f"must be one of {FORMATS}")
        return v

    @field_validator("start_date", "end_date")
    def yyyy_mm_dd(cls, v):
        if len(v) != 10:
            raise ValueError(f"Date must be in yyyy-mm-dd format")
        if v.count("-") != 3:
            raise ValueError(
                f"Date must be in yyyy-mm-dd format. You have {v.count('-')} occurences"
            )

        if EXPECTED_LENGTHS != [len(i) for i in v.split("-")]:
            raise ValueError(f"Date must be in yyyy-mm-dd format. You have entered {v}")

        return v
