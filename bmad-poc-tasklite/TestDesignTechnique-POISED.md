# POISED Test Design Approach

## Overview

**POISED** is a testing heuristic used to design and structure tests for
APIs and service interfaces. It helps testers systematically explore
different aspects of an API by focusing on six key areas of quality.

The acronym **POISED** stands for:

-   **P** -- Parameters\
-   **O** -- Output\
-   **I** -- Interoperability\
-   **S** -- Security\
-   **E** -- Error Handling\
-   **D** -- Data

Testing heuristics like POISED provide guidelines rather than strict
rules. They help testers generate test ideas and explore systems even
when requirements are incomplete or unclear.

------------------------------------------------------------------------

## The POISED Test Design Model

The POISED heuristic organizes test design into six categories.

  -----------------------------------------------------------------------
Category                Focus                   Testing Goal
  ----------------------- ----------------------- -----------------------
**P -- Parameters**     API inputs              Validate input values
and parameter handling

**O -- Output**         API responses           Verify correctness and
structure of returned
data

**I --                  Integration             Ensure the API works
Interoperability**                              with other systems

**S -- Security**       Protection              Validate
authentication,
authorization, and
vulnerabilities

**E -- Error Handling** Failure scenarios       Check error messages
and codes

**D -- Data**           Data quality            Validate integrity and
consistency of
exchanged data
  -----------------------------------------------------------------------

Each category helps testers explore different risks and quality aspects
of an API.

------------------------------------------------------------------------

## P --- Parameters

The **Parameters** dimension focuses on the inputs provided to the API.

Typical tests include:

-   Valid parameters
-   Invalid parameters
-   Boundary values
-   Missing parameters
-   Data type validation
-   Parameter combinations

Example tests:

GET /weather?city=London\
GET /weather?city=\
GET /weather?city=123\
GET /weather

Goal:

Ensure the API correctly validates and processes input parameters.

------------------------------------------------------------------------

## O --- Output

The **Output** dimension focuses on the correctness and structure of
responses returned by the API.

Typical checks include:

-   HTTP status codes
-   Response schema validation
-   Response format (JSON, XML)
-   Field presence
-   Response completeness

Example tests:

Response code = 200\
Response body contains expected fields\
Response structure matches schema

Goal:

Ensure the API returns accurate and correctly structured results.

------------------------------------------------------------------------

## I --- Interoperability

The **Interoperability** dimension evaluates how well the API integrates
with other systems.

Typical tests include:

-   Compatibility with different clients
-   Interaction with other services
-   Cross-platform behavior
-   Different API consumers

Example scenarios:

-   Mobile app consuming the API
-   Web frontend using the API
-   Third-party system integration

Goal:

Ensure the API works reliably across different environments and systems.

------------------------------------------------------------------------

## S --- Security

The **Security** dimension verifies that the API protects data and
access properly.

Typical tests include:

-   Authentication validation
-   Authorization checks
-   Token validation
-   Injection attacks
-   Data exposure checks
-   Encryption verification

Example tests:

Unauthorized request\
Expired token\
Invalid authentication credentials

Goal:

Ensure the API is protected against unauthorized access and
vulnerabilities.

------------------------------------------------------------------------

## E --- Error Handling

The **Error Handling** dimension focuses on how the API behaves when
something goes wrong.

Typical checks include:

-   Correct error status codes
-   Meaningful error messages
-   Error structure consistency
-   System stability during failure

Example tests:

Invalid endpoint\
Missing required parameter\
Internal server failure

Goal:

Ensure the API communicates failures clearly and behaves predictably
under error conditions.

------------------------------------------------------------------------

## D --- Data

The **Data** dimension verifies the quality and integrity of data
processed by the API.

Typical tests include:

-   Data consistency
-   Data accuracy
-   Data persistence
-   Data integrity
-   Data transformations

Example tests:

Verify stored data matches request\
Validate returned data accuracy\
Check database consistency

Goal:

Ensure data exchanged through the API is correct, consistent, and
reliable.

------------------------------------------------------------------------

## Applying POISED in Test Design

The POISED approach can be used during test design workshops or
exploratory testing sessions.

Typical process:

1.  Identify the API endpoint to test
2.  Apply the POISED dimensions
3.  Generate test ideas for each dimension
4.  Prioritize tests based on risk
5.  Implement manual or automated tests

Example structure:

Endpoint: GET /weather

P -- Parameters\
Test city parameter variations

O -- Output\
Validate response schema

I -- Interoperability\
Test from web and mobile clients

S -- Security\
Test authentication token

E -- Error\
Test invalid city input

D -- Data\
Verify data consistency with backend

------------------------------------------------------------------------

## Benefits of POISED Test Design

Using the POISED heuristic provides several advantages:

-   Structured API test exploration
-   Broader test coverage
-   Better identification of edge cases
-   Improved API reliability
-   Faster test idea generation

Heuristics like POISED allow testers to think systematically about
potential issues without rigid test scripts.

------------------------------------------------------------------------

## When to Use the POISED Approach

The POISED heuristic is particularly useful for:

-   API testing
-   Microservices testing
-   Contract testing
-   Integration testing
-   Exploratory testing sessions

It is especially helpful when:

-   documentation is limited
-   systems are complex
-   rapid test design is required

------------------------------------------------------------------------

## Summary

The **POISED Test Design approach** is a practical heuristic for
designing API tests. By systematically exploring **Parameters, Output,
Interoperability, Security, Error Handling, and Data**, testers can
identify risks and improve the quality and robustness of APIs.

The approach provides a structured yet flexible framework for exploring
API behavior and ensuring comprehensive test coverage.