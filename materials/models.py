from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Polymer(models.Model):
	polymer_name = models.CharField(max_length = 100)
	owner = models.ForeignKey('auth.User', related_name='polymers')
	def __unicode__(self):
		return '%s' % (self.polymer_name)

class Producer(models.Model):
	producer_name = models.CharField(max_length = 100)
	owner = models.ForeignKey('auth.User', related_name='producers')
	def __unicode__(self):
		return '%s' % (self.producer_name)

class Product(models.Model):
	grade_name = models.CharField(max_length=100)
	polymer = models.ForeignKey(Polymer, related_name = 'polymer', null=True)
	producer = models.ForeignKey(Producer, related_name = 'producer', null=True)
	mold_temperature = models.FloatField()
	melt_temperature = models.FloatField()
	owner = models.ForeignKey('auth.User', related_name='products')