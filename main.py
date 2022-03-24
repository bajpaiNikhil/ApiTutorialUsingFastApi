from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(content={"error":"Z can not be zero"} , status_code=400)
        # return fastapi.Response(content='{"error":"Error: Z CANT BE ZERO"}',
        #                         media_type="application/json", status_code=400)
    if z is not None:
        value = z * (x + y)
    else:
        value = (x + y)

    return {
        "x": x,
        "y": y,
        "z": z,
        "value": value
    }


if __name__ == '__main__':
    uvicorn.run(api)
