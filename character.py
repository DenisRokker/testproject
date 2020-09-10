import psycopg2


class Character:
    def __init__(self, name, power, intellect, dexterity, health):
        self.name = name
        self.health = health
        self.power = power
        self.intellect = intellect
        self.dexterity = dexterity

        self.has_sword = False

    def add_inventory(self, inventory):
        self.power += inventory.power
        self.intellect += inventory.intellect
        self.dexterity += inventory.dexterity
        self.health += inventory.health

    def save(self):
        """
            Saving character to database
        """

        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
        cursor = conn.cursor()

        # Insert
        cursor.execute(
            "INSERT INTO players (name, health, power, intellect, dexterity) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (self.name, self.health, self.power, self.intellect, self.dexterity),
        )

        player_id = cursor.fetchone()[0]

        conn.commit()
        cursor.close()
        conn.close()

        return player_id
