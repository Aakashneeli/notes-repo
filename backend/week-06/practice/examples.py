"""Completed small teaching mechanisms; not a finished ingestion backend."""
import secrets
from fastapi import FastAPI, BackgroundTasks, Depends, HTTPException
from fastapi.security import APIKeyHeader

def matches(provided, expected):
    return bool(provided and expected) and secrets.compare_digest(provided.encode(), expected.encode())

def bounded(chunks, limit):
    data = bytearray()
    for chunk in chunks:
        if len(data) + len(chunk) > limit:
            raise ValueError("too_large")
        data.extend(chunk)
    return bytes(data)

ALLOWED = {"pending": {"running"}, "running": {"completed", "failed", "retrying"},
           "retrying": {"pending"}, "completed": set(), "failed": set()}
def can_move(old, new):
    return new in ALLOWED.get(old, set())

def demo_app(events):
    app = FastAPI()
    key = APIKeyHeader(name="X-API-Key", auto_error=False)
    def authorized(value=Depends(key)):
        if not matches(value, "demo-only"):
            raise HTTPException(401, "Invalid API key")
    def record(value):
        events.append(value)
    @app.post("/receipts", status_code=202, dependencies=[Depends(authorized)])
    def receipt(tasks: BackgroundTasks):
        events.append("handler")
        tasks.add_task(record, "after-response")
        return {"accepted": True}
    return app

if __name__ == "__main__":
    print(bounded([b"ab", b"cd"], 4))
    print(can_move("pending", "running"), can_move("completed", "running"))


def preview_app():
    """Completed multipart mechanism only: no persistence, auth or jobs."""
    from fastapi import UploadFile
    app = FastAPI()
    @app.post('/preview')
    async def preview(file: UploadFile):
        try:
            data = await file.read(5)  # tiny demonstration: limit 4 plus one
            if len(data) > 4:
                raise HTTPException(413, 'too_large')
            return {'name': file.filename, 'bytes': len(data)}
        finally:
            await file.close()
    return app
