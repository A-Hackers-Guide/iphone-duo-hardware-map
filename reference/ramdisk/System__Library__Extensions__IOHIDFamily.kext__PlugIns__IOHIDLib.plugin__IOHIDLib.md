# `/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDLib.plugin/IOHIDLib`

From the upgrade restore ramdisk (141-29011-104.dmg). 155,968 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 3656)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (9)

- `/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDLib.plugin/IOHIDLib (compatibility version 0.0.0, current version 0.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/HID.framework/HID (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (1 classes, 0 protocols)

Classes: `IOHIDUPSClass`

## Strings (256)

```
IOHIDEventServiceFastPathClass failed to retain service object with err %x\n
IOConnectCallMethod (kIOHIDEventServiceFastPathUserClientClose): 0x%x\n
No shared memory\n
Nothing to commit skip
Power Source status isACSource : %s , isCharging : %s , isDischarging : %s
deviceProperties not valid
Over Release IOHIDIUnknown Reference
Transaction not valid
Feature element (UP : %x, U : %x) added for polling
Create timer for polling feature reports (interval: %.2f sec)
Failed to set transaction direction %x
Constant feature element UP : %x , U : %x updated
Unable to update element UP: %x, U : %x no value
Device not valid
Failed to open device with error %x
IOServiceOpen(kIOHIDEventServiceFastPathUserClientType): 0x%x\n
Invalid transaction
Unable to update element UP: %x, U : %x failed(%#x)
Skipping duplicate element (UP : %x U : %x Type : %u IV: %ld) with key %@\n
sendCommand: %@
IOConnectSetCFProperty: 0x%x\n
Using custom power feature poll rate: %.2f sec
Failed to create plugin interface with error %x
Plugin not valid
Elements not valid
Failed to get queue interface with error %d
IOConnectMapMemory (sharedMemorySize:%d): 0x%x\n
Invalid argument (pEvent = null)\n
IOConnectCallMethod (kIOHIDEventServiceFastPathUserClientCopyEvent): 0x%x (copySpec = %@)\n
capabilities: %@
Failed to get transaction interface with error %d
IOConnectGetService(kIOHIDEventServiceFastPathUserClientType): 0x%x\n
Failed to add element to transaction %x
Failed to query properties with error %x
Failed to get device interface with error %d
Failed to copy matching elements with error %x
IOConnectCallMethod (kIOHIDEventServiceFastPathUserClientOpen): 0x%x\n
properties: %@
Failed to commit input element transaction with error %x
Queue not valid
%@: %@
Debug Information
IOHIDEventService
Keyboard
Internal Failure
Time to Full Charge
timer dispatchEvent
Transport
Vendor ID
PowerFeaturePollRateSec
Enable Charging
Cell 1 Voltage
Lifetime Time Above Mid Temperature
Lifetime Cell0 Max Q
PrimaryUsage
Cell 0 Voltage
InductiveStatus
Attach Count AirPods Case
IOHIDDevice
GameControllerType
Is Charging
Send Current State of Charge
Current Capacity
CycleCount
Address
PrimaryUsagePage
Battery Case Charging Voltage
Lifetime Max Charge Current
Lifetime Max Temperature
v16@?0@\"NSTimer\"8
getEvent
ModelNumber
Battery Case Cumulative Current
Incoming Voltage
Incoming Current
Attach Count Less Than 5W Adapter
Attach Count 7.5W Adapter
No
Product ID
Send Current Temperature
Attach Count Other
Rx Power Limit
AC Power
J1
Transport Type
VendorID
Accessory Identifier
Mouse
Startup Delay
Current
AppleRawCurrentCapacity
Send Average Charging Current
Model Number
Game Controller
Power Source State
ChargingStatus
Lifetime Cell0 Max Voltage
Lifetime Max Discharge Current
Lifetime Min Temperature
Lifetime Time Above Low Temperature
Temperature
Attach Count Device Type 1
Attach Count 5W Adapter
i
Battery Power
Name
Manufacturer
PowerStatus
Lifetime Cell1 Min Voltage
Lifetime Time Below Low Temperature
Lifetime Time Above High Temperature
Yes
QueueSize
Time to Empty
Set Address
Lifetime Firmware Runtime
Attach Count 10.5W Adapter
v32@?0@\"NSString\"8@16^B24
SerialNumber
Accessory Category
Nominal Capacity
Lifetime Cell1 Max Voltage
Kiosk Mode Count
Attach Count Device Type 0
Attach Count 12W Adapter
Attach Count 15W Adapter
Product
Set Required Voltage
Enable Audible Alarm
Max Capacity
Lifetime Cell1 Max Q
dispatchEvent
ProductID
Delayed Remove Power
Lifetime Cell0 Min Voltage
Host Available Power dW
Device Color
Voltage
Battery Case Available Current
Set Current Limit
FamilyCode
Battery Case Average Charging Current
Attach Count 18 - 20W Adapter
Attach Count Over 20W Adapter
IOHIDUPSClass
queryInterface:outInterface:
removeObjectForKey:
_powerFeaturePollInterval
setIsConstant:
setIsUpdated:
addEntriesFromDictionary:
_commandElements
createAsyncEventSource:
getEvent:
objectForKey:
parseElements:
dealloc
_upsEvent
parseProperties:
getCapabilities:
initWithFireDate:interval:repeats:block:
isEqual:
sendCommand:
updateEvent
valueAvailableCallback:
addObject:
copyElements:psKey:
stop
type
_eventRefcon
_runLoopSource
doubleValue
numberWithInteger:
setDataValue:
_upsUpdatedEvent
date
initWithElementRef:
intValue
isConstant
_elements
_timer
getProperties:
indexOfObject:
objectForKeyedSubscript:
_properties
addObjectsFromArray:
initialEventUpdate
numberWithInt:
timestamp
_device
_capabilities
pollEventUpdate
_eventElements
setIntegerValue:
unit
.cxx_destruct
_transaction
_ups
isEqualToString:
probe:service:outScore:
psKey
start:service:
usage
_eventTarget
mutableCopy
usagePage
valueRef
dataValue
enumerateKeysAndObjectsUsingBlock:
init
invalidate
isUpdated
latestElement:psKey:
setObject:forKeyedSubscript:
setPsKey:
_queue
setValueRef:
unitExponent
_debugInformation
updateElements:
countByEnumeratingWithState:objects:count:
integerValue
removeAllObjects
objectAtIndex:
setEventCallback:target:refcon:
_eventCallback
count
elementRef
^{__CFRunLoopSource=}
d
v20@0:8i16
v16@0:8
i28@0:8@16I24
i24@0:8r^^v16
@16@0:8
^^{IOHIDDeviceTimeStampedDeviceInterface}
^^{IOHIDDeviceTransactionInterface}
^?
i40@0:8{?=CCCCCCCCCCCCCCCC}16^^v32
v24@0:8@16
@32@0:8@16@24
i16@0:8
^{IOUPSPlugInInterface_v140=^v^?^?^?^?^?^?^?^?^?}
@\"NSMutableDictionary\"
@\"NSMutableSet\"
{?=\"input\"@\"NSMutableArray\"\"output\"@\"NSMutableArray\"\"feature\"@\"NSMutableArray\"}
i40@0:8^?16^v24^v32
@\"NSMutableArray\"
^v
@\"NSTimer\"
i24@0:8@16
i36@0:8@16I24^i28
B16@0:8
i24@0:8r^^{__CFDictionary}16
i24@0:8r^^{__CFSet}16
^^{IOHIDDeviceQueueInterface}
```
