# `/usr/lib/system/libsystem_configuration.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 114,560 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 29 (Size: 2464)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (11)

- `/usr/lib/system/libsystem_configuration.dylib (compatibility version 1.0.0, current version 1453.40.1)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libsystem_asl.dylib (compatibility version 1.0.0, current version 409.40.3)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_notify.dylib (compatibility version 1.0.0, current version 368.40.2)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_trace.dylib (compatibility version 1.0.0, current version 1966.40.15)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3, upward)`

## Entitlements

```xml
  - no entitlements
```

## Strings (44)

```
com.apple.SystemConfiguration.DNSConfiguration
v16@?0^v8
ProxyAgent
OutOfBandDataUUID
com.apple.system.SystemConfiguration.dns_configuration
nwi notify_check: failed with %u\n
DNS configuration
configuration
Attempting to free invalid resolver
DNSAgent(m)
B24@?0Q8^v16
generation
com.apple.SystemConfiguration.NetworkInformation
Cannot parse config agent (%s). No data available
Network information
  reply
SearchDomains
AgentType
nwi_state: registration failed (%u)\n
DNSAgent
NameServers
DNSAgent(p)
proc_name
request_op
com.apple.system.SystemConfiguration.nwi
AgentUUID
v8@?0
AgentData
  dict = 
Attempting to free proxy configuration
SystemConfig
*** DNS configuration requested between fork() and exec()
DNS configuration: size error (%zu != %zu)
%s: server failed
%s: connection error: %d : %s
%s server failure, retrying
%s server not available
%s xpc_connection_send_message_with_reply_sync() with unexpected reply
DNS configuration: padding error (%u > %zu)
*** network information requested between fork() and exec()
%s: unexpected message
%s: server not available
%s: unknown event type : %p
%s = %s
```
