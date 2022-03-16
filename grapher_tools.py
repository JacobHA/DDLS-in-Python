from numpy import sin, cos, linspace, outer, ones, pi, meshgrid
from plotly.graph_objs import Figure, Surface, Layout
import os


def figure_saver(fig, filename, rx, ry, rz):
    
    rs = [rx,ry,rz]
    RX, RY, RZ = [i/max(rs) for i in rs]

    layout = Layout(
        title=filename,
        autosize=True,

        scene=dict(
            aspectmode = 'manual',
            aspectratio = {'x': RX, 'y': RY, 'z': RZ},
            xaxis_title='x [nm]',
            yaxis_title='y [nm]',
            zaxis_title='z [nm]',
            
        ),

    )

    
    # Write the figure to html file and auto open
    save_location = f'{os.getcwd()}/{filename}.html'
    fig.update_layout(layout)
    fig.update_traces(showscale=False)

    fig.write_html(save_location, auto_open=True)

    print(f'File saved at {save_location}')


def sphere_plotter(filename, rx,ry,rz):
    #just a sphere
    theta = linspace(0,2*pi,100)
    phi = linspace(0,pi,100)
    x = outer(cos(theta),sin(phi))
    y = outer(sin(theta),sin(phi))
    z = outer(ones(100),cos(phi))  # note this is 2d now

    x *= rx
    y *= ry
    z *= rz

    data = Surface(
            x=x,
            y=y,
            z=z,
            colorscale='plotly3',
            opacity=0.9,              
    )

    fig = Figure(data=data)

    figure_saver(fig, filename, rx, ry, rz)



# Based on https://community.plotly.com/t/basic-3d-cylinders/27990

def cylinder(r, h, a=0, nt=100, nv = 50):
    """
    parametrize the cylinder of radius r, height h, base point a
    """
    theta = linspace(0, 2*pi, nt)
    v = linspace(a, a + h, nv )
    theta, v = meshgrid(theta, v)
    x = r*cos(theta)
    y = r*sin(theta)
    z = v
    return x, y, z

# Not working:
def boundary_circle(r, h, nt=100):
    """
    r - boundary circle radius
    h - height above xy-plane where the circle is included
    returns the circle parameterization
    """
    theta = linspace(0, 2*pi, nt)
    x = r*cos(theta)
    y = r*sin(theta)
    z = h*ones(theta.shape)
    return x, y, z


def cylinder_plotter(filename, r, h, a = 0, nt=100, nv =50):

    # Create the cylinder
    x, y, z = cylinder(r, h, a=a, nt=nt, nv=nv)

    cyl = Surface(x=x, y=y, z=z,
                    colorscale = 'plotly3',
                    opacity=0.9
                    )


    fig =  Figure(data=[cyl])

    figure_saver(fig, filename, r, r, h)

