from app.models.product import Product
from app.repository.product_repository import ProductRepository


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, request):
        product = Product(
            product_code=request.product_code,
            product_name=request.product_name,
            dosage_form=request.dosage_form,
            strength=request.strength,
            manufacturer=request.manufacturer
        )

        return self.repository.create(product)

    def get_all_products(self):
        return self.repository.get_all()