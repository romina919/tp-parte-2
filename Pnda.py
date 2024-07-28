import pandas as pd 

dfl1 = pd.read_csv('C:/Users/rcorter/Desktop/Prueba-/tp-parte-2/ecommerce_customers_dataset.csv',encoding='utf-8')
dfl1 = pd.read_csv('C:/Users/rcorter/Desktop/Prueba-/tp-parte-2/ecommerce_customers_dataset.csv',encoding='utf-8')
dfl2 = pd.read_csv('C:/Users/rcorter/Desktop/Prueba-/tp-parte-2/ecommerce_order_items_dataset.csv',encoding='utf-8')
dfl3 = pd.read_csv('C:/Users/rcorter/Desktop/Prueba-/tp-parte-2/ecommerce_order_payments_dataset.csv',encoding='utf-8')
dfl4 = pd.read_csv('C:/Users/rcorter/Desktop/Prueba-/tp-parte-2/ecommerce_orders_dataset.csv',encoding='utf-8')
dfl5 = pd.read_csv('C:/Users/rcorter/Desktop/Prueba-/tp-parte-2/ecommerce_products_dataset.csv',encoding='utf-8')

dfl1.set_index('customer_id', inplace=True)
dfl2.set_index('order_id', inplace=True)
dfl3.set_index('order_id', inplace=True)
dfl4.set_index('order_id', inplace=True)
dfl5.set_index('product_id', inplace=True)


clientes_unicos = dfl1['customer_unique_id'].nunique()
print(f"completo el numero total de clientes unicos son:{clientes_unicos}")

v_promedio = dfl3['payment_value'].mean()
print(f"completo muestra el valor promedio pagado por pedido: {v_promedio}")

category_max_vendida = dfl5['product_category_name'].value_counts()
print(f"completo muestra la categoria mas vendida: {category_max_vendida}")

#total_pedidos = 
#print(f"completo el total de pedidos realizados es: {total_pedidos}")





