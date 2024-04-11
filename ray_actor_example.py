"""
See: https://docs.ray.io/en/latest/ray-core/actors.html#ray-remote-classes
"""
import ray

ray.init()

@ray.remote
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

    def get_counter(self):
        return self.value

# Create an actor from this class.
counter = Counter.remote()
obj_ref = counter.increment.remote()
print(ray.get(obj_ref))
