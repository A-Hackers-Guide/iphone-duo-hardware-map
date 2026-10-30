# `/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 321,040 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 32 (Size: 5072)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (15)

- `/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/Combine.framework/Combine (compatibility version 1.0.0, current version 3023.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices (compatibility version 1.0.0, current version 1226.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftOSLog.dylib (compatibility version 1.0.0, current version 10.0.0, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (7 classes, 3 protocols)

Classes: `DriverApprovalState`, `DriverManager`, `ProxyDriverManagerObserver`, `_SwiftDriverApprovalState`, `_SwiftDriverManager`, `_TtC16DriverManagement21DriverKitDaemonClient`, `_TtC16DriverManagement26ApprovalStateUpdateRequest`

Protocols: `_SwiftDriverManagerObserver`, `_TtP16DriverManagement29DriverKitDaemonClientProtocol_`, `_TtP16DriverManagement32DriverKitDaemonAppClientProtocol_`

## Strings (173)

```
_TtC16DriverManagement26ApprovalStateUpdateRequest
_SwiftDriverManager
_SwiftDriverApprovalState
DriverApprovalState
ProxyDriverManagerObserver
DriverManager
_TtP16DriverManagement29DriverKitDaemonClientProtocol_
_TtC16DriverManagement21DriverKitDaemonClient
_SwiftDriverManagerObserver
_TtP16DriverManagement32DriverKitDaemonAppClientProtocol_
driverApprovalStatesForCurrentAppWithError:
getApprovalStateForCallingAppWithReplyBlock:
objectAtIndex:
$__lazy_storage_$_appConnection
.cxx_destruct
driver
setInvalidationHandler:
addObject:
nextObject
remoteObjectInterface
_approvalState
_swiftManager
array
countByEnumeratingWithState:objects:count:
initWithMachServiceName:options:
launchServicesQueue
thirdPartyDriverCount
refresh
client
enumeratorWithOptions:
unlock
$__lazy_storage_$_connection
initWithObserver:
installSessionIdentifier
observers
remoteObjectProxyWithErrorHandler:
URL
initWithSwiftManager:
dumpStateWithReplyBlock:
getApprovalStateForSettingsWithReplyBlock:
timestamp
description
driverIsApproved
sharedManager
updatePending
approvalStateDidChange:
driverApprovalStatesForThirdPartyApp:
entry
uniqueInstallIdentifier
_updateStatus
arrayWithCapacity:
canAccess
count
driverApprovalStatesLock
usageText
_observer
bundleRecordForCurrentProcess
displayName
enqueueApprovalStateUpdateWithEntry:replyBlock:
lock
dealloc
removeObserver:
_swiftDriverApprovalState
callback
setInterruptionHandler:
setRemoteObjectInterface:
T@\"NSString\",N,R
_observers
driverCountForAppID:
interfaceWithProtocol:
localizedName
removeObjectAtIndex:
resume
setDriverState:approved:
_driverApprovalStates
addObserver:
initWithDomain:code:userInfo:
initWithSwiftDriverApprovalState:
launchDriverWithBundleID:userServerName:tag:replyBlock:
observerLock
sharedDatabaseContext
synchronousRemoteObjectProxyWithErrorHandler:
driverCount
driverExtensionPaths
init
$__lazy_storage_$_clientIdentifier
bundleIdentifier
v24@0:8@?<v@?@\"NSString\"@\"NSError\">16
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
v24@?0@\"NSString\"8@\"NSError\"16
v8@?0
@16@0:8
v16@0:8
q16@0:8
q24@0:8@16
v28@0:8@16B24
@\"_SwiftDriverManager\"
v24@0:8@?16
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\"@\"NSError\">40
@24@0:8@16
v24@0:8@16
@\"NSMutableArray\"
v48@0:8@16@24@32@?40
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
v20@0:8B16
v16@?0@\"<OS_xpc_object>\"8
@\"_SwiftDriverApprovalState\"
v32@0:8@16@?24
v16@?0@\"NSError\"8
v24@?0@\"NSData\"8@\"NSError\"16
B16@0:8
@\"<DriverManagerObserver>\"
@24@0:8^@16
Failed to get scoped approval state
addObserver(_:)
Found two applications with the same install session identifier: %{public}s: %{public}s
Connection to service %{public}s invalidated
Update in progress
Updating approval state of %{public}s to %{public}s
Unexpected non-third-party entry on scoped app path: %{public}s
Connection to service %{public}s interrupted
DriverManagement.DriverApprovalState
removeObserver(_:)
, install session identifier 
App with install session identifier 
Received state update notification
refresh()
fetchApprovalStatesForCurrentAppSync()
Failed to get approval states for current app: %{public}s
com.apple.driverkitd.DriverApprovalsChanged
Request enqueued at 
driverCount()
driverApprovalStatesForCurrentApp(withError:)
Failed to get all of the application records because the current process doesn't have the access to the LS database.
Third Party, in app 
No update in progress
Could not find application for driver %{public}s
Remote object proxy error: %{public}s
Fatal error
com.apple.driverkitd.DriverKitDaemonClient-
Successfully refreshed approval state
Failed to construct the current process' application record because the install session ID is not valid.
DriverManagement/DriverKitDaemonClient.swift
thirdPartyDriverCount()
driverIdentifier
\nApproval State: 
ApprovalSettingsState: 
initiateApprovalStatesRefresh()
State was updated, sending notification to %d observer%{public}s
Failed to get approval state: %{public}s
setDriverState(driverApprovalState:state:)
XPC Event %{public}s: Failed to create reply for event
Could not find: 
Failed to enqueue driver state update for %{public}s: %{public}s
init()
(no bundle identifier)
getAllApplicationRecords()
updateApprovalStates(from:with:)
appInstallSessionIdentifier
Received approvals change notification after deinit
Unable to create remote object interface.
Failed to set driver approval state for %{public}s to %{public}s. Refreshing state.
Failed to construct the current process' application record because the record of the current process itself is missing.
com.apple.DriverKitAppServer
Invalid number of keys found, expected one.
driverCount(forAppID:)
sharedManager()
com.apple.driverkitd.DriverKitSettings.LaunchServices
com.apple.DriverKitExtensionServer
Invalid argument: 
Uninstalled app, install session identifier 
Driver Identifier: 
%s
```
