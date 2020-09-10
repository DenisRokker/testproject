
CREATE TABLE players (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY NOT NULL,

    name TEXT NOT NULL,
    health INT NOT NULL,
    power INT NOT NULL,
    intellect INT NOT NULL,
    dexterity INT NOT NULL
);

CREATE TABLE inventory (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY NOT NULL,

    name TEXT NOT NULL,
    health INT NOT NULL,
    power INT NOT NULL,
    intellect INT NOT NULL,
    dexterity INT NOT NULL,

    player_id INT NOT NULL,

    FOREIGN KEY (player_id) REFERENCES players(id),
);
