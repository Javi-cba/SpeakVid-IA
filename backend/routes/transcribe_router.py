from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from services.download_service import download_video

router = APIRouter()

@router.get("/get")
async def get_transcribe():
    try:
        
        response = download_video('https://www.youtube.com/watch?v=M2VT32Wnppw')

        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
