"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["25/12/2021"],
            "answer": "2021-12-25"
        },
        {
            "input": ["01/01/2000"],
            "answer": "2000-01-01"
        },
        {
            "input": ["15/06/1995"],
            "answer": "1995-06-15"
        },
        {
            "input": ["29/02/2020"],
            "answer": "2020-02-29"
        },
        {
            "input": ["10/10/2010"],
            "answer": "2010-10-10"
        },
        {
            "input": ["31/05/1985"],
            "answer": "1985-05-31"
        },
        {
            "input": ["07/08/1960"],
            "answer": "1960-08-07"
        },
        {
            "input": ["02/09/1999"],
            "answer": "1999-09-02"
        },
        {
            "input": ["30/04/1975"],
            "answer": "1975-04-30"
        },
        {
            "input": ["29/02/2019"],
            "answer": "Error: Invalid date."
        },
        {
            "input": ["30/04/1975/1"],
            "answer": "Error: Invalid date."
        },
    ],
    "Extra": [
        {
            "input": ["04/07/2004"],
            "answer": "2004-07-04"
        },
        {
            "input": ["13/13/2013"],
            "answer": "Error: Invalid date."
        },
        {
            "input": ["31/04/2013"],
            "answer": "Error: Invalid date."
        },
    ]
}
