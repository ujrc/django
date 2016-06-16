from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):

	def __init__(self,order_fields=None,*args,**kwargs):
		self.order_fields=order_fields
		super(OrderField,self).__init__(*args,**kwargs)

	def pre_save(self,model_instance,add):
		if getattr(model_instance,self.attname) is None:
			# No value provided
			try:
				qs=self.model.objects.all()
				if self.order_fields:
					# filter by objects with the same field values
					# for the fields in "for_fields"
					query={field:getattr(model_instance,field) for 
					field in self.order_fields }

					qs=qs.filter(**query)

				# Get the order of the last item
				last_item =qs.latest(self.attname)
				value = last_item.order+1

			except ObjectDoesNotExist:
				value=0
			setattr(model_instance,self.attname,value)
			return value
		else:
			return super(OrderField,self).pre_save(model_instance,add)



