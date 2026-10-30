# `/System/Library/CoreAccessories/PlugIns/Platform/Platform-Bluetooth.platform/Platform-Bluetooth`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 3 classes, 5 protocols, 73 methods, 25 properties

### Class pages

Every class and protocol, with its methods: [`ACCPlatformBluetoothAccessoryInformationPluginProtocol`](../objc/ACCPlatformBluetoothAccessoryInformationPluginProtocol_Platform-Bluetooth.protocol.md), [`ACCPlatformBluetoothStatusAccessory`](../objc/ACCPlatformBluetoothStatusAccessory_Platform-Bluetooth.md), [`ACCPlatformBluetoothStatusPluginProtocol`](../objc/ACCPlatformBluetoothStatusPluginProtocol_Platform-Bluetooth.protocol.md), [`ACCPlatformPluginBluetooth`](../objc/ACCPlatformPluginBluetooth_Platform-Bluetooth.md), [`ACCPlatformPluginProtocol`](../objc/ACCPlatformPluginProtocol_Platform-Bluetooth.protocol.md), [`ACCPluginProtocol`](../objc/ACCPluginProtocol_Platform-Bluetooth.protocol.md), [`NSObject`](../objc/NSObject_Platform-Bluetooth.protocol.md), [`_ACCBluetoothStatusComponent`](../objc/_ACCBluetoothStatusComponent_Platform-Bluetooth.md)

### Classes

`ACCPlatformBluetoothStatusAccessory`, `ACCPlatformPluginBluetooth`, `_ACCBluetoothStatusComponent`

### Protocols

`ACCPlatformBluetoothAccessoryInformationPluginProtocol`, `ACCPlatformBluetoothStatusPluginProtocol`, `ACCPlatformPluginProtocol`, `ACCPluginProtocol`, `NSObject`

### Properties

```
@property (T@"NSString",R,N) pluginName;
@property (TB,R,N) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N,V_accessoryUID) accessoryUID;
@property (T@"NSMutableDictionary",R,N,V_componentList) componentList;
@property (TB,N,V_isRunning) isRunning;
@property (TB,N,V_btUpdatesStarted) btUpdatesStarted;
@property (T^{BTSessionImpl=},N,V_btSession) btSession;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_btEventQueue) btEventQueue;
@property (T@"NSMutableDictionary",&,N,V_accessoryList) accessoryList;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
@property (T@"NSString",R,N,V_accessoryUID) accessoryUID;
@property (T@"NSString",R,N,V_componentUID) componentUID;
@property (T@"NSData",R,N,V_macAddr) macAddr;
@property (T@"NSString",R,N,V_name) name;
@property (T^{BTAccessoryManagerImpl=},N,V_btAccessoryManager) btAccessoryManager;
@property (T^{BTDeviceImpl=},N,V_btDevice) btDevice;
@property (TB,N,V_needToUnplugBTDevice) needToUnplugBTDevice;
```

## Strings (76)

```
WiFiSharing
<Undefined>
v8@?0
com.apple.accessories.signposts
General
Transport
_ACCBluetoothStatusComponent<%@ name=%@ needToUnplugBTDevice=%d>
com.apple.plugin.platform.bluetooth
\"
ACCPlatformBluetoothStatusAccessory<%@ comonentList=%@>
com.apple.iaptransportd-%d
ACCBluetoothStatusComponentInfoID
ACCBluetoothStatusComponentInfoName
ACCBluetoothStatusComponentInfoMACAddr
ACCBluetoothStatusComponentInfoEnabled
ACCBluetoothStatusComponentUpdateInfoUID
ACCBluetoothStatusComponentUpdateInfoProfiles
ACCBluetoothStatusComponentUpdateInfoAccessoryUID
com.apple.accessories.platform-plugins
Power
Connection
Endpoint
ACCBluetoothStatusComponentInfoAccessoryUID
ACCBluetoothStatusComponentInfoUID
ACCBluetoothStatusComponentUpdateNotification
_BTLocalDeviceCallback object=%@
ERROR - failed getting MAC address for device
Failed to create os_log_t object %s: %s!
btUpdates NOT Started, object=%@
Failed to get device from address.
Created %d log object(s)!
accessoryUID=%@ componentDict=%@
ERROR - no accessory registered for accessoryUID %@
Failed to get device address from string.
Error - NULL BT session
Error - Failed to get device.
ERROR - failed getting local BT device
Added new accessory to list, accessoryList=%@
ERROR - NULL BT Session.
BluetoothConnectionStatusNotification: service mask 0x%04X(0x%04X), accessoryUID: %@, componentUID: %@
ERROR - failed getting connected BT devices
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
accessory=%@
component=%@
Unable to find accessory for %@
ERROR - BTDeviceConnect (%@) failed!
No Address. Result = %d.
_DetachFromBTServer object=%@
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Created log object %s: %s
Remove accessory from list, accessoryList=%@
call BTAccessoryManagerUnplugDevice, component=%@
Failed to allocate memory for name.
Error - Failed to get local BT device
ERROR - failed attaching to BT server, result=%d
ERROR - called with a NULL BTSession
ERROR - called with a BTResult of %d
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
call BTAccessoryManagerPlugInDevice, component=%@
updateBTComponent: componentDict=%@ enabled=%d
ERROR - BTDeviceDisconnect (%@) failed!
Error - Failed to get local BT device power status
_BTServiceCallback object=%@
ERROR - failed detaching from BT server, result=%d
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
ERROR - BTAccessoryManagerUnplugDevice (%@) failed (with %d result)!
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
Error - Failed to get BT Accessory Manager
Error - NULL parameter
ERROR - BTDeviceFromAddress failed.
_AttachToBTServer object=%@
_BTSessionCallback object=%@
accessoryUID=%@
ERROR - BTAccessoryManagerPlugInDevice (%@) failed (with %d result)!
ERROR - NULL MAC Address.
Error - Bluetooth is not enabled.
```
