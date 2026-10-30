# `/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDLib.plugin/IOHIDLib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 155,968 bytes.

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
dealloc
_transaction
parseElements:
setIsConstant:
valueRef
_eventElements
addObject:
count
elementRef
psKey
timestamp
_device
_eventCallback
removeAllObjects
start:service:
type
_capabilities
.cxx_destruct
_eventTarget
getEvent:
getProperties:
unitExponent
usagePage
_debugInformation
addEntriesFromDictionary:
copyElements:psKey:
isUpdated
parseProperties:
setIntegerValue:
_ups
date
latestElement:psKey:
queryInterface:outInterface:
_eventRefcon
_queue
_upsEvent
indexOfObject:
isConstant
_commandElements
_powerFeaturePollInterval
_upsUpdatedEvent
setPsKey:
stop
updateEvent
usage
valueAvailableCallback:
createAsyncEventSource:
enumerateKeysAndObjectsUsingBlock:
initialEventUpdate
integerValue
numberWithInt:
objectForKeyedSubscript:
doubleValue
getCapabilities:
isEqualToString:
numberWithInteger:
removeObjectForKey:
setDataValue:
_timer
addObjectsFromArray:
_properties
_runLoopSource
dataValue
sendCommand:
pollEventUpdate
setEventCallback:target:refcon:
initWithFireDate:interval:repeats:block:
invalidate
isEqual:
setIsUpdated:
unit
initWithElementRef:
intValue
probe:service:outScore:
init
objectForKey:
setObject:forKeyedSubscript:
updateElements:
_elements
countByEnumeratingWithState:objects:count:
mutableCopy
objectAtIndex:
setValueRef:
@\"NSMutableArray\"
v24@0:8@16
@32@0:8@16@24
B16@0:8
v16@0:8
i24@0:8r^^{__CFDictionary}16
i24@0:8r^^{__CFSet}16
{?=\"input\"@\"NSMutableArray\"\"output\"@\"NSMutableArray\"\"feature\"@\"NSMutableArray\"}
@\"NSTimer\"
i40@0:8{?=CCCCCCCCCCCCCCCC}16^^v32
i36@0:8@16I24^i28
^^{IOHIDDeviceTimeStampedDeviceInterface}
^^{IOHIDDeviceQueueInterface}
^v
^{__CFRunLoopSource=}
d
i24@0:8r^^v16
i28@0:8@16I24
i24@0:8@16
@16@0:8
^{IOUPSPlugInInterface_v140=^v^?^?^?^?^?^?^?^?^?}
^^{IOHIDDeviceTransactionInterface}
@\"NSMutableSet\"
^?
v20@0:8i16
i16@0:8
i40@0:8^?16^v24^v32
@\"NSMutableDictionary\"
Plugin not valid
Failed to get device interface with error %d
Over Release IOHIDIUnknown Reference
No shared memory\n
Invalid argument (pEvent = null)\n
Feature element (UP : %x, U : %x) added for polling
Invalid transaction
Failed to add element to transaction %x
Failed to commit input element transaction with error %x
deviceProperties not valid
IOConnectCallMethod (kIOHIDEventServiceFastPathUserClientOpen): 0x%x\n
Failed to set transaction direction %x
Failed to open device with error %x
Transaction not valid
IOHIDEventServiceFastPathClass failed to retain service object with err %x\n
IOConnectGetService(kIOHIDEventServiceFastPathUserClientType): 0x%x\n
IOConnectCallMethod (kIOHIDEventServiceFastPathUserClientClose): 0x%x\n
Create timer for polling feature reports (interval: %.2f sec)
Failed to get queue interface with error %d
IOServiceOpen(kIOHIDEventServiceFastPathUserClientType): 0x%x\n
IOConnectSetCFProperty: 0x%x\n
Constant feature element UP : %x , U : %x updated
Unable to update element UP: %x, U : %x failed(%#x)
Unable to update element UP: %x, U : %x no value
Skipping duplicate element (UP : %x U : %x Type : %u IV: %ld) with key %@\n
Elements not valid
Queue not valid
IOConnectMapMemory (sharedMemorySize:%d): 0x%x\n
properties: %@
capabilities: %@
Device not valid
sendCommand: %@
Using custom power feature poll rate: %.2f sec
Nothing to commit skip
Power Source status isACSource : %s , isCharging : %s , isDischarging : %s
Failed to create plugin interface with error %x
Failed to copy matching elements with error %x
Failed to get transaction interface with error %d
%@: %@
IOConnectCallMethod (kIOHIDEventServiceFastPathUserClientCopyEvent): 0x%x (copySpec = %@)\n
Failed to query properties with error %x
PowerStatus
Lifetime Cell0 Max Voltage
Lifetime Cell0 Min Voltage
Vendor ID
Temperature
Lifetime Max Temperature
Attach Count Less Than 5W Adapter
Attach Count 7.5W Adapter
Lifetime Cell0 Max Q
Battery Power
SerialNumber
Accessory Identifier
Accessory Category
Lifetime Time Above High Temperature
Attach Count 5W Adapter
Attach Count 15W Adapter
Host Available Power dW
Transport Type
ChargingStatus
Lifetime Firmware Runtime
Attach Count 12W Adapter
Attach Count Over 20W Adapter
Device Color
PrimaryUsage
Lifetime Max Discharge Current
getEvent
QueueSize
Current
Max Capacity
Time to Full Charge
Model Number
GameControllerType
Time to Empty
Lifetime Min Temperature
Lifetime Cell1 Max Q
timer dispatchEvent
Yes
IOHIDDevice
VendorID
Set Required Voltage
AppleRawCurrentCapacity
Cell 1 Voltage
Lifetime Cell1 Max Voltage
Attach Count 10.5W Adapter
AC Power
ProductID
Keyboard
PowerFeaturePollRateSec
Delayed Remove Power
CycleCount
Lifetime Max Charge Current
Kiosk Mode Count
Attach Count AirPods Case
Battery Case Charging Voltage
Send Average Charging Current
Incoming Current
Manufacturer
Startup Delay
Voltage
Current Capacity
Attach Count 18 - 20W Adapter
Name
Battery Case Available Current
Set Current Limit
Battery Case Cumulative Current
Battery Case Average Charging Current
InductiveStatus
Attach Count Device Type 0
Attach Count Other
Mouse
Game Controller
Send Current Temperature
Lifetime Time Below Low Temperature
Lifetime Time Above Low Temperature
i
Debug Information
v32@?0@\"NSString\"8@16^B24
Transport
Send Current State of Charge
Cell 0 Voltage
Rx Power Limit
v16@?0@\"NSTimer\"8
dispatchEvent
J1
Enable Audible Alarm
Lifetime Cell1 Min Voltage
Product
Address
Lifetime Time Above Mid Temperature
Attach Count Device Type 1
Nominal Capacity
FamilyCode
Incoming Voltage
Product ID
ModelNumber
Enable Charging
Is Charging
No
IOHIDEventService
PrimaryUsagePage
Internal Failure
Power Source State
Set Address
IOHIDUPSClass
```
