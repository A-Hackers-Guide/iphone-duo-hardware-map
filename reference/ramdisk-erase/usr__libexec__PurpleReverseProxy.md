# `/usr/libexec/PurpleReverseProxy`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 111,744 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1888)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, PIE
```

## Linked libraries (4)

- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.security.network.server</key>
	<true/>
</dict>
</plist>
```

## Strings (204)

```
Ending os transaction for %@\n
~RPSocket_lockdown_service
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/ReverseProxyDeviceService/PurpleReverseProxyService.c
v8@?0
csops1(%d): %s\n
CFDictionaryGetValue for ReleaseType failed\n
RPSocketRead
copyEntitlementsForPid
bad magic 0x%08x\n
isRestoreOS
RPSocketWrite
fromSock->_targetQueue == toSock->_targetQueue
com.apple.PurpleReverseProxy.RPSocket
%s%s%s%s%s
SetDefaultLogLevel
isRestoreOSSystemVersion
failed to write length to %@\n
listen(port=%d)
ExchangeDataHelper
]
:
proxy running\n
com.apple.PurpleReverseProxy
getpeername for %@
invoke
No client callback, missing event %d for socket %p
%s%.*s%s
fd fd=%d
got a %s connection for %@\n
RegisterNotify
w
invalid message from %@, expecting '%s'\n
wrong kCFStreamEventOpenCompleted from %@\n
Closed %@ after reading %lld bytes and writing %lld bytes\n
notify socket checkin failed\n
launch_activate_socket: no sockets for %s\n
client dictionary doesn't contain a command\n
Mismatched ctrl proto version (expected %d, got %d); this may or may not work\n
startProxy_block_invoke_2
ctrl socket read
unknown event type %lu\n
RPSocket %p (ref: %p): got signal with event %d and current _cb: %p
unpause_block_invoke
sending a client notification that the proxy %s online\n
Command
RPSocket_fd
%@: listening on %s
RPSocket
startProxy_block_invoke
ConnProtoVersion
Host didn't specify ctrl proto version\n
failed to read length from %@\n
failed to write %zu bytes to %@\n
Beginning data exchange:   %@  <==>  %@\n
unix:
~RPSocket
com.apple.PurpleReverseProxy.Conn
SetLogLevel
CtrlConn
no dictionary to send to %@\n
RPSocket.cpp
lockdown_send
<RPSocket %p %p: %@>
Identifier
ctrl socket eof\n
: 
Debug
getsockopt
ReleaseType
mobile
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/RPSocket.cpp
plist from %@ was not a dictionary\n
com.apple.PurpleReverseProxy.Ctrl
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/Logging.c
Reset stats for %@ after reading %lld bytes and writing %lld bytes\n
Releasing RPSocket_fd: %p
NotifyConn
HelloConn
is
is not
%s:%d(%s): 
Warning
kern.bootargs
rd=md0
RPSocketRead from %@
unknown command from client\n
got a ctrl connection from a host so we can now accept socks connections\n
RPSocketCopyEntitlements failed\n
RPCreateSocketAcceptingWithAddress
getsockname for %@
no conn listener\n
Client-%@
BeginCtrl
%s[%d] <%s>: 
Critical
!has_synced_to_queue_hint(oldTargetQ, _queue)
startProxy_block_invoke_5
acceptConnection
lockdown_recv
set_client
reset_stats
pthread_cond_timedwait from %@: %s\n
no current ctrl connection exists from the host so we can't accept socks connections right now\n
ConnPort
unexpected data on ctrl socket\n
Reading %lu bytes from socket %p to buffer %p
bind(port=%d)
launch_activate_socket: %s\n
HelloCtrl
com.apple.private.PurpleReverseProxy.allowed
set default log level to %d (%s)\n
socket(%d, SOCK_STREAM)
v16@?0Q8
Host-%@
sendANotification
com.apple.PurpleReverseProxy.transaction
RPSocketReadBuffer failed from %@\n
kCFStreamEventEndEncountered from %@\n
Releasing RPSocket_lockdown_service: %p
OBqqs000I0SR+EbJ7VO8UQ
%b %d %H:%M:%S 
ClientListenerDelay
Asking MobileGestalt for ReleaseType, isRestoreOS: %d\n
read error on %@
RPSocketReceiveExpectedMessage
failed to serialize dictionary to %@: %@\n
accept
CtrlProtoVersion
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/Utilities.c
kqueue
kevent
RPSocketReadDictionary
data too big for %@: %lu\n
RPSocketExchangeData:   %p  <==>  %p\n
RPSocket %p: setting client. old: %p. new: %p
<RPSocket %p %p: %@ %@>
RPSocketReadBuffer
/usr/lib/liblockdown.dylib
RPSocketWrite failed to %@
com.apple.PurpleReverseProxy.FDQueue
~RPSocket_fd
--ramdisk
get_launchd_socket
acceptConnection failed\n
no value for key %@
Calling sysctlbyname for kern.bootargs failed: %d\n
CFDataCreateMutable failed for len %d for %@\n
Creating RPSocket_fd: %p for fd: %d and mode: %d
socks
client dictionary has invalid level\n
lockdown_disconnect
could not allocate socket\n
Creating RPSocket: %p (_sockRef: %p)
lockdown_service service=%s
Info
createCommandDictionaryWithArgs
RPSocketWriteDictionary
ctrl
no ctrl listener\n
com.apple.PurpleReverseProxy.ProxyOnline
%08x%08x%08x
Notice
CFCopySystemVersionDictionary failed\n
Restore
Asking for kMGQReleaseType failed: %d\n
set_target_queue
lockdown fd=%d
socks socket checkin failed\n
startProxy_block_invoke_4
<LogCtxRef: %p>
/dev/console
Emergency
Alert
copyEntitlementsForSocketPeer
<unknown>
FinalizeRPSocket
[
%@: with unknown mode with address: %s
%@: accepted %s <- %s
csops2(%d): %s\n
RPSocketExchangeData
lockdown_checkin_xpc
setsockopt for %@
Releasing RPSocket: %p (_sockRef: %p)
main
%s
v24@?0^{_lockdown_connection=}8^{__CFDictionary=}16
RPSocketCreateAccepted failed\n
Host is using deprecated ReverseProxy protocol; allowing for now\n
client not entitled to use proxy\n
LogCtx
Error
Did not find rd=md0 in bootargs, assuming not RestoreOS\n
failed to deserialize dictionary from %@: %@\n
EOF from %@\n
accept for %@
Level
startProxy_block_invoke_3
failed to convert string\n
Checking SystemVersion failed: %d\n
EOF on %@\n
notify
WaitSocket
lockdown_get_socket
```
