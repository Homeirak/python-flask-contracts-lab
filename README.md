# Flask Contracts Lab

## Project Overview

This Flask-based app simulates a contract management system with two key routes for securely handling sensitive data.

---

## Features

- `GET /contract/<id>`  
  - Returns contract information if found (200 OK)  
  - Returns error message if not found (404 Not Found)

- `GET /customer/<customer_name>`  
  - Confirms existence of a customer without returning data (204 No Content)  
  - Returns error message if customer not found (404 Not Found)

---

## Testing

All routes were manually tested using:
- Web browser
- DevTools Network tab
- `curl` in terminal

---

## Example URLs

- `http://127.0.0.1:5555/contract/1`
- `http://127.0.0.1:5555/customer/bob`

---

## Status Codes Used

| Route                       | Condition                  | Response Code |
|----------------------------|----------------------------|---------------|
| `/contract/<id>`           | Contract exists            | 200           |
| `/contract/<id>`           | Contract not found         | 404           |
| `/customer/<customer_name>`| Customer exists            | 204           |
| `/customer/<customer_name>`| Customer not found         | 404           |

---

## Cleanup

- Old feature branch deleted after merge  
- No sensitive data or commented code left  
- `.gitignore` updated if necessary (N/A in this case)