# `/System/Library/PrivateFrameworks/BluetoothAudio.framework/BluetoothAudio`

iOS 27.2 dyld shared cache image. Version `2701.7.1.0.0`. **[DSC]**

## Linked libraries (12)

- `/usr/lib/libFDR.dylib`
- `/System/Library/Frameworks/CoreAudio.framework/CoreAudio`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`
- `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager`
- `/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 1 classes, 0 protocols, 39 methods, 11 properties

### Class pages

Every class and protocol, with its methods: [`BluetoothBridge`](../objc/BluetoothBridge_BluetoothAudio.md)

### Classes

`BluetoothBridge`

### Properties

```
@property (TB,N,V_noHFPSupport) noHFPSupport;
@property (T@"NSMutableDictionary",&,N,V_lecaSessionIDCache) lecaSessionIDCache;
@property (T@"NSObject<OS_dispatch_semaphore>",&,V_connectedSemaphore) connectedSemaphore;
@property (T^{OpaqueFigEndpointManager=},N,V_manager) manager;
@property (T@"CBDiscovery",&,V_deviceDiscovery) deviceDiscovery;
@property (TB,V_targetUserSession) targetUserSession;
@property (T@"CUSystemMonitor",&,V_systemMonitor) systemMonitor;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@?,C,V_lowerScanRate) lowerScanRate;
@property (T@?,C,V_activation) activation;
@property (T@?,C,V_activationTimeoutBlock) activationTimeoutBlock;
```

## Strings (155)

```
BluetoothEndpointStreamAudio
Connected
BTFigE
Features
Headset
v8@?0
1`
com.apple.bluetooth
%@-btaudio
Shareable
ConversationDetectEnable
%d
Found an existing entry
supported
BT%@%d,%d
BluetoothBridge
Name
UserPickedRoute
IsGenuineAirPods
DeviceSupportsWirelessSplitting
v20@?0I8r^{AudioObjectPropertyAddress=III}12
BluetoothEndpointStreamQueue
Started
tsco
BluetoothEndpointCollectionQueue
Speaker
Headphones
DeviceClass
BluetoothEndpointManager
HearingAid
v16@?0@\"CBDevice\"8
<APEndpointStreamAudio %p '%@'>
HFP
BatteryLevels
ListeningMode
SpatialAudioEnabled
Bluetooth Endpoint
v16@?0@\"NSError\"8
%@-%s
Bluetooth Endpoint Manager
no endpoints
SupportsConversationDetect
WirelessSplitter
endpoints present
Earbud
SpatialAudioMode
ModelID
SupportedListeningModes
SupportsSpatialAudio
BluetoothEndpointNotification
disconnected
SmartRoutingEnabled
Didn't find an entry
A2DP
DeviceID
SupportedFormats
BluetoothEndpointQueue
tacl
AudioAccessory
TargetUserSession
SupportsSmartRouting
v12@?0i8
connected
not supported
Error Service Mask isn't right %@ has service mask 0x%X
Wireless Splitter this is a guest not in contacts blocking HFP & GATT services
Update %@ err:%d
ModelID %@->%@
Error setting listening mode
No device
Connect to device %@
Activated
Listening mode %d->%d
Set conversationDetect mode to %d for %@
First unlock handler
Dropping scan rate to low
No longer paired
Baseband connected to %@
BluetoothEndpointManager %p already exists!
Device with address %@ is %s
Battery Levels %@->%@
Spatial audio Allowed : %d->%d
Is Genuine AirPods : %d->%d
Set setSpatialAudioAllowed mode to %d for %@
Disconnected with no nearby status
%@ is guest not in contacts removing handsfree service
HFP %s
HAL: %@ %@
Activation block is nil
BluetoothEndpointCreateWithDescription %@
ProductID 0x%04X->0x%04X
SmartRouting Enabled : %d->%d
Couldn't find a paired device with identifier %@
DeviceID %@->%@
Shareable %d->%d
Failed to get listening mode property value
Can't get PID/VID before first unlock
Failed to set audio route hidden to no
Created BluetoothEndpointManager %p with TargetUserSession: %d
Connected %d->%d
Device found %@ with flags:%@
Device lost %@
Starting Discovery error %@
Handle Remove All Event
Posting Available Endpoints Changed Notification #endpoints:%d
Copy property %@ not supported
Error setting setSpatialAudioAllowed
Destroy Collection entry
Device doesn't support audio?
Error connecting to %@
Error creating Bluetooth Endpoint Manager 0x%x
We have %{public}s
modelID=%@
Find endpoint for a NULL address?
Remove entry
Can't start LE scans on HomePod
%s is not published for %@
Posting Endpoints Present Changed Notification #endpoints:%d
Support SmartRouting : %d->%d
Error setting conversationDetect mode
Removing %@
Audio devices changed
Couldn't get audio objects
Conversation Detect Enabled : %d->%d
Activate %@
%{public}s for %@
No device usable
Error getting controller info to determine HFP support
Supported Listening Modes %d->%d
Finalize %@
Error setting setSpatialAudioMode
Error setting spatial mode with a CFType != CFNumber
Set UserRouted failed: device not found for ID %@
Activate Timeout
Not changing scan parameters
Deactivate %@
Support Conversation Detect : %d->%d
Set user routed: %d
Set UserRouted failed: device %@, value %d, error %@
Activated %@ with result %d
Name %@->%@
Spatial Audio mode %d->%d
pid=%@
vid=%@
Set setSpatialAudioMode mode to %d for %@
Starting LE scanning (%d) fast:%d
Discovery Mode set to %{public}@
VendorID 0x%04X->0x%04X
Spatial audio Support : %d->%d
Set listening mode to %d for %@
Stop LE scanning
Removing LECA device using cached session ID %@
Copy property %@ returns %@
Add Listeners
Failed to add AudioDevice listener %d
```
