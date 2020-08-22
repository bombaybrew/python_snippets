from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="web/")

@app.get("/test")
async def test():
    return 'Ok Computer!'

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", context={'request': request})

@app.get("/auth")
async def auth(request: Request):
    scopes = 'user-read-email'
    client_id = 'dc7da18389194e0b95da32a828891d7a'
    redirect_uri = "https://myserver.com/auth/callback"
    spotify_auth_url = 'https://accounts.spotify.com/authorize?response_type=code&client_id=' \
    + client_id + '&scope=' + scopes \
    + '&redirect_uri=' + redirect_uri

    return RedirectResponse(url=spotify_auth_url)

@app.get("/auth/callback")
async def authCallback(request: Request):
    # TODO
    # Once this is hosted to the server. Spotify server will try to call this method.
    # Parse the token and proceed with your future request.
    return 0

if __name__ == '__main__':
    uvicorn.run("auth_spotify:app", host='0.0.0.0', port=9200, reload=True)