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

| Name                      | Description                  | Required | Default   |
|---------------------------|------------------------------|----------|-----------|
| LOG_LEVEL                 | Logs severity level          | No       | INFO      |
| TYPESENSE_HOST            | Typesense server host        | No       | localhost |
| TYPESENSE_PORT            | Typesense server port        | No       | 8108      |
| TYPESENSE_API_KEY         | Typesense API key            | Yes      | -         |
| TYPESENSE_COLLECTION_NAME | Typesense collection name    | No       | products  |

4. Start Typesense using Docker Compose:
```bash
docker-compose up -d
```

## Usage

### API Endpoints

The service provides the following endpoints:

- `GET /search-using-radius?zipcode=99999999&radius=10`: Search products by latitude and longitude using typesense native GeoSearch
- `GET /search-using-pluscode?zipcode=99999999&radius=10`: Search products by latitude and longitude using pluscode
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
- [Plus Codes](https://plus.codes/) for the location encoding system
- [pgeocode](https://github.com/symerio/pgeocode) for postal code geocoding
- [postalcodes](https://symerio.github.io/postal-codes-data/data/geonames/BR.txt)