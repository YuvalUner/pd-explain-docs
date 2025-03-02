.. _explain-function-many-to-one-explainer:

Many to One Explainer
=====================
The `many to one` explainer creates rule based explanations for many to one relationships.
It provides insights into how the input features define groups of output features.

Many to One Explainer Usage Example
-----------------------------------
.. code-block::

    # Import the necessary libraries
    import pandas as pd
    import pd_explain

    # Load the "adult" dataset
    adult = pd.read_csv(r'C:\adult.csv')

    # Call the many to one explainer
    adult.explain(explainer='many_to_one', labels='class')

**Output**:
.. table::
    +-----------------+----------------------------------------------------------+----------+------------------+--------------------------+
    | Group / Cluster | Explanation                                              | Coverage | Separation Error | Separation Error Origins |
    +=================+==========================================================+==========+==================+==========================+
    | <=50K           | 1 <= education-num <= 10                                 | 0.75     | 0.15             | 100.00% from group >50K  |
    | <=50k           | 0 <= capital-gain <= 5095.5                              | 1.0      | 0.21             | 100.00% from group >50K  |
    | <=50k           | 0 <= capital-gain <= 5095.5 AND 1 <= education-num <= 10 | 0.75     | 0.13             | 100.00% from group >50K  |
    | <=50k           | 0 <= capital-gain <= 4243.5                              | 0.99     | 0.2              | 100.00% from group >50K  |
    | >50K            | No explanation found                                     | NaN      | NaN              | NaN                      |
    +-----------------+----------------------------------------------------------+----------+------------------+--------------------------+

Coverage is the % of the group that is covered by the explanation.
Separation Error is the % of data outside the group that is covered by the explanation.

Parameters
-----------------------------------
- ``labels`` (str | list | Series | DataFrame | ndarray | None): The labels defining the many to one relationship. Can be a name (or list of names) of a column in the DataFrame, a Series, a DataFrame, a numpy array, or None. None is only applicable for when the explainer is called on the result of a GroupBy operation, in which case the GroupBy groups will be inferred automatically. Otherwise, the labels must be provided. Defaults to `None`.
- ``coverage_threshold`` (float, optional): The minimum coverage required for an explanation to be considered. Default is `0.7`.
- ``separation_threshold`` (float, optional): The minimum separation error required for an explanation to be considered. Default is `0.3`.
- ``max_explanation_length`` (int, optional): The maximum number of conditions in an explanation. Default is `3`.
- ``p_value`` (float, optional): A scaling parameter for the number of top attributes to consider when generating explanations. Number of attributes to consider = `p_value` * `max_explanation_length`. Default is `1`.
- ``explanation_form`` (str, optional): The form of the explanation. Default is `conjunction`. Other options are `disjunction`.
- ``attributes`` (list, optional): The attributes to consider when generating explanations. Default is `None`.
- ``use_sampling`` (bool, optional): Whether to use sampling to speed up the computation. Default is `True`.
- ``sample_size`` (int, optional): The number of samples to use. Default is `5000`.
- ``prune_if_too_many_labels`` (bool, optional): Whether to prune the labels to a smaller subset if there are too many. Default is `True`.
- ``max_labels`` (int, optional): The number of labels to keep if `prune_if_too_many_labels` is `True`. If there are less labels, no pruning will be performed. Default is `10`.
- ``pruning_method`` (str, optional): The method to use for pruning labels. The options are:

    - `largest`: Keeps the k most frequent labels.
    - `smallest`: Keeps the k least frequent labels.
    - `random`: Keeps k random labels.
    - `max_dist`: Keeps the k labels with the largest mean distance between their centroids and the centroids of other labels, multiplied by the number of samples.
    - `min_dist`: Keeps the k labels with the smallest mean distance between their centroids and the centroids of other labels, multiplied by the number of samples.
    - `max_silhouette`: Keeps k labels with the largest silhouette score, multiplied by the number of samples.
    - `min_silhouette`: Keeps k labels with the smallest silhouette score, multiplied by the number of samples.
    Default is `largest`.

- ``bin_numeric`` (bool, optional): If the labels are numeric, whether to bin them into categories. Default is `False`.
- ``num_bins`` (int, optional): The number of bins to use if `bin_numeric` is `True`. If there are less unique values than `num_bins`, no binning will be performed. Default is `10`.
- ``bin_method`` (str, optional): The method to use for binning. The options are:

    - `uniform`: Bins are of equal width.
    - `quantile`: Bins are of equal frequency.
    Default is `quantile`.

- ``labels_name`` (str, optional): The name to give the labels if they are binned. Default is `Label`. Only needed if the labels do not come from a Series / DataFrame with a name, and will only affect its display in the explanation. For example, you may see `x <= label <= y` as an explanation rule.
- ``explain_errors`` (bool, optional): Whether to provide explanations for the origins of the separation error. Default is `True`.
- ``error_explanation_threshold`` (float, optional): The threshold for much a group must individually contribute to the separation error to appear in the explanation. Groups that contribute less than this will be grouped together. Default is `0.05`.

Other Usage Examples
--------------------
We will now show other examples of how to use the `many_to_one` explainer with different parameters.

Example 1: Explaining Clustering Results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block::

    # Import the necessary libraries
    import pandas as pd
    import pd_explain
    from sklearn.cluster import KMeans

    # Load the adult dataset
    adult = pd.read_csv(r'C:\adult.csv')

    # Perform a clustering operation
    clusters = KMeans(n_clusters=3).fit_predict(adult)

    # Call the many to one explainer
    adult.explain(explainer='many_to_one', labels=clusters)

**Output**:
.. table::
    +-----------------+----------------------------------------------------------------+----------+------------------+-------------------------------+
    | Group / Cluster | Explanation                                                    | Coverage | Separation Error | Separation Error Origins      |
    +=================+================================================================+==========+==================+===============================+
    | 0               | 149278.5 <= fnlwgt <= 1490400                                  | 1.0      | 0.22             | 100.00% from group 1          |
    | 0               | 149278.5 <= fnlwgt <= 1490400 AND 8.5 <= education-num <= 16.0 | 0.87     | 0.21             | 100.00% from group 1          |
    | 1               | 291277.5 <= fnlwgt <= 1490400                                  | 1.0      | 0.0              | Rule has no separation error. |
    | 2               | 13769 <= fnlwgt <= 149278.5                                    | 1.0      | 0.0              | Rule has no separation error. |
    +-----------------+----------------------------------------------------------------+----------+------------------+-------------------------------+






