mysql -uambimax -p20ambimax18 -e "use ambimax_management; create table if not exists users(ID int NOT NULL auto_increment, staff_id int(3), name char(40), group_id int(3), PRIMARY KEY (ID))"
mysql -uambimax -p20ambimax18 -e "use ambimax_management; create table if not exists groups(group_id int NOT NULL auto_increment, group_name char(8), PRIMARY KEY (group_id))"
mysql -uambimax -p20ambimax18 -e "use ambimax_management; create table if not exists fingerprints(ID int NOT NULL auto_increment, staff_id int(3), finger_print LONGTEXT, PRIMARY KEY (ID))"
