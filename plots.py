import data

def indicator(x, plot_title):

    graph = dict(
        data = [
            dict(
                mode = "number+delta",
                value = x,
                type = 'indicator',
                domain = {'x': [0.5, 0], 'y': [0.5, 1]}
            )
        ],
        layout = dict(
            height = 200, 
            title = '<b>' + plot_title + '<b>',
            titlefont = dict(size = 12, color = '#51a9dc'),
            margin = dict(t=50, r=0, l=0, b=0, pad=400)
        )
    )
    return graph

def line_plot(x, y, labels, plot_title, x_title, y_title):
    graph = dict(
        data = [
            dict(
                x = x,
                y = y,
                text = labels,
                mode = 'lines+markers',
                line = dict(color = '#803f98', width=3),
                type = 'scatter',
                marker = dict(size=9)
            )
        ],
        layout = dict(
            title = '<b>' + plot_title + '<b>',
            titlefont = dict(size = 13, color = '#51a9dc'),
            margin = dict(t=50, r=20, l=60, b=100),
            xaxis = dict(title = x_title, tickfont = dict(size = 11)),
            yaxis = dict(title = y_title)
        )
    )
    return graph

def line_plot_2(x, y1, y2, labels, plot_title, x_title, y_title):
    graph = dict(
        data = [
            dict(
                x = x,
                y = y1,
                text = labels,
                mode = 'lines+markers',
                name = 'Total Revenue',
                line = dict(color = '#803f98', width=3),
                type = 'scatter',
                marker = dict(size=9)
            ),
            dict(
                x = x,
                y = y2,
                text = labels,
                mode = 'lines+markers',
                name = 'Scholarship Amount Given',
                line = dict(color='#000000', width=3),
                type = 'scatter',
                marker = dict(size=9)
            )
        ],
        layout = dict(
            title = '<b>' + plot_title + '<b>',
            titlefont = dict(size = 13, color = '#51a9dc'),
            margin = dict(t=50, r=20, l=60, b=100),
            xaxis = dict(title = x_title, tickfont = dict(size = 11)),
            yaxis = dict(title = y_title)
        )
    )
    return graph

def pie_plot(x, y, plot_title):
    graph = dict(
        data = [
            dict(
                labels = x,
                values = y,
                type = 'pie'
            )
        ], 
        layout = dict(
            height = 300,
            title = '<b>' + plot_title + '<b>',
            titlefont = dict(size = 12, color='#51a9dc'),
            margin = dict(t=50, r=10, l=10, b=0, pad=4)
        )
    )
    return graph

def dot_plot(plot_title):
    graph = dict(
        data = [
            dict(
                type='scatter',
                x = x_val,
                y = y_val,
                mode = 'markers',
                marker = dict(color='#803f98', line = dict(color='rgba(156, 16665, 196, 1.0)', width=1),symbol='circle', size=16)
            )
        ],
        layout = dict(
            title = '<b>' + plot_title + '<b>',
            xaxis = dict(
                showgrid = False, 
                showline=True, 
                linecolor='rgb(102,102,102)', 
                titlefont=dict(
                    font=dict(
                        color='rgb(204,204,204)'
                    )
                ), 
                autotick=False, 
                dtick=10, 
                ticks='outside',
                tickcolor='rbg(102,102,102)'),
                margin = dict(l=140, r=40, b=50, t=80)
        )
    )
    return graph