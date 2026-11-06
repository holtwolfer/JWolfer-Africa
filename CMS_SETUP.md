# Family editing dashboard — setup and limitations

This package includes all 101 existing records as separate `content/artifacts/*.json` files, a Decap CMS editor at `/admin/`, and a GitHub Actions catalog generator. Existing numbers and photographs are retained. New records may be unnumbered. The gallery reads the generated `catalog.json`.

## 1. Upload the update

Upload all new/changed files and directories to `holtwolfer/JWolfer-Africa` on `main` (GitHub Desktop is easiest for hundreds of files). Keep the existing `images/` directory. No need to re-upload unchanged images if merging these files into the existing repo.

## 2. Configure GitHub Actions

In repository Settings → Actions → General, set Workflow permissions to **Read and write permissions** (if your repository settings allow it). Run the **Build approved catalog** workflow once under Actions to verify it. This workflow commits the compiled `catalog.json` whenever artifact records are merged into `main`. GitHub Pages then serves the updated catalog.

## 3. Set up authentication (required)

GitHub Pages cannot host an OAuth server. Decap's GitHub backend needs a separately hosted, trusted OAuth authentication proxy and a GitHub OAuth App. Create the OAuth App under GitHub Developer settings, using the proxy's documented callback URL; configure the proxy with its GitHub client ID and secret; then uncomment and set `base_url` and (if necessary) `auth_endpoint` in `admin/config.yml`. **Never commit OAuth client secrets or access tokens to this public repository.** Until this is configured, `/admin/` will not be able to log in. A managed service or a separately hosted OAuth proxy may have costs; check current provider pricing and instructions.

## 4. Require your approval

Invite family members as GitHub collaborators with individual accounts. In repository Settings → Branches or Rules → Rulesets, protect `main`: require pull requests before merging, require at least one approving review, prevent bypass by collaborators, and restrict direct pushes as appropriate. The repository owner can still bypass some rules depending on configuration; test with a collaborator account. **Important:** an approving review by the repository owner cannot be guaranteed by a generic one-review rule alone. To enforce specifically *your* approval, consider a CODEOWNERS file and required code-owner reviews, and verify that the rules are enforced on your plan and repository. GitHub's own permissions and enforcement, not Decap's editorial labels, determine whether a change can reach `main`.

Decap `editorial_workflow` lets contributors save drafts and request review. For reliable approvals, use GitHub pull requests and protected `main` as the final publication gate. Some Decap editorial-workflow operations require additional write permissions; test the workflow with a separate family account before relying on it.

## 5. Add an artifact

In `/admin/`, create an Artifact, choose a new stable lowercase ID such as `artifact-102` (not an original catalog number), leave Catalog number empty if unnumbered, enter information, and upload photos. The first photo in the list becomes the gallery image. Do not change an existing stable ID. Save the proposed entry, review it on GitHub, then merge it to `main` after approval. The generator places new artifacts after the original 101, ordered by ID.

## Notes

- If image URLs are incorrect after upload, check Decap's `media_folder` and `public_folder` settings; paths must remain relative to this project site.
- Decap list/image widgets and the existing JSON array structure should be tested with one artifact before inviting contributors.
- `catalog.json` is now generated. Make lasting edits in `content/artifacts/*.json` via CMS, not in `catalog.json`.
- For cultural sensitivity and attribution accuracy, review all descriptions and images before public publication.
