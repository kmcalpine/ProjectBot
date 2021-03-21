const logger = require('winston');
const auth = require('./auth.json');
const Commands = require('./commandHandler');
const Discord = require('discord.js');
const client = new Discord.Client();

// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(new logger.transports.Console, {
    colorize: true
});

logger.level = 'debug';
client.login(auth.token);

console.log('running...');

const command = new Commands(client, Discord);
client.on('message', (message) =>  {
    command.handle(message);
});