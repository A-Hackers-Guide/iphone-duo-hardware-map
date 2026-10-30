# `/System/Library/PrivateFrameworks/AlwaysOnExclavesDaemon.framework/AlwaysOnExclavesDaemon`

iOS 27.2 dyld shared cache image. Version `66.40.15.0.0`. **[DSC]**

## Linked libraries (17)

- `/System/Library/PrivateFrameworks/TrustedClockingServices.framework/TrustedClockingServices`
- `/System/Library/PrivateFrameworks/AlwaysOnExclavesServices.framework/AlwaysOnExclavesServices`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags`
- `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftOSLog.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 6 classes, 2 protocols, 20 methods, 4 properties

### Class pages

Every class and protocol, with its methods: [`NSObject`](../objc/NSObject_AlwaysOnExclavesDaemon.protocol.md), [`OS_xpc_object`](../objc/OS_xpc_object_AlwaysOnExclavesDaemon.protocol.md), [`_TtC22AlwaysOnExclavesDaemon13EnableTracker`](../objc/_TtC22AlwaysOnExclavesDaemon13EnableTracker_AlwaysOnExclavesDaemon.md), [`_TtC22AlwaysOnExclavesDaemon16WorkerThreadPool`](../objc/_TtC22AlwaysOnExclavesDaemon16WorkerThreadPool_AlwaysOnExclavesDaemon.md), [`_TtC22AlwaysOnExclavesDaemon18AlwaysOnXPCService`](../objc/_TtC22AlwaysOnExclavesDaemon18AlwaysOnXPCService_AlwaysOnExclavesDaemon.md), [`_TtC22AlwaysOnExclavesDaemon24CrossConclaveIpcReceiver`](../objc/_TtC22AlwaysOnExclavesDaemon24CrossConclaveIpcReceiver_AlwaysOnExclavesDaemon.md), [`_TtC22AlwaysOnExclavesDaemon25AlwaysOnExclavesForwarder`](../objc/_TtC22AlwaysOnExclavesDaemon25AlwaysOnExclavesForwarder_AlwaysOnExclavesDaemon.md), [`_TtC22AlwaysOnExclavesDaemon6Daemon`](../objc/_TtC22AlwaysOnExclavesDaemon6Daemon_AlwaysOnExclavesDaemon.md)

### Classes

`_TtC22AlwaysOnExclavesDaemon13EnableTracker`, `_TtC22AlwaysOnExclavesDaemon16WorkerThreadPool`, `_TtC22AlwaysOnExclavesDaemon18AlwaysOnXPCService`, `_TtC22AlwaysOnExclavesDaemon24CrossConclaveIpcReceiver`, `_TtC22AlwaysOnExclavesDaemon25AlwaysOnExclavesForwarder`, `_TtC22AlwaysOnExclavesDaemon6Daemon`

### Protocols

`NSObject`, `OS_xpc_object`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Swift types (13)

`AlwaysOnExclavesDaemon.AlwaysOnExclaves`, `AlwaysOnExclavesDaemon.AlwaysOnExclavesForwarder`, `AlwaysOnExclavesDaemon.AlwaysOnExclavesForwarder.ForwardConnectionInfo`, `AlwaysOnExclavesDaemon.AlwaysOnXPCService`, `AlwaysOnExclavesDaemon.CrossConclaveIpcReceiver`, `AlwaysOnExclavesDaemon.CrossConclaveIpcReceiverError`, `AlwaysOnExclavesDaemon.CrossConclaveIpcReceiverOptions`, `AlwaysOnExclavesDaemon.Daemon`, `AlwaysOnExclavesDaemon.EnableTracker`, `AlwaysOnExclavesDaemon.WorkerThreadPool`, `AlwaysOnExclavesDaemon.WorkerThreadPoolError`, `__C.exclaves_aoe_service_info`, `conformance`

## Strings (78)

```
(error: %d): failed to launch conclave
conclave for %s is not present, daemon.launch() skipped
%s: no conclave present, cannot setup IPC receiver
[XPCService] the daemon does not have a conclave
[XPCService] %s requested overdisablement of %s
[XPCService] %s successfully requested enablement of %s
starting %s
[Forwarder] Forwarding connection setup for serviceName: %s, serviceId: %llu
%s: xpcService: new boot detected, old bootuuid was %s, resetting to clean defaults
%s: xpcService: the existing defaults for current boot: %@
Task Conclave Name: %s
%s is feature-flag disabled, refusing to start conclave
Started %ld message and %ld worker threads
%s: created dedicated workgroup '%s_c2cc'
[xpcService] No more requesters, exiting
[XPCService] AlwaysOnXPCService initialized
inited %s
[warn] daemon %s has no conclave
[Forwarder] Service lookup failed for service %s with kr = %d
[XPCService] %s requested overenablement of %s
[XPCService] the daemon is not enabled
%s: xpcService: bootuuid is %s
%s created %d IPC receiver threads
[XPCService] %s successfully requested disablement of %s
[XPCService] Sender does not have the required entitlement
started %s
Failed to initialize TrustedClockingServices
(error %d): exclaves_aoe_enumerate_and_setup_services failed
(error %d): exclaves_aoe_enumerate_and_setup_services succeeded but returned zero services
[XPCService] AlwaysOnExclaves is not available, please enable the alwaysonexclavesd feature flag
Foundation/arm64e-apple-ios.private.swiftinterface
): failed to mark thread as detached
): failed to enable CrossConclaveIpcReceiver
exclaves_aoe_message_loop unexpectedly returned
): failed pthread_setname_np for CrossConclaveIpcReceiver thread
error
, could not launch daemon
 has previously enabled AOE but enable count is zero
com.apple.alwaysonexclavesd
): failed to create thread attribute
): failed to set thread QoS
): failed to create workgroup for 
serviceName
from
enable
sendPort
kern.task_conclave
_worker_thread_for_service_
): failed pthread_setname_np for worker thread
exclaves_aoe_work_loop unexpectedly returned
lifecycle
exclaves_c2cc_recv_loop unexpectedly returned
Fatal error
success
input of String.init(cString:encoding:) must be null-terminated
): failed pthread_setname_np for message thread
): exclaves_aoe_get_all_service_infos failed
[xpcService] xpc_dictionary_create_reply failed
[XPCService] error: 
kern.bootsessionuuid
: xpcService: sysctl kern.bootsessionuuid failed, size 
: xpcService: failed to parse bootuuid
AlwaysOnExclavesDaemon/daemon.swift
: failed to parse conclave name
): failed to set thread attribute
): failed to set thread stacksize
alwaysonexclavesd
AlwaysOnExclavesDaemon/workerThreadPool.swift
error: invalid EndpointSchedulingCategory 
AlwaysOnExclavesDaemon/crossConclaveIpcReceiver.swift
AlwaysOnExclavesDaemon/xpcService.swift
hasConclave
com.apple.private.exclaves.conclave-host
_aoe_enabled_by__
, could not launch conclave for 
): failed to create pthread
_message_thread_for_service_
): failed to set workgroup attributes for 
```
