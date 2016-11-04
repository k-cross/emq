insert into user (username, fname, lname, email, street, zip, city, state, password) values ('dmcdonald0', 'Deborah', 'Mcdonald', 'dmcdonald0@about.me', '1456 Chavez Way', '95131', 'San Jose', 'CA', 'toasty');
insert into user (username, fname, lname, email, street, zip, city, state, password) values ('bblack1', 'Brenda', 'Black', 'bblack1@godaddy.com', '05 Calypso Road', '89135', 'Las Vegas', 'NV', 'test');
insert into user (username, fname, lname, email, street, zip, city, state, password) values ('kfrazier2', 'Kelly', 'Frazier', 'kfrazier2@tripod.com', '568 Kensington Avenue', '17405', 'York', 'PA', 'qwerty');
insert into user (username, fname, lname, email, street, zip, city, state, password) values ('tcarroll3', 'Teresa', 'Carroll', 'tcarroll3@godaddy.com', '93 Sachs Place', '54313', 'Green Bay', 'WI', '123qweasd' );
insert into user (username, fname, lname, email, street, zip, city, state, password) values ('bhanson4', 'Billy', 'Hanson', 'bhanson4@mlb.com', '6 Larry Court', '10039', 'New York City', 'NY', 'asdfasd');

/*
insert into payment (userID, card_number, card_type, pin, cvv) values (1, '1111222233334444', 'VISA', 1234, 000);
insert into payment (userID, card_number, card_type, pin, cvv) values (3, '2222333344441111', 'Mastercard', 4321, 000);
insert into payment (userID, card_number, card_type, pin, cvv) values (5, '2222333311114444', 'Discover', 1234, 000);
*/

/*insert into store (street, zip, city, state) values ('44 Pennsylvania Court', 68110, 'Omaha', 'NE');
insert into store (street, zip, city, state) values ('72352 Upham Lane', 27157, 'Winston Salem', 'NC');
insert into store (street, zip, city, state) values ('912 Pawling Point', 20414, 'Washington', 'DC');
insert into store (street, zip, city, state) values ('94097 Bunting Terrace', 93111, 'Santa Barbara', 'CA');
insert into store (street, zip, city, state) values ('846 Spenser Pass', 33487, 'Boca Raton', 'FL');*/
insert into store (street, city, state, zip) values ('30600 Dyer St', 'Union City', 'CA', 94587); /*6*/
insert into store (street, city, state, zip) values ('1919 Davis St', 'San Leandro', 'CA', 94577);
insert into store (street, city, state, zip) values ('40580 Albrae St', 'Fremont', 'CA', 94538);
insert into store (street, city, state, zip) values ('777 Story rd', 'San Jose', 'CA', 95122);
insert into store (street, city, state, zip) values ('301 Ranch Dr', 'Milpitas', 'CA', 95035);
insert into store (street, city, state, zip) values ('600 Showers Dr', 'Mountain View', 'CA', 94094);
insert into store (street, city, state, zip) values ('4080 Stevens Creek Blvd', 'San Jose', 'CA', 95128);
insert into store (street, city, state, zip) values ('2485 El Camino Real', 'Redwood City', 'CA', 94063);
insert into store (street, city, state, zip) values ('2220 Bridgepointe Pkwy', 'San Mateo', 'CA', 94404);
insert into store (street, city, state, zip) values ('1150 El Camino Real', 'San Bruno', 'CA', 94066);
insert into store (street, city, state, zip) values ('1830 Ocean Ave', 'San Francisco', 'CA', 94112);
insert into store (street, city, state, zip) values ('2675 Geary Blvd', 'San Francisco', 'CA', 94118);
insert into store (street, city, state, zip) values ('2700 5th St', 'Alameda', 'CA', 94501);

/*
insert into inventory (pname, image, description, category, brand, price) values ('Samsung television', '/product_images/samtelevision.jpg', 'It\'s a Samsung tv', 'television', 'Samsung', 5000.00);
insert into inventory (pname, image, description, category, brand, price) values ('Sony television', '/product_images/sonytelevision.jpg', 'It\'s a Sony tv', 'television', 'Sony', 4400.00);
insert into inventory (pname, image, description, category, brand, price) values ('samsung note 7', '/product_images/note7.jpg', 'It\'s the Note 7', 'phone', 'Samsung', 849.00);
insert into inventory (pname, image, description, category, brand, price) values ('Apple iPhone 7', '/product_images/iphone7.jpg', 'It\'s iPhone 7', 'phone', 'Apple', 649.00);
insert into inventory (pname, image, description, category, brand, price) values ('Apple iPhone 7 Plus', '/product_images/iphone7plus.jpg', 'It\'s the iPhone 7 Plus', 'phone', 'Apple', 849.00);
insert into inventory (pname, image, description, category, brand, price) values ('Google Pixel', '/product_images/pixel.jpg', 'It\'s the Google Pixel', 'phone', 'Google', 649.00);
insert into inventory (pname, image, description, category, brand, price) values ('Google Pixel XL', '/product_images/pixelxl.jpg', 'It\'s the Google Pixel XL', 'phone', 'Google', 769.00);
*/
insert into inventory (pname, image, description, category, brand, price) values ('HP Spectre x360', 'http://core0.staticworld.net/images/article/2015/02/hp-spectre-x360_beauty-100570598-orig.jpg', 'The all-new Spectre x360 was designed for those who crave uninhibited freedom. With alluring power in our thinnest convertible frame.', 'laptop', 'HP', 299);
insert into inventory (pname, image, description, category, brand, price) values ('Samsung 40" LED 4K TV', 'http://i.imgur.com/fL32mJ5.jpg?1', 'Watch TV or play games in stunning detail on this Samsung 6-Series 4K UHD TV. Four times the sharpness of Full HD TVs, and upscaling picture quality.', 'Samsung', 'television', 299);
insert into inventory (pname, image, description, category, brand, price) values ('Sandisk Extreme 900 Portable SSD', 'https://images-na.ssl-images-amazon.com/images/I/51joAVOcKBL._SL1000_.jpg', 'The SanDisk Extreme 900 portable SSD delivers up to 9x faster speeds than typical external hard drives.', 'SanDisk', 'storage drive', 100);
insert into inventory (pname, image, description, category, brand, price) values ('BOSE A20 Headset', 'http://www.pilotshop.com/catalog/graphics/b/bosea20.png', 'The A20 Aviation Headset is a top of the line headset that is engineered to be more comfortable and provide more noise reduction than any headset.', 'Bose', 'headphone', 200);
insert into inventory (pname, image, description, category, brand, price) values ('Roku 4', 'https://images-na.ssl-images-amazon.com/images/I/51BXju3LMpL._SL1000_.jpg', 'Roku delivers fast performance and stunning high definition video while being able to stream all your favorite apps at a tremendous value.', 'Roku', 'media player', 20);

insert into inventory_details (pId, storeID) values (1, 1);
insert into inventory_details (pId, storeID) values (1, 2);
insert into inventory_details (pId, storeID) values (1, 3);
insert into inventory_details (pId, storeID) values (1, 4);
insert into inventory_details (pId, storeID) values (1, 5);
insert into inventory_details (pId, storeID) values (1, 6);
insert into inventory_details (pId, storeID) values (1, 7);
insert into inventory_details (pId, storeID) values (1, 8);
insert into inventory_details (pId, storeID) values (1, 9);
insert into inventory_details (pId, storeID) values (1, 10);
insert into inventory_details (pId, storeID) values (1, 11);
insert into inventory_details (pId, storeID) values (1, 12);
insert into inventory_details (pId, storeID) values (1, 13);

insert into inventory_details (pId, storeID) values (2, 1);
insert into inventory_details (pId, storeID) values (2, 2);
insert into inventory_details (pId, storeID) values (2, 3);
insert into inventory_details (pId, storeID) values (2, 4);
insert into inventory_details (pId, storeID) values (2, 5);
insert into inventory_details (pId, storeID) values (2, 6);
insert into inventory_details (pId, storeID) values (2, 7);
insert into inventory_details (pId, storeID) values (2, 8);
insert into inventory_details (pId, storeID) values (2, 9);
insert into inventory_details (pId, storeID) values (2, 10);
insert into inventory_details (pId, storeID) values (2, 11);
insert into inventory_details (pId, storeID) values (2, 12);

insert into inventory_details (pId, storeID) values (3, 1);
insert into inventory_details (pId, storeID) values (3, 2);
insert into inventory_details (pId, storeID) values (3, 3);
insert into inventory_details (pId, storeID) values (3, 4);
insert into inventory_details (pId, storeID) values (3, 5);
insert into inventory_details (pId, storeID) values (3, 6);
insert into inventory_details (pId, storeID) values (3, 7);
insert into inventory_details (pId, storeID) values (3, 8);
insert into inventory_details (pId, storeID) values (3, 9);
insert into inventory_details (pId, storeID) values (3, 10);
insert into inventory_details (pId, storeID) values (3, 11);
insert into inventory_details (pId, storeID) values (3, 12);

insert into inventory_details (pId, storeID) values (4, 1);
insert into inventory_details (pId, storeID) values (4, 2);
insert into inventory_details (pId, storeID) values (4, 3);
insert into inventory_details (pId, storeID) values (4, 4);
insert into inventory_details (pId, storeID) values (4, 5);
insert into inventory_details (pId, storeID) values (4, 6);
insert into inventory_details (pId, storeID) values (4, 7);
insert into inventory_details (pId, storeID) values (4, 8);
insert into inventory_details (pId, storeID) values (4, 9);
insert into inventory_details (pId, storeID) values (4, 10);
insert into inventory_details (pId, storeID) values (4, 11);
insert into inventory_details (pId, storeID) values (4, 12);

insert into inventory_details (pId, storeID) values (5, 1);
insert into inventory_details (pId, storeID) values (5, 2);
insert into inventory_details (pId, storeID) values (5, 3);
insert into inventory_details (pId, storeID) values (5, 4);
insert into inventory_details (pId, storeID) values (5, 5);
insert into inventory_details (pId, storeID) values (5, 6);
insert into inventory_details (pId, storeID) values (5, 7);
insert into inventory_details (pId, storeID) values (5, 8);
insert into inventory_details (pId, storeID) values (5, 9);
insert into inventory_details (pId, storeID) values (5, 10);
insert into inventory_details (pId, storeID) values (5, 11);
insert into inventory_details (pId, storeID) values (5, 12);
/*
insert into inventory_details (pId, storeID) values (6, 1);
insert into inventory_details (pId, storeID) values (6, 2);
insert into inventory_details (pId, storeID) values (6, 3);
insert into inventory_details (pId, storeID) values (6, 4);
insert into inventory_details (pId, storeID) values (6, 5);
insert into inventory_details (pId, storeID) values (6, 6);
insert into inventory_details (pId, storeID) values (6, 7);
insert into inventory_details (pId, storeID) values (6, 8);
insert into inventory_details (pId, storeID) values (6, 9);
insert into inventory_details (pId, storeID) values (6, 10);
insert into inventory_details (pId, storeID) values (6, 11);
insert into inventory_details (pId, storeID) values (6, 12);

insert into inventory_details (pId, storeID) values (7, 1);
insert into inventory_details (pId, storeID) values (7, 2);
insert into inventory_details (pId, storeID) values (7, 3);
insert into inventory_details (pId, storeID) values (7, 4);
insert into inventory_details (pId, storeID) values (7, 5);
insert into inventory_details (pId, storeID) values (7, 6);
insert into inventory_details (pId, storeID) values (7, 7);
insert into inventory_details (pId, storeID) values (7, 8);
insert into inventory_details (pId, storeID) values (7, 9);
insert into inventory_details (pId, storeID) values (7, 10);
insert into inventory_details (pId, storeID) values (7, 11);
insert into inventory_details (pId, storeID) values (7, 12);
*/
insert into transaction(userID, total_price) values (1, 9400.00);
insert into transaction_details(transID, pID, price, storeID, quantity) values(1, 1, 5000.00, 6, 1);
insert into transaction_details(transID, pID, price, storeID, quantity) values(1, 2, 4400.00, 6, 1);
insert into transaction(userID, total_price) values (5, 10698.00);
insert into transaction_details(transID, pID, price, storeID, quantity) values(2, 1, 5000.00, 10, 1);
insert into transaction_details(transID, pID, price, storeID, quantity) values(2, 2, 4400.00, 10, 1);
insert into transaction_details(transID, pID, price, storeID, quantity) values(2, 4, 649.00, 10, 1);
insert into transaction_details(transID, pID, price, storeID, quantity) values(2, 6, 649.00, 10, 1);
insert into transaction(userID, total_price) values (5, 1398.00);
insert into transaction_details(transID, pID, price, storeID, quantity) values(3, 4, 649.00, 10, 2);
/*select* from user, payment where user.userID = payment.userID;*/
select* from inventory, inventory_details where inventory.pID=inventory_details.pID;

select* from orders_test;
/*select  CONCAT('\'', store.street, ', ', store.city, ', ', store.state, '\'') from store;*/
select * from orders where transID = 1;
/*insert into orders(userID,
    transID,
    totalCost,
    orderPlacedTime,
    items, deliveryAddress) SELECT user.userID as userID, t.transID, t.total_price, t.trans_time, 
									CONCAT('[', GROUP_CONCAT(td.pID SEPARATOR ', '), ']'),
                                    CONCAT(user.street, ', ', user.city, ', ', user.state, ' ', user.zip)
								from transaction t,
									transaction_details td,
                                    user
								where t.transID = td.transID and
                                    t.userId = user.userId
								GROUP BY user.userID, t.transID;
                                */

/*Update orders SET storeAddress = '("''301 Ranch Dr, Milpitas, CA''",), 9347)', deliveryEstimateSeconds = 1209, deliverDistanceMeters = 9346, deliverDistanceMiles = '5.8 mi', speed = 7.73036 where transID = 1;*/

select * from orders where transID = 1;
/* How the orders table insert might work 
1. Insert values that can be gotten from other tables (userID, transID,...,deliveryAddress)
2. Update with values found from getDeliveryInfo(deliveryAddress)
3. ???
4. Profit

insert into orders (userID, transID, totalCost, orderPlacedTime, items, deliveryAddress)
	SELECT user.userID as userID, t.transID, t.total_price, t.trans_time, 
									CONCAT('[', GROUP_CONCAT(td.pID SEPARATOR ', '), ']'),
                                    CONCAT(user.street, ', ', user.city, ', ', user.state, ' ', user.zip)
								from transaction t,
									transaction_details td,
                                    store,
                                    user
								where t.transID = td.transID and
                                    t.userId = user.userId
								GROUP BY user.userID, t.transID;
Update orders SET storeAddress = %s, deliveryEstimateSeconds = %s, deliverDistanceMeters = %s, deliverDistanceMiles = %s, speed %s;