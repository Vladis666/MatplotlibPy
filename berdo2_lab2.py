import schemdraw
import schemdraw.elements as elm

# 1. Black-box model scheme
def black_box_model():
    with schemdraw.Drawing() as d:
        d += elm.RBox(w=5, h=2, label='System', fill='lightgray')
        d += elm.Arrow().left().at((2.5, 1)).label('Input')
        d += elm.Arrow().right().at((2.5, -1)).label('Output')
        d.save('black_box_model.png')  # Save as an image file
        print("Black-box model saved as 'black_box_model.png'")

# 2. System composition model scheme
def system_composition_model():
    with schemdraw.Drawing() as d:
        d += elm.RBox(w=4, h=2, label='Subsystem 1', fill='lightblue')
        d += elm.Arrow().right().at((2, 1)).length(1)
        d += elm.RBox(w=4, h=2, label='Subsystem 2', fill='lightgreen').at((3, 0))
        d += elm.Arrow().right().at((5, 1)).length(1)
        d += elm.RBox(w=4, h=2, label='Subsystem 3', fill='lightyellow').at((6, 0))
        d += elm.Arrow().right().at((8, 1)).length(1)
        d += elm.RBox(w=4, h=2, label='Final Output', fill='lightgray').at((9, 0))
        d.save('system_composition_model.png')  # Save as an image file
        print("System composition model saved as 'system_composition_model.png'")

# 3. Flowchart model
def flowchart_model():
    with schemdraw.Drawing() as d:
        d += elm.Start().label('Start')
        d += elm.Arrow().down()
        d += elm.RBox(label='Process 1').down()
        d += elm.Arrow().down()
        d += elm.Decision().label('Condition?')
        d += elm.Arrow().left().label('Yes')
        d += elm.RBox(label='Process 2').left()
        d += elm.Arrow().down().at((2, -4)).label('End')
        d.save('flowchart_model.png')  # Save as an image file
        print("Flowchart model saved as 'flowchart_model.png'")

# 4. Block diagram
def block_diagram():
    with schemdraw.Drawing() as d:
        d += elm.RBox(w=4, h=2, label='Block 1', fill='lightblue')
        d += elm.Arrow().right().at((2, 0)).length(2)
        d += elm.RBox(w=4, h=2, label='Block 2', fill='lightgreen').at((4, 0))
        d += elm.Arrow().right().at((6, 0)).length(2)
        d += elm.RBox(w=4, h=2, label='Block 3', fill='lightyellow').at((8, 0))
        d.save('block_diagram.png')  # Save as an image file
        print("Block diagram saved as 'block_diagram.png'")

# Call each scheme
black_box_model()
system_composition_model()
flowchart_model()
block_diagram()
