from django.urls import path
from .views import (
    FAQListCreateView, FAQRetrieveUpdateDestroyView,
    BlogListCreateView, BlogRetrieveUpdateDestroyView,
    ReviewListCreateView, ReviewRetrieveUpdateDestroyView,
    ContactUsListCreateView, ContactUsRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('faqs/', FAQListCreateView.as_view(), name='faq-list-create'),
    path('faqs/<int:pk>/', FAQRetrieveUpdateDestroyView.as_view(), name='faq-retrieve-update-destroy'),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroyView.as_view(), name='blog-retrieve-update-destroy'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-retrieve-update-destroy'),
    path('contact/', ContactUsListCreateView.as_view(), name='contact-us-list-create'),
    path('contact/<int:pk>/', ContactUsRetrieveUpdateDestroyView.as_view(), name='contact-us-retrieve-update-destroy'),
]
