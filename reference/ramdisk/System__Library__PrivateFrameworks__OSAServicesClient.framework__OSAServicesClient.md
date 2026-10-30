# `/System/Library/PrivateFrameworks/OSAServicesClient.framework/OSAServicesClient`

From the upgrade restore ramdisk (141-29011-104.dmg). 158,880 bytes.

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
-[OSAServicesClient queryKey:]
com.apple.osanalytics.OTATaskingAgent
v16@?0@\"NSString\"8
baadbaadbaaadbaaaadbaadbaadbaaadbaaaad01
failed
com.apple.osanalytics.diagnosticmonitor
bugType
OSALogEvent details could not be deserialized: %@
CFStringCompare(question, kMGQInverseDeviceID, 0) == kCFCompareEqualTo
v8@?0
com.apple.osanalytics.diagnosticsmonitor
identity
v12@?0B8
AnalyticsReporterKey
com.apple.osanalytics.diagnosticmonitor.calloutqueue
com.apple.osanalytics.diagnosticsmonitorclient
com.apple.OTATaskingAgent
OSAServicesClient.m
com.apple.osanalytics.services_client.crk
succeeded
OSALogEvent missing details serialization
path
OSALogWriteResult: path and error both null
<no_entitlement>
B32@?0@\"EventObserver\"8Q16^B24
B32@?0@\"WriteObserver\"8Q16^B24
%@ (%@)
incidentID
OSALogWriteResult missing log identity
DiagnosticMonitor
details
com.apple.osanalytics
B32@?0@\"ObserverShim\"8Q16^B24
baadbaadbaaadbaaaadbaadbaadbaaadbaaaad03
OSALogEvent missing identity
InverseDeviceID
baadbaadbaaadbaaaadbaadbaadbaaadbaaaad02
v16@?0@\"NSError\"8
OSALogIdentity missing incidentID
OSALogIdentity missing bugType
error
Querying crashreporterKey/awdKey now requires the entitlement - com.apple.osanalytics.otatasking-service-access. Please add that to your process.
Client: with %ld event observers, observed event types = %@
Client: tearing down server connection after removing last observer.
Log event details could not be serialized: %@
Error while retrieving crashreporterKey. Does this process have the entitlement - com.apple.osanalytics.otatasking-service-access ?
Unknown user '%@', skipping request
Error registering event types with the diagnostic monitor server: %@
Client: reconnecting to server after connection interruption.
Error while retrieving awdKey. Does this process have the entitlement - com.apple.osanalytics.otatasking-service-access ?
Received log event %{public}@ of type %{public}@
Will write log %{public}@ of type %{public}@
Did write log %{public}@ of type %{public}@ (result: %{public}@)
Client: creating server connection.
Modifying defaults as root is not allowed, skipping request
Client: with %ld write observers, observed write types = %@
Error registering write types with the diagnostic monitor server: %@
Connection error to OTATaskingAgent. Error: %@
NSSecureCoding
NSCoding
OSALogWriteResult
OSADiagnosticEventObserver
OSADiagnosticWriteObserver
OSALogIdentity
ObserverShim
OSADiagnosticMonitorClient
EventObserver
OSADiagnosticMonitor
OSADiagnosticMonitorClientProtocol
OSALogEvent
WriteObserver
NSObject
OTAAgentServices
OSAServicesClient
OSADiagnosticMonitorServerProtocol
willWriteLog:
TB,R
_observedEventTypes
didReceiveDiagnosticLog:ofType:details:
identity
matches:
q_addWriteObserver:forTypes:
remoteObjectProxyWithErrorHandler:
willWriteDiagnosticLog:logId:logInfo:
addObject:
addWriteObserver:forTypes:
awdKey
q_registerForWriteTypes
removeWriteObserver:
removeObserver:
debugDescription
initWithCoder:
q_computeWriteObserverTypes
T@\"NSString\",R,N,V_bugType
_observer
deliverWillWrite:on:
init
performSelector:withObject:withObject:
setExportedObject:
q_serverConnection
zone
performSelector:withObject:
T@\"NSString\",R,N,V_incidentID
_bugType
failedToWriteDiagnosticLog:ofType:error:
initWithIdentity:error:
q_removeEventObserver:andComputeObservedTypes:
_calloutQueue
_observers
deliverEvent:on:
initWithObserver:bugTypes:
respondsToSelector:
setRemoteObjectInterface:
setWithObjects:
T#,R
deletePreferenceForDomain:preference:UID:withReply:
isKindOfClass:
removeEventObserver:
self
setPreference:forUser:inDomain:toValue:
set
UTF8String
setClasses:forSelector:argumentIndex:ofReply:
T@\"NSString\",R,N,V_filePath
T@\"OSALogIdentity\",R,N,V_identity
awdKeyWithReply:
hash
T@\"NSError\",R,N,V_error
T@\"OSADiagnosticMonitorClient\",R,N
_observedWriteTypes
_queue
addObserver:forTypes:
encodeObject:forKey:
filePath
_eventObservers
_filePath
_identity
didWriteLog:
setPreferenceForDomain:preference:value:UID:withReply:
T@\"<OSADiagnosticWriteObserver>\",R,W,N,V_observer
class
initWithObserver:
objectAtIndexedSubscript:
q_computeEventObserverTypes
receivedLogEvent:
containsObject:
release
error
removeObjectAtIndex:
stringWithFormat:
_serverConnection
initWithIdentity:details:
resume
isProxy
isEqualToString:
q_removeWriteObserver:andComputeObservedTypes:
crashreporterKeyWithReply:
setWithArray:
synchronousRemoteObjectProxyWithErrorHandler:
T@\"<OSADiagnosticObserver>\",R,W,N,V_observer
_setQueue:
didWriteDiagnosticLog:logId:logFilePath:logInfo:error:
interfaceWithProtocol:
sharedMonitor
superclass
unionSet:
count
incidentID
indexOfObjectPassingTest:
T@\"<OSADiagnosticEventObserver>\",R,W,N,V_observer
_bugTypes
_error
initWithMachServiceName:options:
observer
raise:format:
sharedClient
supportsSecureCoding
isEqual:
bugType
details
_incidentID
_synchRemoteObjectProxy
autorelease
conformsToProtocol:
deletePreference:forUser:inDomain:
T@\"NSSet\",R,N,V_bugTypes
crashreporterKey
description
propertyListWithData:options:format:error:
q_addEventObserver:forTypes:
q_teardownServerConnectionIfNoMoreObservers
retainCount
uidForUser:
T@\"NSDictionary\",R,N,V_details
TQ,R
array
bugTypes
deliverDidWrite:on:
encodeWithCoder:
initWithIncidentID:bugType:
q_shimWrappingObserver:creatingIfAbsent:removingIfPresent:
.cxx_destruct
_writeObservers
didWriteDiagnosticLog:ofType:toPath:
invalidate
setExportedInterface:
setInterruptionHandler:
willWriteDiagnosticLog:ofType:
queryKey:
registerForEvents:replyHandler:
_connection
countByEnumeratingWithState:objects:count:
dataWithPropertyList:format:options:error:
isMemberOfClass:
performSelector:
q_registerForEventTypes
retain
dealloc
T@\"NSString\",?,R,C
_details
addEventObserver:forTypes:
initWithIdentity:filePath:
T@\"OSADiagnosticMonitor\",R,N
localizedDescription
removeAllObjects
registerForWrites:replyHandler:
T@\"NSString\",R,C
decodeObjectOfClass:forKey:
v32@0:8@\"NSString\"16@\"NSString\"24
v24@0:8@?16
@\"NSMutableArray\"
@\"NSXPCConnection\"
@24@0:8@\"NSCoder\"16
@\"OSALogIdentity\"
@\"NSDictionary\"
@\"NSObject<OS_dispatch_queue>\"
@24@0:8:16
B24@0:8@\"Protocol\"16
@32@0:8@16B24B28
v52@0:8@\"NSString\"16@\"NSString\"24@32I40@?<v@?B>44
B48@0:8@16@24@32^v40
B40@0:8@16@24@32
@16@0:8
@\"NSMutableSet\"
#16@0:8
@40@0:8:16@24@32
B24@0:8#16
B24@0:8:16
@\"NSString\"
v40@0:8@16@24@32
v32@0:8@16@24
Vv16@0:8
v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24
v24@0:8@\"NSCoder\"16
@\"NSError\"
v40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32
@\"<OSADiagnosticObserver>\"
v52@0:8@16@24@32I40@?44
v16@0:8
v24@0:8@16
v28@0:8@16B24
B16@0:8
^{_NSZone=}16@0:8
v24@0:8@\"OSALogEvent\"16
@24@0:8@16
v40@0:8@\"NSString\"16@\"NSString\"24@\"NSError\"32
@32@0:8@16@24
B24@0:8@16
@\"<OSADiagnosticEventObserver>\"
@\"NSSet\"
v32@0:8@16@?24
v44@0:8@16@24I32@?36
v44@0:8@\"NSString\"16@\"NSString\"24I32@?<v@?B>36
v24@0:8@?<v@?@\"NSString\">16
@\"<OSADiagnosticWriteObserver>\"
@32@0:8:16@24
v24@0:8@\"OSALogWriteResult\"16
@24@0:8^{__CFString=}16
I24@0:8@16
@\"<OTAAgentServices>\"
Q16@0:8
@\"NSString\"16@0:8
v24@0:8@\"OSALogIdentity\"16
v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32
```
