from database import Base, engine
import models

# Baza modellari yaratiladi
Base.metadata.create_all(bind=engine)
