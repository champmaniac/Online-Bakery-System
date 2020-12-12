from django.urls import path
from shop import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("signup/", views.handleSignup, name="handleSignup"),
	path("login/", views.handleLogin, name="handleLogin"),
	path("logout/", views.handleLogout, name="handleLogout"),
	path("checkout/", views.checkout, name="Checkout"),

]