from django import template


register=template.Library()


# if we wants to use decorators in this case we write like that

@register.filter(name='cut')


def cut(value,arg):

	"""
	This  cuts all value of args from thh strings!

	"""
	return value.replace(arg,'')

# register.filter('cut',cut)
# Note:In this filter custum first value is the name of custom filter and argyment is the function name,this process is without decorators
