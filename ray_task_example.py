"""Simple example of a Ray task.

See: https://docs.ray.io/en/latest/ray-core/tasks.html#ray-remote-functions
"""
import subprocess

import ray

ray.init()

@ray.remote
def hostname():
    result = subprocess.run("hostname")
    return result

futures = [hostname.remote() for i in range(10)]
# Retrieve results.
print(ray.get(futures))
