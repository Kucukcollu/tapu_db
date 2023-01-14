-- Tapu Müdürlüğü Tablo Şeması

-------------------------------------------------------

-- DROP TABLE property;
CREATE TABLE property (
	pType    			varchar(15) not null, 
	pOwnerName    	    varchar(20) not null,
	pOwnerSurname       varchar(20) not null,
	pOwnerID			int not null,
	pPrice	            int not null,
	pRoomNumber	        int,
	pSurvey	            int not null,
	pAddress            varchar(40) not null,
	pEstateID           int not null,
	primary key(pOwnerID, pEstateID)
);
-------------------------------------------------------

-- DROP TABLE seller;
CREATE TABLE seller(
	sName    	    	varchar(20) not null,
	sSurname       		varchar(20) not null,
	sID					int not null,
	pType    			varchar(15) not null, 
	pOwnerID			int not null,
	sBudget				int not null,
	primary key(sID, pOwnerID)
);
-------------------------------------------------------

-- DROP TABLE buyyer;
CREATE TABLE buyyer(
	bName    	    	varchar(20) not null,
	bSurname       		varchar(20) not null,
	bID					int not null,
	pType    			varchar(15) not null, 
	pOwnerID			int not null,
	bBudget				int not null,
	primary key(bID, pOwnerID)
);
-------------------------------------------------------

-- DROP TABLE sales;
CREATE TABLE sales(
	pEstateID           int not null,
	bID					int not null,
	sID					int not null,
	pPrice	            int not null,
	sComission			int not null,
	sCirCap 			int not null,			
	sIsDonation	        boolean not null
);
-------------------------------------------------------