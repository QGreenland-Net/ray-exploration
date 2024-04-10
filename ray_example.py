import subprocess

import ray

ray.init()

# Define the square task.
@ray.remote
def square(x):
    return x * x

@ray.remote
def hostname():
    result = subprocess.run("hostname")
    return result

futures = [hostname.remote() for i in range(10)]
# Retrieve results.
print(ray.get(futures))
