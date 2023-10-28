# Telegram to Discord Message Bot — Forward Telegram Messages to Discord 

<img src="https://img.shields.io/badge/Status-works%20after%20lot%20of%20debugging-red"> <img src="https://img.shields.io/badge/Python%20Skill-intermediate%20-brightgreen"> 

* This repo will soon be archived and won't be supported.


## Description
AUTO-TELEGRAM-TO-DISCORD-FORWARDER is a free and open source, can automatically sends posts of telegram to discord bot in form of TEXT, IMAGE(.jpg), VIDEO(.mp4). It enables one to forward posts from Multiple Telegram channels to one (or more) Telegram/Discord channels of your own. This python bot monitors multiple telegram channels. When a new message/entity is sent, it will parse the response and forward it to a discord channel using your own personalized bot. It will also forward the same message to your own Telegram channel.


## Getting Started

1. Create a [github]([https://github.com/login](https://github.com/signup?source=login)) account. It always helps !
2. Star this repository. Its FREE !
3. Please follow me here if you like my contribution: [<img src="https://p.kindpng.com/picc/s/726-7262336_deadpool-logo-pixel-art-hd-png-download.png" width="25"/>](https://github.com/Rohiteswar)

### Dependencies

1. Install Docker: If you haven't already, you need to install Docker on your machine. You can download it from the [official Docker website Docs](https://docs.docker.com/engine/install/). 
2. Run This Command to check docker is installed Successfully or NOT. this command shows the Docker's Version : `docker -v`
2. Create your own discord bot, add it to your server and retrive token. Follow Steps [here](https://www.writebots.com/discord-bot-token/).
3. Have a Telegram account with valid phone number


### Installing and Setup

* This Porject can Easily deployed and run on different systems without worrying about dependencies or system-specific issues until and unless you have Docker Installed on your PC.
1. Clone this repository
2. Open your choice of console (or VSCode console) and navigate to cloned folder 
3. Fill out a configuration file. An exmaple file can be found at `config.yml-sample`. 

### First Run and Usage

1. Change the name of `config.yaml-sample` to `config.yaml`

#### Filling `config.yml` file

* Create a two channels on Telegram as `channel_send` and `channel_recieve` and fill in their channel ids in config.yaml
* Add your Telegram `api_id` and `api_hash` to config.yml | Read more [here](https://core.telegram.org/api/obtaining_api_id)
* Add your `discord_bot_token` to config.yml | Read more [here](https://www.writebots.com/discord-bot-token/)
* Add your `discord_1_channel` channel id. Remember when you remove extra discord channels you have to update code in `discord_forward.py` under comment `DISCORD SERVER START EVENT` and `MESSAGE SCREENER`

#### Editing `discord_messager.py`

* Whenever you add and delete discord channels in `config.yml`; `discord_messager.py` will have to be updated. If you know basic python you will understand the code.
* Multiple send/recieve telegram channels in `config.yml` can added without any code change.

2. Read the Version History and Changelog and below before running the script.

3. Run The Command To Build An Image: `docker build -t AUTO-BOT .`.

4. RUN THE COMMAND TO START THE APPLICATION : `docker run`

```
***PLEASE NOTE:  In the first time you are running the docker image, you will be requried to validate your phone number using telegram API. This happens only at the first time (per session name).
```

## Author

* Rohiteswar Velagapudi

<a href="https://www.buymeacoffee.com/rohiteswar" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
