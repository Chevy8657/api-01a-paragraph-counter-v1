# Paragraph Counter

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/paragraph-count?text=`

## Example

Request:
`/v1/paragraph-count?text=Para%201%0A%0APara%202%0A%0APara%203`

Response:
```json
{
  "input": "Para 1\n\nPara 2\n\nPara 3",
  "paragraph_count": 3
}
