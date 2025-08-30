
https://github.com/d2l-ai/d2l-en/blob/master/config.ini

curl -s “https://giscus.app/api/discussions” -X POST -H “Content-Type:
application/json” -H “Authorization: Bearer TOKEN” -d
‘{“repo”:“IVIA-AF/livre”,“repoId”:“1017141320”,“category”:“Commentaire”,“categoryId”:“45815247”,“term”:“test”}’

| curl -s -X POST https://api.github.com/graphql
| -H “Authorization: bearer TOKEN”
| -H “Content-Type: application/json”
| -d ‘{ “query”: “query { repository(owner:"IVIA-AF", name:"livre") { id
  name } }” }’

| curl -s -X POST https://api.github.com/graphql
| -H “Authorization: bearer TOKEN”
| -H “Content-Type: application/json”
| -d ‘{ “query”: “query { repository(owner:"IVIA-AF", name:"livre") {
  discussionCategories(first:10) { nodes { id name } } } }” }’

| curl -s -X POST https://api.github.com/graphql
| -H “Authorization: bearer TOKEN”
| -H “Content-Type: application/json”
| -d ‘{ “query”: “mutation {
  createDiscussion(input:{repositoryId:"R_kgDOPKBYSA",
  categoryId:"DIC_kwDOPKBYSM4CuxXP", title:"Test", body:"Hello world"})
  { discussion { id url }}}” }’

2. Rewrite Git history to remove the secret
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

brew install git-filter-repo # macOS

git filter-repo –path README.md –replace-text <(echo
"ghp_[a-zA-Z0-9]*==>REMOVED_TOKEN")
