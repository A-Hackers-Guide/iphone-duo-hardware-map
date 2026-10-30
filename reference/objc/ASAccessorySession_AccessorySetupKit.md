# `ASAccessorySession`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 9 properties, 52 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@"NSMutableDictionary" _accessories;
B _bluetoothTCCStateUnknown;
@"NSString" _bundleID;
@"NSMutableDictionary" _discoveredAccessories;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
B _invalidateCalled;
B _invalidateDone;
@"NSObject<OS_dispatch_queue>" _sessionQueue;
B _disablePickerItemMaxLimit;
B _disableWiFiAwareEnforcement;
@"ASPickerDisplaySettings" _pickerDisplaySettings;
@"DASession" _daSession;
@"NSObject<OS_xpc_object>" _xpcListenerEndpoint;
@? _eventHandler;
@"NSString" _overrideAppBundleID;
```

## Properties

```
@property (T@"DASession",&,N,V_daSession) daSession;
@property (T@"NSObject<OS_xpc_object>",&,N,V_xpcListenerEndpoint) xpcListenerEndpoint;
@property (T@?,C,N,V_eventHandler) eventHandler;
@property (T@"NSObject<OS_dispatch_queue>",R,N) queue;
@property (TB,N,V_disablePickerItemMaxLimit) disablePickerItemMaxLimit;
@property (TB,N,V_disableWiFiAwareEnforcement) disableWiFiAwareEnforcement;
@property (T@"NSString",C,N,V_overrideAppBundleID) overrideAppBundleID;
@property (T@"NSArray",R,C,N) accessories;
@property (T@"ASPickerDisplaySettings",C,N,V_pickerDisplaySettings) pickerDisplaySettings;
```

## Class methods

```
+[ASAccessorySession validateAccessorySetupBundleInfo:error:];
```

## Instance methods

```
-[ASAccessorySession eventHandler];
-[ASAccessorySession setEventHandler:];
-[ASAccessorySession init];
-[ASAccessorySession dealloc];
-[ASAccessorySession xpcListenerEndpoint];
-[ASAccessorySession accessories];
-[ASAccessorySession queue];
-[ASAccessorySession invalidate];
-[ASAccessorySession _applicationWillEnterForegroundNotification];
-[ASAccessorySession setXpcListenerEndpoint:];
-[ASAccessorySession _invalidated];
-[ASAccessorySession _removeAccessory:completionHandler:];
-[ASAccessorySession removeAccessory:completionHandler:];
-[ASAccessorySession overrideAppBundleID];
-[ASAccessorySession setOverrideAppBundleID:];
-[ASAccessorySession setDisableWiFiAwareEnforcement:];
-[ASAccessorySession activateWithQueue:eventHandler:];
-[ASAccessorySession _activateWithQueue:eventHandler:];
-[ASAccessorySession _fetchAuthorizedAccesoriesIfNeeded];
-[ASAccessorySession _fetchBluetoothGlobalTCC];
-[ASAccessorySession _finishDiscovery:];
-[ASAccessorySession _handleDASessionEventHandler:session:];
-[ASAccessorySession _hasBluetoothASK];
-[ASAccessorySession _notifyAccesoriesChangedIfNeeded:bundleID:eventType:];
-[ASAccessorySession _setupDeviceAccessSession];
-[ASAccessorySession _showPickerForDisplayItems:completionHandler:];
-[ASAccessorySession _updateAccessory:settings:completionHandler:];
-[ASAccessorySession _updatePickerWithDiscoveredDisplayItems:completionHandler:];
-[ASAccessorySession _validateDiscoveryDescriptor:];
-[ASAccessorySession _validateDisplayItem:];
-[ASAccessorySession _validateMigrationDisplayItem:];
-[ASAccessorySession _verifyCoreBluetoothStateToActivatePicker:];
-[ASAccessorySession activateWithEventHandler:];
-[ASAccessorySession daSession];
-[ASAccessorySession disablePickerItemMaxLimit];
-[ASAccessorySession disableWiFiAwareEnforcement];
-[ASAccessorySession failAuthorization:completionHandler:];
-[ASAccessorySession finishAuthorization:settings:completionHandler:];
-[ASAccessorySession finishPickerDiscovery:];
-[ASAccessorySession pickerDidReport:];
-[ASAccessorySession pickerDisplaySettings];
-[ASAccessorySession relayPickerEvent:];
-[ASAccessorySession renameAccessory:options:completionHandler:];
-[ASAccessorySession setDaSession:];
-[ASAccessorySession setDisablePickerItemMaxLimit:];
-[ASAccessorySession setPickerDisplaySettings:];
-[ASAccessorySession showPickerForDisplayItems:completionHandler:];
-[ASAccessorySession showPickerWithCompletionHandler:];
-[ASAccessorySession showPickerWithDisplayItems:completionHandler:];
-[ASAccessorySession updateAccessory:settings:completionHandler:];
-[ASAccessorySession updateAuthorization:descriptor:completionHandler:];
-[ASAccessorySession updatePickerShowingDiscoveredDisplayItems:completionHandler:];
```
