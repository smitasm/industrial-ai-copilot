from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PDF_PATH = PROJECT_ROOT / "data" / "manuals" / "nasa_handbook.pdf"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150