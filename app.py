import requests

def get_file_content(repo_url, file_path, pat_token):
    headers = {
        "Authorization": f"Bearer {pat_token}",
        "Accept": "application/vnd.github.v3.raw"
    }

    # Get the raw content of the file from the GitHub API
    raw_url = f"{repo_url}/raw/main/{file_path}"
    response = requests.get(raw_url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve file content. Status Code: {response.status_code}")
        return None

if __name__ == "__main__":
    # Replace with your private Git repository URL
    git_repo_url = "https://github.com/Tejanarni/cdk-aws"

    # Replace with the path to the file within the repository
    file_path = "loftware.yml"

    # Replace with your Personal Access Token (PAT)
    pat_token = "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"

    file_content = get_file_content(git_repo_url, file_path, pat_token)
    if file_content is not None:
        print(file_content)
