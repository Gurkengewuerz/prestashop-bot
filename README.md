# prestashop-bot

### STILL IN DEVELOPMENT

This is a bot for the Open Source webshop software PrestaShop.
In the course of a small project at school, we are programming a bot in python with the REST API.


#### TODO:
- [x] Idea for the idea
- [x] Python Bot
- [x] DataBase designe
- [ ] Python Frontend (Django?, Bottle?)
- [x] alternative stuff? (Telegram...)


### SetUp:
bot/dbsettings.sample.py -> bot/dbsettings.py  
bot/config.py

        telegram_api = "" # BOT TOKEN
        telegram_chat = "" # CHATID /getUpdates

webbinterface/dbsettings.sample.py -> webinterface/dbsettings.py

#### MySQL Statement:
    CREATE TABLE `ita_licencekey` (
        `key_id` INT(11) NOT NULL AUTO_INCREMENT,
        `licence` VARCHAR(50) NOT NULL,
        `product_reference` VARCHAR(50) NOT NULL,
        `created_timestamp` INT(11) NOT NULL,
        `rented_timestamp` INT(11) NULL,
        PRIMARY KEY (`key_id`)
    ) COLLATE='latin1_swedish_ci' ENGINE=InnoDB;  
      
    CREATE TABLE `ita_shop` (
        `shop_id` INT(11) NOT NULL AUTO_INCREMENT,
        `url` VARCHAR(254) NOT NULL,
        `api_key` VARCHAR(254) NOT NULL,
        `shop_name` VARCHAR(50) NOT NULL DEFAULT 'Unknown',
        `delivstat` INT(11) NOT NULL DEFAULT '0',
        PRIMARY KEY (`shop_id`)
    ) COLLATE='latin1_swedish_ci' ENGINE=InnoDB;
      
    CREATE TABLE `ita_shop_stat` (
        `stat_id` INT(11) NOT NULL AUTO_INCREMENT,
        `shop_id` INT(11) NOT NULL,
        `stat` INT(11) NOT NULL,
        PRIMARY KEY (`stat_id`),
        INDEX `shop_id` (`shop_id`),
        CONSTRAINT `shop_id` FOREIGN KEY (`shop_id`) REFERENCES `ita_shop` (`shop_id`) ON UPDATE CASCADE ON DELETE CASCADE
    ) COLLATE='latin1_swedish_ci' ENGINE=InnoDB;



#### Libraries
- https://github.com/PrestaShop/PrestaShop
- https://core.telegram.org/methods

Twitter: @Gurkengewuerz  
Twitter: @Paraodx_1337
