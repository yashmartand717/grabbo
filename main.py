from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Product database for categories
CATEGORIES = {
    "dairy": {
        "name": "Dairy, Bread & Eggs",
        "items": [
            {"name": "Amul Fresh Milk (1L)", "price": "₹68", "desc": "Carton packaging", "icon": "https://cdn-icons-png.flaticon.com/512/3050/3050153.png"},
            {"name": "English Oven Brown Bread", "price": "₹45", "desc": "Whole wheat fresh loaf", "icon": "https://cdn-icons-png.flaticon.com/512/3014/3014620.png"},
            {"name": "Farm Fresh Organic Eggs (6 pcs)", "price": "₹90", "desc": "Grade A brown eggs", "icon": "https://cdn-icons-png.flaticon.com/512/1047/1047607.png"}
        ]
    },
    "fruits": {
        "name": "Fruits & Vegetables",
        "items": [
            {"name": "Organic Hass Avocados", "price": "₹290", "desc": "Pack of 2 imported", "icon": "https://cdn-icons-png.flaticon.com/512/3194/3194585.png"},
            {"name": "Fresh Alphonso Mangoes", "price": "₹450", "desc": "1kg box premium grade", "icon": "https://cdn-icons-png.flaticon.com/512/3194/3194585.png"},
            {"name": "Ooty Carrots & Greens", "price": "₹60", "desc": "500g farm fresh bundle", "icon": "https://cdn-icons-png.flaticon.com/512/3194/3194585.png"}
        ]
    },
    "drinks": {
        "name": "Cold Drinks & Juices",
        "items": [
            {"name": "Pepsi Black Can (300ml)", "price": "₹40", "desc": "Single unit", "icon": "https://cdn-icons-png.flaticon.com/512/2405/2405479.png"},
            {"name": "Tropicana 100% Orange Juice", "price": "₹140", "desc": "1L carton", "icon": "https://cdn-icons-png.flaticon.com/512/2405/2405479.png"},
            {"name": "Bisleri Mineral Water (1L)", "price": "₹20", "desc": "Pack of 1", "icon": "https://cdn-icons-png.flaticon.com/512/2405/2405479.png"}
        ]
    },
    "snacks": {
        "name": "Snacks & Munchies",
        "items": [
            {"name": "Lays Classic Salted Chips", "price": "₹20", "desc": "Large pack", "icon": "https://cdn-icons-png.flaticon.com/512/2553/2553690.png"},
            {"name": "Haldiram's Bhujia Sev", "price": "₹55", "desc": "400g pouch", "icon": "https://cdn-icons-png.flaticon.com/512/2553/2553690.png"}
        ]
    },
    "breakfast": {
        "name": "Breakfast & Instant Food",
        "items": [
            {"name": "Kellogg's Corn Flakes", "price": "₹210", "desc": "Original 500g box", "icon": "https://cdn-icons-png.flaticon.com/512/2619/2619554.png"},
            {"name": "Maggi 2-Minute Noodles", "price": "₹60", "desc": "Pack of 4", "icon": "https://cdn-icons-png.flaticon.com/512/2619/2619554.png"}
        ]
    },
    "sweets": {
        "name": "Sweet Tooth",
        "items": [
            {"name": "Cadbury Dairy Milk Silk", "price": "₹175", "desc": "Roast Almond 150g", "icon": "https://cdn-icons-png.flaticon.com/512/1047/1047607.png"},
            {"name": "Ferrero Rocher (16 pcs)", "price": "₹699", "desc": "Gift box", "icon": "https://cdn-icons-png.flaticon.com/512/1047/1047607.png"}
        ]
    },
    "bakery": {
        "name": "Bakery & Biscuits",
        "items": [
            {"name": "Parle-G Gold Biscuits", "price": "₹30", "desc": "Family pack", "icon": "https://cdn-icons-png.flaticon.com/512/3014/3014620.png"},
            {"name": "Dark Fantasy Choco Fills", "price": "₹75", "desc": "Cookie pack", "icon": "https://cdn-icons-png.flaticon.com/512/3014/3014620.png"}
        ]
    },
    "tea": {
        "name": "Tea, Coffee & Milk Drinks",
        "items": [
            {"name": "Tata Tea Gold (500g)", "price": "₹320", "desc": "Rich aroma loose tea", "icon": "https://cdn-icons-png.flaticon.com/512/2738/2738730.png"},
            {"name": "Nescafe Classic Coffee", "price": "₹295", "desc": "Instant coffee jar 100g", "icon": "https://cdn-icons-png.flaticon.com/512/2738/2738730.png"}
        ]
    }
}

@app.get("/")
async def store_page(request: Request):
    return templates.TemplateResponse(request=request, name="store.html")

@app.get("/inventory")
async def inventory_page(request: Request):
    return templates.TemplateResponse(request=request, name="inventory.html")

@app.get("/cart")
async def cart_page(request: Request):
    return templates.TemplateResponse(request=request, name="cart.html")

@app.get("/events")
async def events_page(request: Request):
    return templates.TemplateResponse(request=request, name="events.html")

@app.get("/category/{category_id}")
async def category_detail(request: Request, category_id: str):
    category = CATEGORIES.get(category_id, {"name": "Category", "items": []})
    return templates.TemplateResponse(request=request, name="category.html", context={"category": category})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)