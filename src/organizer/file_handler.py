import os
from pathlib import Path

home_dir = Path.home()
downloadPath = Path(home_dir / "Downloads")

documents = downloadPath.rglob('*.pdf')
