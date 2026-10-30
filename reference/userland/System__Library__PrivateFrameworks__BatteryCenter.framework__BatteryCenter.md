# `/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter`

iOS 27.2 dyld shared cache image. Version `328.0.0.0.0`. **[DSC]**

## Linked libraries (8)

- `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 4 classes, 5 protocols, 120 methods, 38 properties

### Class pages

Every class and protocol, with its methods: [`BCBatteryCenterPrototypingDomain`](../objc/BCBatteryCenterPrototypingDomain_BatteryCenter.md), [`BCBatteryDevice`](../objc/BCBatteryDevice_BatteryCenter.md), [`BCBatteryDeviceController`](../objc/BCBatteryDeviceController_BatteryCenter.md), [`BCBatteryDeviceObservable`](../objc/BCBatteryDeviceObservable_BatteryCenter.protocol.md), [`NSCoding`](../objc/NSCoding_BatteryCenter.protocol.md), [`NSCopying`](../objc/NSCopying_BatteryCenter.protocol.md), [`NSObject`](../objc/NSObject_BatteryCenter.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_BatteryCenter.protocol.md), [`_BCPowerSourceController`](../objc/_BCPowerSourceController_BatteryCenter.md)

### Classes

`BCBatteryCenterPrototypingDomain`, `BCBatteryDevice`, `BCBatteryDeviceController`, `_BCPowerSourceController`

### Protocols

`BCBatteryDeviceObservable`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_name) name;
@property (Tq,N,V_percentCharge) percentCharge;
@property (TB,N,GisConnected,V_connected) connected;
@property (TB,N,GisCharging,V_charging) charging;
@property (TB,N,GisPaused,V_paused) paused;
@property (TB,N,GisInternal,V_internal) internal;
@property (TB,N,GisPowerSource,V_powerSource) powerSource;
@property (TB,N,V_approximatesPercentCharge) approximatesPercentCharge;
@property (TQ,N,V_parts) parts;
@property (TB,N,GisWirelesslyCharging,V_wirelesslyCharging) wirelesslyCharging;
@property (T@"NSString",C,N,V_groupName) groupName;
@property (T@"NSString",R,C,N,V_matchIdentifier) matchIdentifier;
@property (Tq,N,V_transportType) transportType;
@property (Tq,N,V_powerSourceState) powerSourceState;
@property (TB,N,GisFake,V_fake) fake;
@property (TB,N,GisLowPowerModeActive,V_lowPowerModeActive) lowPowerModeActive;
@property (TB,N,GisLowBattery,V_lowBattery) lowBattery;
@property (T@"NSString",C,N,V_accessoryIdentifier) accessoryIdentifier;
@property (TQ,N,V_accessoryCategory) accessoryCategory;
@property (T@"NSString",C,N,V_modelNumber) modelNumber;
@property (Tq,R,N,V_vendor) vendor;
@property (Tq,R,N,V_productIdentifier) productIdentifier;
@property (T@"NSArray",R,C,N) connectedDevices;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",R,C,N) connectedDevices;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (143)

```
(%{public}@) Successfully registered for %{public}s notifications
(%{public}@) Failed to register for %{public}s notifications
(%{public}@) Unregistering for power source change notifications
(%{public}@) Query for connected devices
(%{public}@) Notifying observer: <%{public}@: %p>
(%{public}@) Error in fetching charging status %d
(%{public}@) No value for %@ in chargingStatusDictionary
(%{public}@) Found power source: %{public}@
(%{public}@) Low Power Mode changed: %d
(%{public}@) initializing new power source controller
(%{public}@) Got a list of %ld sources
(%{public}@) Failed to obtain power sources info
(%{public}@) State of chargingStatusDictionary post converting to ObjC %@
(%{public}@) Found %lu power sources
(%{public}@) Fetch connected devices
(%{public}@)<%p> Added observer: %@<%p>
(%{public}@)<%p> Removed observer: %@<%p>
(%{public}@) Found device: %{public}@
(%{public}@) Coalesced device: %{public}@
(%{public}@) Received %{public}s notification
(%{public}@) Argument token not nil when registering for %{public}s notifications
(%{public}@) Registering for power source change notifications
(%{public}@) Failed to obtain power sources list
(%{public}@) Power source debug info: %{public}@
v8@?0
connected
Is Charging
Speaker
Unknown
Invalid parameter not satisfying: %@
observer
Off Line
Right
Battery Case
com.apple.system.accpowersources.source
com.apple.system.accpowersources.timeremaining
powerSource
v16@?0@\"<BCBatteryDeviceObserving>\"8
Accessory Category
com.apple.system.powersources.chargingiconography
BatteryCenter
groupName
fake
Apple
Inductive In-Band
Vendor ID
left
Watch
Game Controller
<%@: %p;%@ vendor = %@; productIdentifier = %ld; parts = %@; identifier = %@; matchIdentifier = %@; name = %@; groupName =%@; percentCharge = %ld; lowBattery = %@; lowPowerModeActive = %@; connected = %@; charging = %@; paused = %@; interna
right
Keyboard
Beats
Debug Information
Type
single
Group Identifier
Left
Transport Type
Controller
percentCharge
accessoryCategory
Missing kIOPSPowerSourceIDKey in %@
XnXl4MhKZx3zRKvA7ZwIYQ
-
Name
v12@?0i8
Headset
chargeStatus
InternalBattery
Current Capacity
productIdentifier
Part Identifier
Mouse
Battery Power
com.apple.system.powersources.timeremaining
BatteryDeviceController
Serial
Accessory Identifier
B
Power Source State
Bluetooth
UserAssignedDeviceName
B16@?0@\"BCBatteryDevice\"8
IsWireless
Widget
CombinedLeftRightBatteryStatus
matchIdentifier
Bluetooth LE
Accessory Source
LPM Active
AudioAccessoryFeatures
com.apple.system.lowpowermode
USB
gas-gauge-battery
com.apple.BatteryCenter
Headphone
AC Power
Product ID
Model Number
powerSourceState
transportType
case
Combined
v32@?0@\"BCBatteryDevice\"8Q16^B24
parts
modelNumber
Charging On Hold
com.apple.system.accpowersources.attach
queue
vendor
Case
com.apple.system.powersources.percent
BCPowerSourceController.m
Trackpad
Pencil
Show Charging UI
Part Name
q24@?0@\"BCBatteryDevice\"8@\"BCBatteryDevice\"16
paused
**FAKE DEVICE**
Wired
AID
identifier
v24@?0@\"NSMutableString\"8@\"NSString\"16
Low Warn Level
PowerSourceController
charging
internal
approximatesPercentCharge
-%@
Internal
HearingAid
com.apple.BCBatteryDeviceController
wirelesslyCharging
Max Capacity
Audio Battery Case
%@-synthesized
AdapterDetails
name
accessoryIdentifier
Inductive
Power Source ID
```
