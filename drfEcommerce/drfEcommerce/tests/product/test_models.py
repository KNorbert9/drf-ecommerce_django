class TestCategoryModel:
    def test_str(self):
        category = Category.objects.create(name="Test Category")
        assert str(category) == "Test Category"
        
        
        
class TestBrandModel:
    def test_str(self):
        brand = Brand.objects.create(name="Test Brand")
        assert str(brand) == "Test Brand"
        
        
        
class TestProductModel:
    def test_str(self):
        product = Product.objects.create(name="Test Product")
        assert str(product) == "Test Product"