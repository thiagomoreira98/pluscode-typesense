# PlusCode Typesense

A Python service that integrates Plus Codes with Typesense to enable efficient geospatial product search using postal codes (CEP) for Brazilian addresses.

## Overview

This project provides a service that:
- Stores and searches products in Typesense using Plus Codes
- Enables efficient geospatial product search using postal codes

## Features

- Brazilian postal code (CEP) to coordinates conversion using `pgeocode`
- Plus Code generation for precise location encoding
- Typesense integration for fast and efficient search

## Prerequisites

- Python 3.12 or higher
- Poetry for dependency management
- Docker and Docker Compose

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pluscode-typesense.git
cd pluscode-typesense
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Configure environment variables:
Create a `.env` file in the root directory with the following variables:

| Name                      | Description                  | Required | Default |
|---------------------------|------------------------------|----------|---------|
| DATABASE_HOST             | PostgreSQL database host     | Yes      | -       |
| DATABASE_PORT             | PostgreSQL database port     | Yes      | -       |
| DATABASE_USER             | PostgreSQL database user     | Yes      | -       |
| DATABASE_PASSWORD         | PostgreSQL database password | Yes      | -       |
| DATABASE_NAME             | PostgreSQL database name     | Yes      | -       |
| DATABASE_SHOW_SQL         | Enable SQL query logging     | No       | false   |
| TYPESENSE_HOST            | Typesense server host        | Yes      | -       |
| TYPESENSE_PORT            | Typesense server port        | Yes      | -       |
| TYPESENSE_API_KEY         | Typesense API key            | Yes      | -       |
| TYPESENSE_COLLECTION_NAME | Typesense collection name    | Yes      | -       |

4. Start Typesense using Docker Compose:
```bash
docker-compose up -d
```

## Usage

### API Endpoints

The service provides the following endpoints:

- `GET /search/{zipcode}`: Search products by postal code
- `POST /product/`: Create product
```json
{
    "name": "str",
    "price": 10.1,
    "zipcode": 99999999
}
```

## Development

1. Install development dependencies:
```bash
poetry install
```

2. Start the development server:
```bash
poetry run uvicorn app.server:app --reload
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Typesense](https://typesense.org/) for the search engine
- [PostgreSQL](https://www.postgresql.org/) for the database engine
- [Plus Codes](https://plus.codes/) for the location encoding system
- [pgeocode](https://github.com/symerio/pgeocode) for Brazilian postal code geocoding
