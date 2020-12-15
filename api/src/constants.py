import numpy as np
from datetime import datetime, timedelta

NA = float(np.nan)

FILTERS = {
    "chart_type": [
        "regional",
        "viral"
    ],
    "period": [
        "daily",
        "weekly"
    ],
    "region": [
        "global",
        "us",
        "gb",
        "ar",
        "at",
        "au",
        "be",
        "bg",
        "bo",
        "br",
        "ca",
        "ch",
        "cl",
        "co",
        "cr",
        "cz",
        "de",
        "dk",
        "do",
        "ec",
        "ee",
        "es",
        "fi",
        "fr",
        "gr",
        "gt",
        "hk",
        "hn",
        "hu",
        "id",
        "ie",
        "il",
        "in",
        "is",
        "it",
        "jp",
        "lt",
        "lv",
        "mx",
        "my",
        "ni",
        "nl",
        "no",
        "nz",
        "pa",
        "pe",
        "ph",
        "pl",
        "pt",
        "py",
        "ro",
        "ru",
        "se",
        "sg",
        "sk",
        "sv",
        "th",
        "tr",
        "tw",
        "ua",
        "uy",
        "vn",
        "za"
    ]
}

START_DAILY = datetime(2017, 1, 1)
START_WEEKLY = datetime(2017, 1, 5)
END_DATE = datetime.combine(datetime.today().date(), datetime.min.time()) - timedelta(days=1)