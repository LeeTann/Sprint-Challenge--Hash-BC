#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    
    # source - destination
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # get the location that start w/ NONE
    location = hash_table_retrieve(hashtable, "NONE")

    for i in range(length):
        route[i] = location
        print(route[i])
        location = hash_table_retrieve(hashtable, route[i])
        print("connecting", location)
    
    return route
