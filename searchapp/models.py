from django.db import models


class SiteVisit(models.Model):
    total_visits = models.PositiveIntegerField(default=0)


class tshirtmodel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title_fa = models.TextField()
    caption = models.TextField()
    attributes = models.TextField()
    description = models.TextField()
    image_link = models.URLField(max_length=300)
    embedding = models.JSONField(blank=True, null=True)
    embedding_BGE = models.JSONField(blank=True, null=True)
    embedding_jina = models.JSONField(blank=True, null=True)
    embedding_tooka = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}, {self.title_fa}'


class tshirtmodel_english_json(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title_fa = models.TextField()
    description = models.TextField()
    image_link = models.URLField(max_length=300)
    embedding = models.JSONField(blank=True, null=True)
    embedding_openai = models.JSONField(blank=True, null=True)
    attributes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}, {self.title_fa}'


class pantsmodel_english_json(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title_fa = models.TextField()
    description = models.TextField()
    image_link = models.URLField(max_length=300)
    embedding_openai = models.JSONField(blank=True, null=True)
    attributes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}, {self.title_fa}'


class bagmodel_english_json(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title_fa = models.TextField()
    description = models.TextField()
    image_link = models.URLField(max_length=300)
    embedding_openai = models.JSONField(blank=True, null=True)
    attributes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}, {self.title_fa}'


class shoesmodel_english_json(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title_fa = models.TextField()
    description = models.TextField()
    image_link = models.URLField(max_length=300)
    embedding_openai = models.JSONField(blank=True, null=True)
    attributes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}, {self.title_fa}'


class tshirtmodel_english_desc(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title_fa = models.TextField()
    description = models.TextField()
    image_link = models.URLField(max_length=300)
    embedding = models.JSONField(blank=True, null=True)
    embedding_openai = models.JSONField(blank=True, null=True)
    attributes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}, {self.title_fa}'


class shoesmodel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title_fa = models.TextField()
    caption = models.TextField()
    attributes = models.TextField()
    description = models.TextField()
    image_link = models.URLField(max_length=300)
    embedding = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}, {self.title_fa}'


class bagmodel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title_fa = models.TextField()
    caption = models.TextField()
    attributes = models.TextField()
    description = models.TextField()
    image_link = models.URLField(max_length=300)
    embedding = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}, {self.title_fa}'


class pantsmodel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title_fa = models.TextField()
    caption = models.TextField()
    attributes = models.TextField()
    description = models.TextField()
    image_link = models.URLField(max_length=300)
    embedding = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}, {self.title_fa}'
