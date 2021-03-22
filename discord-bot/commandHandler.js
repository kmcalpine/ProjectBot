const { MessageEmbed } = require('discord.js');
const axios = require('axios');

class Commands {
    constructor(client, discord) {
        this.discord = require('discord.js');
    }

    async handle(message) {
        if (message.content.substring(0, 1) === '!') {
            let args = message.content.substring(1).split(' '),
            cmd = args[0];

            args = args.splice(1);
            try {
                console.log('reading message');
                let response = await axios.get('http://127.0.0.1:8000/api/commands/' + message.guild.id + '/' + cmd +'.json/');
                message.channel.send(response.data[0].fields.msg_response);
            } catch (e) {
                console.log(e)
            }
        }
    }
}

module.exports = Commands;


