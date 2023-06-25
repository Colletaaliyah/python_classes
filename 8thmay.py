no.ONE
INSERT INTO Customers (CustomerName,ContactName,Address,City,PostalCode,Country)
VALUES ('Aaliyah Collet','Anna Andrea','TomMboya','Nairobi','14623','Kenya')
UPDATE Customers
SET Address='Haile Selassie',City='Mombasa'
WHERE CustomerID=92

no.TWO
INSERT INTO Orders(OrderID,CustomerID,EmployeeID,OrderDate,ShipperID)
VALUES ('10444','92','10','1996-12-02','3')

no.THREE
INSERT INTO Products(ProductName,SupplierID,CategoryID,Unit,Price)
VALUES ('Sardine','19','8','40-200g Cans','55')

no.FOUR
INSERT INTO OrderDetails(OrderID,ProductID,Quantity)
VALUES ('10444','78','40')

no.FIVE
DELETE FROM Customers
WHERE CustomerID=56

no.SIX
SELECT * FROM [Customers]
WHERE Country='Brazil' or Country='Italy'

no.SEVEN
SELECT * FROM Customers
WHERE CustomerName LIKE '%son%';

no.EIGHT
SELECT * FROM [Orders]
WHERE OrderDate LIKE "%1996-10%"
ORDER BY OrderDate ASC;

no.NINE
SELECT SUM (ShipperID)
FROM Orders
WHERE ShipperID=1 OR ShipperID=2 OR ShipperID=3;

no.TEN
SELECT * FROM [Products]
WHERE Price > 25
