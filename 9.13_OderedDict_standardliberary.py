from collections import OrderedDict

cars = OrderedDict()
cars["BMW"]        = "i8"
cars["hundai"]     = "i10"
cars["lamborgini"] = "avantador"
cars["Tata"]       = "safari"
cars["rangerover"] = "LandRover"

for k,v in cars.items():
	print(k," : ",v)

