# `/usr/lib/libReverseProxyDevice.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 138,096 bytes.

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
unix:
Emergency
Alert
csops2(%d): %s\n
%@ reachable? %s\n
RPSocketWrite
ClientListenerDelay
copyEntitlementsForSocketPeer
isRestoreOSSystemVersion
RPSocketReadBuffer
%@ (%p): connected to %s as %s
Level
false
kqueue
isRestoreOS
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/ReverseProxyDevice/ReverseProxyDevice.c
RPSocketWriteDictionary failed\n
[
RPSocket
%b %d %H:%M:%S 
Unexpected ping response\n
Creating RPSocket_fd: %p for fd: %d and mode: %d
com.apple.PurpleReverseProxy.FDQueue
failed to convert string\n
Restore
mobile
unexpected event %lu\n
socket(port=%d)
SetLogLevel
_RPRegistrationCallback
com.apple.PurpleReverseProxy.RPSocket
/dev/console
kern.bootargs
RPSocketReadDictionary failed\n
failed to serialize dictionary to %@: %@\n
could not allocate socket\n
RegisterNotify
v16@?0Q8
attampting sendProxyControlMessage\n
RPSocketWrite failed\n
~RPSocket
Notice
WaitSocket
Asking for kMGQReleaseType failed: %d\n
Reading %lu bytes from socket %p to buffer %p
%s%.*s%s
Critical
copyEntitlementsForPid
fd fd=%d
%s:%d(%s): 
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/Utilities.c
%@ is reachable, assuming we don't need a proxy dictionary\n
SCNetworkReachabilityGetFlags
127.0.0.1
%s%s%s%s%s
RPSocketReadDictionary
failed to write length to %@\n
getpeername for %@
Releasing RPSocket_fd: %p
: 
v8@?0
sendPingMessage
Closed %@ after reading %lld bytes and writing %lld bytes\n
true
Returning 'socks://127.0.0.1:%d/' for '%@'\n
EOF on %@\n
%@: accepted %s <- %s
no value for key %@
TestReachability
Failed to ping host proxy service, returning NULL proxy dictionary\n
~RPSocket_fd
bad magic 0x%08x\n
SCNetworkReachabilitySetCallback
connect(port=%d)
Ending os transaction for %@\n
set default log level to %d (%s)\n
Checking SystemVersion failed: %d\n
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/RPSocket.cpp
failed to deserialize dictionary from %@: %@\n
createCommandDictionaryWithArgs
RPCreateSocketForHost
No client callback, missing event %d for socket %p
Calling sysctlbyname for kern.bootargs failed: %d\n
_RPCopyProxyDictionaryWithOptions
w
ReleaseType
<RPSocket %p %p: %@>
Releasing RPSocket: %p (_sockRef: %p)
failed to read length from %@\n
plist from %@ was not a dictionary\n
Error
CFDictionaryGetValue for ReleaseType failed\n
RPSocketReadBuffer failed from %@\n
data too big for %@: %lu\n
getsockname for %@
SetDefaultLogLevel
rd=md0
copyProxyDictionaryForURL
sendProxyControlMessage
accept
Command
kevent
SCNetworkReachabilityCreateWithName
no dictionary to send to %@\n
<unknown>
/Library/Caches/com.apple.xbs/EA8234CA-D33D-4E08-9B40-2A08F0CF3F76/TemporaryDirectory.Z0jxkF/Sources/PurpleReverseProxy/Common/Logging.c
Warning
Info
csops1(%d): %s\n
SCNetworkReachabilitySetDispatchQueue
Ping
read error on %@
%s[%d] <%s>: 
Debug
CFCopySystemVersionDictionary failed\n
Did not find rd=md0 in bootargs, assuming not RestoreOS\n
com.apple.PurpleReverseProxy
www.apple.com
RPSocketRead
accept for %@
reachableDictQueue
CFDataCreateMutable failed for len %d for %@\n
FinalizeRPSocket
<RPSocket %p %p: %@ %@>
invoke
RPSocket %p (ref: %p): got signal with event %d and current _cb: %p
:
failed to write %zu bytes to %@\n
set_client
%s
Asking MobileGestalt for ReleaseType, isRestoreOS: %d\n
reachabilityCB
RPSocketWriteDictionary
RPSocket %p: setting client. old: %p. new: %p
]
<LogCtxRef: %p>
getsockopt
/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
setsockopt for %@
LogCtx
Pong
RPSocket_fd
Creating RPSocket: %p (_sockRef: %p)
sendProxyControlMessage failed\n
```
