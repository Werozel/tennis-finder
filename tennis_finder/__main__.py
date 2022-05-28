"""Run the tennis_finder package."""
import os

from tennis_finder.main import run_app


if __name__ == "__main__":
    if "config.py" not in os.listdir("tennis_finder"):
        import tennis_finder.create_config as cf
        cf.generate_secure_random_string(10)

    run_app()
