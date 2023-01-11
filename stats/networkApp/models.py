from django.db import models

class Base(models.Model):
	name = models.CharField(max_length=50, blank = False, unique = True, db_index = True)
	class Meta:
		abstract = True

class City(Base):
	pass

class Operator(Base):
	pass

class Network(Base):
	twoG = models.BooleanField(blank = False)
	threeG = models.BooleanField(blank = False)
	fourG = models.BooleanField(blank = False)

	class Meta:
		unique_together = ('twoG', 'threeG', 'fourG')

class NetworkOperatorCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, unique=False, db_index = True)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, unique=False)
    network = models.ForeignKey(Network, on_delete=models.CASCADE, unique=False)
    

    class Meta:
        unique_together = ('city', 'operator', 'network')


def get_or_create_city(name):
	try:
		city = City.objects.get(name = name)
		return city

	except Exception as e:
		try:
			city = City(name = name)
			city.save()
			return city
		except Exception as e:
			return None
		
def get_or_create_operator(name):
	try:
		op = Operator.objects.get(name = name)
		return op

	except Exception as e:
		try:
			op = Operator(name = name)
			op.save()
			return op
		except Exception as e:
			return None

def get_or_create_network(name):
	try:
		net = Network.objects.get(name = name)
		return net

	except Exception as e:
		try:
			net = Network(name = name, twoG = name[0], threeG=name[1], fourG=name[2])
			net.save()
			return net
		except Exception as e:
			return None
