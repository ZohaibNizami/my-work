from fastapi import APIRouter, HTTPException


router= APIRouter()

@router.get("/health")
async def health():
    return {"status": "OK"}
