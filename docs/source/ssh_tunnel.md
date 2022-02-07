# Connecting outside MPI-EVA

When connecting from outside the MPI-EVA servers (e.g.) from your laptop, through the VPN, you have to establish a shh tunnel

```bash
ssh -L 10001:pandora.eva.mpg.de:3306 <yourusername>@daghead1
```

You will need to slightly modify the credentials `json` file to account for the shh tunnel. An example `credentials.json` file when working through a ssh tunnel can be found here [assets/example_credentials_ssh_tunnel.json](https://raw.githubusercontent.com/sidora-tools/pydora/main/assets/example_credentials_ssh_tunnel.json)
