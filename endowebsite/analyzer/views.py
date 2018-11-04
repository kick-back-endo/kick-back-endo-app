import json

from django.shortcuts import render

from .tracker_data_parsers import parse_clue_data
from .symptom_checker import symptom_checker


def analize(request):
    loaded_file = request.FILES['file']
    data = json.loads(loaded_file.read())
    parsed_data = parse_clue_data(data)
    result = symptom_checker(parsed_data)
    return render(request, 'analyzer/results.html', {'result': result})
