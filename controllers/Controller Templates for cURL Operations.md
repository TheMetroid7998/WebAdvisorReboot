*This uses USER as a template but applies to all controllers with the right attributes and variables.*
#### CREATE
`curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d "{\"user_id\":\`[USER_ID]`\",\"username\":\"`[USERNAME]`\",\"first_name\":\"`[FIRST_NAME]`\",\"last_name\":\"`[LAST_NAME]`\",\"email\":\"`[EMAIL]`\",\"prof\":`[T/F]`,\"student\":`[T/F]`}"`

#### UPDATE

cURL/HTTP Header: `curl -X PUT "http://localhost:5000/users/`[USER_ID]`" -H "Content-Type: application/json"`

| cURL/HTTP Header | Data Header | Attribute:Value Template        | Data Footer |
| ---------------- | ----------- | ------------------------------- | ----------- |
| [...]            | `-d "{`     | `\"`[ATTRIBUTE]`":\"`[VALUE]`\" | ` }"`       |

#### DELETE
`curl -X DELETE "http://localhost:5000/users/`[USER_ID]`" -H "Content-Type: application/json"`
