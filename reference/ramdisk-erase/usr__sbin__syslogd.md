# `/usr/sbin/syslogd`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 183,456 bytes.

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
mach_port_allocate dead_session_port failed: %d
/var/run/syslog.pid
Size
<utc>
ASL Action Queue
%u
starting mach service\n
file_max=
_asl_dir_today_open: No directory at path %s\n
cancel/close ASL storedata fd %d\n
com.apple.system.hostname
remote_delay_time
    format: %s\n
asl
com.apple.system
_asl_dir_storedata_open ASL storedata %s fd %d\n
setting up quota notification handler\n
com.apple.system.log.kernel.error
remote
%u%s
  %s
                                 C=casefold  N=numeric  S=substring  A=prefix  Z=suffix\n
NetworkListener
*** kernel exceeded %d log message per second limit  -  remaining messages this second discarded ***
[Sender syslogd] [Level 4] [PID %u] [Facility syslog] [Message ASL Store %s was closed with %d pending messages]
ASL Server Queue
  data: NULL
ttl
com.apple.system.notify.service.path:0x87:
%s: error sending message (%s): %s\n
TimeNanoSec
com.apple.asl.access_as_gid
_act_store_dir_setup: storedata write failed %d %s\n
_asl_dir_today_open: fseek %s error %s\n
%s: init\n
FATAL ERROR: mach_msg() send failed with status 0x%08x\n
    raw                  use raw format for printing messages\n
asl_db_file
[base=%s].%s.[ext=%s]\n
CrashMover timeout: resuming crashlog queue\n
%s %d: error on socket %d\n
%s: fcntl: %s\n
2
broadcast    
iOS CrashLog Queue
_act_store_dir asl_file_save FAILED %s\n
_asl_dir_create: asl_out_mkpath failed: %s\n
user
_asl_server_query_2
-dup_delay
/var/mobile/Library/Logs/CrashReporter
_act_dst_close: %s ASL FILE %s\n
BSD Out Queue
_asl_server_match
sweep_lockdown_session_fds: realloc failed\n
asl_store_open_write: %s\n
_asl_dir_storedata_open: stat error %s\n
asl_action
_asl_server_cancel_direct_watch
%s %d: select %d %s\n
asl_dir      
    dbsize [val]         get [set] database size (# of records)\n
 %s
basestamp
_act_file
a
db_memory_str_max
starting work queue\n
%casl_file
set (file)   
_asl_dir_storedata_open: chown %d %d new %s: %s\n
__asl_server_register_direct_watch: pid %u port %hu\n
db_file_max
%lld
crashlog
r+
 ; 
com.apple.system.logger.message
                         modifiers (must follow operator):\n
s
ShimCount
    quit                 exit session\n
broadcast
notice
register_session: %u   PID %d\n
[Plist 
    file [on/off]        enable / disable file store\n
alloc failed (init_modules bsd_out)\n
/etc/asl.conf
dest=
ReadGID
asl_queue_count
bootlog
-klog_in
unset        
_act_store_dir
ASLSHIM
com.apple.system.log.kernel.emergency
memory_size
bsd_out
com.apple.system.lastlog
asl_memory_open: %s\n
send_to_direct_watchers: lockdown %d write error: %d %s\n
StringCount
MaxStringMemory
%d%02d%02dT%02d%02d%02d%c%02u%02u
GID
com.apple.system.utmpx
%s %d: read error on socket %d: %d %s\n
%f
save
gid=
extern
mem
compress
datastore
skip
Work queue disabled.  msize %lld  size %lld  max %lld\n
%llu %llu
ERROR: mach_msg() send failed with MACH_SEND_NO_BUFFER 0x%08x\n
/var/run/lockdown/syslog.sock
ut_type
*
NO ACCESS
    * op key val         search for matching messages (single key/value pair)\n
%s: setsockopt: %s\n
%s: launchd dict is NULL\n
[base=%s].%s\n
%s/%d.%02d.%02d.asl
dispatch_source DISPATCH_VNODE_DELETE fd %d\n
%s: unsupported / unknown output name: %s\n
com.apple.system.log.kernel.warning
%s: couldn't open %s: %s\n
mach_port_allocate listen_set failed: %d
com.apple.system.config.network_change
%cexternal
    ttl: %s\n
BOOT_TIME %lu %u
syslog
Unknown
not watching!\n
%s/module/%s/%s
CHECKPOINT RENAME %s %s\n
/dev/console
remote_delay
client_count
initializing modules\n
    all_max: %lu\n
_asl_file_open ASL file %s fd %d\n
mark_time
com.apple.system.log.kernel.debug
error: can't stat data store %s: %s\n
enter \"help\" for help\n
Facility
com.apple.asl.statistics
no store\n
setting up network change notification handler\n
MaxRecords
none         
sec
-mps_limit
com.apple.system.syslog.master
%casl_directory
UID
SenderMachUUID
_act_dst_close: %s FILE %s\n
CrashMover finished\n
 \t
                         val must be \"file\" or \"mem\"\n
-utmp_ttl
[File\t
 (local)
   M %u %u %lu
bsd_max_dup_time
    select [val]         get [set] current database\n
    std                  use standard format for printing messages\n
%d-%02d-%02dT%02d:%02d:%02d%c%u
/private/var/mobile/Library/Logs/CrashReporter
Work queue re-enabled at 1/2 max.  size %lld  max %lld\n
1 %s
Q %s
cancel/close file fd %d\n
close ASL storedata fd %d\n
*%s
/dev/klog
alloc failed (init_modules)\n
_act_store_dir_setup: _act_dst_open %s failed\n
StoreData
= reset
{XPC_TYPE_ARRAY}
%d-%02d-%02dT%02d:%02d:%02d%c%u:%02u:%02u
access       
notify_register_plain(%s) failed status %u\n
not 
/etc/asl
/var/log/asl
kern
crit
com.apple.system.log.kernel.alert
/etc/asl/.noquota
%d%02d%02dT%02d%02d%02d%c%02u
    flags: 0x%08x
dir
= crash
mach_port_move_member server_port failed: %d
%cnon-std_dir
/Library/Logs/
-2
 
file database is not enabled\n
000
store_dir
unset
idle
W %d %llu
remove_lockdown_session: realloc failed\n
ut_id
/etc/syslog.conf
dbtype
unknown
_asl_dir_today_open: localtime_r error %s\n
[Sender syslogd] [Level 5] [PID %u] [Message Configuration Notice:\nASL Module \"%s\" claims selected messages.\nThose messages may not appear in standard system log files or in the ASL database.] [UID 0] [GID 0] [Facility syslog]
only
action
%d%02d%02dT%02d%02d%02dZ
$ENV(
soft
debug
ERROR: mach_msg() send failed with MACH_SEND_INVALID_HEADER 0x%08x\n
Work Queue
-remote
RecordCount
%ccompress
<utc-basic>
<%d>%s
__asl_server_cancel_direct_watch: %hu\n
w
 %d
forward
com.apple.asl
close ASL fd %d\n
    flush                flush database\n
%d launchd lookup of SERVICE_NAME failed\n
size_only
w+
_act_dst_close: %s ASL DIR %s\n
none
ASLFreeNotify
Time
Session
MsgCount
/
err
CrashMover active: suspending crashlog queue and closing files\n
define
_asl_dir_today_open: asl_file_open_write %s error %s\n
close fd %d\n
[Sender syslogd] [Level 3] [PID %u] [Facility syslog] [Message mach_msg() send failed with status 0x%08x (MACH_SEND_NO_BUFFER)]
{XPC_TYPE_???}
; \t
udp_in
set
[Profile\t
uid=
asl_file     
store
module: %s%s\n
[Sender syslogd] [Level 6] [PID %u] [Message -- MARK --] [UID 0] [UID 0] [Facility syslog]
disaster_occurred
                         operators:  =  <  >  ! (not equal)  T (key exists)  R (regex)\n
ASLOption
style=
_asl_dir_create: stat error %s\n
_act_store_file_setup: asl_file_read_set_position failed %d %s\n
utmp_ttl
Direct Watch Queue
cancel_session: %u\n
ASL Memory Queue
 [%d %s]
notify
%s: fd %d recvfrom %s len %d\n
fmt=
%s%s
Work queue draining: dropped message.\n
ASLExpireTime
%csoft
[base=%s].[ext=%s].%s\n
store        
[Sender syslogd] [Level 4] [PID %u] [Facility syslog] [Message File %s was closed with %d pending messages]
_act_store_file_setup: fseek failed %d %s\n
1
%s.%s
%s/%s.%s.%s
asl_dir
/var/log/syslogd.log
%d 
Commands\n
DB size %u\n
%ccoalesce
0
\n%s syslogd PID %d starting\n
%s: couldn't set O_NONBLOCK for file descriptor %d: %s\n
claim
/Library/Logs/CrashReporter
%s: %s save to %s failed: %s\n
%s --- last message repeated %u time%s ---\n
daemon
alloc failed (init_modules asl_action)\n
    rules: %u\n
        rotatation style: 
%s: open failed for file: %s (%s)\n
%s: --- last message repeated %u time%s ---\n
symlink
db
    * key val            equality search for messages (single key/value pair)\n
add_lockdown_session: realloc failed\n
_act_store_dir_setup: storedata read failed %d %s\n
<unknown>
watchers_active
    memory [on/off]      enable / disable memory store\n
%cbasestamp
output       
disabled
ReadUID
send_to_direct_watchers: exceeded EAGAIN limit - closing connection\n
unknown database type\n
%s: listen: %s\n
appletv
%ccrashlog
Sender
%s: launchd lookup of UDP_SOCKET_NAME failed\n
%d%02d%02dT%02d%02d%02d%c%02u%02u%02u
false
NULL
error: %s is not a directory
    stats                database statistics\n
_asl_dir_storedata_open: fopen new %s: %s\n
__asl_server_message: %s\n
Goodbye\n
%c%llu
%s: malloc: %s\n
access
skip         
RefProc
-config
alloc failed (init_modules udp_in)\n
%csymlink
store_directory
truncate
%s/%s.asl
std
alloc failed (init_modules remote)\n
%d-%02d-%02dT%02d:%02d:%02d%c%u:%02u
    dest: %s\n
    time_format: %s\n
mobile
%s: error writing repeat message (%s): %s\n
com.apple.system.log.kernel.info
_act_dst_open:_asl_dir_today_open %s FAILED!\n
bsd
,.
mach_port_move_member dead_session_port failed (%u)
SIGHUP reset\n
%s\n
%csize_only
checkpoint
-udp_in
v8@?0
%s: bind: %s\n
Host
[Sender syslogd] [Level 1] [PID %u] [Facility syslog] [Message FATAL ERROR: mach_msg() send failed with status 0x%08x]
    *                    show all log messages\n
off
{XPC_TYPE_FD}
[Sender syslogd] [Level 2] [PID %u] [Message Internal memory size limit %lld exceeded - dropping messages] [UID 0] [UID 0] [Facility syslog]
%s: couldn't set O_NONBLOCK for fd %d (%s): %s\n
    watch                print new messages as they arrive\n
%s %d: terminating session for %ssocket %d\n
%s: socket: %s\n
<sequence>
%s: error writing message (%s): %s\n
com.apple.syslogd.message
work_queue_count
iphone
_asl_dir_today_open: asprintf error %s\n
_asl_dir_today_open ASL file %s fd %d\n
notify_register_file_descriptor failed: %d\n
%s: launchd fd array is empty\n
[File 
deleted
Level
asl_action_control_set_param: memory allocation failed\n
file
-1
Server queue dropped message.  message size %u  queue size %lld  max %lld\n
ut_pid
%d-%02d-%02dT%02d:%02d:%02dZ
    stop                 stop watching for new messages\n
enable
klog_in
%s %d: socket %d reported error\n
already watching!\n
Q [%s]
%s: launchd lookup of LAUNCH_JOBKEY_SOCKETS failed\n
__asl_server_create_aux_link: %s\n
memory store\n
{XPC_TYPE_SHMEM}
(none)
cancel/close ASL file fd %d\n
_asl_file_open: asl_file_open_write %s failed %d %s\n
mps_limit
%d
alert
%d launchd checkin failed\n
OSActivityID
_asl_dir_storedata_open: fopen existing %s: %s\n
_asl_file_open: _act_file_create_open %s failed %d %s\n
memory_max
FATAL ERROR: mach_msg() receive failed with status 0x%08x\n
file store\n
B24@?0r*8^v16
set (profile)
_asl_server_create_aux_link
lockdown 
0x%08x\n
asl_directory
asl.conf
dup_delay
_asl_server_message
MachServices
<local>
%s: re-open failed for file: %s (%s)\n
hostname
kernel
[Sender syslogd] [Level 3] [PID %u] [Facility syslog] [Message mach_msg() send failed with status 0x%08x (MACH_SEND_INVALID_HEADER)]
db_memory_max
ut_tv.tv_usec
_act_store_dir_setup: aslfile fseek failed %d %s\n
com.apple.system.log.kernel.notice
-db
-bsd_out
%s: launchd file discriptor array element 0 is NULL\n
directory
[Profile 
ut_tv.tv_sec
reading launch plist\n
dst=
rotate=
_asl_file_open: asl_out_mkpath %s failed\n
memory database is not enabled\n
v12@?0i8
CheckIn
set          
[Sender syslogd] [Level 1] [PID %u] [Facility syslog] [Message FATAL ERROR: mach_msg() receive failed with status 0x%08x]
unrecognized command\n
info
_asl_dir_create: expected a directory at path %s\n
ASLModule
[Sender syslogd] [Level 2] [PID %u] [Message Received message size %u overflows work queue (size %lld limit %lld) - dropping message] [UID 0] [UID 0] [Facility syslog]
com.apple.asl.access_as_root
com.apple.system.logger
control      
warning
(retry) asl_store_save: %s\n
[Sender syslogd] [Level 5] [PID %u] [Message Configuration Notice:\nASL Module \"%s\" sharing output destination \"%s\" with ASL Module \"%s\".\nOutput parameters from ASL Module \"%s\" override any specified in ASL Module \"%s\".] [UID 0] 
%d.%02d.%02d %02d:%02d:%02d UTC
%d\n
{XPC_TYPE_ERROR}
ignore       
ASLFinalNotification
asl_action_control_set_param: no modules loaded\n
_asl_dir_storedata_open: storedata write failed %d %s\n
_asl_dir_storedata_close %p\n
%s %d: %d/%d write data failed: %d %s\n
%s: error re-writing message (%s): %s\n
/usr/local/etc/asl
set (plist)  
[Sender syslogd] [Level 4] [PID %u] [Facility syslog] [Message ASL File %s was closed with %d pending messages]
control
asl_memory_save: %s\n
memory database is %senabled\n
mac
StringMemory
_asl_dir_storedata_open: No directory at path %s\n
(retry) asl_memory_save: %s\n
    mode: 0%o\n
error
%d launchd lookup of LAUNCH_JOBKEY_MACHSERVICES failed\n
com.apple.crash_mover
rotate
%s %d: starting interactive session for %ssocket %d\n
/var/run/lockdown
-launchd_in
Sockets
ignore
enabled
%s/%s
Message
bsd_queue_count
%cenabled
msg
<seconds>
%s
\n========================\nASL is here to serve you\n
claim        
disable
lcl
%s: connection failed for %s\n
    * [op key val] ...   search for matching messages (multiple key/value pairs)\n
mode=
link
RefPID
asl_store_save: %s\n
[Sender syslogd] [Level 2] [PID %u] [Facility syslog] [Message *** MESSAGE QUOTAS DISABLED FOR ALL PROCESSES ***]
    uid:
<local-basic>
all_max=
_act_dst_open:_asl_dir_storedata_open %s FAILED!  Closing today file\n
raw
asl_file
coalesce=
PID
ASL Sender Statistics
alloc failed (init_modules klog_in)\n
    gid:
/var/log/
syslogd
lockdown_session_count
r
localhost
error: can't create data store %s: %s\n
file database is %senabled\n
[Plist\t
shutdown
emerg
_asl_server_register_direct_watch
com.apple.asl.access_as_uid
--- syslogd restarted ---
%s: couldn't set receive buffer size for file descriptor %d: %s\n
notify       
file         
%s: couldn't set O_NONBLOCK for fd %d: %s\n
max_file_size
80
com.apple.system.log.kernel.critical
%s: accept: %s\n
_act_store_file
0x00 0x00 0x00 0x00
%s: getaddrinfo failed for node %s service %s: (%s)\n
warn
asl_input_parse: %s\n
memory
Q [= %s]
    file_max: %lu\n
/var/log
forward      
database
%llu
asl_db_memory
Notice
[Sender syslogd] [Level 2] [PID %u] [Facility syslog] [Message *** MESSAGE QUOTAS ENABLED ***]
ASLMessageID
%crotate
format=
[Sender syslogd] [Level 3] [PID %u] [Facility syslog] [Message Disabling module %s writes to %s following %u failures (%s)]
panic
send_to_direct_watchers: send returned %d (errno %d)\n
stats_interval
%lu
{XPC_TYPE_DICTIONARY}
```
