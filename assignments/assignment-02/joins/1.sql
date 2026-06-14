--Design a database schema in SQL that includes at least three tables: one for bones, one for joints, and one for joint types.
--1 . The bones table should store information about each bone, including a unique ID, bone name, and a description.
use SQLPractice;
CREATE TABLE bones (
    bone_id INT PRIMARY KEY,
    bone_name VARCHAR(255) NOT NULL,
    bone_description text NOT NULL
);

--2. The joints table should include a unique ID, the IDs of the bones it connects (foreign keys referencing the bones table), the type of joint (foreign key referencing the joint types table), and any additional relevant details.

create table joints (
    joint_id int primary key,
    bone_id int,
    type_id int,
    joint_details text,
    
	foreign key (bone_id) references bones(bone_id),
	foreign key (type_id) references joint_types(type_id)

);

--3. The joint types table should store different types of joints (e.g., ball-and-socket, hinge, pivot) with a unique ID and a description for each type.
create table joint_types(
    type_id int primary key,
    type_name varchar(100) not null,
    type_description text
)



--4. Implement the schema in SQL and populate the tables with at least five joints, including their types and the bones they connect.

insert INTO bones (bone_id, bone_name, bone_description) VALUES
(1, 'Femur', 'The thigh bone, the longest and strongest bone in the human body.'),
(2, 'Tibia', 'The shin bone, the second largest bone in the human body.'),
(3, 'Humerus', 'The upper arm bone, connecting the shoulder to the elbow.'),
(4, 'Radius', 'One of the two forearm bones, located on the thumb side.'),
(5, 'Ulna', 'One of the two forearm bones, located on the pinky side.');

select * from bones;

INSERT INTO joints (joint_id, bone_id, type_id, joint_details) VALUES
(1, 1, 1, 'The hip joint connects the femur to the pelvis.'),
(2, 2, 2, 'The knee joint connects the tibia to the femur.'),
(3, 3, 1, 'The shoulder joint connects the humerus to the scapula.'),
(4, 4, 3, 'The elbow joint connects the radius to the humerus.'),
(5, 5, 2, 'The wrist joint connects the ulna to the carpal bones.');

select * from joints;

INSERT INTO joint_types (type_id, type_name, type_description) VALUES
(1, 'Ball-and-Socket', 'A joint that allows for rotational movement in almost all directions.'),
(2, 'Hinge', 'A joint that allows for movement in one plane, like a door hinge.'),
(3, 'Pivot', 'A joint that allows for rotational movement around a single axis.'),
(4, 'Saddle', 'A joint that allows for movement in two planes, but with limited rotation.'),
(5, 'Gliding', 'A joint that allows for sliding movements between flat surfaces.');

-- Queries to verify the data
select * from joint_types;
show tables;

SELECT j.joint_id,
       b.bone_name,
       j.joint_details
FROM joints j
JOIN bones b
ON j.bone_id = b.bone_id
WHERE j.joint_id = 1;