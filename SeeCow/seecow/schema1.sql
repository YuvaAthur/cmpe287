
open /home/ubuntu/CMPE-287-WARRIORS/WARRIORS_PARLOR_STATUS

drop table PARLOR_STATUS;

CREATE TABLE PARLOR_STATUS (
 cattle_id varchar PRIMARY KEY,
 info varchar NOT NULL,
 place varchar NOT NULL,
 time DATE
 );
 
insert into PARLOR_STATUS (cattle_id, info, place, time) values (1, 'IN', 'BLDG1', '2019-07-24 10:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, time) values (2, 'IN', 'BLDG1', '2019-07-24 10:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, time) values (3, 'OUT', 'BLDG1', '2019-07-24 10:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, time) values (4, 'IN', 'BLDG1', '2019-07-24 10:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, time) values (5, 'OUT', 'BLDG1', '2019-07-24 10:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, time) values (6, 'IN', 'BLDG1', '2019-07-24 10:00:00');

.headers on

select * from PARLOR_STATUS;
