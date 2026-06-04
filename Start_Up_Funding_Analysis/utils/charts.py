import plotly.express as px


def line_chart(data, x, y, title):
    fig = px.line(
        data,
        x=x,
        y=y,
        markers=True,
        title=title
    )
    return fig


def bar_chart(data, x, y, title):
    fig = px.bar(
        data,
        x=x,
        y=y,
        title=title
    )
    return fig


def horizontal_bar_chart(data, x, y, title):
    fig = px.bar(
        data,
        x=x,
        y=y,
        orientation="h",
        title=title
    )
    return fig


def pie_chart(data, names, values, title):
    fig = px.pie(
        data,
        names=names,
        values=values,
        hole=0.4,
        title=title
    )
    return fig
