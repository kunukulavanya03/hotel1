# hotel1

Backend API for hotel1

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign.git))

## Project Structure

```
hotel1/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- Room booking management
- Customer management
- Room management
- Reporting and analytics

## API Endpoints

- `POST /api/bookings` - Create a new room booking
- `GET /api/bookings/{booking_id}` - Retrieve a room booking by ID
- `PUT /api/bookings/{booking_id}` - Update a room booking
- `DELETE /api/bookings/{booking_id}` - Delete a room booking
- `GET /api/customers` - Retrieve a list of customers
- `POST /api/customers` - Create a new customer
- `GET /api/rooms` - Retrieve a list of rooms

## License

MIT
