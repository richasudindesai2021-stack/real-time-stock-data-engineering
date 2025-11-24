SELECT
symbol,
current_price,
ROUND(day_high,2) as day_high,
ROUND(day_low,2) as day_low,
ROUND(day_open,2) as day_open,
ROUND(prev_close,2) as prev_close,
change_amount,
ROUND(change_percent,4) as change_percent,
market_timestamp,
fetched_at 
FROM {{ ref('bronze_stg_stock_quotes') }}
WHERE current_price IS NOT NULL