-- Tapu Müdürlüğü Sorgu Örnekleri

--------------------------------------
SELECT *
FROM property
--------------------------------------
SELECT *
FROM seller
--------------------------------------
SELECT *
FROM buyyer
--------------------------------------
SELECT *
FROM sales
--------------------------------------
CREATE VIEW istanbul_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='Istanbul,Turkey'
--------------------------------------
CREATE VIEW tokyo_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='Tokyo,Japan'
--------------------------------------
CREATE VIEW newyork_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='New York,USA'
--------------------------------------
CREATE VIEW london_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='London,England'
--------------------------------------
CREATE VIEW paris_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='Paris,France'
--------------------------------------
CREATE VIEW san_francisco_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='San Francisco,USA'
--------------------------------------
CREATE VIEW seatle_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='Seatle,USA'
--------------------------------------
CREATE VIEW paris_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='Paris,France'
--------------------------------------
CREATE VIEW berlin_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='Berlin,Germany'
--------------------------------------
CREATE VIEW san_diago_places_money AS 
SELECT property.pprice 
FROM property 
WHERE property.paddress='San Diego,USA'
