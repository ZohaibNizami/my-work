from fastapi import APIRouter, HTTPException


router= APIRouter()

@router.get("/health")
async def health():
    return {"status": "OK"}


@router.get("/health/ready")
async def health_ready():
    return {"status": "OK"}


