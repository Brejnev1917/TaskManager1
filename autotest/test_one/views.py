from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.messages import get_messages
