# `AccessoryTransportPluginUSBHost`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](../userland/System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ACCTransportPlugin`
- Protocols: `ACCTransportPluginProtocol`, `ACCPlatformUSBHostPluginProtocol`, `ACCPlatformUSBBillboardDevicePluginProtocol`
- 18 instance variables, 16 properties, 48 instance methods, 1 class methods

## Instance variables

```
^{IONotificationPort=} _iokitNotifyPort;
I _iokitAddedIterator;
I _iokitRemovedIterator;
I temp;
^{IONotificationPort=} _iokitVIDPIDNotifyPort;
I _iokitVIDPIDAddedIterator;
I _iokitVIDPIDRemovedIterator;
B _isRunning;
@"NSMutableDictionary" _accessoryConnections;
@"NSMutableDictionary" _accessoryNativeUSBEndpoints;
@"NSMutableDictionary" _activeEAInterfaces;
@"NSMutableDictionary" _activeUSBCDCInterfaces;
@"NSObject<OS_dispatch_queue>" _accessoryConnectionsLock;
@"NSObject<OS_dispatch_queue>" _activeEAInterfacesLock;
@"NSObject<OS_dispatch_queue>" _accessoryNativeUSBEndpointsLock;
q _accessoryiAPIntefaceTrafficWaitListCount;
@"NSMutableDictionary" _accessoryiAPIntefaceTrafficWaitList;
@"NSObject<OS_dispatch_source>" _accessoryiAPIntefaceTrafficTimer;
```

## Properties

```
@property (TB,N,V_isRunning) isRunning;
@property (T@"NSMutableDictionary",&,N,V_accessoryConnections) accessoryConnections;
@property (T@"NSMutableDictionary",&,N,V_accessoryNativeUSBEndpoints) accessoryNativeUSBEndpoints;
@property (T@"NSMutableDictionary",&,N,V_activeEAInterfaces) activeEAInterfaces;
@property (T@"NSMutableDictionary",&,N,V_activeUSBCDCInterfaces) activeUSBCDCInterfaces;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_accessoryConnectionsLock) accessoryConnectionsLock;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_activeEAInterfacesLock) activeEAInterfacesLock;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_accessoryNativeUSBEndpointsLock) accessoryNativeUSBEndpointsLock;
@property (Tq,N,V_accessoryiAPIntefaceTrafficWaitListCount) accessoryiAPIntefaceTrafficWaitListCount;
@property (T@"NSMutableDictionary",&,N,V_accessoryiAPIntefaceTrafficWaitList) accessoryiAPIntefaceTrafficWaitList;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_accessoryiAPIntefaceTrafficTimer) accessoryiAPIntefaceTrafficTimer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
```

## Class methods

```
+[AccessoryTransportPluginUSBHost _createVIDPIDMatchingDictionary];
```

## Instance methods

```
-[AccessoryTransportPluginUSBHost isRunning];
-[AccessoryTransportPluginUSBHost stopPlugin];
-[AccessoryTransportPluginUSBHost pluginName];
-[AccessoryTransportPluginUSBHost sendOutgoingData:forEndpointWithUUID:connectionUUID:];
-[AccessoryTransportPluginUSBHost startPlugin];
-[AccessoryTransportPluginUSBHost initPlugin];
-[AccessoryTransportPluginUSBHost setIsRunning:];
-[AccessoryTransportPluginUSBHost serviceRemoved:];
-[AccessoryTransportPluginUSBHost setAccessoryNativeUSBEndpoints:];
-[AccessoryTransportPluginUSBHost accessoryNativeUSBEndpointsLock];
-[AccessoryTransportPluginUSBHost VIDPIDServiceAdded:];
-[AccessoryTransportPluginUSBHost VIDPIDServiceRemoved:];
-[AccessoryTransportPluginUSBHost _handleCloseEASessionNotificationForEndpoint:connection:];
-[AccessoryTransportPluginUSBHost _handleOpenEASessionNotificationForEndpoint:connection:];
-[AccessoryTransportPluginUSBHost _handleOpenSocketFromAccessoryToAppNotification:];
-[AccessoryTransportPluginUSBHost _handleOpenSocketFromAppToAccessoryNotification:];
-[AccessoryTransportPluginUSBHost accessoryConnections];
-[AccessoryTransportPluginUSBHost accessoryConnectionsLock];
-[AccessoryTransportPluginUSBHost accessoryNativeUSBEndpoints];
-[AccessoryTransportPluginUSBHost accessoryiAPIntefaceTrafficTimer];
-[AccessoryTransportPluginUSBHost accessoryiAPIntefaceTrafficWaitList];
-[AccessoryTransportPluginUSBHost accessoryiAPIntefaceTrafficWaitListCount];
-[AccessoryTransportPluginUSBHost activeEAInterfaces];
-[AccessoryTransportPluginUSBHost activeEAInterfacesLock];
-[AccessoryTransportPluginUSBHost activeUSBCDCInterfaces];
-[AccessoryTransportPluginUSBHost clearUSBHostHIDInterfacesForConnectionUUID:];
-[AccessoryTransportPluginUSBHost configureIOKit];
-[AccessoryTransportPluginUSBHost configureIOKitVIDPID];
-[AccessoryTransportPluginUSBHost configureUSBHostNCMInterface:asCarPlay:forConnectionUUID:];
-[AccessoryTransportPluginUSBHost lockUSBHostInterfacesForConnectionUUID:];
-[AccessoryTransportPluginUSBHost serviceAdded:];
-[AccessoryTransportPluginUSBHost setAccessoryConnections:];
-[AccessoryTransportPluginUSBHost setAccessoryConnectionsLock:];
-[AccessoryTransportPluginUSBHost setAccessoryNativeUSBEndpointsLock:];
-[AccessoryTransportPluginUSBHost setAccessoryiAPIntefaceTrafficTimer:];
-[AccessoryTransportPluginUSBHost setAccessoryiAPIntefaceTrafficWaitList:];
-[AccessoryTransportPluginUSBHost setAccessoryiAPIntefaceTrafficWaitListCount:];
-[AccessoryTransportPluginUSBHost setActiveEAInterfaces:];
-[AccessoryTransportPluginUSBHost setActiveEAInterfacesLock:];
-[AccessoryTransportPluginUSBHost setActiveUSBCDCInterfaces:];
-[AccessoryTransportPluginUSBHost setNeedOutZLP:maxOutLength:forConnectionUUID:];
-[AccessoryTransportPluginUSBHost setUSBHostHIDInterface:withHIDFunction:forConnectionUUID:];
-[AccessoryTransportPluginUSBHost startConfiguringIOKit];
-[AccessoryTransportPluginUSBHost startDetectUSBBillboardDeviceWithVID:PID:];
-[AccessoryTransportPluginUSBHost stopDetectUSBBillboardDeviceWithVID:PID:];
-[AccessoryTransportPluginUSBHost tearDownIOKit];
-[AccessoryTransportPluginUSBHost tearDownIOKitVIDPID];
-[AccessoryTransportPluginUSBHost unlockUSBHostInterfacesForConnectionUUID:];
```
