# Basics of HTTP/HTTPS

## HTTP vs HTTPS — Differences

| Aspect                | HTTP                                | HTTPS                                        |
|-----------------------|-------------------------------------|----------------------------------------------|
| **Security**          | Not secure, data is in plain text   | Secure via **SSL/TLS** (encryption)          |
| **Default Port**      | 80                                  | 443                                          |
| **Certificate**       | No certificate required             | Requires a valid **SSL/TLS certificate**     |
| **URL Scheme**        | Starts with `http://`               | Starts with `https://`                       |
| **Protection**        | Vulnerable to interception/sniffing | Protects against interception and MITM       |
| **Typical Usage**     | Public sites with no sensitive data | E-commerce, banking, social media            |

> **Summary**: HTTPS is essential when exchanging personal or sensitive data. It is now the **standard** for most websites.

---

## Structure of an HTTP Request & Response

### HTTP Request (Example: GET)
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

### HTTP Response (Example: 200 OK)
```
HTTP/1.1 200 OK
Date: Mon, 06 Oct 2025 09:00:00 GMT
Server: Apache/2.4.1
Content-Type: text/html; charset=UTF-8
Content-Length: 137

<html>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
```

---

## Common HTTP Methods

| Method   | Description                                      | Typical Use Case                          |
|----------|--------------------------------------------------|-------------------------------------------|
| **GET**  | Retrieves data without modifying the resource     | Load a webpage, fetch API data            |
| **POST** | Sends data to the server (creates a resource)     | Submit a form, create a user              |
| **PUT**  | Updates or creates a resource                     | Update a user profile                     |
| **DELETE** | Deletes a resource                              | Remove an article or a user account       |
| **PATCH** | Partially updates a resource                     | Modify a specific field in a resource     |

---

## Common HTTP Status Codes

| Code  | Meaning                 | Description & Scenario                                                |
|-------|-------------------------|------------------------------------------------------------------------|
| **200** | OK                     | Request succeeded (e.g., page loads without error)                     |
| **201** | Created                | A new resource was created (e.g., POST to create a user)               |
| **301** | Moved Permanently      | The resource has been permanently moved (e.g., URL redirection)        |
| **404** | Not Found              | The requested resource doesn't exist (e.g., invalid page URL)          |
| **500** | Internal Server Error  | Server-side error (e.g., broken script or misconfigured server)        |

---

## Objectives Achieved

Differentiate between HTTP and HTTPS.
Understand the structure of an HTTP request and response.
Identify and explain common HTTP methods.
Interpret common HTTP status codes.