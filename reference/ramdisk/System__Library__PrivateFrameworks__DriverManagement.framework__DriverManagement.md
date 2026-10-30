# `/System/Library/PrivateFrameworks/DriverManagement.framework/DriverManagement`

From the upgrade restore ramdisk (141-29011-104.dmg). 321,040 bytes.

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
com.apple.driverkitd.DriverKitSettings.LaunchServices
initiateApprovalStatesRefresh()
getAllApplicationRecords()
, install session identifier 
State was updated, sending notification to %d observer%{public}s
Could not find application for driver %{public}s
No update in progress
Received state update notification
Connection to service %{public}s invalidated
Driver Identifier: 
Failed to get all of the application records because the current process doesn't have the access to the LS database.
Remote object proxy error: %{public}s
driverCount(forAppID:)
com.apple.driverkitd.DriverApprovalsChanged
Found two applications with the same install session identifier: %{public}s: %{public}s
Unexpected non-third-party entry on scoped app path: %{public}s
DriverManagement/DriverKitDaemonClient.swift
com.apple.driverkitd.DriverKitDaemonClient-
Failed to get scoped approval state
Request enqueued at 
Invalid number of keys found, expected one.
refresh()
setDriverState(driverApprovalState:state:)
Invalid argument: 
sharedManager()
addObserver(_:)
thirdPartyDriverCount()
Fatal error
driverApprovalStatesForCurrentApp(withError:)
Successfully refreshed approval state
Third Party, in app 
appInstallSessionIdentifier
driverCount()
XPC Event %{public}s: Failed to create reply for event
fetchApprovalStatesForCurrentAppSync()
Failed to get approval states for current app: %{public}s
\nApproval State: 
driverIdentifier
Failed to get approval state: %{public}s
Failed to construct the current process' application record because the install session ID is not valid.
Connection to service %{public}s interrupted
Could not find: 
removeObserver(_:)
Failed to enqueue driver state update for %{public}s: %{public}s
Received approvals change notification after deinit
Failed to set driver approval state for %{public}s to %{public}s. Refreshing state.
ApprovalSettingsState: 
com.apple.DriverKitExtensionServer
Unable to create remote object interface.
Uninstalled app, install session identifier 
init()
updateApprovalStates(from:with:)
Updating approval state of %{public}s to %{public}s
Failed to construct the current process' application record because the record of the current process itself is missing.
com.apple.DriverKitAppServer
Update in progress
App with install session identifier 
DriverManagement.DriverApprovalState
(no bundle identifier)
%s
_SwiftDriverManagerObserver
_TtP16DriverManagement32DriverKitDaemonAppClientProtocol_
_TtC16DriverManagement26ApprovalStateUpdateRequest
DriverApprovalState
ProxyDriverManagerObserver
_TtP16DriverManagement29DriverKitDaemonClientProtocol_
_SwiftDriverManager
_TtC16DriverManagement21DriverKitDaemonClient
_SwiftDriverApprovalState
DriverManager
driver
driverExtensionPaths
driverIsApproved
getApprovalStateForSettingsWithReplyBlock:
initWithSwiftManager:
thirdPartyDriverCount
_driverApprovalStates
uniqueInstallIdentifier
bundleRecordForCurrentProcess
dealloc
addObject:
addObserver:
setInterruptionHandler:
setRemoteObjectInterface:
$__lazy_storage_$_appConnection
_swiftManager
description
setDriverState:approved:
_approvalState
driverApprovalStatesForCurrentAppWithError:
URL
enqueueApprovalStateUpdateWithEntry:replyBlock:
init
count
interfaceWithProtocol:
canAccess
launchDriverWithBundleID:userServerName:tag:replyBlock:
remoteObjectInterface
T@\"NSString\",N,R
.cxx_destruct
entry
initWithDomain:code:userInfo:
timestamp
$__lazy_storage_$_connection
_observers
bundleIdentifier
countByEnumeratingWithState:objects:count:
driverApprovalStatesForThirdPartyApp:
initWithSwiftDriverApprovalState:
localizedName
nextObject
arrayWithCapacity:
_swiftDriverApprovalState
refresh
_observer
approvalStateDidChange:
displayName
driverApprovalStatesLock
driverCountForAppID:
array
client
enumeratorWithOptions:
lock
objectAtIndex:
observers
remoteObjectProxyWithErrorHandler:
removeObjectAtIndex:
$__lazy_storage_$_clientIdentifier
getApprovalStateForCallingAppWithReplyBlock:
setInvalidationHandler:
sharedManager
synchronousRemoteObjectProxyWithErrorHandler:
unlock
updatePending
callback
initWithObserver:
launchServicesQueue
observerLock
resume
sharedDatabaseContext
usageText
removeObserver:
driverCount
dumpStateWithReplyBlock:
initWithMachServiceName:options:
installSessionIdentifier
_updateStatus
@\"_SwiftDriverApprovalState\"
@\"<DriverManagerObserver>\"
v24@0:8@16
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
v16@?0@\"<OS_xpc_object>\"8
v24@?0@\"NSData\"8@\"NSError\"16
v24@?0@\"NSString\"8@\"NSError\"16
q16@0:8
@\"_SwiftDriverManager\"
@\"NSMutableArray\"
v8@?0
v16@0:8
@24@0:8^@16
v24@0:8@?<v@?@\"NSString\"@\"NSError\">16
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\"@\"NSError\">40
v20@0:8B16
v16@?0@\"NSError\"8
@24@0:8@16
B16@0:8
q24@0:8@16
v28@0:8@16B24
v24@0:8@?16
v48@0:8@16@24@32@?40
v32@0:8@16@?24
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
@16@0:8
```
