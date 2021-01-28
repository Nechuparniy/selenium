def test_task19(app, products_count=3):

    for x in range(products_count):
        app.add_product_to_cart()

    app.delete_all_products()
