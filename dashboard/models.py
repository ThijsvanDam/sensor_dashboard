from django.db import models


# class DataList(models.Model):
#     dataItem = models.ForeignKey(Data, on_delete=models.CASCADE)


class Graph(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_updated = models.DateTimeField()


class Data(models.Model):
    value = None
    date = models.DateTimeField()
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value) + " " + self.date.strftime("%m/%d/%Y, %H:%M")


class Location(Data):
    value = models.TextField()


class RoomInhabited(Data):
    value = models.BooleanField()


class Temperature(Data):
    value = models.FloatField()

