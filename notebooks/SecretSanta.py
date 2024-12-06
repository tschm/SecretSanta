import marimo

__generated_with = "0.9.31"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(r"""# Secret Santa""")
    return


@app.cell
def __():
    from random import shuffle
    import collections

    return collections, shuffle


@app.cell
def __(collections):
    # We are using collections as we want to use the rotate function
    groupA = collections.deque(["A", "B", "C"])
    groupB = collections.deque(["D", "E", "F"])
    return groupA, groupB


@app.cell
def __(groupA, groupB, shuffle):
    # We have two groups of equal length
    # A pair is always between members of the two different groups
    assert len(groupA) == len(groupB)
    shuffle(groupA)
    shuffle(groupB)
    return


@app.cell
def __(groupA, groupB):
    for _x, _y in zip(groupA, groupB):
        print(_x, _y)
    return


@app.cell
def __(groupA, groupB):
    groupA.rotate(-1)
    for _x, _y in zip(groupB, groupA):
        print(_x, _y)
    return


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
