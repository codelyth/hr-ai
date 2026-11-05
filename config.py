from pathlib import Path
from dotenv import load_dotenv

# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# Project directories
DATA_DIR = BASE_DIR / "data"
AUDIO_DIR = BASE_DIR / "audio"
VISION_DIR = BASE_DIR / "vision"

# Create local data directory if missing
DATA_DIR.mkdir(exist_ok=True)