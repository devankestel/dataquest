## 2. Joining Three Tables ##

SELECT t.track_id, t.name track_name, mt.name track_type, il.unit_price, il.quantity 
FROM track t
INNER JOIN invoice_line il ON il.track_id = t.track_id
INNER JOIN media_type mt ON t.media_type_id = mt.media_type_id
WHERE il.invoice_id = 4;

## 3. Joining More Than Three Tables ##

SELECT
    il.track_id,
    t.name track_name,
    a.name artist_name,
    mt.name track_type,
    il.unit_price,
    il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
INNER JOIN album al ON t.album_id = al.album_id
INNER JOIN artist a ON al.artist_id = a.artist_id 
WHERE il.invoice_id = 4;

## 4. Combining Multiple Joins with Subqueries ##

SELECT
    ta.album_name album,
    ta.artist_name artist,
    COUNT(*) tracks_purchased
FROM invoice_line il
INNER JOIN (
            SELECT
                t.track_id,
                al.title album_name,
                ar.name artist_name
            FROM track t
            INNER JOIN album al ON al.album_id = t.album_id
            INNER JOIN artist ar ON ar.artist_id = al.artist_id
           ) ta
           ON ta.track_id = il.track_id
GROUP BY album
ORDER BY tracks_purchased DESC LIMIT 5;

## 5. Recursive Joins ##

SELECT e.first_name || " " || e.last_name employee_name,
e.title employee_title, 
s.first_name || " " || s.last_name supervisor_name,
s.title supervisor_title
FROM employee e
LEFT JOIN employee s on e.reports_to = s.employee_id
ORDER BY employee_name;

## 6. Pattern Matching Using Like ##

SELECT first_name, last_name, phone
FROM customer
WHERE first_name LIKE "%belle%";