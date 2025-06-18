## GitHub Copilot Chat

- Extension Version: 0.28.0 (prod)
- VS Code: vscode/1.101.0
- OS: Windows

## Network

User Settings:
```json
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: 20.207.73.85 (120 ms)
- DNS ipv6 Lookup: Error (183 ms): getaddrinfo ENOTFOUND api.github.com
- Proxy URL: None (0 ms)
- Electron fetch (configured): HTTP 200 (218 ms)
- Node.js https: HTTP 200 (108 ms)
- Node.js fetch: HTTP 200 (296 ms)
- Helix fetch: HTTP 200 (107 ms)

Connecting to https://api.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 146.112.61.104 (44 ms)
- DNS ipv6 Lookup: Error (85 ms): getaddrinfo ENOENT api.individual.githubcopilot.com
- Proxy URL: None (1 ms)
- Electron fetch (configured): HTTP 403 (349 ms)
- Node.js https: HTTP 403 (397 ms)
- Node.js fetch: HTTP 403 (418 ms)
- Helix fetch: HTTP 403 (740 ms)

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).