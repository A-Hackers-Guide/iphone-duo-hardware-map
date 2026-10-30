# `/usr/lib/libReverseProxyDevice.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 138,096 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 2448)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libReverseProxyDevice.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (144)

```
RPSocketWrite
Releasing RPSocket_fd: %p
No client callback, missing event %d for socket %p
sendPingMessage
RPSocket %p (ref: %p): got signal with event %d and current _cb: %p
accept
Notice
no value for key %@
invoke
getsockopt
Did not find rd=md0 in bootargs, assuming not RestoreOS\n
Ping
LogCtx
kevent
ReleaseType
RegisterNotify
v16@?0Q8
/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
plist from %@ was not a dictionary\n
Ending os transaction for %@\n
www.apple.com
false
RPSocketWriteDictionary
setsockopt for %@
<unknown>
Checking SystemVersion failed: %d\n
%b %d %H:%M:%S 
Level
v8@?0
Closed %@ after reading %lld bytes and writing %lld bytes\n
]
Debug
kern.bootargs
copyProxyDictionaryForURL
Pong
RPSocketWriteDictionary failed\n
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/RPSocket.cpp
failed to write length to %@\n
%s:%d(%s): 
isRestoreOSSystemVersion
rd=md0
%@ reachable? %s\n
failed to read length from %@\n
ClientListenerDelay
SetLogLevel
FinalizeRPSocket
: 
RPSocketReadBuffer
:
copyEntitlementsForPid
mobile
sendProxyControlMessage failed\n
CFDictionaryGetValue for ReleaseType failed\n
Asking for kMGQReleaseType failed: %d\n
com.apple.PurpleReverseProxy
RPSocket_fd
Reading %lu bytes from socket %p to buffer %p
CFDataCreateMutable failed for len %d for %@\n
RPSocket %p: setting client. old: %p. new: %p
accept for %@
RPSocketReadDictionary
RPCreateSocketForHost
connect(port=%d)
createCommandDictionaryWithArgs
RPSocketRead
%@ (%p): connected to %s as %s
Creating RPSocket: %p (_sockRef: %p)
SCNetworkReachabilityGetFlags
set_client
getsockname for %@
Releasing RPSocket: %p (_sockRef: %p)
SCNetworkReachabilityCreateWithName
SCNetworkReachabilitySetCallback
data too big for %@: %lu\n
socket(port=%d)
unix:
%s%s%s%s%s
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/Logging.c
/dev/console
copyEntitlementsForSocketPeer
_RPCopyProxyDictionaryWithOptions
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/Utilities.c
TestReachability
true
sendProxyControlMessage
RPSocketReadDictionary failed\n
%@: accepted %s <- %s
%s[%d] <%s>: 
Critical
reachableDictQueue
attampting sendProxyControlMessage\n
Emergency
Unexpected ping response\n
Info
kqueue
%@ is reachable, assuming we don't need a proxy dictionary\n
EOF on %@\n
no dictionary to send to %@\n
failed to serialize dictionary to %@: %@\n
Creating RPSocket_fd: %p for fd: %d and mode: %d
RPSocket
w
reachabilityCB
RPSocketReadBuffer failed from %@\n
failed to write %zu bytes to %@\n
fd fd=%d
failed to convert string\n
<LogCtxRef: %p>
csops2(%d): %s\n
isRestoreOS
_RPRegistrationCallback
com.apple.PurpleReverseProxy.FDQueue
could not allocate socket\n
~RPSocket_fd
Error
Command
com.apple.PurpleReverseProxy.RPSocket
<RPSocket %p %p: %@ %@>
CFCopySystemVersionDictionary failed\n
%s%.*s%s
~RPSocket
csops1(%d): %s\n
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/ReverseProxyDevice/ReverseProxyDevice.c
SCNetworkReachabilitySetDispatchQueue
unexpected event %lu\n
[
Calling sysctlbyname for kern.bootargs failed: %d\n
getpeername for %@
Asking MobileGestalt for ReleaseType, isRestoreOS: %d\n
127.0.0.1
Restore
%s
WaitSocket
bad magic 0x%08x\n
Returning 'socks://127.0.0.1:%d/' for '%@'\n
RPSocketWrite failed\n
<RPSocket %p %p: %@>
SetDefaultLogLevel
set default log level to %d (%s)\n
Alert
Warning
Failed to ping host proxy service, returning NULL proxy dictionary\n
failed to deserialize dictionary from %@: %@\n
read error on %@
```
