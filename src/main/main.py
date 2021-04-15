from oauth2client.service_account import ServiceAccountCredentials
from plotly import graph_objects as go
from graph import Grapher
import gspread


def main():
    input("Welcome to SigmaDraconis Map! Press ENTER to start!")
    gr = Grapher()
    ########################## Setup google credentials and API access ##########################################
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('src/main/starmap-310623-baf93c6b9991.json', scope)

    gc = gspread.authorize(credentials)
    #############################################################################################################

    # Get records from spread sheet
    wks = gc.open('CSV-SDW-GPS').sheet1

    records_dict = wks.get_all_records()
    objects = []
    annots = []
    for record in records_dict:
        # Make solar bodies
        if record['Visible'] == 'Y':
            objects.append(gr.spheres(record['Size'],record['Colour'],record['X'], record['Y'], record['Z'], record['Name']))
            if record["ShowName"] == 'Y':
                annots.append(gr.annot(record['X'], record['Y'], record['Z']+ record['Size']*2, record['Name']))
    
    layout=go.Layout(title = 'Solar System', showlegend=False,
                paper_bgcolor = 'grey',
                scene = dict(xaxis=dict(title='X', 
                                        titlefont_color='black', 
                                        range=[-10000000,10000000], 
                                        backgroundcolor='black',
                                        color='black',
                                        gridcolor='black'),
                            yaxis=dict(title='Y',
                                        titlefont_color='black',
                                        range=[-10000000,10000000],
                                        backgroundcolor='black',
                                        color='black',
                                        gridcolor='black'
                                        ),
                            zaxis=dict(title='Z', 
                                        titlefont_color='black',
                                        range=[-10000000,10000000],
                                        backgroundcolor='black',
                                        color='white', 
                                        gridcolor='black'
                                        ),
                            aspectmode='manual', #this string can be 'data', 'cube', 'auto', 'manual'
        #a custom aspectratio is defined as follows:
                            aspectratio=dict(x=1, y=1, z=1),
                            annotations=annots
                            ))
    
    
    fig = go.Figure(layout = layout)
    for item in objects:
        fig.add_trace(item)

    fig.show()
    fig.write_html("Solar_system.html")