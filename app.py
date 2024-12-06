import marimo

__generated_with = "0.9.31"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(r"""# Secret Santa""")
    return


@app.cell
def __input_names_a(mo):
    names_A = mo.ui.text(placeholder="A,B,C...")
    names_B = mo.ui.text(placeholder="A,B,C...")

    # Create shuffle button with conditional enabling
    mo.md(
        f"""
        Enter a comma-separated list of names for the 1st group: {names_A}

        Enter a comma-separated list of names for the 2nd group: {names_B}
        """
    )
    return names_A, names_B


@app.cell
def __(mo, names_A, names_B):
    from random import shuffle

    aa = list([name.strip() for name in names_A.value.split(",") if name.strip()])
    bb = list([name.strip() for name in names_B.value.split(",") if name.strip()])

    shuffle(aa)
    shuffle(bb)

    mo.md(
        f"""
        Shuffled 1st group: {aa}

        Shuffled 2nd group: {bb}
        """
    )


@app.cell
def __():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
