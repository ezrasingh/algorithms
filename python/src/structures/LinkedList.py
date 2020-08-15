from copy import deepcopy
from Data import DataNode

class LinkedList(object):
    ''' initialize the data structure '''
    def __init__(self, state=[None]):
        if isinstance(state, (list, tuple)):
            state = state[::-1] # ? reverse the state to feed forward data
            self.head = DataNode(state[0])
            for data in state[1:]:
                self.prepend(data)
        else:
            self.head = DataNode(state)

    ''' add node to the beginning of the list '''
    def prepend(self, data):
        # ? O(1)
        self.head = DataNode(data, self.head)
        return self

    ''' add node to the end of the list '''
    def append(self, data):
        cursor = self.head
        # ? O(n)
        while isinstance(cursor, DataNode):
            if not cursor.next:
                if isinstance(data, DataNode):
                    cursor.next = data
                else:
                    cursor.next = DataNode(data)
                break
            else:
                cursor = cursor.next
        return self

    ''' add data between node by key '''
    def insert(self, data, destination):
        cursor = self.head
        # ? O(n)
        while isinstance(cursor, DataNode):
            if cursor.key == destination:
                cursor.next = DataNode(data, cursor.next)
                break
            elif not cursor.next:
                raise KeyError("No node with that key found")
            else:
                cursor = cursor.next
        return self

    ''' update data stored within a node '''
    def update(self, target, data):
        cursor = self.head
        # ? O(n)
        while isinstance(cursor, DataNode):
            if cursor.key == target:
                cursor.data = data
                break
            elif not cursor.next:
                raise KeyError("No node with that key found")
            else:
                cursor = cursor.next
        return self

    ''' remove node from the list by key '''
    def delete(self, target):
        predeccessor = None
        cursor = self.head
        # ? O(n)
        while isinstance(cursor, DataNode):
            if cursor.key == target:
                if predeccessor:
                    predeccessor.next = cursor.next
                else:
                    self.head = cursor.next
                del cursor
                break
            elif not cursor.next:
                raise KeyError("No node with that key found")
            else:
                predeccessor = cursor
                cursor = cursor.next
        return self

    ''' search list for node by key '''
    def search(self, key):
        key = int(key)
        cursor = self.head
        # ? O(n)
        while isinstance(cursor, DataNode):
            if cursor.key == key:
                # ? node found at cursor
                return cursor
            elif not cursor.next:
                # ? node not found
                return None
            else:
                cursor = cursor.next

    ''' apply reducer function sequentially across all nodes, alters list state '''
    def mutate(self, reducer):
        cursor = self.head
        # ? O(n)
        while isinstance(cursor, DataNode):
            cursor.data = reducer(key=cursor.key, data=cursor.data, collection=self)
            if cursor.next:
                cursor = cursor.next
            else:
                break
        return self

    ''' print data representation '''
    def __str__(self):
        return str(self.head)

    ''' implement list concatination '''
    def __add__(self, list):
        # ? O(n)
        return deepcopy(self).append(list.head)

    ''' determine size of list '''
    def __len__(self):
        cursor = self.head
        accumulator = 1
        # ? O(n)
        while isinstance(cursor, DataNode):
            if not cursor.next:
                break
            else:
                accumulator += 1
                cursor = cursor.next
        return accumulator

''' example reducer function '''
def lowercase(key, data, collection):
    return str(data).lower()

''' driver code '''
if __name__ == '__main__':
    List = LinkedList(state=[12, 10, 9])
    print(List)
    print(List.update(1, 'UPADTE'))
    print(List.insert('INSERT', 2))
    print(List.delete(2))
    print(List.delete(0))
    print(List.mutate(lowercase))