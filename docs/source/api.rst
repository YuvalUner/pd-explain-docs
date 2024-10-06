.. _exp_dataframe:

=============================================
ExpDataFrame Class API
=============================================

Overview
--------

`ExpDataFrame` is a specialized DataFrame class that extends the functionality of the popular pandas DataFrame. It is designed to provide additional capabilities for explaining data operations applied to DataFrames, making it easier to understand and work with data transformations.

.. inheritance-diagram:: ExpDataFrame
   :parts: 1

Key Attributes
--------------

- `operation`: An object representing the data operation that led to the current state of the DataFrame.
- `explanation`: A high-level explanation of the data operation.
- `filter_items`: A list of column names that have been filtered or selected from the DataFrame.

Methods
-------
ef explain(self, schema: dict = None, attributes: List = None, top_k: int = None, explainer='fedex', target=None, dir=None,
                figs_in_row: int = 2, show_scores: bool = False, title: str = None, corr_TH: float = 0.7, consider='right', value=None, attr=None, ignore=[]):


.. method:: explain(schema=None, attributes=None, top_k=1, figs_in_row=2, show_scores=False, title=None, corr_TH=0.7)

    Generate explanations for the DataFrame based on the applied data operation.

    :param schema: A dictionary specifying result columns and optionally renaming columns.
    :type schema: dict, optional
    :param attributes: A list of specific columns to consider in the explanation.
    :type attributes: list, optional
    :param top_k: The number of top explanations to generate.
    :type top_k: int, optional
    :param explainer: The explainer the user wishes to use for the explanation generation.
    :type explainer: string, optional
:param target: The target group of outlier explainer
    :type target: string, optional
:param dir: The direction of outlier for the explainer, either "high" or "low".
    :type dir: string, optional
    :param figs_in_row: The number of explanation figures to display in one row.
    :type figs_in_row: int, optional
    :param show_scores: Show scores on the explanation figures.
    :type show_scores: bool, optional
    :param title: A title for the explanation.
    :type title: str, optional
    :param corr_TH: The threshold for correlation between features.
    :type corr_TH: float, optional
    :param consider: Specifies which table to consider in shapley join explanations.
    :type consider: string, optional
    :param attrs: Specifies which attributes to consider in the explanations.
    :type attrs: list, optional

    :return: Explanation Figures

.. method:: present_deleted_correlated(figs_in_row=2)

    Generate explanations for features that were removed due to high correlation with other features.

    :param figs_in_row: The number of explanation figures to display in one row.
    :type figs_in_row: int, optional
    :return: Explanation Figures

.. method:: copy(deep=True)

    Create a copy of the `ExpDataFrame`.

    :param deep: If `True`, make a deep copy, including data and indices.
    :type deep: bool, optional
    :return: A copy of the `ExpDataFrame`.
