from fastapi import APIRouter, Depends

from app.schemes import BonusAccrualResponse, BonusAccrualSearchParameters
from app.services import BonusAccrualService

router = APIRouter(tags=['BonusAccrual'])


@router.post('/calculate-bonus/', response_model=BonusAccrualResponse)
async def get_wildberries_products(
    search_params: BonusAccrualSearchParameters,
    bonus_accrual_service: BonusAccrualService = Depends(),
):
    return await bonus_accrual_service.calculate_bonus(
        search_params=search_params,
    )
