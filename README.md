# ray-exploration

Exploration of the use of [ray](https://docs.ray.io/en/latest/index.html) for
data processing pipelines in k8s:

> Ray is an open-source unified framework for scaling AI and Python
> applications. It provides the compute layer for parallel processing so that
> you don’t need to be a distributed systems expert.


## Configuring Ray on Kubernetes

The [Ray on
Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html) docs
provides a good starting point. Follow the [RayCluster
Quickstart](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/raycluster-quick-start.html#kuberay-raycluster-quickstart)
to learn how to deploy the `KubeRay` operator and `RayCluster` custom resource
using [Helm](https://helm.sh/).

> [!WARNING]
> If using a local Rancher instance of k8s, you may need to increase CPU and
> memory resource limits. We reccomend giving Rancher 50-75% of available cores,
> and 50% of memory


## Submitting jobs

First, create a local python env w/ `ray` installed, and activate the env.

```
mamba env create -f environment.yml
mamba activate ray-exploration
```

Then, use the `ray submit` command to submit jobs:

> [!NOTE]
> These examples assume you have port-forwarded the kuberay head service as
> described in the [RayCluster
> Quickstart](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/raycluster-quick-start.html#method-2-submit-a-ray-job-to-the-raycluster-via-ray-job-submission-sdk)

```
ray job submit --address http://localhost:8265 -- python -c "import ray; ray.init(); print('hello world')"
```

You can submit a python script that uses ray like this:

```
ray job submit --working-dir ./ -- python ray_example.py
```


## Additional resources

* [RayCluster Configuration](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/config.html)
* [Quickstart using the Ray Jobs CLI](https://docs.ray.io/en/latest/cluster/running-applications/job-submission/quickstart.html)
