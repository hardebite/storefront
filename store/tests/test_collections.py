from math import prod
from urllib import response
from  django.contrib.auth.models import User

from multiprocessing.connection import Client
from store.models import Collection, Product
from rest_framework import status
import pytest
from model_bakery import baker

from store.tests.conftest import api_client, authenticate

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/',collection)
    return do_create_collection
@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/',product)
    return do_create_product

@pytest.fixture
def delete_collection(api_client):
    def do_delete_collection(collection):
        return api_client.delete('/store/collections/',collection)
    return do_delete_collection

@pytest.fixture
def delete_product(api_client):
    def do_delete_product(product):
        return api_client.delete('/store/products/',product)
    return do_delete_product

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self,create_collection):
        
        response = create_collection({'title': 'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self,api_client,authenticate,create_collection):
        
        authenticate(is_staff=False)
        
        response = create_collection({'title': 'a'})
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
     
    def  test_if_data_is_invalid_returns_400(self,api_client,authenticate,create_collection):
        authenticate(is_staff=True)
        
        response = create_collection({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
  

    def test_if_data_is_valid_returns_201(self,api_client,authenticate, create_collection):
        authenticate(is_staff=True)
        
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self,create_product):
        
        response = create_product({'title': 'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self,api_client,authenticate,create_product):
        
        authenticate(is_staff=False)
        
        response = create_product({'title': 'a'})
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
     
    def  test_if_data_is_invalid_returns_400(self,api_client,authenticate,create_product):
        authenticate(is_staff=True)
        
        response = create_product({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
  

   

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_return_200(self,api_client):
        
        collection = baker.make(Collection)

        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
               'id':collection.id,
               'title': collection.title ,
               'products_count' : 0    
        }
@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exists_return_200(self,api_client):
      
        product = baker.make(Product)

        response = api_client.get(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestDeleteCollection:
    def test_if_user_is_anonymous_returns_401(self,delete_collection):
        
        response = delete_collection({'title': 'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self,api_client,authenticate,delete_collection):
        
        authenticate(is_staff=False)
        
        response = delete_collection({'title': 'a'})
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
     
    def  test_if_method_is_not_allowed_returns_405(self,api_client,authenticate,delete_collection):
        authenticate(is_staff=True)
        
        response = delete_collection({'title': ''})

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        


@pytest.mark.django_db
class TestDeleteProduct:
    def test_if_user_is_anonymous_returns_401(self,delete_product):
        
        response = delete_product({'title': 'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self,api_client,authenticate,delete_product):
        
        authenticate(is_staff=False)
        
        response = delete_product({'title': 'a'})
        
        assert response.status_code == status.HTTP_403_FORBIDDEN
     
    def  test_if_method_is_not_allowed_returns_405(self,api_client,authenticate,delete_product):
        authenticate(is_staff=True)
        
        response = delete_product({'title': ''})

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
  
