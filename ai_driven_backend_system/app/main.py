from fastapi import Depends, FastAPI
from schemas import PromptQuery
from database import get_session, create_db_and_tables
from crud import createKeyValue, updateKeyValue, deleteKeyValue
from database import SessionDep

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World!"}

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/llm")
def parsePrompt(session: SessionDep):
    # promptDict = prompt.model_dump()

    action = "Insert"
    key = "1"
    value = "abcd"

    if action == "Insert":
        createKeyValue(key, value, session)
    elif action == "Update":
        updateKeyValue(key, value, session)
    elif action == "Delete":
        deleteKeyValue(key, session)

    action = "Update"
    key = "1"
    value = "efgh"

    if action == "Insert":
        createKeyValue(key, value, session)
    elif action == "Update":
        updateKeyValue(key, value, session)
    elif action == "Delete":
        deleteKeyValue(key, session)

    action = "Delete"
    key = "1"
    value = ""

    if action == "Insert":
        createKeyValue(key, value, session)
    elif action == "Update":
        updateKeyValue(key, value, session)
    elif action == "Delete":
        deleteKeyValue(key, session)

@app.get("/get-log-stats/{year}/{month}/{day}")
def log_stats(year: int, month: int, day: int):
    stats = {
        'Inserted': 0,
        'Updated': 0,
        'Deleted': 0
    }
    with open('myapp.log') as f:
        for log in f:
            log = log.strip()

            # Extract year (0 - 3)
            logYear = int(log[0: 4])

            # Extract month (5 - 6)
            logMonth = int(log[5: 7])

            # Extract day (8 - 10)
            logDay = int(log[8: 11])

            # Message of the log
            splitStrList = log.split("-")[-1].lstrip()

            op = splitStrList.split(" ")[0]

            # Process log if it only matches given query criteria
            if year == logYear and month == logMonth and day == logDay:
                stats[op] += 1

    return stats
