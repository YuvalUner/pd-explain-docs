.. _explain-function - Global Values:

Global Values
=====================
Here you can find an explanation for global values you can use and control when using pd-explain.

Use Sampling
----------------
The `use_sampling` parameter controls the global behavior of whether sampling is used by default when generating explanations.

Using sampling can greatly speed up explanation generation, albeit at a minor cost to accuracy.

By default, sampling is enabled to provide a balance between speed and accuracy.

To see the value of `use_sampling`:

.. code-block:: python

    import pd_explain
    pd_explain.get_use_sampling_value()

To change the value of `use_sampling`:

.. code-block:: python

    import pd_explain
    pd_explain.toggle_sampling()

Or alternatively:

.. code-block:: python

    import pd_explain
    pd_explain.toggle_sampling(True)

The function `toggle_sampling` will switch the value of `use_sampling` between `True` and `False` if no argument is provided.
Otherwise, it will set the value of `use_sampling` to the provided argument.

This parameter can be overridden for individual explanations by setting the `use_sampling` parameter in the `explain` function.

.. code-block:: python

    some_df.explain(use_sampling=False)
