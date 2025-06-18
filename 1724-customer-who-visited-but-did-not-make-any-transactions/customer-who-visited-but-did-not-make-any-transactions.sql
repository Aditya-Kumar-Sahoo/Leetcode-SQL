# Write your MySQL query statement below
Select V.customer_id,
COUNT(*) As count_no_trans
From Visits V
Left Join Transactions T on V.visit_id = T.visit_id
Where T.transaction_id IS NULL
Group By V.customer_id
Order By count_no_trans asc, V.customer_id;