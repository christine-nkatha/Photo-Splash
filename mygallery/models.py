from django.db import models


class LocationModel(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self) -> str:
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self) -> str:
        return self.name
class ImageModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    location = models.ForeignKey(LocationModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def save_image():
        pass

    def delete_image():
        pass

    def get_image_by_id():
        pass

    def search_image(category):
        pass

    def filter_by_location(location):
        pass



