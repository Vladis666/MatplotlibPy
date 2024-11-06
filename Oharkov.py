from graphviz import Digraph


def create_app_schema():
    # Create a new directed graph
    dot = Digraph(comment='Flask Application Schema')
    dot.attr(size='30,30')
    # Define nodes for each route and function
    dot.node('A', 'Flask App')
    dot.node('B', 'Home (/ or /index)')
    dot.node('C', 'About (/about)')
    dot.node('D', 'Contacts (/contacts)')
    dot.node('E', 'Contact Form (/contact)')

    # Define edges (relationships)
    dot.edges(['AB', 'AC', 'AD', 'AE'])

    # Optional: Add details about each function
    dot.node('F', 'Renders index_pro.html')
    dot.node('G', 'Renders about_pro.html\nMenu: [Service 0, Service 1, Service 2]')
    dot.node('H', 'Renders contacts_pro.html')
    dot.node('I', 'Handles form input\nRenders contact_pro.html')

    # Connect functions to their respective routes
    dot.edge('B', 'F')
    dot.edge('C', 'G')
    dot.edge('D', 'H')
    dot.edge('E', 'I')

    # Save the graph to a file
    dot.render('flask_app_schema', format='png', cleanup=True)


if __name__ == '__main__':
    create_app_schema()
