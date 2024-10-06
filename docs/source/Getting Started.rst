.. _getting-started:

Getting Started
===============

Welcome to the world of **pd-explain**! (This is Itay, test...) This guide will walk you through the essential steps to get started with your data exploration and storytelling journey.

Installation
------------

First, you'll need to install the pd-explain library. You can easily install it using pip:

.. code-block:: bash

    pip install pd-explain

Importing pd-explain
--------------------

Import the library in your Python script or Jupyter Notebook to get started:

.. code-block:: python

    import pd_explain

Reading a Table
---------------

You can read your dataset into an explainable DataFrame (ExpDataFrame) using Pandas. Here's an example of how to read a CSV file:

.. code-block:: python

    import pandas as pd

    # Replace 'your_data.csv' with the path to your dataset
    data = pd.read_csv('your_data.csv')

    # Create an ExpDataFrame from the loaded data
    df = ExpDataFrame(data)

Now you have your dataset loaded into an ExpDataFrame, and you're ready to start exploring and explaining your data.

Making it Explainable
----------------------

The real power of pd-explain lies in its ability to provide explanations for your data transformations. Whether you want to filter, group, or manipulate your data, pd-explain allows you to generate insightful narratives and visualizations to better understand your data.

Explore the documentation to learn more about how to use pd-explain's features for in-depth data exploration and storytelling.

That's it! You're all set to begin your data exploration journey with pd-explain. Dive into the documentation to discover the full range of capabilities and features at your disposal.
