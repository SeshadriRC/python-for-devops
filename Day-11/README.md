# Dictionaries and Sets

## Additional things

-  On the gitbash cli run `pip install requests`
-  Below is the api details of Pull requests in github. For this integration we are using Kubernetes repo.
   [URL](https://docs.github.com/en/rest/pulls/pulls?apiVersion=2026-03-10)

<img width="1919" height="727" alt="image" src="https://github.com/user-attachments/assets/75a90159-c04a-4a3b-9366-a47d3a0c2dc7" />

`https://github.com/kubernetes/kubernetes`  -> URL of kubernetes repo

`first kubernetes` --> is a owner

`second kubernetes` --> is a repo

`/repos/{owner}/{repo}/pulls` --> github code

`api.github.com/repos/kubernetes/kubernetes/pulls` --> Modified code

- Paste the above  link in browser, we can see the list of dictionaries.

<img width="1919" height="938" alt="image" src="https://github.com/user-attachments/assets/d77c18a3-9ac7-4407-9cad-522e745a5571" />


```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls
```
