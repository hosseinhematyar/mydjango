from django.shortcuts import render

# from django.http import HttpResponse


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce website',
        'description': 'Fully functional ecommerce website',
    },
    {
        'id': '2',
        'title': 'Portfolio website',
        'description': 'This was a project where I built out my portfolio',
    },
    {
        'id': '3',
        'title': 'Social website',
        'description': 'Awesome open source project I am still working',
    }
]


def projects(request):
    # return HttpResponse('Here are our projects')
    page = 'Projects List'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    # return HttpResponse('Single Project' + ' ' + str(pk))
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
