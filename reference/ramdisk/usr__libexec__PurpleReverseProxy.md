# `/usr/libexec/PurpleReverseProxy`

From the upgrade restore ramdisk (141-29011-104.dmg). 111,744 bytes.

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
setsockopt for %@
no conn listener\n
bad magic 0x%08x\n
lockdown_send
!has_synced_to_queue_hint(oldTargetQ, _queue)
getpeername for %@
%s%s%s%s%s
accept for %@
got a %s connection for %@\n
socks
Debug
Command
kevent
set default log level to %d (%s)\n
lockdown_disconnect
lockdown_get_socket
RPSocket
<RPSocket %p %p: %@ %@>
~RPSocket
ClientListenerDelay
RPSocketRead
failed to write length to %@\n
RPSocket_fd
lockdown_service service=%s
notify
startProxy_block_invoke
client dictionary doesn't contain a command\n
<LogCtxRef: %p>
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/Utilities.c
getsockopt
RPSocket %p: setting client. old: %p. new: %p
set_target_queue
kCFStreamEventEndEncountered from %@\n
pthread_cond_timedwait from %@: %s\n
OBqqs000I0SR+EbJ7VO8UQ
/dev/console
RPSocketExchangeData:   %p  <==>  %p\n
Closed %@ after reading %lld bytes and writing %lld bytes\n
unpause_block_invoke
launch_activate_socket: no sockets for %s\n
RegisterNotify
Client-%@
Warning
lockdown_checkin_xpc
getsockname for %@
socks socket checkin failed\n
com.apple.PurpleReverseProxy.Ctrl
SetLogLevel
Level
no current ctrl connection exists from the host so we can't accept socks connections right now\n
main
got a ctrl connection from a host so we can now accept socks connections\n
acceptConnection
is
bind(port=%d)
accept
Releasing RPSocket_fd: %p
no ctrl listener\n
v16@?0Q8
ConnPort
Alert
Error
Asking for kMGQReleaseType failed: %d\n
com.apple.PurpleReverseProxy.FDQueue
com.apple.PurpleReverseProxy.RPSocket
startProxy_block_invoke_4
CtrlConn
unexpected data on ctrl socket\n
RPSocketRead from %@
Restore
com.apple.PurpleReverseProxy.transaction
createCommandDictionaryWithArgs
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/ReverseProxyDeviceService/PurpleReverseProxyService.c
unknown event type %lu\n
%s[%d] <%s>: 
failed to write %zu bytes to %@\n
lockdown_recv
Releasing RPSocket_lockdown_service: %p
startProxy_block_invoke_2
client not entitled to use proxy\n
w
Info
%@: listening on %s
client dictionary has invalid level\n
Host-%@
<unknown>
:
: 
Emergency
ReleaseType
com.apple.PurpleReverseProxy
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/RPSocket.cpp
Creating RPSocket_fd: %p for fd: %d and mode: %d
proxy running\n
Host didn't specify ctrl proto version\n
Did not find rd=md0 in bootargs, assuming not RestoreOS\n
Reading %lu bytes from socket %p to buffer %p
/usr/lib/liblockdown.dylib
Creating RPSocket: %p (_sockRef: %p)
<RPSocket %p %p: %@>
startProxy_block_invoke_5
com.apple.private.PurpleReverseProxy.allowed
RPSocketReadBuffer
failed to deserialize dictionary from %@: %@\n
%s
Notice
Asking MobileGestalt for ReleaseType, isRestoreOS: %d\n
Ending os transaction for %@\n
Releasing RPSocket: %p (_sockRef: %p)
v24@?0^{_lockdown_connection=}8^{__CFDictionary=}16
acceptConnection failed\n
startProxy_block_invoke_3
EOF on %@\n
failed to convert string\n
%s:%d(%s): 
Critical
RPSocketReceiveExpectedMessage
CFDataCreateMutable failed for len %d for %@\n
RPSocketExchangeData
reset_stats
CFCopySystemVersionDictionary failed\n
no dictionary to send to %@\n
fromSock->_targetQueue == toSock->_targetQueue
RPSocketWrite failed to %@
]
~RPSocket_lockdown_service
com.apple.PurpleReverseProxy.Conn
launch_activate_socket: %s\n
kern.bootargs
unknown command from client\n
Identifier
com.apple.PurpleReverseProxy.ProxyOnline
is not
SetDefaultLogLevel
invalid message from %@, expecting '%s'\n
RPSocketWriteDictionary
%@: accepted %s <- %s
%s%.*s%s
ctrl
NotifyConn
CtrlProtoVersion
no value for key %@
listen(port=%d)
EOF from %@\n
No client callback, missing event %d for socket %p
fd fd=%d
get_launchd_socket
sendANotification
WaitSocket
failed to read length from %@\n
wrong kCFStreamEventOpenCompleted from %@\n
notify socket checkin failed\n
RPSocketCopyEntitlements failed\n
isRestoreOS
rd=md0
mobile
RPSocketReadDictionary
[
lockdown fd=%d
ctrl socket eof\n
sending a client notification that the proxy %s online\n
%b %d %H:%M:%S 
Reset stats for %@ after reading %lld bytes and writing %lld bytes\n
invoke
--ramdisk
BeginCtrl
Host is using deprecated ReverseProxy protocol; allowing for now\n
data too big for %@: %lu\n
RPSocket.cpp
Beginning data exchange:   %@  <==>  %@\n
set_client
could not allocate socket\n
csops1(%d): %s\n
CFDictionaryGetValue for ReleaseType failed\n
copyEntitlementsForPid
LogCtx
kqueue
csops2(%d): %s\n
copyEntitlementsForSocketPeer
plist from %@ was not a dictionary\n
socket(%d, SOCK_STREAM)
ExchangeDataHelper
%@: with unknown mode with address: %s
read error on %@
RPCreateSocketAcceptingWithAddress
FinalizeRPSocket
unix:
~RPSocket_fd
ConnProtoVersion
ctrl socket read
Calling sysctlbyname for kern.bootargs failed: %d\n
RPSocketWrite
RPSocketReadBuffer failed from %@\n
failed to serialize dictionary to %@: %@\n
RPSocketCreateAccepted failed\n
%08x%08x%08x
v8@?0
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/Logging.c
RPSocket %p (ref: %p): got signal with event %d and current _cb: %p
HelloConn
Mismatched ctrl proto version (expected %d, got %d); this may or may not work\n
HelloCtrl
isRestoreOSSystemVersion
Checking SystemVersion failed: %d\n
```
