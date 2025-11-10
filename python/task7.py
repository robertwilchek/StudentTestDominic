
from collections import defaultdict
from orders_data import ORDERS  # reuse from Task 3

def group_totals_by_customer(orders):
    """
    Return a dict mapping 'Last, First' -> total_spent (float).
    TODO: implement
    """
    sums = defaultdict(float)
    for record in orders:
        sums[f'{record['customer']['last']}, {record['customer']['first']}'] += record['total']
    return dict(sums)

def top_customers(sums, n=3):
    """
    Return a list of (name, total) sorted by total DESC, then name ASC.
    TODO: implement
    """
    customers = [(name, total) for name, total in sums.items()]
    
    customers.sort(key = lambda x: (-x[1], x[0]))
    return customers

def render_html(top_list):
    """
    Return a minimal HTML string with a <ul> of 'Name — $Total'.
    TODO: implement (simple string builder is fine)
    """
    title = "Customer Spend — Top 3"
    output =  f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>{title}</title>
        </head>
        <body>
            <ul>
    """
    for name, total in top_list:
        output += f"\n\t\t\t\t<li>{name} — ${total}</li>"

    output += """
            </ul>
        </body>
    </html>
    """
    return output

if __name__ == "__main__":
    sums = group_totals_by_customer(ORDERS)
    top3 = top_customers(sums, n=3)
    html = render_html(top3)
    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote report.html")