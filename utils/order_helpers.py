from datetime import datetime, timedelta

from order_data import OrderData


def get_order_date(days_ahead: int = 1, fmt: str = "%d.%m.%Y") -> str:
    """Дата заказа: текущая + N дней."""
    return (datetime.now() + timedelta(days=days_ahead)).strftime(fmt)



def create_order_data(
    first_name: str = "Никита",
    last_name: str = "Тест",
    address: str = "Улица Пушкина",
    station_index: int = 1,
    phone_number: str = "89013676214",
    days_ahead: int = 1,
    period_index: int = 3,
    comments: str = "Нет комментов.",
) -> OrderData:
    """Фабрика тестовых данных для заказа."""
    return OrderData(
        first_name=first_name,
        last_name=last_name,
        address=address,
        station_index=station_index,
        phone_number=phone_number,
        date_order=get_order_date(days_ahead),
        period_index=period_index,
        comments=comments,
    )