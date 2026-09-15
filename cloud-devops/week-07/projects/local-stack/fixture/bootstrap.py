"""Run as `python -m fixture.bootstrap` before the API accepts uploads."""
from .core import initialize

if __name__ == "__main__":
    initialize()
    print("fixture schema ready")
