from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def update_meal(request, meal_id):
	template = "update_meal.html"
	meal = Meal.objects.get(id=int(meal_id))

	if request.method == "POST":
		form = MealForm(request.POST, instance=meal)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('food:index'))
	else:
		context = {
			'meal_form': MealForm(instance=meal),
		}
		return render(request, template, context)