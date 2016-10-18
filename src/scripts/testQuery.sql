insert into user (username, fname, lname, email, street, zip, city, state) values ('dmcdonald0', 'Deborah', 'Mcdonald', 'dmcdonald0@about.me', '34393 Thackeray Alley', '40256', 'Louisville', 'KY');
insert into user (username, fname, lname, email, street, zip, city, state) values ('bblack1', 'Brenda', 'Black', 'bblack1@godaddy.com', '05 Calypso Road', '89135', 'Las Vegas', 'NV');
insert into user (username, fname, lname, email, street, zip, city, state) values ('kfrazier2', 'Kelly', 'Frazier', 'kfrazier2@tripod.com', '568 Kensington Avenue', '17405', 'York', 'PA');
insert into user (username, fname, lname, email, street, zip, city, state) values ('tcarroll3', 'Teresa', 'Carroll', 'tcarroll3@godaddy.com', '93 Sachs Place', '54313', 'Green Bay', 'WI');
insert into user (username, fname, lname, email, street, zip, city, state) values ('bhanson4', 'Billy', 'Hanson', 'bhanson4@mlb.com', '6 Larry Court', '10039', 'New York City', 'NY');

insert into payment (userID, card_number, card_type, pin, cvv) values (1, '1111222233334444', 'VISA', 1234, 000);
insert into payment (userID, card_number, card_type, pin, cvv) values (3, '2222333344441111', 'Mastercard', 4321, 000);
insert into payment (userID, card_number, card_type, pin, cvv) values (5, '2222333311114444', 'Discover', 1234, 000);

insert into store (street, zip, city, state) values ('44 Pennsylvania Court', '68110', 'Omaha', 'NE');
insert into store (street, zip, city, state) values ('72352 Upham Lane', '27157', 'Winston Salem', 'NC');
insert into store (street, zip, city, state) values ('912 Pawling Point', '20414', 'Washington', 'DC');
insert into store (street, zip, city, state) values ('94097 Bunting Terrace', '93111', 'Santa Barbara', 'CA');
insert into store (street, zip, city, state) values ('846 Spenser Pass', '33487', 'Boca Raton', 'FL');

insert into inventory (pname, image, description, category, brand) values ('samsung television', 'product_images/samtelevision.jpg', 'It\'s a Samsung tv', 'electronic', 'Samsung');
insert into inventory (pname, image, description, category, brand) values ('sony television', 'product_images/sonytelevision.jpg', 'It\'s a Sony tv', 'electronic', 'Sony');

insert into inventory_details (pId, storeID, price, stock) values (1, 1, 5000.00, 10);
insert into inventory_details (pId, storeID, price, stock) values (1, 2, 5000.00, 7);
insert into inventory_details (pId, storeID, price, stock) values (1, 3, 5000.00, 22);
insert into inventory_details (pId, storeID, price, stock) values (2, 1, 4400.00, 8);

select* from user, payment where user.userID = payment.userID;
select* from inventory, inventory_details where inventory.pID=inventory_details.pID;