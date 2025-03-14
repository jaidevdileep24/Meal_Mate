# MealMate

🍴 MealMate
A full-stack food Ordering platform that allows customers to browse restaurants, place orders, and make payments while allowing vendors to manage their restaurant details, orders, and menus. The platform includes secure user authentication and role-based access control to ensure only authorized users can access specific resources.



## Features

### 🛒 Customer Features:
- Customer Registration and Login: Customers can register and log in to place an order. Only active users can log in.
- Profile Management: Customers can edit their personal details (name, email, etc.).
- Order Management: Customers can view their order history, including vendor, items, total price, and order status.
- Marketplace: Customers can browse a marketplace of approved restaurants.
- Order Placement: Customers can place orders from multiple vendors and view available menus.
- Payment: PayPal integration for order payments. 💳
- Access Control: Unauthorized access to vendor-specific links or pages results in an error message.

### 🏪 Vendor Features:
- Vendor Registration and Login: Vendors can register and log in to manage their restaurant and orders.
- Restaurant Management: Vendors can add and edit restaurant details, categories, menu items, and opening hours.
- Order Management: Vendors can view and manage orders placed for their restaurant, including customer information, items ordered, and payment status.
- Access Control: Unauthorized access to customer-specific pages results in an error message.
- Marketplace Display: Vendors' restaurants are displayed in the marketplace only after backend approval.

### 📦 Backend Features:
- Approval Process: New restaurant listings must be approved by the backend before being visible in the marketplace.
- User Management: Admins can manage customer and vendor accounts, activating/deactivating users as needed.
- Order Verification: Vendors can verify and update the status of orders placed at their restaurants.

### 📋 Error Handling and Access Control:
- Unauthorized Access: Users trying to access pages or resources they don't have permission to should be redirected to an "Unauthorized User" page.
- Authentication and Authorization: Both customers and vendors must authenticate before accessing specific functionalities.

## Database Requirements:
- **Users Table**: Store customer and vendor information (user type, email, password, etc.) and track user status (active/inactive).
- **Restaurants Table**: Store restaurant details (name, description, categories, menu items, opening hours, approval status).
- **Orders Table**: Store order details (customer, vendor, items, total price, payment status, order status).
- **Menus Table**: Store menu items for each restaurant, including item name, description, price, and availability.
- **Categories Table**: Store food categories (e.g., appetizers, main course, desserts) for each restaurant.

## Technologies and Tools:
### Frontend:
- HTML, CSS, JavaScript
- React.js or Vue.js for dynamic, responsive user interfaces

### Backend:
- Django (with Django REST Framework) or Flask
- MySQL or PostgreSQL for the database
- JWT (JSON Web Tokens) for secure user authentication

### Payment Integration:
- PayPal API for payment processing

### Authentication:
- Django's built-in authentication or JWT for secure login and role-based access control

### Error Handling:
- Proper error handling and redirection for unauthorized access

### Security Considerations:
- **Data Validation**: Ensure that all user inputs are validated and sanitized to prevent SQL injection and XSS attacks.
- **Role-based Access Control**: Ensure that only authorized users can access specific resources.

## Installation Instructions
### Prerequisites:
- Python 3.x
- Node.js
- MySQL or PostgreSQL database
- PayPal API credentials

### Backend Setup:
1. Clone the repository:
   ```bash
   git clone [https://github.com//MealMate](https://github.com/jaidevdileep24/Meal_Mate.git)
   cd MealMate
