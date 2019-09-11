#!/usr/bin/python3
import os
import random
import argparse

def get_parser():
	parser = argparse.ArgumentParser(description="Parotify Linux")
	parser.add_argument('--parotify', '-p', help='Make terminal look like parrot os',
					action="store_true")
	parser.add_argument('--revert', '-r', help='Revert to normal look',
					action="store_true")
	return parser

def parrotify(path):
	print(path)
	t = open(path , 'w+')
	payload = ['# Winter Says  parrot is awesome OS\n',  '#\n', '#\n', '# ~/.bashrc: executed by bash(1) for non-login shells.\n', '# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)\n', '# for examples\n', '\n', "# If not running interactively, don't do anything\n", '[ -z "$PS1" ] && return\n', '\n', "# don't put duplicate lines in the history. See bash(1) for more options\n", '# ... or force ignoredups and ignorespace\n', 'HISTCONTROL=ignoredups:ignorespace\n', '\n', "# append to the history file, don't overwrite it\n", 'shopt -s histappend\n', '\n', '# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)\n', 'HISTSIZE=1000\n', 'HISTFILESIZE=2000\n', '\n', '# check the window size after each command and, if necessary,\n', '# update the values of LINES and COLUMNS.\n', 'shopt -s checkwinsize\n', '\n', '# make less more friendly for non-text input files, see lesspipe(1)\n', '[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"\n', '\n', '# set variable identifying the chroot you work in (used in the prompt below)\n', 'if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then\n', '    debian_chroot=$(cat /etc/debian_chroot)\n', 'fi\n', '\n', '# set a fancy prompt (non-color, unless we know we "want" color)\n', 'case "$TERM" in\n', '    xterm-color) color_prompt=yes;;\n', 'esac\n', '\n', '# uncomment for a colored prompt, if the terminal has the capability; turned\n', '# off by default to not distract the user: the focus in a terminal window\n', '# should be on the output of commands, not on the prompt\n', '#force_color_prompt=yes\n', '\n', 'if [ -n "$force_color_prompt" ]; then\n', '    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then\n', " # We have color support; assume it's compliant with Ecma-48\n", ' # (ISO/IEC-6429). (Lack of such support is extremely rare, and such\n', ' # a case would tend to support setf rather than setaf.)\n', ' color_prompt=yes\n', '    else\n', ' color_prompt=\n', '    fi\n', 'fi\n', '\n', 'if [ "$color_prompt" = yes ]; then\n', '    PS1="\\[\\033[0;31m\\]\\342\\224\\214\\342\\224\\200\\$([[ \\$? != 0 ]] && echo \\"[\\[\\033[0;31m\\]\\342\\234\\227\\[\\033[0;37m\\]]\\342\\224\\200\\")[$(if [[ ${EUID} == 0 ]]; then echo \'\\[\\033[01;31m\\]root\\[\\033[01;33m\\]@\\[\\033[01;96m\\]\\h\'; else echo \'\\[\\033[0;39m\\]\\u\\[\\033[01;33m\\]@\\[\\033[01;96m\\]\\h\'; fi)\\[\\033[0;31m\\]]\\342\\224\\200[\\[\\033[0;32m\\]\\w\\[\\033[0;31m\\]]\\n\\[\\033[0;31m\\]\\342\\224\\224\\342\\224\\200\\342\\224\\200\\342\\225\\274 \\[\\033[0m\\]\\[\\e[01;33m\\]\\\\$\\[\\e[0m\\]"\n', "    #PS1='${debian_chroot:+($debian_chroot)}\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]\\$ '\n", 'else\n', '    PS1="\\[\\033[0;31m\\]\\342\\224\\214\\342\\224\\200\\$([[ \\$? != 0 ]] && echo \\"[\\[\\033[0;31m\\]\\342\\234\\227\\[\\033[0;37m\\]]\\342\\224\\200\\")[$(if [[ ${EUID} == 0 ]]; then echo \'\\[\\033[01;31m\\]root\\[\\033[01;33m\\]@\\[\\033[01;96m\\]\\h\'; else echo \'\\[\\033[0;39m\\]\\u\\[\\033[01;33m\\]@\\[\\033[01;96m\\]\\h\'; fi)\\[\\033[0;31m\\]]\\342\\224\\200[\\[\\033[0;32m\\]\\w\\[\\033[0;31m\\]]\\n\\[\\033[0;31m\\]\\342\\224\\224\\342\\224\\200\\342\\224\\200\\342\\225\\274 \\[\\033[0m\\]\\[\\e[01;33m\\]\\\\$\\[\\e[0m\\]"\n', "    #PS1='${debian_chroot:+($debian_chroot)}\\u@\\h:\\w\\$ '\n", 'fi\n', 'unset color_prompt force_color_prompt\n', '\n', '# If this is an xterm set the title to user@host:dir\n', 'case "$TERM" in\n', 'xterm*|rxvt*)\n', '    PS1="\\[\\033[0;31m\\]\\342\\224\\214\\342\\224\\200\\$([[ \\$? != 0 ]] && echo \\"[\\[\\033[0;31m\\]\\342\\234\\227\\[\\033[0;37m\\]]\\342\\224\\200\\")[$(if [[ ${EUID} == 0 ]]; then echo \'\\[\\033[01;31m\\]root\\[\\033[01;33m\\]@\\[\\033[01;96m\\]\\h\'; else echo \'\\[\\033[0;39m\\]\\u\\[\\033[01;33m\\]@\\[\\033[01;96m\\]\\h\'; fi)\\[\\033[0;31m\\]]\\342\\224\\200[\\[\\033[0;32m\\]\\w\\[\\033[0;31m\\]]\\n\\[\\033[0;31m\\]\\342\\224\\224\\342\\224\\200\\342\\224\\200\\342\\225\\274 \\[\\033[0m\\]\\[\\e[01;33m\\]\\\\$\\[\\e[0m\\]"\n', '    #PS1="\\[\\e]0;${debian_chroot:+($debian_chroot)}\\u@\\h: \\w\\a\\]$PS1"\n', '    ;;\n', '*)\n', '    ;;\n', 'esac\n', '\n', '# enable color support of ls and also add handy aliases\n', 'if [ -x /usr/bin/dircolors ]; then\n', '    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"\n', "    alias ls='ls --color=auto'\n", "    #alias dir='dir --color=auto'\n", "    #alias vdir='vdir --color=auto'\n", '\n', "    alias grep='grep --color=auto'\n", "    alias fgrep='fgrep --color=auto'\n", "    alias egrep='egrep --color=auto'\n", 'fi\n', '\n', '# some more ls aliases\n', "alias ll='ls -alF'\n", "alias la='ls -A'\n", "alias l='ls -CF'\n", '\n', '# Add an "alert" alias for long running commands.  Use like so:\n', '#   sleep 10; alert\n', 'alias alert=\'notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e \'\\\'\'s/^\\s*[0-9]\\+\\s*//;s/[;&|]\\s*alert$//\'\\\'\')"\'\n', '\n', '# Alias definitions.\n', '# You may want to put all your additions into a separate file like\n', '# ~/.bash_aliases, instead of adding them here directly.\n', '# See /usr/share/doc/bash-doc/examples in the bash-doc package.\n', '\n', 'if [ -f ~/.bash_aliases ]; then\n', '    . ~/.bash_aliases\n', 'fi\n', '\n', "# enable programmable completion features (you don't need to enable\n", "# this, if it's already enabled in /etc/bash.bashrc and /etc/profile\n", '# sources /etc/bash.bashrc).\n', 'if [ -f /etc/bash_completion ] && ! shopt -oq posix; then\n', '    . /etc/bash_completion\n', 'fi\n']
	for i in payload:
		t.write(i)
	t.close()
	
	
def backup_bashrc(old, new, parser):
	if  os.path.isfile(new):
		print("your parrot terminal has alreaady been set up \n ")
		parser.print_help()
	else:
		os.system(f'mv {old} {new} ')
		parrotify(old)
		
def reversify(old, new, user=os.getlogin()):
	if  os.path.isfile(new):
		os.system(f'mv {new} {old} ')
		
def main():
	fonts = ["block","bubble","digital","ivrit","mini","script","shadow","slant","small","smscript","smshadow","smslant","standard"]
	random.shuffle(fonts)
	os.system("clear")
	os.system('echo  "\\e[1;31m\"')
	os.system(f"figlet -c -f {fonts[random.randint(0, len(fonts)-1)]}    PAR0tifyTerm   ")
	os.system('echo "\\e[1;32m\"')
	os.system('echo "\\e[1;32m\"')
	os.system('echo "\\e[1;34m Created By W1nterFr3ak\\e[0m"')
	os.system('echo "\\e[2;32m Winter says Parrot is awesome \\e[0m"')
	os.system('echo "\\e[1;32m   Mail: WinterFreak@protonmaail.comm \\e[0m"')
	print()
	user=os.getlogin()
	path = '/home/' + user + '/.bashrc'
	pathn = '/home/' + user + '/.bashrcold'
	parser  = get_parser()
	args  = vars(parser.parse_args())
	parrot = args['parotify']
	rev = args['revert']
	
	if parrot:
		backup_bashrc(path, pathn, parser)
	elif rev:
		reversify(path, pathn)
	else:
		parser.print_help()
	

if __name__ == "__main__":
	main()
