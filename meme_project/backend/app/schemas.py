from pydantic import BaseModel

class MemeBase(BaseModel):
    text: str

    class Config:
        from_attributes = True

class MemeCreate(MemeBase):
    pass

    class Config:
        from_attributes = True
class MemeUpdate(MemeBase):
    pass

    class Config:
        from_attributes = True
class Meme(MemeBase):
    id: int
    image_url: str

    class Config:
        from_attributes = True
    class Config:
        from_attributes = True
