"""Local loopback server; fails intentionally until learner implements create_app."""
from bridge import FixtureRag
from workflow import create_app
import uvicorn

if __name__ == '__main__':
    uvicorn.run(create_app(FixtureRag()), host='127.0.0.1', port=8009)
