from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import *

#keep this code for example
# def preferences(request):
#     walk_city = Walk.objects.order_by('-city')[:50]
#     return render(request, 'preferences.html', {'cities': walk_city})

'''
user 
'''

def preferences(request):
  return HttpResponse("Hello, world. You're at the polls index.")
  # searchVectors = ['approp_title', 'year', 'county', 'expended_amount_min', 'expended_amount_max']
  # for i in searchVectors:
  #   if i in request.GET and request.GET[i]:

  #     kwargs = {}

  #     project_name = request.GET.get('approp_title', None)
  #     if project_name:
  #       kwargs['approp_title__contains'] = project_name


      # year = request.GET.get('year', None)
      # if year:
      #   kwargs['year'] = year

      # county = request.GET.get('county', None)
      # if county:
      #   kwargs['county'] = county

      # expended_amount_min = request.GET.get('expended_amount_min', None)
      # if expended_amount_min:
      #   kwargs['expended_amount__gte'] = expended_amount_min

      # expended_amount_max = request.GET.get('expended_amount_max', None)
      # if expended_amount_max:
      #   kwargs['expended_amount__lte'] = expended_amount_max 

      # results = Projects.objects.filter(**kwargs)
      # # import pdb; pdb.set_trace()

      # results_table = ProjectsTable(results)
      # RequestConfig(request, paginate={"per_page": 100}).configure(results_table)
      
      # if str(request.GET.get('approp_title')) == 'None':
      #   queryresult = ""
      # else: 
      #   queryresult = request.GET.get('approp_title')

      # return render(request, 'results.html', 
      #     {'projects': results_table, 'query': queryresult, 'years':
      #      pretty_results(years), 'counties': pretty_results(counties), 
      #      'expended_amount_min': expended_amount_min, 
      #      'expended_amount_max': expended_amount_max,
      #      'searchPath': request.get_full_path(), 
      #      'basePath': request.build_absolute_uri('/')})

      # return kwargs


def priorities(request):
    # walk_city = Walk.objects.order_by('-city')[:50]
    # return render(request, 'priorities.html', {'cities': walk_city})
    return HttpResponse("PITOOO")
    if request.session.test_cookie_worked():
      request.session.delete_test_cookie()
      return HttpResponse("You're logged in.")
    else:
      return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    

    # kwargs = {}
    # return kwargs

#each view has to return an httpresponse or exception
'''
func to get kwargs, transform and get data from model objects

getting data:
Walk.objects.get(city='Chicago')
.filter(**kwargs)
.exlucde(**kwargs)
.get().filter()
.filter(something __lt=10)
.filter(city__inexact="Chicago")
.filter(city__icontains="Chicago")

get data from multiple table objects

'''

