from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext as _
from .utils import get_century

# Create your models here


class Author(models.Model):
    first_name = models.CharField(
        max_length=30, null=True, blank=True, verbose_name=_("Prénom")
    )
    last_name = models.CharField(max_length=30,verbose_name=_("Nom"))
    name = models.CharField(max_length=61, editable=False)
    century_birth = models.IntegerField(
        null=True, blank=True, verbose_name=_("Siècle")
    )
    date_birth = models.DateField(
        null=True, blank=True, verbose_name=_("Date de naissance")
    ) 
    place_birth = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Lieu de naissance")
    )

    date_died = models.DateField(
        null=True, blank=True, verbose_name=_("Date de décès")
    ) 
    place_died = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Lieu de décès")
    )

    content = models.TextField(null=True, blank=True, verbose_name=_("Contenu")) 
    image_url = models.URLField(
        null=True, blank=True, verbose_name=_("URL d'une image")
    )
    image_file = models.ImageField(
        null=True, blank=True, verbose_name=_("Fichier image")
    )

    class Meta:
        ordering = ['last_name']
        verbose_name = _("Auteur")

    def __str__(self):
        if self.first_name:
            return f"{self.last_name} {self.first_name}"
        else:
            return self.last_name

    def clean(self):
        """
        update of century from date_birth using catalog.utils.get_century function
        update name in <first_name space last_name> or <last_name>
        """
        if self.date_birth:
            century = get_century(self.date_birth.year)
            self.century_birth = century
        if self.first_name:
            self.name = f"{self.first_name} {self.last_name}"
        else:
            self.name = self.last_name


class Dewey(models.Model):
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=3)
    bg_color = models.CharField(max_length=7, default="*")
    text_color = models.CharField(max_length=7, default="*")

    class Meta:
        ordering = ['number']

    DEWEY_COLOR_CHOICES = [
        ("000", "#000000", "#fff"),  # Black
        ("100", "#8B4513", "#000"),  # Maroon
        ("200", "#FF0000", "#000"),  # Red
        ("300", "#FF4500", "#000"),  # Orange
        ("400", "#FFFF00", "#000"),  # Yellow
        ("500", "#32CD32", "#000"),  # Green
        ("600", "#1E90FF", "#000"),  # Blue
        ("700", "#8B008B", "#000"),  # Purple
        ("800", "#A9A9A9", "#000"),  # Grey
        ("900", "#FFFFFF", "#000"),  # White
    ]

    def colored_number(self):
        if self.number:
            try:
                i = int(self.number[:1])
                return format_html(
                    '<span style="background-color: {}; color: {}; display: inline-block; padding: .3rem; min-width: 50px;">{}</span>',
                    self.DEWEY_COLOR_CHOICES[i][1],  # bg color
                    self.DEWEY_COLOR_CHOICES[i][2],  # text color
                    self.number,
                )
            except:
                return "Wrong format"

    def __str__(self):
        return f"{self.number} {self.name}"
        # return self.colored_number()
      

class Publication(models.Model):
    TYPE_PUBLICATION_CHOICES = [
        ("B", "Livre"),
        ("M", "Musique"),
        ("F", "Film"),
        ("_", "Autre"),
    ]

    dewey_number = models.ForeignKey(Dewey, models.PROTECT, null=True)
    type_publication = models.CharField(
        max_length=1, choices=TYPE_PUBLICATION_CHOICES, default="B")
    isbn = models.CharField(max_length=14, null=True, blank=True)
    name = models.CharField(max_length=61)
    author = models.ForeignKey(Author, models.PROTECT, null=True)
    label_editor = models.CharField(max_length=50, null=True, blank=True)
    reference = models.CharField(max_length=61, editable=False)
    genre = models.CharField(max_length=35)
    date_publication = models.DateField(null=True, blank=True) 
    nb_tracks_pages = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True) 
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)
  
    class Meta:
        ordering = ['reference']

    def __str__(self):
        return f"{self.reference} {self.name}"

    def clean(self):
        if self.dewey_number and self.author:
            self.reference = f"{self.dewey_number.number}.{self.author.last_name[:3].upper()}.{self.pk}"
        else:
            self.reference = ""
