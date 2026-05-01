from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def deploy():
    return {'message':'FastAPI is Deploy'}
