from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from about.models import AboutPost
from about.forms import CreateAboutPostForm, UpdateAboutPostForm

from account.models import Account


def create_about_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateAboutPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateAboutPostForm()

	context['form'] = form

	return render(request, "about/create_about.html", context)


def detail_about_view(request, slug):

	context = {}

	about_post = get_object_or_404(AboutPost, slug=slug)
	context['about_post'] = about_post

	return render(request, 'about/detail_about.html', context)



def edit_about_view(request, slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	about_post = get_object_or_404(AboutPost, slug=slug)

	if about_post.author != user:
		return HttpResponse("You are not the author of that post.")

	if request.POST:
		form = UpdateAboutPostForm(request.POST or None, request.FILES or None, instance=about_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			about_post = obj

	form = UpdateAboutPostForm(
			initial = {
					"title": about_post.title,
					"body": about_post.body,
					"image": about_post.image,
			}
		)

	context['form'] = form
	return render(request, 'about/edit_about.html', context)


def get_about_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = AboutPost.objects.filter(
				Q(title__icontains=q) |
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))
