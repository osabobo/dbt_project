with source as (
    select * from {{ source('raw', 'seed_data') }}
)
select
    customer_id,
    customer_name,
    purchase_date,
    purchase_amount
from source

