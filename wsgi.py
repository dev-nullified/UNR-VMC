"""App entry point."""
from app import create_app
from pathlib import Path  # python3 only
from dotenv import load_dotenv
import os



# LOAD ENV FILE
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


app = create_app()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)