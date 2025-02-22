from sql_connection import get_sql_connection
def get_all_products(connection):
    
    cursor = connection.cursor()

    query = "SELECT products.product_id , products.name , products.uom_id , products.price_per_unit , uom.uom_name FROM grocery_store.products inner join uom on products.uom_id = uom.uom_id;"
    cursor.execute(query)

    response = []

    for (product_id , name , uom_id , price_per_unit,uom_name  ) in cursor :
        response.append(
            {
                'product_id' : product_id , 
                'name' : name , 
                'uom-id' : uom_id , 
                'price_per_unit' : price_per_unit , 
                'uom_name' : uom_name
            }
        )

    return response

def insert_new_products(connection,product):
    cursor = connection.cursor()
    query = ("insert into products (name,uom_id , price_per_unit  ) values (%s , %s , %s )")

    data = (product['product_name'],product['uom_id'] , product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id =" + str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor


def update_product(connection , product_id ,new_name, new_price,):
    cursor = connection.cursor()
    query = ('UPDATE products SET name = %s , price_per_unit = %s WHERE product_id = %s')
    cursor.execute(query, (new_name, new_price, product_id))
    connection.commit()
    return cursor




if __name__ == "__main__" :
    connection = get_sql_connection()
    product = {
        'product_name' : "Maggi" , 
        'uom_id' : 2 ,
        'price_per_unit' : 14
    }
    print(insert_new_products(connection,product))
    print(get_all_products(connection))