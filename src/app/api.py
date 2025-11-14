from fastapi import FastAPI
from routes import validar, gerar

app = FastAPI(
    title='API de verificação e Geração de senhas',
    description='',
    version='0.1.0'
)

app.include_router(validar.router, prefix='/api')
app.include_router(gerar.router, prefix="/api")

@app.get('/')
async def root():
    return {
        "message" : "caminho raiz"
    }