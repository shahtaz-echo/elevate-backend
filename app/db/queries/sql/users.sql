-- name: get-user-by-email^
SELECT id,
       first_name,
       last_name,
       username,
       email,
       salt,
       hashed_password,
       bio,
       designation,
       image,
       created_at,
       updated_at
FROM users
WHERE email = :email
LIMIT 1;

-- name: get-user-by-username^
SELECT id,
       first_name,
       last_name,
       username,
       email,
       salt,
       hashed_password,
       bio,
       designation,
       image,
       created_at,
       updated_at
FROM users
WHERE username = :username
LIMIT 1;

-- name: create-new-user<!
INSERT INTO users (first_name, last_name, username, email, salt, hashed_password, bio, designation, image)
VALUES (:first_name, :last_name, :username, :email, :salt, :hashed_password, :bio, :designation, :image)
RETURNING id, created_at, updated_at;

-- name: update-user-by-username<!
UPDATE users
SET username        = :new_username,
    email           = :new_email,
    salt            = :new_salt,
    hashed_password = :new_password,
    bio             = :new_bio,
    designation     = :new_designation,
    image           = :new_image,
    updated_at      = now()
WHERE username = :username
RETURNING updated_at;
