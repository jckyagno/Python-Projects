// initializes shell element which   is written to and read from
const shell = document.getElementById('shell');

// creates a sleep function which allows for easy access to delay async functions
const sleep = ms => new Promise(r => setTimeout(r,  ms));

// creates a list of characters that will not be displayed 
const restricted = [
  'Shift', 'Alt','Control','Meta','ArrowUp','ArrowDown','ArrowLeft', 'ArrowRight', 'Tab', 'Home', 'End', 'Delete'
];

// creates a list of characters to be used for interaction
const interactionKeys = [
  'Backspace', 'Enter'
];

events = [];

// creates a dictionary which stores all of the main data and provides functions to allow easy access to it in different ways
var local = {
  id: '',
  prompt: 'clip ~ % ',
  commandline: '',
  cursor: '',
  history: '',
  compose: (text='') => {
    return local['history'] + local['prompt'] + local['commandline'] + text;
  },
  get command() { 
    return local['commandline'].split(' ')[0];
  },
  get args() {
    return local['commandline'].split(' ').slice(1, local['commandline'].split(' ').length);
  },
  clear: () => {
    local['commandline'] = local['history'] = '';
  },
}

// this doesnt do anything but if i remove it the code breaks
window.onload = () => {}

// makes the cursor blink every 500ms
(async function() {
  for (let i = 1; i < 2; i = (!i * 1)) {
    if (i==0) {
      local['cursor'] += '_';
    } else {
      local['cursor'] = '';
    }
    await sleep(500);
  }
})();

// refreshes the shell every 40ms and saves the data
// this could cause performance issues but i dont care
(async function() {
  while (true) {
    await sleep(40);
    shell.innerHTML = local['compose']() + local['cursor'];
  }
})();

async function scroll() {
  await sleep(50);
  shell.scrollIntoView(false);
}

// creates an event listener which sends a keypress to the parse function if it is not restricted
document.body.addEventListener('keydown', (input) => {
  if (restricted.indexOf(input.key) == -1) {
    parse(input.key);
  }
});

// determines whether or not a character given to it is an interaction key
// if it is, it sends the character to the interact function, if not, it adds the character to the commandline
function parse(input) {
  if (interactionKeys.indexOf(input) != -1) {
    interact(input);
  }
  else {
    local['commandline'] += input;
  }
}

// determines what to do with an interaction key
// if it is a backspace, it removes the last character from the commandline
// if it is an enter, it triggers the run function
function interact(input) {
  if (input == 'Backspace') {
    local['commandline'] = local['commandline'].slice(0, -1);
  }
  else if (input == 'Enter') {
    run();
  }
}

// checks if entered command is a valid command and runs it if it is
// if it is not, it returns an error
function run() {
  if (local.command in commands) {
    commands[local.command](local.args);
  }
  else {
    local['history'] = local['compose'](`\ncommand not found: ${local.command}\n`);
    local['commandline'] = '';
  }
  scroll();
}

// creates a dictionary which stores all of the commands their functions
const commands = {
  // when called this gives the help commands
  help: (args) => {
    if (!(args in commands)) {
      local['history'] = local['compose'](helpText['help']);
      local['commandline'] = '';
    }
    else {
      local['history'] = local['compose'](helpText[args]);
      local['commandline'] = '';
    }
  },
  // when called, this clears the commandline and history
  clear: () => {
    local['clear']();
    
  },
  // provides a number of features for interacting with the database
  event: (args) => {
    // fetches any data from the server
    if (args == 'view') {
      fetch('/clip/data/', {
        headers:{
          'Accept': 'CLI_Planner/json',
          'X-Requested-With': 'XMLHttpRequest',
        },
      })
      .then(response => {
        return response.json();
      })
      .then(data => {
        console.log(data);
        if (data.length != 0) {
          local['history'] = local['compose'](getSummary(data));
          local['commandline'] = '';
        }
        else {
          local['history'] = local['compose']('\nNo events found, create one with the create event button\n');
          local['commandline'] = '';
        }
      });
    }
    else if (args[0] == 'details') {
      fetch('/clip/data/', {
        headers:{
          'Accept': 'CLI_Planner/json',
          'X-Requested-With': 'XMLHttpRequest',
        },
      })
      .then(response => {
        return response.json();
      })
      .then(data => {
        for (let i = 0; i < data.length; i++) {
          if (data[i]['id'] == args[1]) {
            local['history'] = local['compose'](parseItem(data[i]));
            local['commandline'] = '';
            local['id'] = '';
          }
          else {
            local['id'] == 'null';
          }
        }
        if (args[1] == undefined) {
          local['history'] = local['compose']('\n Please run the command with an event id, run \n | event view to see a list of events\n');
          local['commandline'] = '';
        }
        else if (local['id'] == 'null'){
          local['history'] = local['compose']('\n Event not found, create one with the create event button\n For example: \n | event details 12\n');
          local['commandline'] = '';
        }
      });
    }
    else if (args == '') {
      local['history'] = local['compose']('\n Type "help event" for more information\n');
      local['commandline'] = '';
    }
    else if (args == 'help') {
      commands['help']('event');
    }
    else {
      local['history'] = local['compose']('\n Command not found, run "help" for more information\n');
      local['commandline'] = '';
    }
  }
}

// stores all of the help text for each command
// there must be a matching key here for each command in the commands dictionary or else things will break
// i do not care
const helpText = {
  help: '\n This is a simple command line interface planner.\n The following subcommands are available:\n\n | help clear\n | help event\n\n To get more information on a specific command\n use the help command followed by the command name.\n',
  clear: '\n | clear: clears the screen\n',
  event: '\n The event command is how you interact with\n the events you have planned.\n The following subcommands are available:\n\n | event view (no arguments): displays all events and ids\n | event details (event id): displays details of a specific event\n\n * Note: you can only create events using the create event button\n',
}

// parses the json data returned from the server and returns it as a string
function getSummary(response) {
  out = '\n The following events were found:\n';
    for (let i = 0; i < response.length; i++) {
      out += ' | ID: ' + JSON.stringify(response[i]['id']) + '\n'
      out += ' | Name: ' + JSON.stringify(response[i]['event_name']) + '\n\n'
  }
  out += ' For more information on an event, run the command\n | event details (event id)\n';
  return out.replace(/"/g, '');
}

function parseItem(response) {
  out = '\n\n';
  out += ' Event name: ' + JSON.stringify(response['event_name']) + '\n'
  out += ' | Starts: ' + JSON.stringify(response['start_date']) + '\n';
  out += ' | Ends: ' + JSON.stringify(response['start_date']) + '\n';
  out += ' | Description: ' + JSON.stringify(response['description']) + '\n\n';
  return out.replace(/"/g, '');
}

