drop table if exists 	
    cart,
    payment, 
    user,  
    transaction_details, 
    transaction,
    inventory_details,
    inventory, 
    store;
    

create table user(
	userID int NOT NULL AUTO_INCREMENT, 
    username varchar(50) NOT NULL UNIQUE,
    password varchar(256) NOT NULL,	
    email varchar(50) NOT NULL UNIQUE, 
    fname varchar(50) NOT NULL, 
    lname varchar(50) NOT NULL, 
    street varchar(256) NOT NULL, 
    zip int(5) NOT NULL, 
    city varchar(50) NOT NULL, 
    state char(2) NOT NULL,
    constraint u_ID primary key(userID)
);

/*might not even need this table if we have users enter this info on checkout*/    
/*
create table payment(
	userID int NOT NULL, 
    card_number varchar(16) NOT NULL, 
    card_type enum('VISA', 'Mastercard', 'American Express', 'Discover') NOT NULL default 'VISA', 
    pin int(4) NOT NULL, 
    cvv int(3) NOT NULL,
    FOREIGN KEY (userID) REFERENCES USER(userID) on DELETE CASCADE,
    constraint p_ID primary key(userID, card_number)
);
*/

create table transaction(
	transID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userID int NOT NULL,
    total_price decimal(6,2), /*not sure about this just yet. could probably just call a sum query on transaction_details whenever we need the total*/
    trans_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status enum('Pending', 'Out for delivery', 'Complete') DEFAULT 'Pending'
);

create table transaction_details(
	transID int NOT NULL,
    pID int NOT NULL,
    price float NOT NULL,
    quantity int NOT NULL,
    storeID int NOT NULL,
    foreign key (transID) REFERENCES transaction(transID) on DELETE CASCADE,
    constraint td_ID primary key(transID, pID, storeID)
);

create table inventory(
	pID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pname VARCHAR(256) NOT NULL,
    price float NOT NULL,
    image VARCHAR(256) NOT NULL /*stores the path to the image, which is actually stored locally*/,
    description VARCHAR(256) NOT NULL,
    category VARCHAR(256) NOT NULL,
    brand VARCHAR(256) NOT NULL
);

create table store(
	storeID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    street VARCHAR(256) NOT NULL,
    zip int(5) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state CHAR(2) NOT NULL
);
create table inventory_details(
	pID int NOT NULL,
    storeID int NOT NULL,
    stock int NOT NULL,    
    FOREIGN KEY (pID) REFERENCES inventory(pID) on DELETE CASCADE,
    foreign key (storeID) REFERENCES store(storeID) on DELETE CASCADE,
    constraint id_ID primary key (pID, storeID)
);

/* Make un a fk with users */
create table cart(
    username varchar(50) NOT NULL,
	pID int NOT NULL,
	quantity int DEFAULT 1
);


create table delivery_info(
	deliveryID int NOT NULL,
    deliveryTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    closestStore VARCHAR(256) NOT NULL,
    deliveryAddress VARCHAR(256) NOT NULL,
    deliveryEstimateTotalSeconds INT NOT NULL,
    deliveryDistanceMiles VARCHAR(20) NOT NULL,
    deliveryDistanceMeters INT NOT NULL,
    speed FLOAT NOT NULL DEFAULT 1.0
    FOREIGN KEY (deliveryID) REFERENCES transaction(transID)
);
