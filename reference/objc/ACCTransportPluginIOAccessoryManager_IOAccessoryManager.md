# `ACCTransportPluginIOAccessoryManager`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ACCTransportPlugin`
- Protocols: `ACCTransportPluginProtocol`, `ACCPlatformUSBModePluginProtocol`, `ACCPlatformPowerPluginProtocol`, `ACCPlatformLightningPluginProtocol`
- 1 instance variables, 6 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _isRunning;
```

## Properties

```
@property (TB,N,V_isRunning) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
```

## Instance methods

```
-[ACCTransportPluginIOAccessoryManager isRunning];
-[ACCTransportPluginIOAccessoryManager setUSBCurrentOffset:forConnectionUUID:];
-[ACCTransportPluginIOAccessoryManager USBChargingVoltageInmV:];
-[ACCTransportPluginIOAccessoryManager USBCurrentLimitBaseInmA:];
-[ACCTransportPluginIOAccessoryManager setUSBMode:forEndpointUUID:];
-[ACCTransportPluginIOAccessoryManager resetAccessoryBaseCurrent:];
-[ACCTransportPluginIOAccessoryManager stopPlugin];
-[ACCTransportPluginIOAccessoryManager USBModeForConnectionUUID:];
-[ACCTransportPluginIOAccessoryManager authStatusDidChange:forConnectionWithUUID:previousAuthStatus:authType:connectionIsAuthenticated:connectionWasAuthenticated:];
-[ACCTransportPluginIOAccessoryManager _setHashOnFirstMagSafePortOverInductive:];
-[ACCTransportPluginIOAccessoryManager isPowerDuringSleepSupported:];
-[ACCTransportPluginIOAccessoryManager pluginName];
-[ACCTransportPluginIOAccessoryManager resetLightningBusForEndpointWithUUID:];
-[ACCTransportPluginIOAccessoryManager CableType:];
-[ACCTransportPluginIOAccessoryManager accessoryChargingCurrentInmA:];
-[ACCTransportPluginIOAccessoryManager sendOutgoingData:forEndpointWithUUID:connectionUUID:];
-[ACCTransportPluginIOAccessoryManager startPlugin];
-[ACCTransportPluginIOAccessoryManager USBModeForEndpointUUID:];
-[ACCTransportPluginIOAccessoryManager initPlugin];
-[ACCTransportPluginIOAccessoryManager USBCurrentLimitInmA:];
-[ACCTransportPluginIOAccessoryManager setUSBMode:forConnectionUUID:];
-[ACCTransportPluginIOAccessoryManager configureAccessoryPowerMode:forConnectionUUID:];
-[ACCTransportPluginIOAccessoryManager setBatteryPackMode:forConnectionUUID:forceResponse:];
-[ACCTransportPluginIOAccessoryManager setAccessoryUsedCurrent:forConnectionUUID:];
-[ACCTransportPluginIOAccessoryManager sleepPowerCurrentLimitInmA:];
-[ACCTransportPluginIOAccessoryManager USBCurrentLimitOffsetInmA:];
-[ACCTransportPluginIOAccessoryManager setUSBCurrentLimitBase:forConnectionUUID:forceResponse:];
-[ACCTransportPluginIOAccessoryManager isPowerDuringSleepEnabled:];
-[ACCTransportPluginIOAccessoryManager setIsRunning:];
-[ACCTransportPluginIOAccessoryManager setPowerDuringSleepEnabled:forConnectionUUID:];
-[ACCTransportPluginIOAccessoryManager accessoryPowerModeCurrentLimitInmA:forConnectionUUID:];
-[ACCTransportPluginIOAccessoryManager isBatteryPackModeEnabled:];
-[ACCTransportPluginIOAccessoryManager setAccessoryRequestedCurrent:forConnectionUUID:];
```
