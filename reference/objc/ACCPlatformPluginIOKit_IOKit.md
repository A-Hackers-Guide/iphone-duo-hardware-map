# `ACCPlatformPluginIOKit`

- Image: [`/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit`](../userland/System__Library__CoreAccessories__PlugIns__Platform__IOKit.platform__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCPlatformUSBFaultPluginProtocol`, `ACCPlatformUSBCableTypePluginProtocol`, `ACCPlatformIOKitPowerPluginProtocol`, `ACCPlatformUSBCameraKitHubPluginProtocol`, `ACCPlatformSleepAssertionPluginProtocol`
- 2 instance variables, 7 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _isRunning;
@"USBFaultMonitor" _monitor;
```

## Properties

```
@property (TB,N,V_isRunning) isRunning;
@property (T@"USBFaultMonitor",&,N,V_monitor) monitor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
```

## Instance methods

```
-[ACCPlatformPluginIOKit monitor];
-[ACCPlatformPluginIOKit isRunning];
-[ACCPlatformPluginIOKit setMonitor:];
-[ACCPlatformPluginIOKit stopPlugin];
-[ACCPlatformPluginIOKit pluginName];
-[ACCPlatformPluginIOKit startPlugin];
-[ACCPlatformPluginIOKit initPlugin];
-[ACCPlatformPluginIOKit setIsRunning:];
-[ACCPlatformPluginIOKit createBatteryNotificationClient];
-[ACCPlatformPluginIOKit removeApplePencilSleepAssertion];
-[ACCPlatformPluginIOKit clientHandledSleepNotification:];
-[ACCPlatformPluginIOKit createApplePencilSleepAssertion];
-[ACCPlatformPluginIOKit createEASleepAssertion];
-[ACCPlatformPluginIOKit createMFi4SleepAssertion];
-[ACCPlatformPluginIOKit createSleepAssertionForUUID:];
-[ACCPlatformPluginIOKit createSleepNotificationClient];
-[ACCPlatformPluginIOKit destroyBatteryNotificationsForClient:];
-[ACCPlatformPluginIOKit destroySleepAssertionForUUID:];
-[ACCPlatformPluginIOKit destroySleepNotificationsForClient:];
-[ACCPlatformPluginIOKit getBatteryChargeLevel];
-[ACCPlatformPluginIOKit getBatteryChargingState];
-[ACCPlatformPluginIOKit getBatteryChargingType];
-[ACCPlatformPluginIOKit getBatteryChargingTypeIsInductive];
-[ACCPlatformPluginIOKit getExternalBatteryChargingType];
-[ACCPlatformPluginIOKit getExternalBatteryChargingTypeIsInductive];
-[ACCPlatformPluginIOKit getUSBFaultStateforType:];
-[ACCPlatformPluginIOKit getUSBHubOverCurrentState:];
-[ACCPlatformPluginIOKit getUSBHubSiphoningCurrentActualRequirementInmA:];
-[ACCPlatformPluginIOKit getUSBHubSiphoningCurrentRequirementInmA:];
-[ACCPlatformPluginIOKit getUSBHubUnitLoadInmA:];
-[ACCPlatformPluginIOKit initUSBCameraKitHubNotifications:];
-[ACCPlatformPluginIOKit isExternalChargerConnected];
-[ACCPlatformPluginIOKit removeEASleepAssertion];
-[ACCPlatformPluginIOKit removeMFi4SleepAssertion];
-[ACCPlatformPluginIOKit resetUSBHubOverCurrentSiphoning:];
-[ACCPlatformPluginIOKit setUSBHubOverCurrentSiphoning:];
-[ACCPlatformPluginIOKit usbCableTypeMonitor:forUUID:];
-[ACCPlatformPluginIOKit usbFaultMonitor:forUUID:];
```
