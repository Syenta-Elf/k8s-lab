from fastapi import FastAPI
import socket
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from k8s-lab!"}


@app.get("/health")
def get_health():
    return {"message": "Health page"}

@app.get("/info")
def get_page():
    return {
        "hostname": socket.gethostname(),
        "version": "1.0.0"
    }