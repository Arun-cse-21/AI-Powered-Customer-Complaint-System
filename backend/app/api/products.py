from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.permissions import require_roles
from app.database.database import get_db
from app.repository.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(
    request: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("ADMIN"))
):
    repository = ProductRepository(db)
    service = ProductService(repository)

    return service.create_product(request)


@router.get("/", response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("ADMIN", "QA_MANAGER", "QA_EXECUTIVE", "CUSTOMER"))
):
    repository = ProductRepository(db)
    service = ProductService(repository)

    return service.get_all_products()