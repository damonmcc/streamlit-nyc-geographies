import sys
from pathlib import Path

_repo_root = Path(__file__).resolve().parent

# Make all modules available
sys.path.append(str(_repo_root))