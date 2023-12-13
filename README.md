# Upload and Download Management with Custom Error Handling

This Spring Boot application utilizes the Lombok framework to simplify code and provides functionality for uploading and downloading files with custom error handling.
This application allows users to download files. Below are some of the possible error scenarios:

## Errors

### 1. File Not Found (HTTP 404)
   - **Endpoint:** `/download/file-not-found`
   - **Description:** Attempting to download a file that does not exist.
   - **Error Message:** Error 404 - File not found 🚫📄

### 2. Filename Invalid (HTTP 400)
   - **Endpoint:** `/download/filename-invalid`
   - **Description:** Providing an invalid filename during download.
   - **Error Message:** Error 400 - Invalid filename 🚫📄

### 3. Not Implemented (HTTP 501)
   - **Endpoint:** `/download/not-implemented`
   - **Description:** Trying to download a file download feature that is not yet implemented.
   - **Error Message:** Error 501 - Not implemented 🚧📄

## Technologies Used

- Java
- Spring Boot
- Lombok

## Prerequisites

- Java 17
- Maven
- Web browser
- Postman

## Features

- **File Upload:** Users can upload files through the application.
- **File Download:** Uploaded files can be downloaded.
- **Custom Error Handling:** Custom errors are returned for specific situations, such as file already existing, invalid file type, file size exceeding the limit, etc.
## Participation
[Vohizy](https://github.com/Vohizy) and 
[jaonary-74](https://github.com/jaonary-74)

## Usage

1. Clone the repository.
2. Build and run the application.
3. Access the specified endpoints to simulate errors.
