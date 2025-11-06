# orders_data.py
from typing import List, Dict, Any

Order = Dict[str, Any]
ORDERS: List[Order] = [
    {"id": 101, "total": 29.99, "created": "2025-01-15T09:30:00", "customer": {"first": "Ana", "last": "Zhang"}},
    {"id": 102, "total": 120.00, "created": "2025-01-14T16:10:00", "customer": {"first": "Ben", "last": "Adams"}},
    {"id": 103, "total": 120.00, "created": "2025-01-14T08:05:00", "customer": {"first": "Ben", "last": "Adams"}},
    {"id": 104, "total": 75.50, "created": "2025-01-13T12:00:00", "customer": {"first": "Cara", "last": "Lopez"}},
]

def sort_orders(ORDERS, sort_key, reverse_order=False):
    if sort_key == 'id':
        ORDERS.sort(key = lambda x: x['id'], reverse=reverse_order)

    elif sort_key == 'total':
        ORDERS.sort(key = lambda x: x['total'], reverse=reverse_order)

    elif sort_key == 'created':
        def create_list(date_string):
            date_list = []
            date_list.append(int(date_string[:4]))
            date_list.append(int(date_string[5:7]))
            date_list.append(int(date_string[8:10]))
            date_list.append(int(date_string[11:13]))
            date_list.append(int(date_string[14:16]))
            date_list.append(int(date_string[17:]))
            return date_list

        ORDERS.sort(key = lambda x: create_list(x['created']), reverse=reverse_order)

    elif sort_key == 'first':
        ORDERS.sort(key = lambda x: x['customer']['first'], reverse=reverse_order)

    elif sort_key == 'last':
        ORDERS.sort(key = lambda x: x['customer']['last'], reverse=reverse_order)

"""
sort_orders(ORDERS, 'total')
for item in ORDERS:
    print(item)

outputs:
{'id': 101, 'total': 29.99, 'created': '2025-01-15T09:30:00', 'customer': {'first': 'Ana', 'last': 'Zhang'}}
{'id': 104, 'total': 75.5, 'created': '2025-01-13T12:00:00', 'customer': {'first': 'Cara', 'last': 'Lopez'}}
{'id': 102, 'total': 120.0, 'created': '2025-01-14T16:10:00', 'customer': {'first': 'Ben', 'last': 'Adams'}}
{'id': 103, 'total': 120.0, 'created': '2025-01-14T08:05:00', 'customer': {'first': 'Ben', 'last': 'Adams'}}



sort_orders(ORDERS, 'created', True)
for item in ORDERS:
    print(item)

outputs:

{'id': 101, 'total': 29.99, 'created': '2025-01-15T09:30:00', 'customer': {'first': 'Ana', 'last': 'Zhang'}}
{'id': 102, 'total': 120.0, 'created': '2025-01-14T16:10:00', 'customer': {'first': 'Ben', 'last': 'Adams'}}
{'id': 103, 'total': 120.0, 'created': '2025-01-14T08:05:00', 'customer': {'first': 'Ben', 'last': 'Adams'}}
{'id': 104, 'total': 75.5, 'created': '2025-01-13T12:00:00', 'customer': {'first': 'Cara', 'last': 'Lopez'}}

Does assume valid input
"""