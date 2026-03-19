"""Weatherly configuration module.

Provides API configuration constants and a Config dataclass for
customizing weather data requests.
"""

from dataclasses import dataclass

API_BASE_URL: str = 'https://wttr.in'
DEFAULT_FORMAT: str = 'j1'
DEFAULT_UNITS: str = 'metric'
REQUEST_TIMEOUT: int = 10


@dataclass
class Config:
    """Configuration for weather data requests."""

    location: str = ''
    units: str = DEFAULT_UNITS
    format: str = DEFAULT_FORMAT
