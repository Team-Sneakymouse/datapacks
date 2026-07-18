docker run --rm -it ^
  -e EULA=TRUE ^
  -e TYPE=PAPER ^
  -e VERSION=26.1.1 ^
  -e RCON_CMDS_STARTUP=stop ^
  -v "%cd%\.testserver:/data" ^
  -v "%cd%\plots:/data/world/datapacks/plots" ^
  -p 25565:25565 ^
  itzg/minecraft-server
