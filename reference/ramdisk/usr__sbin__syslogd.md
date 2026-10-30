# `/usr/sbin/syslogd`

From the upgrade restore ramdisk (141-29011-104.dmg). 183,456 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 19 (Size: 1656)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (2)

- `/usr/lib/libbsm.0.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (570)

```
[Sender syslogd] [Level 1] [PID %u] [Facility syslog] [Message FATAL ERROR: mach_msg() receive failed with status 0x%08x]
%s %d: read error on socket %d: %d %s\n
%d%02d%02dT%02d%02d%02d%c%02u
enable
only
[Sender syslogd] [Level 2] [PID %u] [Message Internal memory size limit %lld exceeded - dropping messages] [UID 0] [UID 0] [Facility syslog]
com.apple.system.logger
ASLFreeNotify
_act_store_dir_setup: _act_dst_open %s failed\n
Work queue draining: dropped message.\n
= crash
__asl_server_create_aux_link: %s\n
__asl_server_cancel_direct_watch: %hu\n
%d\n
ASLFinalNotification
define
%d 
SenderMachUUID
mach_port_allocate listen_set failed: %d
/Library/Logs/
v12@?0i8
_asl_dir_storedata_close %p\n
/etc/syslog.conf
user
asl_memory_open: %s\n
MachServices
Work Queue
truncate
crit
hostname
com.apple.syslogd.message
com.apple.system.log.kernel.emergency
watchers_active
_act_store_file
alert
%casl_file
[base=%s].%s\n
    mode: 0%o\n
client_count
                         modifiers (must follow operator):\n
ASL Action Queue
Time
[Sender syslogd] [Level 5] [PID %u] [Message Configuration Notice:\nASL Module \"%s\" claims selected messages.\nThose messages may not appear in standard system log files or in the ASL database.] [UID 0] [GID 0] [Facility syslog]
_asl_server_query_2
__asl_server_message: %s\n
StoreData
r+
close ASL fd %d\n
_asl_file_open ASL file %s fd %d\n
_asl_server_register_direct_watch
com.apple.system.syslog.master
w
klog_in
    raw                  use raw format for printing messages\n
%s: %s save to %s failed: %s\n
mach_port_move_member dead_session_port failed (%u)
-launchd_in
%s\n
mobile
_asl_dir_storedata_open: chown %d %d new %s: %s\n
control
asl_input_parse: %s\n
StringMemory
$ENV(
com.apple.system.utmpx
%csize_only
%s/module/%s/%s
%s: getaddrinfo failed for node %s service %s: (%s)\n
Unknown
%lld
reading launch plist\n
claim
false
style=
crashlog
    * op key val         search for matching messages (single key/value pair)\n
asl_dir      
w+
\n========================\nASL is here to serve you\n
_act_store_dir asl_file_save FAILED %s\n
utmp_ttl
CheckIn
uid=
%s/%s.asl
%s: open failed for file: %s (%s)\n
/dev/console
%s %d: error on socket %d\n
memory database is not enabled\n
-klog_in
com.apple.system.notify.service.path:0x87:
db
UID
%csoft
%s: connection failed for %s\n
datastore
%s: launchd file discriptor array element 0 is NULL\n
%d-%02d-%02dT%02d:%02d:%02dZ
asl_directory
already watching!\n
mach_port_allocate dead_session_port failed: %d
forward      
CrashMover finished\n
com.apple.system.log.kernel.info
/etc/asl.conf
NULL
remote
%d launchd lookup of SERVICE_NAME failed\n
2
000
access
com.apple.crash_mover
_asl_dir_today_open: fseek %s error %s\n
W %d %llu
GID
%u
com.apple.asl.access_as_uid
alloc failed (init_modules asl_action)\n
output       
_asl_dir_create: asl_out_mkpath failed: %s\n
send_to_direct_watchers: exceeded EAGAIN limit - closing connection\n
DB size %u\n
NetworkListener
%cenabled
%casl_directory
control      
 \t
mem
notify_register_plain(%s) failed status %u\n
Direct Watch Queue
%d launchd checkin failed\n
_act_file
send_to_direct_watchers: lockdown %d write error: %d %s\n
bsd_queue_count
%s: launchd lookup of UDP_SOCKET_NAME failed\n
    format: %s\n
_act_store_file_setup: asl_file_read_set_position failed %d %s\n
%s %d: starting interactive session for %ssocket %d\n
%s %d: terminating session for %ssocket %d\n
daemon
TimeNanoSec
__asl_server_register_direct_watch: pid %u port %hu\n
{XPC_TYPE_ARRAY}
disabled
%s: error sending message (%s): %s\n
MaxStringMemory
link
kernel
    ttl: %s\n
add_lockdown_session: realloc failed\n
FATAL ERROR: mach_msg() receive failed with status 0x%08x\n
/usr/local/etc/asl
<local-basic>
cancel/close ASL storedata fd %d\n
                         operators:  =  <  >  ! (not equal)  T (key exists)  R (regex)\n
%s: fcntl: %s\n
%s: setsockopt: %s\n
{XPC_TYPE_SHMEM}
ttl
_asl_dir_storedata_open: fopen existing %s: %s\n
Level
r
com.apple.system.log.kernel.error
%s: fd %d recvfrom %s len %d\n
Sockets
format=
coalesce=
Message
s
[Plist\t
soft
file         
stats_interval
-1
ASLExpireTime
    * [op key val] ...   search for matching messages (multiple key/value pairs)\n
ASLMessageID
fmt=
none         
notify       
_act_dst_close: %s ASL DIR %s\n
ASL Sender Statistics
alloc failed (init_modules klog_in)\n
%s: couldn't set O_NONBLOCK for file descriptor %d: %s\n
broadcast    
_asl_dir_storedata_open: fopen new %s: %s\n
*%s
[Sender syslogd] [Level 3] [PID %u] [Facility syslog] [Message mach_msg() send failed with status 0x%08x (MACH_SEND_INVALID_HEADER)]
asl_dir
/var/log/
%s %d: select %d %s\n
%cexternal
unset
_asl_file_open: asl_file_open_write %s failed %d %s\n
appletv
(none)
    uid:
checkpoint
asl_db_memory
/var/run/lockdown/syslog.sock
%f
rotate
,.
/
msg
_asl_dir_storedata_open: No directory at path %s\n
%u%s
<unknown>
com.apple.system.config.network_change
udp_in
    file_max: %lu\n
_act_store_dir_setup: storedata write failed %d %s\n
cancel/close ASL file fd %d\n
remove_lockdown_session: realloc failed\n
ut_id
    all_max: %lu\n
%s/%s
%s: error re-writing message (%s): %s\n
broadcast
_asl_file_open: asl_out_mkpath %s failed\n
BSD Out Queue
(retry) asl_store_save: %s\n
db_memory_str_max
SIGHUP reset\n
asl_file     
_act_store_dir_setup: aslfile fseek failed %d %s\n
_act_dst_open:_asl_dir_storedata_open %s FAILED!  Closing today file\n
0
action
Q [%s]
%s %d: %d/%d write data failed: %d %s\n
[Plist 
(retry) asl_memory_save: %s\n
lockdown_session_count
    std                  use standard format for printing messages\n
%crotate
[File\t
asl_action_control_set_param: memory allocation failed\n
MaxRecords
StringCount
%d%02d%02dT%02d%02d%02d%c%02u%02u%02u
%s: init\n
= reset
sweep_lockdown_session_fds: realloc failed\n
set
_asl_dir_today_open: asl_file_open_write %s error %s\n
 ; 
file database is not enabled\n
%s
_asl_server_message
raw
  data: NULL
store
CHECKPOINT RENAME %s %s\n
%s%s
[Sender syslogd] [Level 3] [PID %u] [Facility syslog] [Message mach_msg() send failed with status 0x%08x (MACH_SEND_NO_BUFFER)]
alloc failed (init_modules)\n
[Sender syslogd] [Level 4] [PID %u] [Facility syslog] [Message File %s was closed with %d pending messages]
sec
/var/run/lockdown
ut_pid
{XPC_TYPE_ERROR}
_asl_dir_today_open: localtime_r error %s\n
error
err
    select [val]         get [set] current database\n
    flush                flush database\n
-udp_in
off
Q [= %s]
deleted
syslogd
notify
error: can't create data store %s: %s\n
FATAL ERROR: mach_msg() send failed with status 0x%08x\n
%s/%s.%s.%s
; \t
unknown database type\n
mach_port_move_member server_port failed: %d
debug
[Sender syslogd] [Level 6] [PID %u] [Message -- MARK --] [UID 0] [UID 0] [Facility syslog]
%s: couldn't set receive buffer size for file descriptor %d: %s\n
RecordCount
    flags: 0x%08x
compress
cancel/close file fd %d\n
/var/log/syslogd.log
[Sender syslogd] [Level 5] [PID %u] [Message Configuration Notice:\nASL Module \"%s\" sharing output destination \"%s\" with ASL Module \"%s\".\nOutput parameters from ASL Module \"%s\" override any specified in ASL Module \"%s\".] [UID 0] 
%s: malloc: %s\n
-bsd_out
starting mach service\n
%c%llu
 %d
ASLModule
_asl_dir_storedata_open: stat error %s\n
remote_delay_time
    quit                 exit session\n
-utmp_ttl
    time_format: %s\n
%ccrashlog
error: can't stat data store %s: %s\n
not watching!\n
%d-%02d-%02dT%02d:%02d:%02d%c%u
 %s
<seconds>
%s: bind: %s\n
-config
{XPC_TYPE_DICTIONARY}
[base=%s].[ext=%s].%s\n
db_file_max
/etc/asl
extern
basestamp
%s: couldn't set O_NONBLOCK for fd %d: %s\n
set          
set (file)   
kern
%lu
 
Goodbye\n
gid=
_act_dst_close: %s ASL FILE %s\n
%s: error writing repeat message (%s): %s\n
%s: unsupported / unknown output name: %s\n
lockdown 
    dbsize [val]         get [set] database size (# of records)\n
%ccoalesce
%s: --- last message repeated %u time%s ---\n
error: %s is not a directory
%s: couldn't set O_NONBLOCK for fd %d (%s): %s\n
    dest: %s\n
        rotatation style: 
_act_store_dir_setup: storedata read failed %d %s\n
idle
com.apple.system.hostname
ASL Server Queue
directory
/Library/Logs/CrashReporter
initializing modules\n
[Sender syslogd] [Level 2] [PID %u] [Facility syslog] [Message *** MESSAGE QUOTAS DISABLED FOR ALL PROCESSES ***]
[base=%s].%s.[ext=%s]\n
_asl_dir_storedata_open ASL storedata %s fd %d\n
bsd_out
syslog
ERROR: mach_msg() send failed with MACH_SEND_INVALID_HEADER 0x%08x\n
    rules: %u\n
ignore
mark_time
dup_delay
mps_limit
remote_delay
   M %u %u %lu
com.apple.system.log.kernel.alert
dbtype
                                 C=casefold  N=numeric  S=substring  A=prefix  Z=suffix\n
ignore       
_act_dst_open:_asl_dir_today_open %s FAILED!\n
com.apple.system.lastlog
_asl_server_create_aux_link
    *                    show all log messages\n
file store\n
{XPC_TYPE_???}
0x%08x\n
store_dir
panic
memory_max
{XPC_TYPE_FD}
%csymlink
RefPID
work_queue_count
%s: error writing message (%s): %s\n
dispatch_source DISPATCH_VNODE_DELETE fd %d\n
ERROR: mach_msg() send failed with MACH_SEND_NO_BUFFER 0x%08x\n
enter \"help\" for help\n
1
\n%s syslogd PID %d starting\n
skip
dst=
Session
not 
setting up network change notification handler\n
_asl_file_open: _act_file_create_open %s failed %d %s\n
none
Work queue disabled.  msize %lld  size %lld  max %lld\n
localhost
1 %s
ut_tv.tv_usec
%s: launchd fd array is empty\n
asl_store_open_write: %s\n
    * key val            equality search for messages (single key/value pair)\n
  %s
[Profile\t
CrashMover active: suspending crashlog queue and closing files\n
_asl_dir_create: expected a directory at path %s\n
%s: couldn't open %s: %s\n
Commands\n
                         val must be \"file\" or \"mem\"\n
Q %s
%cbasestamp
enabled
emerg
-dup_delay
starting work queue\n
com.apple.system
store_directory
warning
asl_queue_count
    stop                 stop watching for new messages\n
-mps_limit
ASL Memory Queue
all_max=
-remote
/var/log/asl
[Profile 
unset        
v8@?0
_asl_dir_today_open ASL file %s fd %d\n
*
notify_register_file_descriptor failed: %d\n
%s.%s
Work queue re-enabled at 1/2 max.  size %lld  max %lld\n
%s: listen: %s\n
/var/log
_asl_dir_today_open: asprintf error %s\n
shutdown
[Sender syslogd] [Level 4] [PID %u] [Facility syslog] [Message ASL File %s was closed with %d pending messages]
/dev/klog
[Sender syslogd] [Level 3] [PID %u] [Facility syslog] [Message Disabling module %s writes to %s following %u failures (%s)]
notice
com.apple.asl.access_as_root
%d-%02d-%02dT%02d:%02d:%02d%c%u:%02u:%02u
Facility
80
setting up quota notification handler\n
access       
<sequence>
 (local)
Sender
store        
set (plist)  
_act_dst_close: %s FILE %s\n
ShimCount
memory database is %senabled\n
B24@?0r*8^v16
RefProc
db_memory_max
save
[File 
file
_asl_server_match
[Sender syslogd] [Level 2] [PID %u] [Message Received message size %u overflows work queue (size %lld limit %lld) - dropping message] [UID 0] [UID 0] [Facility syslog]
bootlog
claim        
MsgCount
com.apple.system.log.kernel.warning
memory
set (profile)
disable
%d.%02d.%02d %02d:%02d:%02d UTC
    watch                print new messages as they arrive\n
%s: socket: %s\n
%s: launchd lookup of LAUNCH_JOBKEY_SOCKETS failed\n
%cnon-std_dir
 [%d %s]
iphone
mode=
asl.conf
ReadGID
*** kernel exceeded %d log message per second limit  -  remaining messages this second discarded ***
disaster_occurred
register_session: %u   PID %d\n
--- syslogd restarted ---
asl_db_file
%s %d: socket %d reported error\n
ut_tv.tv_sec
-db
%d-%02d-%02dT%02d:%02d:%02d%c%u:%02u
dest=
<utc-basic>
Server queue dropped message.  message size %u  queue size %lld  max %lld\n
cancel_session: %u\n
ut_type
/var/mobile/Library/Logs/CrashReporter
iOS CrashLog Queue
_act_store_dir
bsd
%d
com.apple.asl.statistics
file database is %senabled\n
dir
<local>
no store\n
warn
-2
com.apple.system.log.kernel.notice
mac
asl
_asl_dir_today_open: No directory at path %s\n
database
%d launchd lookup of LAUNCH_JOBKEY_MACHSERVICES failed\n
Size
    gid:
[Sender syslogd] [Level 1] [PID %u] [Facility syslog] [Message FATAL ERROR: mach_msg() send failed with status 0x%08x]
com.apple.asl
%s/%d.%02d.%02d.asl
module: %s%s\n
%s: re-open failed for file: %s (%s)\n
%d%02d%02dT%02d%02d%02dZ
ASLOption
file_max=
/private/var/mobile/Library/Logs/CrashReporter
a
PID
/etc/asl/.noquota
[Sender syslogd] [Level 2] [PID %u] [Facility syslog] [Message *** MESSAGE QUOTAS ENABLED ***]
skip         
forward
CrashMover timeout: resuming crashlog queue\n
close fd %d\n
_act_store_file_setup: fseek failed %d %s\n
ASLSHIM
%s: accept: %s\n
OSActivityID
<%d>%s
%llu
asl_memory_save: %s\n
    stats                database statistics\n
memory store\n
alloc failed (init_modules remote)\n
_asl_dir_storedata_open: storedata write failed %d %s\n
asl_action
    memory [on/off]      enable / disable memory store\n
<utc>
com.apple.asl.access_as_gid
asl_action_control_set_param: no modules loaded\n
%ccompress
symlink
[Sender syslogd] [Level 4] [PID %u] [Facility syslog] [Message ASL Store %s was closed with %d pending messages]
bsd_max_dup_time
    file [on/off]        enable / disable file store\n
unrecognized command\n
size_only
NO ACCESS
_asl_server_cancel_direct_watch
/var/run/syslog.pid
rotate=
ReadUID
lcl
com.apple.system.logger.message
unknown
memory_size
alloc failed (init_modules udp_in)\n
_asl_dir_create: stat error %s\n
close ASL storedata fd %d\n
Host
std
send_to_direct_watchers: send returned %d (errno %d)\n
%s: launchd dict is NULL\n
%d%02d%02dT%02d%02d%02d%c%02u%02u
max_file_size
%llu %llu
%s --- last message repeated %u time%s ---\n
com.apple.system.log.kernel.debug
Notice
BOOT_TIME %lu %u
0x00 0x00 0x00 0x00
alloc failed (init_modules bsd_out)\n
asl_file
asl_store_save: %s\n
info
com.apple.system.log.kernel.critical
```
