from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field


class BonusAccrualSearchParameters(BaseModel):
    transaction_amount: int = Field(
        description='Сумма покупки',
        examples=[150],
    )
    timestamp: datetime = Field(
        description='Дата покупки',
        examples=['2025-03-08T12:00:00'],
    )
    customer_status: Literal['vip', 'customer'] = Field(
        description='Статус',
        examples=['vip', 'customer'],
    )


class BonusAccrualRule(BaseModel):
    rule: str = Field(
        description='Название правила начисления бонусов',
        examples=['base_rate', 'holiday_bonus', 'vip_boost'],
    )
    bonus: int = Field(
        description='Количество бонусов, начисленных по данному правилу',
        examples=[15],
    )


class BonusAccrualResponse(BaseModel):
    total_bonus: int = Field(
        description='Количество начисленных бонусов',
        examples=[50],
    )
    applied_rules: list[BonusAccrualRule] = Field(
        description='Какие правила были применены',
    )
