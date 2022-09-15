#Импортируем все зависимости, которые описываются в FastAPI
import uvicorn
from fastapi import  FastAPI
#Запускаем локальный хост
if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8000, reload = True, log_level="info")
    server = uvicorn.Server(config)
    server.run()
##Прописываем путь к главной странице
app = FastAPI()
@app.get("/")
async def home():
    return ("Наша главная страница"}