SELECT * FROM users;

SELECT * FROM friendships;

INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Franklin', 'Roosevelt', now(), now()), ('Abraham', 'Lincoln', now(), now()), ('John', 'Kennedy', now(), now()), ('George', 'Washington', now(), now());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 3, now(), now()), (3, 2, now(), now()), (3, 4, now(), now()), (4, 2, now(), now());


SELECT users.first_name, users.last_name, users2.first_name as friend_firstname, users2.last_name as friend_lastname
FROM users
LEFT JOIN friendships ON friendships.user_id = users.id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;
 


