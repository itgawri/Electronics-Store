# Electronics-Store
The "Electronics Store" project aims to analyze and format data related to electronic products available in the store. Below, we present the project's code and its description.

In the project, we have data representing various electronic products in the form of a text string (variable "data"). Each product is described as "product name, price," where the product name may contain special characters such as "@" or "$."

The project's code begins by splitting the data into individual products using the "|" separator (variable "device_list"). Then, each product is analyzed separately.

The project performs the following tasks:

For each product, we split the information into the product name and price using the "," separator (variable "device_info_list").

Next, we calculate a new price for the product by increasing the price by 10% (variable "new_price").

We format the data by creating well-formatted product information, including the name and price in the format "Product Name: {name}, Product Price: ${price}."

We correct the product names by removing special characters "@" and replacing them with standard letters.

We add the formatted data to a list (variable "formatted_list").

At the end of the project, we display the formatted product data, including their names and prices.

This project aims to analyze and format data for electronic products in the store, making it easier to present to customers and for further processing.
