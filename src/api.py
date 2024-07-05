import fastapi as api
from fastapi import FastAPI, File,Request, UploadFile
from fastapi.responses import FileResponse

from typing import Union
from pydantic import BaseModel

from PIL import Image
import io

import uuid

IMAGEDIR = "upload/"


app = FastAPI()

class img(BaseModel):
    data: str

@app.get("/")
def page():
    return {"message": "Hello World"}

@app.post("/files/")
async def create_file(file: bytes = File()):
    
    # Convert the byte string to bytes
    byte_data = bytes(file)

    # # Use BytesIO to handle the byte data
    byte_io = io.BytesIO(byte_data)

    print(byte_io)

    # image = Image.open(byte_io)
    
    with open('output_image.raw', 'wb') as file:
        file.write(byte_data)
    
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # open("./", "wb").write(file)
    print(file)
    return {"filename": file.filename}



 
@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
 
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    
    byte_data = bytes(contents)
        # # Use BytesIO to handle the byte data
    # byte_io = io.BytesIO(byte_data)
 
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(byte_data)
    print(f"{IMAGEDIR}{file.filename}")
 
    return FileResponse(f"{IMAGEDIR}{file.filename}")
 
 
@app.get("/show/")
async def read_random_file():
 
    # # get random file from the image directory
    # files = os.listdir(IMAGEDIR)
    # random_index = randint(0, len(files) - 1)
 
    path = f"./upload/1f17d302-ac21-4f27-9299-2b49e3c43d5d.jpg"
     
    return FileResponse(path)

@app.get("/p")
async def print_request(request: Request):
    # Print the request method
    print("Request method:", request.method)
    
    # Print the request URL
    print("Request URL:", request.url)
    
    # Print the request headers
    print("Request headers:", request.headers)
    
    # Print the request query parameters
    query_params = request.query_params
    print("Query parameters:", query_params)
    
    # Print the request body (if any)
    body = await request.body()
    print("Request body:", body.decode('utf-8'))
    
    return {"message": "Request details printed in the console"}



# @app.post("/predict/")
# async def read_item(txt: mail = None ):
   
#     pred = int(user.predict(txt.data))
#     proba= float(user.predict_proba(txt.data)[1])
   
#     return {"predction": pred, "probability of spam": "{:.2f}".format(proba) }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)