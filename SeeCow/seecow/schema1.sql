
open /home/ubuntu/CMPE-287-WARRIORS/WARRIORS_PARLOR_STATUS

drop table PARLOR_STATUS;

CREATE TABLE PARLOR_STATUS (
 CATTLE_ID varchar PRIMARY KEY,
 Status varchar NOT NULL,
 LOCATION varchar NOT NULL,
 Time_IN DATE,
 Time_OUT DATE
 );
 
insert into PARLOR_STATUS (cattle_id, info, place, Time_IN, Time_OUT) values (1, 'IN', 'BLDG1', '2019-07-24 10:00:00', '2007-07-24 11:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, Time_IN, Time_OUT) values (2, 'IN', 'BLDG1', '2019-07-24 10:00:00', '2007-07-24 11:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, Time_IN, Time_OUT) values (3, 'OUT', 'BLDG1', '2019-07-24 10:00:00', '2007-07-24 11:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, Time_IN, Time_OUT) values (4, 'IN', 'BLDG1', '2019-07-24 10:00:00', '2007-07-24 11:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, Time_IN, Time_OUT) values (5, 'OUT', 'BLDG1', '2019-07-24 10:00:00', '2007-07-24 11:00:00');
insert into PARLOR_STATUS (cattle_id, info, place, Time_IN, Time_OUT) values (6, 'IN', 'BLDG1', '2019-07-24 10:00:00', '2007-07-24 11:00:00');

.mode column
.headers on

select CATTLE_ID, Status, LOCATION, Time_IN, Time_OUT from PARLOR_STATUS;
