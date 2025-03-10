from fastapi import APIRouter

from app.routers.bonus_accrual import router as bonus_accrual_router

from app.settings import settings

router = APIRouter(prefix='/api/v1', include_in_schema=settings.DEVELOP)
router.include_router(bonus_accrual_router)
