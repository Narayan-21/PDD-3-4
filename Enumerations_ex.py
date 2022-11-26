from enum import Enum

class Phase(Enum):
    READY = 'ready'
    RUNNING = 'running'
    FINISHED = 'finished'

    def __str__(self):
        return self.value
    def __eq__(self, other):
        if isinstance(other, Phase):
            return self is other
        elif isinstance(other, str):
            return self.value == other
        return False
    def __lt__(self, other):
        ordered_items = list(Phase)
        self_order_index = ordered_items.index(self)
        if isinstance(other, Phase):
            other_order_index = ordered_items.index(other)
            return self_order_index < other_order_index
        if isinstance(other, str):
            try:
                other_member = Phase(other)
                other_order_index = ordered_items.index(other_member)
                return self_order_index < other_order_index
            except ValueError:
                return False
        
print(Phase.READY == 'ready')
print(Phase.READY < Phase.RUNNING)
print(Phase.READY < 'finished')
