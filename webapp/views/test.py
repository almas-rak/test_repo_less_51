cat = {'name': None, 'age': 4, 'happy': 10, 'satiety': 40, 'status': 'not_sleep'}

def stats_cat():
    if request.method == 'GET':
        render index
    else:
        if not cat['name']:
            cat['name'] = request.POST.get('name')
        action = request.POST.get('action')
        if action == 'play':

