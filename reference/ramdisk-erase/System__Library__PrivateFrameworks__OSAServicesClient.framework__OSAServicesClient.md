# `/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 158,880 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 3608)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (9 classes, 8 protocols)

Classes: `EventObserver`, `OSADiagnosticMonitor`, `OSADiagnosticMonitorClient`, `OSALogEvent`, `OSALogIdentity`, `OSALogWriteResult`, `OSAServicesClient`, `ObserverShim`, `WriteObserver`

Protocols: `NSCoding`, `NSObject`, `NSSecureCoding`, `OSADiagnosticEventObserver`, `OSADiagnosticMonitorClientProtocol`, `OSADiagnosticMonitorServerProtocol`, `OSADiagnosticWriteObserver`, `OTAAgentServices`

## Strings (284)

```
Vv16@0:8
v24@0:8@\"OSALogEvent\"16
v24@0:8@\"OSALogWriteResult\"16
@24@0:8@\"NSCoder\"16
v40@0:8@16@24@32
v40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32
@\"<OSADiagnosticObserver>\"
@32@0:8@16@24
v24@0:8@16
@\"NSMutableSet\"
Q16@0:8
v24@0:8@\"NSCoder\"16
v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32
v44@0:8@16@24I32@?36
v24@0:8@?<v@?@\"NSString\">16
B24@0:8@16
v32@0:8@16@24
@16@0:8
v16@0:8
@24@0:8:16
I24@0:8@16
@\"<OSADiagnosticEventObserver>\"
#16@0:8
@\"NSString\"16@0:8
@24@0:8@16
@\"NSError\"
v40@0:8@\"NSString\"16@\"NSString\"24@\"NSError\"32
v52@0:8@16@24@32I40@?44
v52@0:8@\"NSString\"16@\"NSString\"24@32I40@?<v@?B>44
v28@0:8@16B24
@\"NSMutableArray\"
@32@0:8:16@24
@40@0:8:16@24@32
v24@0:8@\"OSALogIdentity\"16
@32@0:8@16B24B28
B48@0:8@16@24@32^v40
@24@0:8^{__CFString=}16
B16@0:8
B24@0:8@\"Protocol\"16
v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24
@\"NSString\"
@\"NSDictionary\"
v32@0:8@\"NSString\"16@\"NSString\"24
@\"<OTAAgentServices>\"
@\"<OSADiagnosticWriteObserver>\"
B24@0:8:16
^{_NSZone=}16@0:8
@\"OSALogIdentity\"
v24@0:8@?16
B40@0:8@16@24@32
@\"NSObject<OS_dispatch_queue>\"
@\"NSXPCConnection\"
B24@0:8#16
v32@0:8@16@?24
v44@0:8@\"NSString\"16@\"NSString\"24I32@?<v@?B>36
@\"NSSet\"
com.apple.osanalytics.services_client.crk
failed
OSALogIdentity missing incidentID
OSALogWriteResult: path and error both null
InverseDeviceID
baadbaadbaaadbaaaadbaadbaadbaaadbaaaad01
baadbaadbaaadbaaaadbaadbaadbaaadbaaaad02
OSALogEvent missing identity
OSALogWriteResult missing log identity
OSAServicesClient.m
<no_entitlement>
v16@?0@\"NSError\"8
path
B32@?0@\"WriteObserver\"8Q16^B24
com.apple.osanalytics.diagnosticmonitor
%@ (%@)
v16@?0@\"NSString\"8
v8@?0
com.apple.osanalytics.diagnosticmonitor.calloutqueue
succeeded
bugType
B32@?0@\"ObserverShim\"8Q16^B24
v12@?0B8
CFStringCompare(question, kMGQInverseDeviceID, 0) == kCFCompareEqualTo
incidentID
OSALogIdentity missing bugType
com.apple.osanalytics.diagnosticsmonitorclient
-[OSAServicesClient queryKey:]
AnalyticsReporterKey
com.apple.osanalytics.OTATaskingAgent
baadbaadbaaadbaaaadbaadbaadbaaadbaaaad03
com.apple.osanalytics.diagnosticsmonitor
details
OSALogEvent details could not be deserialized: %@
error
com.apple.osanalytics
com.apple.OTATaskingAgent
B32@?0@\"EventObserver\"8Q16^B24
identity
OSALogEvent missing details serialization
DiagnosticMonitor
Error while retrieving crashreporterKey. Does this process have the entitlement - com.apple.osanalytics.otatasking-service-access ?
Unknown user '%@', skipping request
Client: with %ld event observers, observed event types = %@
Will write log %{public}@ of type %{public}@
Client: tearing down server connection after removing last observer.
Error while retrieving awdKey. Does this process have the entitlement - com.apple.osanalytics.otatasking-service-access ?
Error registering event types with the diagnostic monitor server: %@
Client: reconnecting to server after connection interruption.
Connection error to OTATaskingAgent. Error: %@
Client: with %ld write observers, observed write types = %@
Error registering write types with the diagnostic monitor server: %@
Received log event %{public}@ of type %{public}@
Did write log %{public}@ of type %{public}@ (result: %{public}@)
Client: creating server connection.
Log event details could not be serialized: %@
Querying crashreporterKey/awdKey now requires the entitlement - com.apple.osanalytics.otatasking-service-access. Please add that to your process.
Modifying defaults as root is not allowed, skipping request
EventObserver
OSADiagnosticMonitor
OSALogWriteResult
OSADiagnosticWriteObserver
WriteObserver
OSADiagnosticMonitorServerProtocol
NSObject
OSADiagnosticMonitorClientProtocol
ObserverShim
OSADiagnosticEventObserver
NSSecureCoding
NSCoding
OSADiagnosticMonitorClient
OSALogIdentity
OSALogEvent
OTAAgentServices
OSAServicesClient
removeEventObserver:
matches:
q_removeEventObserver:andComputeObservedTypes:
setRemoteObjectInterface:
sharedMonitor
objectAtIndexedSubscript:
_writeObservers
set
initWithIdentity:details:
q_computeWriteObserverTypes
containsObject:
_filePath
_synchRemoteObjectProxy
description
error
indexOfObjectPassingTest:
invalidate
retainCount
_eventObservers
T@\"<OSADiagnosticObserver>\",R,W,N,V_observer
dealloc
isProxy
details
_bugTypes
array
deliverEvent:on:
T@\"NSSet\",R,N,V_bugTypes
_calloutQueue
_queue
isEqual:
failedToWriteDiagnosticLog:ofType:error:
isMemberOfClass:
willWriteDiagnosticLog:logId:logInfo:
willWriteLog:
awdKey
deliverWillWrite:on:
observer
removeObjectAtIndex:
setPreferenceForDomain:preference:value:UID:withReply:
supportsSecureCoding
uidForUser:
T@\"NSString\",R,N,V_bugType
T@\"NSString\",R,N,V_incidentID
_connection
_observedEventTypes
autorelease
countByEnumeratingWithState:objects:count:
removeWriteObserver:
willWriteDiagnosticLog:ofType:
addObserver:forTypes:
conformsToProtocol:
interfaceWithProtocol:
isEqualToString:
synchronousRemoteObjectProxyWithErrorHandler:
_observer
crashreporterKey
dataWithPropertyList:format:options:error:
incidentID
encodeObject:forKey:
sharedClient
.cxx_destruct
T@\"<OSADiagnosticEventObserver>\",R,W,N,V_observer
q_computeEventObserverTypes
setExportedObject:
superclass
T#,R
setWithObjects:
q_serverConnection
_incidentID
filePath
hash
q_teardownServerConnectionIfNoMoreObservers
_details
addObject:
addWriteObserver:forTypes:
count
T@\"NSString\",R,N,V_filePath
registerForEvents:replyHandler:
didReceiveDiagnosticLog:ofType:details:
initWithIncidentID:bugType:
q_removeWriteObserver:andComputeObservedTypes:
q_shimWrappingObserver:creatingIfAbsent:removingIfPresent:
setExportedInterface:
TQ,R
bugTypes
removeObserver:
_serverConnection
q_addWriteObserver:forTypes:
T@\"NSString\",?,R,C
T@\"OSADiagnosticMonitorClient\",R,N
_identity
initWithIdentity:error:
localizedDescription
self
q_addEventObserver:forTypes:
setPreference:forUser:inDomain:toValue:
stringWithFormat:
T@\"NSDictionary\",R,N,V_details
addEventObserver:forTypes:
didWriteDiagnosticLog:logId:logFilePath:logInfo:error:
T@\"<OSADiagnosticWriteObserver>\",R,W,N,V_observer
release
_error
_setQueue:
initWithMachServiceName:options:
performSelector:withObject:
propertyListWithData:options:format:error:
setClasses:forSelector:argumentIndex:ofReply:
UTF8String
respondsToSelector:
TB,R
resume
setInterruptionHandler:
T@\"OSADiagnosticMonitor\",R,N
init
initWithIdentity:filePath:
unionSet:
bugType
T@\"NSError\",R,N,V_error
_bugType
deletePreference:forUser:inDomain:
deliverDidWrite:on:
isKindOfClass:
q_registerForEventTypes
initWithCoder:
performSelector:withObject:withObject:
queryKey:
T@\"OSALogIdentity\",R,N,V_identity
debugDescription
deletePreferenceForDomain:preference:UID:withReply:
didWriteDiagnosticLog:ofType:toPath:
encodeWithCoder:
q_registerForWriteTypes
setWithArray:
_observedWriteTypes
_observers
performSelector:
removeAllObjects
class
didWriteLog:
initWithObserver:
initWithObserver:bugTypes:
receivedLogEvent:
remoteObjectProxyWithErrorHandler:
T@\"NSString\",R,C
awdKeyWithReply:
decodeObjectOfClass:forKey:
identity
retain
zone
registerForWrites:replyHandler:
crashreporterKeyWithReply:
raise:format:
```
