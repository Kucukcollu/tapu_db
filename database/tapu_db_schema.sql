-- Tapu Müdürlüğü Tablo Şeması

-------------------------------------------------------

-- DROP TABLE property;
CREATE TABLE property (
	pType    			varchar(25) not null, 
	pOwnerName    	    varchar(30) not null,
	pOwnerSurname       varchar(30) not null,
	pOwnerID			bigint not null,
	pPrice	            bigint not null,
	pRoomNumber	        bigint,
	pSurvey	            bigint not null,
	pAddress            varchar(40) not null,
	pEstateID           bigint not null primary key
);
-------------------------------------------------------

-- DROP TABLE seller;
CREATE TABLE seller(
	sName    	    	varchar(30) not null,
	sSurname       		varchar(30) not null,
	sID					bigint not null,
	pType    			varchar(25) not null, 
	pOwnerID			bigint not null,
	sBudget				bigint not null,
	primary key(sID, pOwnerID)
);
-------------------------------------------------------

-- DROP TABLE buyyer;
CREATE TABLE buyyer(
	bName    	    	varchar(30) not null,
	bSurname       		varchar(30) not null,
	bID					bigint not null,
	pType    			varchar(25) not null, 
	pOwnerID			bigint not null,
	bBudget				bigint not null,
	primary key(bID, pOwnerID)
);
-------------------------------------------------------

-- DROP TABLE sales;
CREATE TABLE sales(
	bID					bigint not null,
	sID					bigint not null,
	pPrice	            bigint not null,
	sComission			bigint not null,
	sCirCap 			bigint not null,			
	sIsDonation	        boolean not null,
	pEstateID           bigint references property(pEstateID),
	UNIQUE(pEstateID)
);
-------------------------------------------------------