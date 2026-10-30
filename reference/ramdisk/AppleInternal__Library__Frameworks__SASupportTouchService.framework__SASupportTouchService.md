# `/AppleInternal/Library/Frameworks/SASupportTouchService.framework/SASupportTouchService`

From the upgrade restore ramdisk (141-29011-104.dmg). 117,856 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 3320)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/AppleInternal/Library/Frameworks/SASupportTouchService.framework/SASupportTouchService (compatibility version 1.0.0, current version 1.0.0)`
- `@rpath/SensingAlgsSupport.framework/SensingAlgsSupport (compatibility version 0.0.0, current version 10100.29.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (7 classes, 0 protocols)

Classes: `SAEventInformation`, `SAPathStats`, `SAPathStatsCollection`, `SATouchServiceDevice`, `SATouchServiceFrame`, `SATouchServiceFrameActive`, `SATouchServiceFrameTTW`

## Strings (383)

```
fingers
ttw-tap
EventInfo
D38
D84
Stationary
contacts
Fingers:\n
Node data is not the expected SADeviceOrientation class
eventInfoArray
\n
Interpolated Event Info -
Hand:\n
ttwTap
CoreAnalyticsStep
D64
handArray
 - deviceReady:
Interpolated Fingers:\n
stats
CoverGestureEvent
AtomicWakeEvent
Active
PrimaryUsage
i
V62
event-infos
coverGestureEvent
D16
TouchServiceTTWPlan
WakeEvent:
EventGenerationStep
V159
data
DeviceReady
WakeEventDetected
ttwResults
NotificationEvent:
TTW Tap Event: 
D93
numPaths
V54
event-info
HandEvent
s\n
V63
Unknown
hand
interpolated-fingers
TouchTask
RadiusCorrectionStep
D73
TouchServiceActivePlan
telemetryData
Hand:\n  
EventInfoParams
%s
interpolatedEventInfo
HandEventArray
fingersArray
PathStats
Event Info -
quantization-dpi
D74
V53
touchSystemReady
EventInfoArray
durationBetweenTouches
D83
D23
V67
value
Node data is not the expected SAPlainDataUInt32 class
pathStats
Duration Between Touches: 
TTW Results: 
TouchService
LocationID
D48
DeviceOrientation
Node data is not the expected SASurfaceDescriptor class
interpolated-event-info
Paths
interpolatedFingers
EventInfoStep
D63
D94
K114
%sminGeoMean:%.3fmm maxGeoMean:%.3fmm eccentForMin:%.3f eccentForMax:%.3f initialIdentity:%u liftoffIdentity:%u\n
AtomicWakeEvent:
TTWResults
HysteresisFilterStep
wakeEvent
InterpolatedEventInfo
TipOffsetStep
SurfaceDescriptor
file
YES
Interpolated Hand:\n  
D47
NO
None
BaselineAdapt
InterpolatedFingerEvents
CoverGestureEvent:
PrimaryUsagePage
V57
Notification
D27
D37
V64
K116
ExternalActive
InterpolatedHandEvent
Telemetry Data - 
D28
InterpolationParams
QuantizationDPI
Node data is not the expected SAEventInfoParams class
atomicWakeEvent
interpolated-hand
PhoneTelemetryData
D17
V59
Node data is not the expected SAInterpolationParams class
ExternalTTW
notificationEvent
FingerEvents
interpolatedHand
FingerEventsArray
 - touchSystemReady:
Path Stats:\n
TTW
InterpolationStep
maxPaths
%s IsNextEventExpected:%s IsInformationEvent:%s InformationReason:%s NextEventDeadline:%lluus NextRealEventTimestamp:%lluus\n
DurationBetweenTouches
V69
v8@?0
deviceReady
TapEvent
PathTrackingStep
InterpolatedEventGenerationStep
TouchSystemReady
TapEventGenerationStep
payload
eventInfo
Contacts:\n
  
numContacts
numberWithUnsignedShort:
registerDataClass
_fingers
data
internalControls
T^{?=C[0{?=ffffII}]},N,V_header
_eventInfo
addObject:
name
printTo:withLabel:
_hand
appendFormat:
getEventInfoParams:
notificationEvent
wakeEvent
initWithLength:
stringToNodeId:
T@\"SATouchServiceEventCollection\",R,N,V_interpolatedFingers
_interpolatedFingers
_stats
nextEventDeadlineUs
platformCategory
setHeader:
T@\"SAWakeEvent\",R,N,V_wakeEvent
fingers
TC,R,N
TI,N
_interpolatedEventInfo
copy
unsignedCharValue
usagePage
T@\"NSData\",R,N,V_payload
init
initWithPayload:
maxGeometricMean
setIsNextEventExpected:
getOrientation:
setInformationReason:
setMaxGeometricMean:
setMinGeometricMean:
ttwResults
_eventInfoArray
T@\"SADynamicArray\",R,N,V_handArray
T@\"SAEventInformation\",R,N,V_interpolatedEventInfo
_contacts
_durationBetweenTouches
setInitialIdentity:
UTF8String
_coverGestureEvent
dictionaryToPayload:
initWithName:points:
length
telemetryData
ttwTap
_ttwTap
Tf,N
_payload
extractionData
initWithWorkNode:dataNode:isPrologue:tag:
usage
T@\"SANotificationEvent\",R,N,V_notificationEvent
_atomicWakeEvent
bytes
excludeProperties
frameClass
defaultMatching
atomicWakeEvent
contacts
isInformationEvent
registerFrameClass
setEccentricityForMin:
setInterpolationParams:error:
setSurfaceDescriptor:error:
T@\"SADynamicArray\",R,N,V_eventInfoArray
T@\"SATouchServiceEvent\",R,N,V_ttwTap
appendString:
array
initWithCapacity:
initWithData:offset:
initWithMaxPaths:
minGeometricMean
defaultTransport
getQuantizationDPI:
TQ,N
_telemetryData
numPaths
_handArray
handArray
setNextEventDeadlineUs:
_interpolatedHand
emptyFrame
eventInfoArray
initWithWorkNode:dataNode:isPrologue:data:
setNumPaths:
_ttwResults
durationBetweenTouches
_header
fingersArray
frameType
internalContents
load
setLiftoffIdentity:
liftoffIdentity
initialIdentity
T@\"SAPathCollection\",R,N,V_contacts
_notificationEvent
hwModelPlatforms
informationReason
interpolatedHand
mergeComponent:withComponent:
T@\"SAPlainDataFloat\",R,N,V_durationBetweenTouches
_wakeEvent
getInterpolationParams:
header
initWithName:workNode:dataNode:isPrologue:tag:
setEventInfoParams:error:
stats
T@\"SATouchServiceEvent\",R,N,V_hand
dataWithBytesNoCopy:length:freeWhenDone:
eccentricityForMin
T@\"SAPlainDataBoolean\",R,N,V_deviceReady
countByEnumeratingWithState:objects:count:
initWithInjectionInfo:injectionData:extractionData:
nextRealEventTimestampUs
setIsInformationEvent:
setNextRealEventTimestampUs:
reasonToString:
T@\"SAPlainDataBoolean\",R,N,V_touchSystemReady
TB,N
arrayWithObjects:count:
deviceReady
T@\"SACoverGestureEvent\",R,N,V_coverGestureEvent
_touchSystemReady
fromRunFrame:
injectionData
printInternalTo:withLabel:
setEccentricityForMax:
setObject:forKeyedSubscript:
eventInfo
expectedDataType
initWithRunFrame:
objectAtIndexedSubscript:
payload
count
dictionaryWithObjects:forKeys:count:
fillFromDictionary:
hand
.cxx_destruct
T@\"SADataNodeArray\",R,N,V_fingersArray
T@\"SATouchServiceEvent\",R,N,V_interpolatedHand
T@\"SATouchServiceEventCollection\",R,N,V_fingers
coverGestureEvent
enablePrint
getControl:data:error:
getSurfaceDescriptor:
initWithContacts:
interpolatedEventInfo
isNextEventExpected
printContentsTo:
registerDeviceClass
setControl:payload:error:
T@\"SAPathStatsCollection\",R,N,V_pathStats
_pathStats
initWithType:payload:
maxPaths
touchSystemReady
eccentricityForMax
_deviceReady
T@\"NSData\",R,N,V_data
newError:error:
T@\"SAPhoneTelemetryData\",R,N,V_telemetryData
T@\"SATTWResults\",R,N,V_ttwResults
_data
interpolatedFingers
T@\"NSArray\",R,N,V_stats
T@\"SAAtomicWakeEvent\",R,N,V_atomicWakeEvent
TC,N
extraNodes
pathStats
workNodeId
T@\"SAEventInformation\",R,N,V_eventInfo
devicePlatforms
_fingersArray
initWithName:workNode:dataNode:isPrologue:dataType:tag:
SATouchServiceFrame
SATouchServiceFrameActive
SATouchServiceFrameTTW
SATouchServiceDevice
SAPathStats
SAPathStatsCollection
SAEventInformation
@\"SAPathStatsCollection\"
#16@0:8
@24@0:8^@16
@24@0:8@16
@\"SAEventInformation\"
S16@0:8
B32@0:8@16^@24
v20@0:8C16
@\"NSArray\"
@\"SATTWResults\"
v24@0:8^{?=C[0{?=ffffII}]}16
^{?=C[0{?=ffffII}]}
B16@0:8
@\"SAPlainDataBoolean\"
@\"SAAtomicWakeEvent\"
@\"SATouchServiceEventCollection\"
@\"SADynamicArray\"
@28@0:8S16@20
@\"SAPlainDataFloat\"
@\"SADataNodeArray\"
v20@0:8I16
@\"NSData\"
v20@0:8B16
v16@0:8
^{?=C[0{?=ffffII}]}16@0:8
@16@0:8
@\"SAPathCollection\"
@\"SATouchServiceEvent\"
@32@0:8@16Q24
v32@0:8@16@24
@20@0:8C16
C16@0:8
Q16@0:8
I16@0:8
v24@0:8@16
@\"SAWakeEvent\"
@\"SANotificationEvent\"
f16@0:8
v24@0:8Q16
v20@0:8f16
@\"SAPhoneTelemetryData\"
@\"SACoverGestureEvent\"
```
