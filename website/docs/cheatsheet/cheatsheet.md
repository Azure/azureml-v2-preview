---
title: Cheat Sheet
id: cheatsheet
slug: /cheatsheet/
---

### Basic setup

**Connect to workspace.**

```python
az ml workspace init
```

For more details: [Workspaces](workspace)

**Prepare Python environment.**  
You can use a `requirements.txt` file to define a Python environment on your compute.

```yaml
az ml environment create --id pytorchenv --from-pip path/to/requirements.txt
```

You can also use conda environments and docker images to prepare your environments.  

For more details: [Environment](environment)

### Submit code

To run code in AML you need to:

1. **Configure**: Configuration includes specifying the code to run, the compute
target to run on and the Python environment to run in.
2. **Submit**: Create or reuse an AML Experiment and submit the run.

#### Create Job

```python
az ml job create thejob.yaml
```

This will take you to the Azure ML Studio where you can monitor your run.

### Connect to data

To work with data in your training scripts using your workspace `ws` and its default datastore:

```python
linked_service_id: ws_default_datastore
path: path/on/datastore>
```

For more details see: [Data](data)
