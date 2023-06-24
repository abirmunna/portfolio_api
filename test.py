import requests
import json

designation = requests.get(
    "https://port.abirmunna.me/designation", headers={"Accept": "application/json"}
)
print(designation.json())

# post request on designation route
# designation_post = requests.post('https://abirmunna-psychic-winner-6rpxg6g5v49h4r4p-8000.preview.app.github.dev/designation',
#                     headers={'Accept': 'application/json'},
#                     json={
#                         "name": "final",
#                         "company": "test",
#                         "location": "done"
#                         })

# print(designation_post.json())
