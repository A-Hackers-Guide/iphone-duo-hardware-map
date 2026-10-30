# `ACCPlatformPluginBluetooth`

- Image: [`/System/Library/CoreAccessories/PlugIns/Platform/Platform-Bluetooth.platform/Platform-Bluetooth`](../userland/System__Library__CoreAccessories__PlugIns__Platform__Platform-Bluetooth.platform__Platform-Bluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCPlatformBluetoothStatusPluginProtocol`, `ACCPlatformBluetoothAccessoryInformationPluginProtocol`
- 5 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _isRunning;
B _btUpdatesStarted;
^{BTSessionImpl=} _btSession;
@"NSObject<OS_dispatch_queue>" _btEventQueue;
@"NSMutableDictionary" _accessoryList;
```

## Properties

```
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
```

## Instance methods

```
-[ACCPlatformPluginBluetooth isRunning];
-[ACCPlatformPluginBluetooth stopPlugin];
-[ACCPlatformPluginBluetooth pluginName];
-[ACCPlatformPluginBluetooth startPlugin];
-[ACCPlatformPluginBluetooth initPlugin];
-[ACCPlatformPluginBluetooth setIsRunning:];
-[ACCPlatformPluginBluetooth accessoryList];
-[ACCPlatformPluginBluetooth accessoryAttached:];
-[ACCPlatformPluginBluetooth accessoryDetached:];
-[ACCPlatformPluginBluetooth setAccessoryList:];
-[ACCPlatformPluginBluetooth btEventQueue];
-[ACCPlatformPluginBluetooth btSession];
-[ACCPlatformPluginBluetooth btUpdatesStarted];
-[ACCPlatformPluginBluetooth getAccessoryList];
-[ACCPlatformPluginBluetooth iterateRegisteredComponentsForKnownAddresses:allOFF:];
-[ACCPlatformPluginBluetooth nameForMacAddress:];
-[ACCPlatformPluginBluetooth performInit];
-[ACCPlatformPluginBluetooth pluginBTDevice:btAccessoryManager:btDevice:];
-[ACCPlatformPluginBluetooth setBtEventQueue:];
-[ACCPlatformPluginBluetooth setBtSession:];
-[ACCPlatformPluginBluetooth setBtUpdatesStarted:];
-[ACCPlatformPluginBluetooth startCheckingForUpdates:forAccessory:];
-[ACCPlatformPluginBluetooth stopCheckingForUpdates:forAccessory:];
-[ACCPlatformPluginBluetooth unplugBTDevice:btAccessoryManager:btDevice:];
-[ACCPlatformPluginBluetooth updateBTComponent:forAccessory:withEnabledState:];
```
