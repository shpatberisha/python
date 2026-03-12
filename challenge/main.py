import uvicorn
from database import Base, engine
import models.recipe
import models.category
from app import app

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)