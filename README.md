# Dynamic Flask Allocation Engine & Inventory Routing System

A lightweight, high-performance web routing application built using the Flask micro-framework. The system acts as a proof-of-concept for dynamic resource distribution, demonstrating secure HTTP `POST` form data ingestion, in-memory inventory mapping, and dynamic server-side template rendering using Jinja2.

## 🚀 Key Features
* **Dynamic Content Routing:** Implements modular Flask endpoint routing to render UI states dynamically based on underlying array configurations.
* **State-Driven Ingestion Pipeline:** Uses an HTTP `POST` method workflow to capture user parameters (`name`, `student_id`, `room`) directly from web inputs.
* **Contextual Data Binding:** Utilizes server-side injection to pass live, in-memory lists to frontend selection structures seamlessly.
* **Secure State Transition:** Maps transactional inputs immediately onto success status screens, isolating individual user contexts per session request.

## 🛠️ Technical Stack & Architecture
* **Language:** Python
* **Backend Framework:** Flask
* **Frontend Engine:** Jinja2 Template Engine, HTML5
* **Architecture Pattern:** Model-View-Controller (MVC) architectural principles

## 🏗️ Technical Highlights & Logic
* **Dynamic Inventory Control:** Rooms are configured inside a global array matrix (`available_rooms`), allowing the backend routing logic to pass the target allocation structure into the view tier on load.
* **HTTP Parameter Extraction:** Implements `request.form` validation blocks within the `/submit` routine to parse form data and route the mapped strings instantly to final receipt displays.

## 🔮 Future Roadmap & Expansion (Mini-Project Progression)
* **Persistent Database Integration:** Swapping out the current in-memory array (`available_rooms`) for a relational SQLite or PostgreSQL database to handle permanent transaction logging.
* **Dynamic Array Mutations:** Updating the `/submit` endpoint logic to pop or remove a selected item from the pool upon successful booking, preventing double-allocations.

## 💻 Installation & Setup
```bash
# Clone the repository
git clone [https://github.com/ppoobesh/Room-slot-booking.git](https://github.com/ppoobesh/Room-slot-booking.git)

# Navigate to the project directory
cd Room-slot-booking

# Install Flask dependency
pip install flask

# Execute the application server
python app.py
