from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

import qrcode

class Category(models.Model):
	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length = 150, db_index=True, null=True)
	icon = models.FileField(upload_to = "category/", null=True, blank=True)
	create_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name

class Writer(models.Model):
	name = models.CharField(max_length = 100)
	firstname = models.CharField(max_length = 100, null=True)
	slug = models.SlugField(max_length=150, db_index=True)
	bio = models.TextField(null=True)
	pic = models.FileField(upload_to = "writer/", null=True)
	create_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name

#class Edition(models.Model):
    #name_ed = models.CharField(max_length = 100)
    #add_ed = models.CharField(max_length = 100)
    #code_ed = models.IntegerField()

class Book(models.Model):
	writer = models.ForeignKey(Writer, on_delete = models.CASCADE)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	#edition = models.ForeignKey(Edition, on_delete=models.CASCADE, null=True)

	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length=100, db_index=True)
	price = models.IntegerField(default = 0)
	stock = models.IntegerField(default = 0)
	nb_page = models.IntegerField(default = 0)
	coverpage = models.FileField(upload_to = "coverpage/")
	bookpage = models.FileField(upload_to = "bookpage/")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	totalreview = models.IntegerField(default=1)
	totalrating = models.IntegerField(default=5)
	status = models.IntegerField(default=0)
	description = models.TextField()
	qr_code = models.ImageField(upload_to='media', null=True, blank=True)
	is_scanned = models.BooleanField(default=False)
 
	def save(self, *args, **kwargs) :
		qr = qrcode.QRCode(
			version = 1,
			error_correction = qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
            border=4 
		)
		data = f"{self.name}-{self.nb_page}-{self.coverpage.url}-{self.stock}"
		qr.add_data(data)
		qr.make(fit=True)
		qr_image = qr.make_image(fill_color="black", black_color="white")
		qr_width, qr_height = qr_image.size
		canvas = Image.new('RGB', (qr_width, qr_height), 'white')
		draw = ImageDraw.Draw(canvas)
		canvas.paste(qr_image)
		file_name = f"{data}.png"
		buffer = BytesIO()
		canvas.save(buffer, 'PNG')
		self.qr_code.save(file_name, File(buffer), save=False)
		canvas.close()
		return super().save(*args, **kwargs)
	

	def __str__(self):
	    return self.name


class Review(models.Model):
	customer = models.ForeignKey(User, on_delete = models.CASCADE)
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	review_star = models.IntegerField()
	review_text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

class Slider(models.Model):
	title = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slideimg = models.FileField(upload_to = "slide/")

	def __str__(self):
		return self.title

STATUS = (
    ('En attente', 'En attente'),
    ('Accepté', 'Accepté'),
    ('Retourné', 'Retourné'),
    ('Refusé', 'Refusé')
)

class History(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
	created = models.DateTimeField(null=True)
	updated = models.DateTimeField(null=True)
	status = models.CharField(max_length=100, choices=STATUS, null=True, default = 'En attente')
