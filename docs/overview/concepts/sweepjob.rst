Hyperparameter tune (SweepJob)
------------------------------

A SweepJob executes a hyperparameter sweep over a specified search space for your training code. The below example uses the command job from the previous section as the 'trial' job in the sweep. It sweeps over different learning rates and subsample values for each trial job. The search space parameters will be passed as arguments to the command in the trial job.

.. literalinclude:: ../../examples/iris/iris_sweep.yml
   :language: yaml

This can be executed by running (after setting compute name in yaml):

.. code-block:: console

    az ml job create --file iris_sweep.yml
