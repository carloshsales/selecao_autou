CREATE TABLE IF NOT EXISTS users(
    regist INT(4) NOT NULL,
    email CHAR(255),
    name CHAR(100),
    last_name CHAR(100),
    departament CHAR (255),
    role CHAR(50),
    image CHAR(255),
    PRIMARY KEY(regist)
);
CREATE TABLE IF NOT EXISTS scores(
    id INT(3) NOT NULL AUTO_INCREMENT,
    score int(10),
    user_regist int(4),
    PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS reactions(
    id INT(3) NOT NULL AUTO_INCREMENT,
    name CHAR(100),
    user_regist int(4),
    PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS comments(
    id INT(3) NOT NULL AUTO_INCREMENT,
    comment VARCHAR(255),
    user_regist int(4),
    PRIMARY KEY(id)
);
ALTER TABLE scores ADD FOREIGN KEY (user_regist) REFERENCES users(regist);
ALTER TABLE reactions ADD FOREIGN KEY (user_regist) REFERENCES users(regist);
ALTER TABLE comments ADD FOREIGN KEY (user_regist) REFERENCES users(regist);