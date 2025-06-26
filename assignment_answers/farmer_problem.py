total_land = 80
division = total_land / 5

tomato_sales = (((30 / 100 * division) * 10000) * 7) + (((70 / 100 * division) * 12000) * 7)
potato_sales = (division * 10000) * 20
cabbage_sales = (division * 14000) * 24
sunflower_sales = (division * 700) * 200
sugarcane_sales = (division * 45) * 4000

overall_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales

print('The overall sales achieved by Mahesh from the 80 acres of land is :',overall_sales)

#sales realization
vegetable_sales = tomato_sales + potato_sales + cabbage_sales

sales_realization = vegetable_sales 
print('Sales realisation from chemical-free farming at the end of 11 months', sales_realization)

