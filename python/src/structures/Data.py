
class DataNode(object):
    # ? gloabl id counter
    __id = 0

    ''' load data node '''
    def __init__(self, data, next_node=None):
        self.data = data
        self.__next = next_node
        self.__key = DataNode.__id
        DataNode.__id += 1

    ''' getter method for key, read-only '''
    @property
    def key(self):
        return self.__key

    ''' getter method for next node ref '''
    @property
    def next(self):
        return self.__next

    ''' setter method for next node ref '''
    @next.setter
    def next(self, next_node):
        if isinstance(next_node, DataNode):
            self.__next = next_node
        elif not next_node:
            self.__next = None
        else:
            raise ValueError('Next reference must be an instance of Node or a Falsey value')

    ''' print node representation '''
    def __str__(self):
        return '[ "{}":< {} > ] -> {}'.format(self.key, self.data, '< Nil >' if not self.next else self.next)

''' driver code '''
if __name__ == '__main__':
    node_a = DataNode(12)
    print(node_a)
    node_b = DataNode(40, node_a)
    print(node_b)