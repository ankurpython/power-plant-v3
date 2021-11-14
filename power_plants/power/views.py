import pandas as pd
from django_filters.rest_framework import DjangoFilterBackend
from matplotlib import pyplot as plt
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class PlantStates(ModelViewSet):
    serializer_class = GeneratorSerializer
    queryset = PowerGenerator.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant_state', 'plant_code']


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class Map(ModelViewSet):
    serializer_class = GeneratorSerializer
    queryset = PowerGenerator.objects.filter(plant_state='AK')
    pagination_class = LargeResultsSetPagination

    
class LibMap(ModelViewSet):
    def list(self, request, *args, **kwargs):
        queryset = PowerGenerator.objects.filter(plant_state='AK').values('plant_name', 'annual_net_gen')
        df = pd.DataFrame(queryset)
        x = df['plant_name'].to_numpy()
        y = df['annual_net_gen'].to_numpy()

        plt.bar(x, y)
        response = HttpResponse(content_type='image/png')
        plt.show()
        return response



'''Data for plotting
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='time (s)', ylabel='voltage (mV)',
               title='About as simple as it gets, folks')
        ax.grid()

        response = HttpResponse(content_type='image/png')
        canvas = FigureCanvasAgg(fig)
        canvas.print_png(response)'''

'''.values('plant_name', 'annual_net_gen')
        df = pd.DataFrame(queryset)
        x = df['plant_name'].to_numpy()
        y = df['annual_net_gen'].to_numpy()

        plt.bar(x, y)
        response = HttpResponse(content_type='image/png')
        plt.show()
        return response'''
