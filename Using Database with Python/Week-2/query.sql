/*CREATE TABLE Users(
	ID INT NOT NULL AUTO_INCREMENT,
	FIRST_NAME VARCHAR(128),
	EMAIL VARCHAR(128),
	PRIMARY KEY(ID)
	);
*/

SELECT * FROM Users ORDER BY ID desc

INSERT INTO Users (ID, FIRST_NAME, EMAIL) VALUES
(4,'Fred', 'fred@gmail.com')

DELETE FROM Users WHERE EMAIL='fred@gmail.com'

UPDATE Users SET EMAIL='noobstep.8@gmail.com' WHERE FIRST_NAME='Vaibhav';