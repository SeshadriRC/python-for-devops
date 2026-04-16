# Dictionaries and Sets

## Additional things

-  On the gitbash cli run `pip install requests`
-  Below is the api details of Pull requests in github.
   [URL](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2026-03-10)

<img width="1919" height="727" alt="image" src="https://github.com/user-attachments/assets/75a90159-c04a-4a3b-9366-a47d3a0c2dc7" />


```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls
```
