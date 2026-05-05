# 🏪 Livestock & AgriPet Store System

## 📋 Professional System Design

A comprehensive Django web application for managing TWO integrated stores (Livestock and AgriPet) with inventory, sales, orders, payment tracking, and staff management.

---

## 🏗️ SYSTEM ARCHITECTURE

### ONE WEB APP • TWO STORES

```
🏪 Livestock & AgriPet Store System
├── 🐄 Livestock Store
│   ├── Animals (Chicken, Pig, etc.)
│   └── Animal Feeds
├── 🐾 AgriPet Store
│   ├── Pets (Dog, Cat, etc.)
│   └── Pet Feeds
└── 👥 Shared Features
    ├── Customer Management
    ├── Order Management
    ├── Payment Tracking
    └── Staff & Attendance
```

---

## 📦 CORE MODULES

### MODULE 1: 🏪 STORE MANAGEMENT

**Purpose:** Distinguish between the two stores in the system

**Models:**
- **Store** - Main store entity
  - Fields: name, store_type (livestock/agripet), description

**Features:**
- Two separate store profiles
- Track products per store
- Manage orders per store
- Track staff per store
- View sales per store

---

### MODULE 2: 📦 INVENTORY SYSTEM

**Purpose:** Track all items with complete product information

**Models:**
- **Product** - All inventory items
  - Fields: name, category, store (FK), price, stock, description, image

**Product Categories:**
- 🐔 Livestock (Chicken, Pig, Duck, etc.)
- 🐕 Pet (Dog, Cat, Bird, etc.)
- 🌾 Feed (Animal Feed, Pet Food, etc.)

**Product Information:**
```
Name         : Product title
Category     : livestock | pet | feed
Store        : Which store sells it
Price        : Sale price (₱)
Stock        : Available quantity
Description  : Details about the product
Image        : Product photo
Created_at   : Timestamp
Updated_at   : Last update time
```

**Admin Features:**
- Color-coded stock levels (Green: >10, Orange: 1-10, Red: 0)
- Quick price format (₱)
- Filter by store and category
- Search products
- Image upload

---

### MODULE 3: 👤 CUSTOMER / BUYER SYSTEM

**Purpose:** Store customer information for orders and tracking

**Models:**
- **Customer** - Buyer profile
  - Fields: name, contact (phone), email, address

**Information Tracked:**
- Full name
- Phone number
- Email address
- Physical address
- Creation date
- Total order count

**Admin Features:**
- Quick view of customer orders
- Search by name, phone, email
- Contact information management
- Order history

---

### MODULE 4: 🛒 ORDER / PURCHASE SYSTEM (SHOPEE STYLE)

**Purpose:** Complete order management from selection to completion

**Models:**
- **Order** - Main purchase order
  - Fields: order_number (auto-generated), customer (FK), store (FK), status, total_amount, notes

- **OrderItem** - Individual items in an order
  - Fields: order (FK), product (FK), quantity, unit_price, subtotal

**Order Workflow:**
```
1. Customer SELECTS items
   ↓
2. System creates ORDER with ITEMS
   ↓
3. Customer INPUT quantity for each item
   ↓
4. System CALCULATES subtotal and total
   ↓
5. Customer UPLOADS payment proof
   ↓
6. System UPDATES order status
   ↓
7. COMPLETED order tracked in sales
```

**Order Status Flow:**
- 🟠 **Pending** - Initial state, awaiting confirmation
- 🔵 **Confirmed** - Order verified and accepted
- 🟢 **Completed** - Order fulfilled and delivered
- 🔴 **Cancelled** - Order cancelled by customer or system

**Order Features:**
- Auto-generated order numbers (ORD-YYYYMMDD-xxxx)
- Multiple items per order
- Price snapshot (captured at order time)
- Order notes/special requests
- Status tracking

**Admin Interface:**
- Inline editing of order items
- Status management with color badges
- Customer information display
- Total amount formatting (₱)
- Search by order number or customer

---

### MODULE 5: 🖼️ PROOF UPLOAD SYSTEM (UNIQUE FEATURE)

**Purpose:** Store and verify payment proof for orders

**Models:**
- **PaymentProof** - Payment receipt/documentation
  - Fields: order (1:1), proof_type, image (Django media), verified, verified_by, notes

**Proof Types:**
- 💳 **Payment Receipt** - Bank transfer or GCash receipt
- 📦 **Delivery Proof** - Delivery confirmation
- 📄 **Other Document** - Additional documentation

**Upload Process:**
```
1. ORDER created
   ↓
2. Customer UPLOADS image
   ↓
3. Image stored in: media/payment_proofs/
   ↓
4. Admin REVIEWS image
   ↓
5. Admin MARKS as verified (verified_by field)
   ↓
6. Order can proceed to COMPLETION
```

**Storage:**
- Location: `media/payment_proofs/`
- Supported formats: JPG, PNG, GIF, WebP
- Size handled by Django media management
- URL accessible via: `http://localhost:8000/media/payment_proofs/...`

**Admin Features:**
- Image preview in admin interface
- Upload date tracking
- Verification status badge (✓ VERIFIED / ✗ PENDING)
- Verified by staff member tracking
- Notes for verification details

---

### MODULE 6: 📊 SALES TRACKING

**Purpose:** Track and report all sales data

**Models:**
- **SaleReport** - Sales summary
  - Fields: order (1:1), product (FK), quantity_sold, total_price, sale_date, store (FK)

**Data Tracked:**
- ✅ What items were bought
- ✅ Quantity sold
- ✅ Total price (₱)
- ✅ Date of sale
- ✅ Which store made the sale
- ✅ Customer information (via Order)

**Sales Report Data:**
```
Product Name    : Item sold
Store          : Which store sold it
Quantity Sold  : Number of units
Total Price    : ₱ amount
Sale Date      : When it was sold
```

**Admin Features:**
- Filter by store and date
- View sales trends
- Search products
- Price formatting
- Date range filtering

---

### MODULE 7: 📋 ATTENDANCE & STAFF MANAGEMENT

**Purpose:** Track employee attendance and schedules

**Models:**
- **Staff** - Employee information
  - Fields: name, role, store (FK), contact, email, hire_date, is_active

- **Attendance** - Daily attendance records
  - Fields: staff (FK), date, time_in, time_out, status, notes

**Staff Roles:**
- 👔 **Store Manager** - Overall store management
- 💳 **Cashier** - Handling transactions
- 📦 **Stock Handler** - Inventory management
- 🚚 **Delivery Staff** - Order delivery
- 🔧 **Other** - Other positions

**Attendance Status:**
- 🟢 **Present** - Staff worked full shift
- 🔴 **Absent** - Staff did not show up
- 🟠 **Late** - Staff arrived late
- 🔵 **Leave** - Staff on approved leave

**Attendance Tracking:**
```
Staff       : Employee name
Date        : Attendance date
Time In     : Clock in time (HH:MM)
Time Out    : Clock out time (HH:MM)
Status      : present | absent | late | leave
Notes       : Additional info (sick leave, etc.)
```

**Admin Features:**
- Staff list per store
- Inline attendance entry
- Time tracking (HH:MM format)
- Active/Inactive status badge
- Unique constraint: One record per staff per day
- Filter by store, role, and date

---

## 🗄️ DATABASE SCHEMA

### Entity Relationships

```
Store (1) ──→ (Many) Product
Store (1) ──→ (Many) Order
Store (1) ──→ (Many) Staff
Store (1) ──→ (Many) SaleReport

Customer (1) ──→ (Many) Order
Order (1) ──→ (Many) OrderItem
Order (1:1)←──→ PaymentProof
Order (1:1)←──→ SaleReport

Product (1) ──→ (Many) OrderItem
Product (1) ──→ (Many) SaleReport

Staff (1) ──→ (Many) Attendance
```

### File Structure

```
livestock_system/
├── manage.py                 # Django command manager
├── db.sqlite3               # Database file
├── config/                  # Project settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # Production server
│   └── asgi.py             # Async server
├── store/                   # Main app
│   ├── models.py           # Database models ✅ COMPLETE
│   ├── admin.py            # Admin interface ✅ COMPLETE
│   ├── views.py            # Views (for future)
│   ├── urls.py             # App URLs
│   ├── apps.py             # App config
│   ├── migrations/         # Database migrations
│   └── templates/         # HTML templates (for future)
├── media/                   # User uploads
│   ├── products/           # Product images
│   └── payment_proofs/     # Payment receipt images
└── staticfiles/            # Static files (CSS, JS)
```

---

## 🎨 ADMIN INTERFACE FEATURES

### Dashboard Customization
- Site header: "🏪 Livestock & AgriPet Store System"
- Site title: "Store Admin"
- Welcome message: "Welcome to Store Management"

### Admin Sections

#### 1. Stores
- View all stores (Livestock, AgriPet)
- Product count per store
- Creation date

#### 2. Products
- Color-coded stock levels
- Formatted prices (₱)
- Filter by store and category
- Image uploads
- Search functionality

#### 3. Customers
- Total orders per customer
- Contact information
- Create date tracking

#### 4. Orders (Advanced)
- Inline item editing
- Payment proof attachment
- Status management with color badges
- Customer information
- Total calculation
- Search by order number

#### 5. Order Items (via Order inline)
- Add/edit multiple items
- Automatic subtotal calculation
- Update order total

#### 6. Payment Proofs
- Image preview in admin
- Verification status
- Verified by staff member
- Upload date tracking
- Notes for review

#### 7. Sales Reports
- Sales by product and date
- Store filtering
- Price formatting
- Sales trends

#### 8. Staff Management
- Per-store staff listing
- Role assignment
- Active/Inactive status
- Hire date tracking

#### 9. Attendance Records
- Staff time tracking
- Daily attendance status
- Inline entry
- Date filtering

---

## 🚀 GETTING STARTED

### 1. Start Development Server

```bash
cd 'c:\Users\User\OneDrive\Desktop\Livestock & AgriPet Store System'
python manage.py runserver
```

Visit: `http://localhost:8000/admin/`

### 2. Create Initial Stores

1. Go to Admin → Stores
2. Add Store: "Livestock Store" (store_type: livestock)
3. Add Store: "AgriPet Store" (store_type: agripet)

### 3. Add Products

1. Ho to Admin → Products
2. Create: Chicken (store: Livestock, category: livestock)
3. Create: Pig (store: Livestock, category: livestock)
4. Create: Dog (store: AgriPet, category: pet)
5. Create: Cat (store: AgriPet, category: pet)
6. Create: Dog Food (store: AgriPet, category: feed)
7. Create: Chicken Feed (store: Livestock, category: feed)

### 4. Add Customers

1. Go to Admin → Customers
2. Add customer information (name, contact, email, address)

### 5. Create Orders

1. Go to Admin → Orders
2. Select customer and store
3. Add order items (inline)
4. Upload payment proof
5. Update order status
6. System automatically creates sale report

### 7. Track Staff Attendance

1. Go to Admin → Staff
2. Add staff members
3. Go to Admin → Attendance
4. Record daily attendance

---

## 📊 WORKFLOW EXAMPLE

### Complete Order Scenario

```
1. CUSTOMER REQUEST
   Customer wants to buy: 3 Chickens, 2 Chicken Feed

2. CREATE ORDER (Admin)
   - Select Customer
   - Select Store (Livestock)
   - Add Items:
     * Chicken x3 @ ₱500 = ₱1,500
     * Chicken Feed x2 @ ₱200 = ₱400
   - Total: ₱1,900

3. UPLOAD PAYMENT PROOF
   - Customer/Admin uploads GCash receipt image
   - Stored in: media/payment_proofs/

4. VERIFY PROOF
   - Admin reviews image
   - Marks as verified
   - Records verified_by name

5. UPDATE ORDER STATUS
   - Change from Pending → Confirmed → Completed

6. AUTO-GENERATE SALES REPORT
   - System creates 2 sale records:
     * Chicken (3 units) - ₱1,500
     * Chicken Feed (2 units) - ₱400

7. TRACK SALES DATA
   - View in Sales Reports
   - Filter by date, store, product
```

---

## 🛠️ USEFUL ADMIN TASKS

### View Sales by Store
Admin → Sales Reports → Filter by Store

### Track Customer Orders
Admin → Customers → Click customer name

### Check Order Items
Admin → Orders → Open order → View inline items

### Verify Payment Proofs
Admin → Payment Proofs → Review image → Mark verified

### Staff Attendance Report
Admin → Attendance → Filter by date and staff

### Inventory Status
Admin → Products → View color-coded stock

---

## 📝 TECHNICAL NOTES

### Media Files
- Stored in: `media/payment_proofs/` and `media/products/`
- Accessible at: `http://localhost:8000/media/...`
- Supports: JPG, PNG, GIF, WebP
- Handled by Django media settings

### Database
- Type: SQLite (can upgrade to PostgreSQL)
- Location: `db.sqlite3`
- Migrations: `store/migrations/`

### URL Patterns
- Admin: `/admin/`
- Media files: `/media/...`
- Static files: `/static/...` (for future)

### Timestamps
- All models have creation/update tracking
- UTC timezone by default
- Can be changed in settings.py

---

## 🎯 FEATURES SUMMARY

✅ **Two Integrated Stores** - Livestock & AgriPet  
✅ **Inventory Management** - Products, categories, stock tracking  
✅ **Customer Management** - Contact info, address, order history  
✅ **Shopping Cart System** - Multiple items per order  
✅ **Order Management** - Status tracking, notes  
✅ **Payment Proof Upload** - Image upload & verification  
✅ **Sales Tracking** - Automatic reporting  
✅ **Staff Management** - Roles, hire dates, status  
✅ **Attendance Tracking** - Time in/out, status  
✅ **Professional Admin** - Color-coded, formatted, searchable  

---

## 📞 SUPPORT

For troubleshooting or customization:
1. Check admin pages for complete data
2. Use Django search functionality
3. View timestamps for recent changes
4. Filter by store, date, or status
5. Upload images for payment proofs

**System Ready for Use! 🎉**
