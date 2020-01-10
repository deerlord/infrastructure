
You should clone this to /opt/infra/

$ pwd
  /opt/infra

a sample config can be found at conf.d/CONFIG.sample
note that HOST_NAME and GATEWAY_MAC are determined automatically. you should confirm these commands return the expected data on your system (they should). You should not have to change any variables that use other variables in their definition. Some variables contain example data (such as IP) addresses. These should be updated to reflect your actual environment.

for easy install
$ bash ./bin/install -c <config_file>

Caveats: you should confirm the $interface variable in `./bin/install` is correct for your host machine. if it isnt, maybe you can make a PR to improve this behavior.

Note that the install script runs `source ./bin/activate` before it does anything serious with the repo. you


