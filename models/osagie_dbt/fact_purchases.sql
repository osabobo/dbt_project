select
    customer_id,
    sum(purchase_amount) as total_spent
from {{ ref('stg_customers') }}
group by customer_id
