import json
import os

from app.schemes import BonusAccrualResponse, BonusAccrualRule, BonusAccrualSearchParameters


class BonusAccrualService:
    def __init__(self):
        self.rules = []

    async def calculate_bonus(
        self,
        search_params: BonusAccrualSearchParameters,
    ) -> BonusAccrualResponse:
        transaction_amount = search_params.transaction_amount
        timestamp = search_params.timestamp
        customer_status = search_params.customer_status

        rules = await self.__load_rules()
        rules.sort(key=lambda rule: rule.get('order', 0))
        base_bonus = self.__calculate_base_bonus(transaction_amount)

        applied_rules = []
        total_bonus = base_bonus

        applied_rules.append(BonusAccrualRule(rule='base_rate', bonus=base_bonus))

        for rule in rules:
            bonus_before = total_bonus
            total_bonus = await self.__apply_rule(total_bonus, rule, timestamp, customer_status)
            bonus_applied = total_bonus - bonus_before
            if bonus_applied > 0:
                applied_rules.append(BonusAccrualRule(rule=rule['type'], bonus=bonus_applied))

        return BonusAccrualResponse(total_bonus=total_bonus, applied_rules=applied_rules)

    @staticmethod
    async def __load_rules():
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        rules_path = os.path.join(current_dir, "rules.json")
        with open(rules_path) as file:
            return json.load(file)

    @staticmethod
    def __calculate_base_bonus(amount):
        return amount // 10

    async def __apply_rule(self, current_bonus, rule, timestamp, customer_status):
        rule_type = rule['type']
        if hasattr(self, rule_type):
            return await getattr(self, rule_type)(current_bonus, rule, timestamp, customer_status)
        return current_bonus

    async def weekend_bonus(self, current_bonus, rule, timestamp, customer_status):
        if self.__is_weekend(timestamp):
            return current_bonus * rule['multiplier']
        return current_bonus

    @staticmethod
    async def vip_bonus(current_bonus, rule, timestamp, customer_status):
        if customer_status == 'vip':
            return current_bonus * (1 + rule['percentage'] / 100)
        return current_bonus

    @staticmethod
    def __is_weekend(timestamp):
        return timestamp.weekday() in (5, 6)
