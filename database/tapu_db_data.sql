-- Tapu Müdürlüğü Data

------------------------------------------------------------------------------------------------------------------
-- datas of property table
--                          (pType, pOwnerName, pOwnerSurname, pOwnerID, pPrice, pRoomNumber, pSurvey, pAddress, pEstateID)
INSERT INTO property VALUES ('Apartment','Tom','Hanks',18034035,4000000,3,105,'New York,USA',3209403233);
INSERT INTO property VALUES ('Office','Jack','Nicholson',22054045,1350000,14,200,'London,England',2892636297);
INSERT INTO property VALUES ('Apartment','Benedict','Cumberbatch',12054042,3002300,5,250,'Istanbul,Turkey',9284638711);
INSERT INTO property VALUES ('Storehouse','Leonardo','DiCaprio',42054545,980000,NULL,1000,'London,England',2846304008);
INSERT INTO property VALUES ('Office','Christian','Bale',25089404,769000,8,400,'Paris,France',3645938383);
INSERT INTO property VALUES ('Storehouse','Natalie','Portman',14254054,450320,NULL,2500,'Tokyo,Japan',6732838470);
INSERT INTO property VALUES ('Apartment','Lena','Headey',10283892,320000,4,280,'Istanbul,Turkey',1523843222);
INSERT INTO property VALUES ('Apartment','Robert','Downey',91283765,14000000,4,350,'San Francisco,USA',1523843222);
INSERT INTO property VALUES ('Office','Elijah','Wood',19383422,340000,15,340,'New York,USA',1523843222);
INSERT INTO property VALUES ('Office','Tom','Hanks',18034035,340985,6,340,'Seatle,USA',5632174590);
INSERT INTO property VALUES ('Storehouse','Benedict','Cumberbatch',12054042,320000,NULL,500,'San Francisco,USA',6784356411);
INSERT INTO property VALUES ('Apartment','Scarlett','Johansson',09983462,1000000,3,180,'London,England',1524386944);
INSERT INTO property VALUES ('Office','Megan','Fox',86654042,4360000,60,4590,'Tokyo,Japan',1439638466);
INSERT INTO property VALUES ('Storehouse','Emma','Watson',12872350,5000000,NULL,430,'Berlin,Germany',1427532099);
INSERT INTO property VALUES ('Apartment','Emilia','Clarke',19283422,4000000,5,400,'New York,USA',1523843222);
INSERT INTO property VALUES ('Apartment','Emilia','Clarke',19283422,6800000,8,550,'New York,USA',3452617843);
INSERT INTO property VALUES ('Storehouse','Jennifer','Lawrence',21285422,8700000,NULL,680,'New York,USA',1523843222);
INSERT INTO property VALUES ('Office','Audrey','Tautou',19280923,680000,32,388,'San Diego,USA',1523843222);
INSERT INTO property VALUES ('Apartment','Lena','Headey',10283892,540000,2,100,'Paris,France',8764037821);
------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------
-- datas of seller table
--                        (sName, sSurname, sID, pType, pOwnerID, sBudget)
INSERT INTO seller VALUES ('Tom','Hanks',16034035,'Apartment',18034035,6000000);
INSERT INTO seller VALUES ('Jack','Nicholson',13034036,'Office',22054045,80000);
INSERT INTO seller VALUES ('Benedict','Cumberbatch',56034523,'Storehouse',12054042,45000);
INSERT INTO seller VALUES ('Leonardo','DiCaprio',74360990,'Storehouse',42054545,1000000);
INSERT INTO seller VALUES ('Christian','Bale',56238776,'Office',25089404,280000);
INSERT INTO seller VALUES ('Natalie','Portman',19283432,'Storehouse',14254054,35000);
INSERT INTO seller VALUES ('Scarlett','Johansson',13245321,'Apartment',09983462,8300000);
INSERT INTO seller VALUES ('Megan','Fox',17716556,'Office',86654042,100000);
INSERT INTO seller VALUES ('Emma','Watson',09098735,'Storehouse',12872350,2000000);
INSERT INTO seller VALUES ('Emilia','Clarke',23432166,'Apartment',19283422,540000);
------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------
-- datas of buyyer table
--                        (bName, bSurname, bID, pType, pOwnerID, bBudget)
INSERT INTO buyyer VALUES ('Leonhard','Euler',24939461,'Apartment',18034035,12000000);
INSERT INTO buyyer VALUES ('Marie','Curie',02184646,'Office',22054045,200000);
INSERT INTO buyyer VALUES ('Nikola','Tesla',98327676,'Storehouse',12054042,450000);
INSERT INTO buyyer VALUES ('Linus','Torvalds',16243215,'Storehouse',42054545,3200);
INSERT INTO buyyer VALUES ('Ada','Lovelace',67435643,'Office',25089404,0);
INSERT INTO buyyer VALUES ('Alan','Turing',98765423,'Storehouse',14254054,2000);
INSERT INTO buyyer VALUES ('Bjarne','Stroustrup',6785643,'Apartment',09983462,5000000);
INSERT INTO buyyer VALUES ('Richard','Stallman',23421621,'Office',86654042,110000);
INSERT INTO buyyer VALUES ('Dennis','Ritchie',98656774,'Storehouse',12872350,650430);
INSERT INTO buyyer VALUES ('William','Shockley',31093290,'Apartment',19283422,4630000);
------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------
-- datas of sales table
--                       s(pEstateID, bID, sID, pPrice, sComission, sCirCap, sIsDonation)
INSERT INTO sales VALUES (3626,24939461,16034035,0,4000,1000,TRUE);
INSERT INTO sales VALUES (9843,02184646,13034036,1350000,5400,600,FALSE);
INSERT INTO sales VALUES (2376,98327676,56034523,0,10000,350,TRUE);
INSERT INTO sales VALUES (2377,16243215,74360990,980000,8600,200,FALSE);
INSERT INTO sales VALUES (1298,67435643,56238776,0,1300,460,TRUE);
INSERT INTO sales VALUES (4343,98765423,19283432,450320,12000,940,FALSE);
INSERT INTO sales VALUES (1923,6785643,13245321,1000000,4380,330,FALSE);
INSERT INTO sales VALUES (9876,23421621,17716556,0,5250,245,TRUE);
INSERT INTO sales VALUES (1421,98656774,09098735,5000000,9000,465,FALSE);
INSERT INTO sales VALUES (0989,31093290,23432166,4000000,7500,250,FALSE);
------------------------------------------------------------------------------------------------------------------