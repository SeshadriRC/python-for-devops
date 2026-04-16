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

- Paste the above  link in browser, we can see the list of dictionaries. And every dictionary has list of properties.

<img width="1919" height="938" alt="image" src="https://github.com/user-attachments/assets/d77c18a3-9ac7-4407-9cad-522e745a5571" />


```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/pulls
```

<img width="1752" height="978" alt="image" src="https://github.com/user-attachments/assets/3c405676-d3e6-47d4-ae5b-aefb1a203c4b" />

- We can see its not showing in proper format. so we need to separate it accordingly.

<img width="1917" height="1000" alt="image" src="https://github.com/user-attachments/assets/b775114a-7cc4-434e-87fb-e03731689517" />



<img width="1577" height="609" alt="image" src="https://github.com/user-attachments/assets/50ea3a30-9f30-4b72-90d7-7abae2ec590c" />

<img width="1919" height="1016" alt="image" src="https://github.com/user-attachments/assets/5a12a189-e068-4611-9cb3-2cd39da91e08" />


