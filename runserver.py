import os

os.system("uvicorn app.api:app --app-dir src --reload")