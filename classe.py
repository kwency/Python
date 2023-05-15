from datetime import datetime


class Command:
    def __init__(self, name):
        self.name = name
        self.timestamp = datetime.now()
        self.next = None
        self.prev = None


class CommandHistory:
    def __init__(self):
        self.commands = {}

    def add_command(self, user_id, command_name):
        command = Command(command_name)
        if user_id not in self.commands:
            self.commands[user_id] = command
        else:
            last_command = self.commands[user_id]
            while last_command.next is not None:
                last_command = last_command.next
            last_command.next = command
            command.prev = last_command

    def get_last_command(self, user_id):
        if user_id not in self.commands:
            return None
        last_command = self.commands[user_id]
        while last_command.next is not None:
            last_command = last_command.next
        return last_command.name

    def get_all_commands(self, user_id):
        if user_id not in self.commands:
            return []
        commands = []
        current_command = self.commands[user_id]
        while current_command is not None:
            commands.append(current_command.name)
            current_command = current_command.next
        return commands

    def get_previous_command(self, user_id):
        if user_id not in self.commands:
            return None
        current_command = self.commands[user_id]
        while current_command.next is not None:
            current_command = current_command.next
        return current_command.prev.name if current_command.prev is not None else None

    def get_next_command(self, user_id):
        if user_id not in self.commands:
            return None
        current_command = self.commands[user_id]
        while current_command.next is not None:
            current_command = current_command.next
        return current_command.next.name if current_command.next is not None else None

    def clear_history(self, user_id):
        if user_id in self.commands:
            del self.commands[user_id]


class hashtable_user:
    def __init__(self, bucket_size):
        self.buckets = []  # on dit que buckets est une liste
        for i in range(bucket_size):
            # on dit que dans buckets on ajoute des listes vident
            self.buckets.append([])


# on indique une clé et une valeur ex "nom" (clé) : "Marie Richardson" (valeur)
def append(self, key, value):
    # on hash la clé et nous donne le resultat de la clé avec des int
    hash_key = hash(key)
    # on fait un modulo avec la longeur de buckets pour avoir exactement le bon nombre de listes en fonction de sa longueur
    indice_bucket = hash_key % len(self.buckets)
    # on ajoute a la case bucket key + valeur
    self.buckets[indice_bucket].append((key, value))
    # dans buckets ca va ajouté dedans ex [  ,Marie Richardson,  ]


def get(self, key):
    hashed_key = hash(key)
    indice_bucket = hashed_key % len(self.buckets)
 # Pour la clé et la valeur dans buckets dans son indice (case) si clé est = à la clé (correspond à la bonne case) on retourne la valeur
    for bucket_key, bucket_value in self.buckets[indice_bucket]:
        if bucket_key == key:
            return bucket_value
    return None
