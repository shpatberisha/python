fom pydantic import BaseModel

class MoivieCretae(BaseModel):
    title: str
    director: str

class Movie(MoivieCreate):
    id:int