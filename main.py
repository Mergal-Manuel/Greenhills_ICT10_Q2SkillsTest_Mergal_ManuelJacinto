from pyscript import display, document

def clubDefine(e):
    document.getElementById('output').innerHTML = "  "
    clubChoice = (document.getElementById("club").value)

    
    clubname = {
        'math': 'Math Club',
        'science': 'Science Club',
        'varsity': 'Basketball Varsity'
    }
    display(f'{clubname[clubChoice]}', target='output')
    
    clubdesc = {
        'math': 'A group for students who enjoy problem-solving and competitions',
        'science': 'Organization for experiments, research, and science fairs',
        'varsity': 'School’s competitive athletics team'
    }
    display(f'{clubdesc[clubChoice]}', target='output')

    clubmeet = {
        'math': 'mondays 2:30–4:30 PM',
        'science': 'Tuesdays 4:00–5:30 PM',
        'varsity': 'mondays 3:00–5:00 PM'
    }
    display(f'{clubmeet[clubChoice]}', target='output')

    clubloc = {
        'math': 'Room 711',
        'science': 'Laboratory room',
        'varsity': 'Quadrangle'
    }
    display(f'{clubloc[clubChoice]}', target='output')

    clubmod = {
        'math': 'Mr. Tamon',
        'science': 'Mr. Calpo',
        'varsity': 'Sir Amargo'
    }
    display(f'{clubmod[clubChoice]}', target='output')

    clubmembers = {
        'math': 'members: 28',
        'science': 'members: 22',
        'varsity': 'members: 33'
    }
    display(f'{clubmembers[clubChoice]}', target='output')
