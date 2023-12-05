import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from api import views

app = FastAPI(
    docs_url='/docs',
    openapi_url='/docs.json',
    default_response_class=ORJSONResponse,
)

app.include_router(views.router, prefix='')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
