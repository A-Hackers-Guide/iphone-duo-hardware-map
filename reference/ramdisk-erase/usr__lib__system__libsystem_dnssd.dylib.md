# `/usr/lib/system/libsystem_dnssd.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 114,480 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 32 (Size: 2600)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (14)

- `/usr/lib/system/libsystem_dnssd.dylib (compatibility version 1.0.0, current version 3111.40.45)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.2)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libsystem_asl.dylib (compatibility version 1.0.0, current version 409.40.3)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`
- `/usr/lib/system/libsystem_featureflags.dylib (compatibility version 1.0.0, current version 111.0.0)`
- `/usr/lib/system/libsystem_networkextension.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`

## Entitlements

```xml
  - no entitlements
```

## Strings (133)

```
NoMemory
NATPortMappingDisabled
dnssd_clientstub DNSServiceRefSockFD called with invalid DNSServiceRef %p %08X %08X
dnssd_clientstub DNSServiceUpdateRecord called with NULL parameter
%u
dnssd_clientstub DNSServiceSleepKeepalive cannot create connection
Refused
NoSuchRecord
NoSuchKey
dnssd_clientstub DNSServiceRefSockFD undefined for kDNSServiceFlagsShareConnection subordinate DNSServiceRef %p
dnssd_clientstub DNSServiceProcessResult daemon version %u does not match client version %d
dnssd_clientstub DNSServiceRemoveRecord called with invalid DNSServiceRef %p %08X %08X
v8@?0
dnssd_clientstub read_all(%d) failed %ld/%ld %d %s
DNSServiceSendQueuedRequestsInternal ERROR: writev(fd:%d, written:%zd, total:%zd bytes) failed, errno[%d]:%s
dnssd_clientstub ConnectToServer: Failed to get the file descriptor flags of socket %d %s
dnssd_clientstub ConnectToServer: SO_DEFUNCTOK failed %d %s
dnssd_clientstub DNSServiceSleepKeepalive could not fit name
PolicyDenied
DNSSD_UDS_PATH
dnssd_clientstub ConnectToServer: connect() failed path:%s Socket:%d Err:%d Errno:%d %s
socketpair
dnssd_clientstub DNSServiceSleepKeepalive remote6 info failed %d
BadParam
BadState
BadFlags
Incompatible
NoRouter
require_privacy
dnssd_clientstub DNSServiceProcessResult error: select indicated data was waiting but read_all returned EWOULDBLOCK
dnssd_clientstub read_all(%d) DEFUNCT
_udp
dnssd_clientstub deliver_request ERROR: sendmsg failed read sd=%d write sd=%d errno %d (%s)
dnssd_clientstub handle_regservice_response: error reading result from daemon
dnssd_clientstub DNSServiceUpdateRecord called with invalid DNSServiceRef %p %08X %08X
dnssd_clientstub DNSServiceSleepKeepalive local info failed %d
dnssd_clientstub DNSServiceSleepKeepalive could not fit unique
dnssd_clientstub:sdRef: CallbackwithError morebytes zero sdr %p
dnssd_clientstub handle_addrinfo_response: error reading result from daemon
BadInterfaceIndex
dnssd_clientstub DNSServiceCreateDelegateConnection: Could not setsockopt() for PID[%d], no entitlements or process(pid) invalid errno:%d (%s)
dnssd_clientstub:Record: CallbackwithError morebytes zero
dnssd_clientstub handle_port_mapping_response: error reading result from daemon
NATTraversal
ServiceNotRunning
NotPermitted
dnssd_clientstub CallbackWithError called with bad op %u
BadKey
PollingMode
dnssd_clientstub DNSServiceSetDispatchQueue dispatch source set already
dnssd_clientstub read_all: SO_ISDEFUNCT failed %d %s
dnssd_clientstub kDNSServiceFlagsShareConnection used with NULL DNSServiceRef
dnssd_clientstub kDNSServiceFlagsShareConnection used with invalid DNSServiceRef %p %08X %08X op %u
dnssd_clientstub ConnectToServer: socket failed %d %s
DaemonVersion
dnssd_clientstub write_all(%d) failed %ld/%ld %d %s
dnssd_clientstub deliver_request: invalid DNSServiceRef %p %08X %08X
Transient
dnssd_clientstub: DNSServiceSetDispatchQueue dispatch queue NULL
dnssd_clientstub handle_browse_response: error reading result from daemon
dnssd_clientstub DNSServiceRefDeallocate called with NULL DNSServiceRef
dnssd_clientstub DNSServiceAddRecord called with non-DNSServiceRegister DNSServiceRef %p %u
dnssd_clientstub DNSServiceRemoveRecord called with invalid DNSRecordRef %p %08X %08X
dnssd_clientstub ConnectionResponse: Record not found
NoError
Unsupported
BadTime
DefunctConnection
dnssd_clientstub DNSServiceProcessResult undefined for kDNSServiceFlagsShareConnection subordinate DNSServiceRef %p
DNSServiceSendQueuedRequestsInternal: !sdr
DNSServiceSendQueuedRequestsInternal: numMsg is 0
dnssd_clientstub DNSServiceAddRecord called with NULL parameter
NoAuth
NATPortMappingUnsupported
<INVALID ERROR CODE>
dnssd_clientstub DNSServiceProcessResult called with DNSServiceRef with no ProcessReply function
dnssd_clientstub DNSServiceSleepKeepalive: getpeername %d\n
dnssd_clientstub write_all: SO_ISDEFUNCT failed %d %s
dnssd_clientstub deliver_request ERROR: write_all(%d, %lu bytes) failed
dnssd_clientstub set_waitlimit:_daemon timed out (%d secs) without any response: Socket %d
Timeout
dnssd_clientstub DNSServiceCreateDelegateConnection: Could not setsockopt() for UUID, no entitlements or process(uuid) invalid errno:%d (%s) 
BadReference
_tcp
dnssd_clientstub DNSServiceProcessResult called with NULL DNSServiceRef
dnssd_clientstub DNSServiceProcessResult called with invalid DNSServiceRef %p %08X %08X
dnssd_clientstub DNSServiceSleepKeepalive remote info failed %d
dnssd_clientstub DNSServiceSleepKeepalive local6 info failed %d
_keepalive._dns-sd._udp.local
dnssd_clientstub SleepKeepaliveCallback context mismatch
dnssd_clientstub DNSServiceRefDeallocate called with invalid DNSServiceRef %p %08X %08X
dnssd_clientstub DNSServiceAddRecord called with invalid DNSServiceRef %p %08X %08X
t=%u h=%s d=%s l=%u r=%u
NotInitialized
dnssd_clientstub DNSServiceRegisterRecord called with NULL parameter
dnssd_clientstub DNSServiceRegisterRecord called with invalid DNSServiceRef %p %08X %08X
dnssd_clientstub DNSServiceRemoveRecord called with bad DNSServiceRef
dnssd_clientstub DNSServiceSetDispatchQueue dispatch_source_create failed
dnssd_clientstub DNSServiceSleepKeepalive local/remote info not same
dnssd_clientstub handle_resolve_response: error reading result from daemon
AlreadyRegistered
resolver_config_plist_data
dnssd_clientstub ConnectionResponse: Record sdr mismatch: rec %p sdr %p
DoubleNAT
dnssd_clientstub DNSServiceRemoveRecord called with NULL DNSRecordRef
dnssd_clientstub DNSService operation with NULL DNSServiceRef
/var/run/mDNSResponder
Unknown
NoSuchName
Firewall
dnssd_clientstub DNSServiceSetDispatchQueue dispatch queue set already
dnssd_clientstub ConnectionResponse: sdr->op != connection_request
t=%u H=%s D=%s l=%u r=%u
dnssd_clientstub read_all: EINTR continue
dnssd_clientstub deliver_request: %s failed %d (%s)
dnssd_clientstub handle_query_response: error reading result from daemon
dnssd_clientstub handle_enumeration_response: error reading result from daemon
dnssd_clientstub DNSServiceRegisterRecord called with non-DNSServiceCreateConnection DNSServiceRef %p %u
dnssd_clientstub ConnectToServer: Failed to set FD_CLOEXEC on socket %d %s
%s.%s
Invalid
dnssd_clientstub attempt to dispose invalid DNSServiceRef %p %08X %08X
NameConflict
dnssd_clientstub ConnectToServer: using default path since env len is invalid
dnssd_clientstub DNSServiceSleepKeepalive could not fit local/remote info
BadSig
dnssd_clientstub DNSServiceRefSockFD called with NULL DNSServiceRef
dnssd_clientstub DNSServiceRemoveRecord called with NULL DNSServiceRef
dnssd_clientstub ConnectToServer: SO_NOSIGPIPE failed %d %s
dnssd_clientstub deliver_request: SO_DEFUNCTOK failed %d %s
DNSServiceSendQueuedRequestsInternal: writev(fd:%d, numMsg:%u, %zd bytes) succeed
dnssd_clientstub DNSServiceSleepKeepalive: getsockname %d\n
dnssd_clientstub write_all(%d) DEFUNCT
```
