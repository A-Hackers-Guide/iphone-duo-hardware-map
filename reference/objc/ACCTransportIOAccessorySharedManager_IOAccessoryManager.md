# `ACCTransportIOAccessorySharedManager`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCTransportIOAccessoryListenerProtocol`, `ACCTransportIOAccessoryManagerProtocol`, `ACCTransportIOAccessoryPortProtocol`, `ACCTransportIOAccessoryAuthCPProtocol`, `ACCTransportIOAccessoryEAProtocol`, `ACCTransportIOAccessoryOOBPairingProtocol`, `ACCTransportIOAccessoryConfigStreamProtocol`
- 14 instance variables, 18 properties, 127 instance methods, 3 class methods

## Instance variables

```
B _isB139OrB164Connected;
B _bIsWatch;
@"ACCTransportPluginIOAccessoryManager" _delegate;
@"NSObject<OS_dispatch_queue>" _listQ;
@"NSMutableSet" _allIOAccessories;
@"NSMutableSet" _allIOAccessoryManagers;
@"NSMutableSet" _rootIOAccessoryManagers;
@"ACCTransportIOAccessoryListener" _ioAccessoryListener;
@"ACCTransportIOAccessoryManager" _rootE75Manager;
@"ACCTransportIOAccessoryManager" _rootOrionManager;
@"NSRecursiveLock" _accessoryPortLock;
@"ACCSettingsState" _enableDirectAWCAuth;
@"NSMutableArray" _deferAuthCPServiceArray;
@"NSMutableArray" _deferEAServiceArray;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_listQ) listQ;
@property (T@"NSMutableSet",&,N,V_allIOAccessories) allIOAccessories;
@property (T@"NSMutableSet",&,N,V_allIOAccessoryManagers) allIOAccessoryManagers;
@property (T@"NSMutableSet",&,N,V_rootIOAccessoryManagers) rootIOAccessoryManagers;
@property (T@"ACCTransportIOAccessoryListener",&,N,V_ioAccessoryListener) ioAccessoryListener;
@property (T@"ACCTransportIOAccessoryManager",R,N,V_rootE75Manager) rootE75Manager;
@property (T@"ACCTransportIOAccessoryManager",R,N,V_rootOrionManager) rootOrionManager;
@property (T@"NSRecursiveLock",&,N,V_accessoryPortLock) accessoryPortLock;
@property (T@"ACCSettingsState",&,N,V_enableDirectAWCAuth) enableDirectAWCAuth;
@property (TB,R,N,V_bIsWatch) bIsWatch;
@property (T@"NSMutableArray",&,N,V_deferAuthCPServiceArray) deferAuthCPServiceArray;
@property (T@"NSMutableArray",&,N,V_deferEAServiceArray) deferEAServiceArray;
@property (T@"ACCTransportPluginIOAccessoryManager",W,N,V_delegate) delegate;
@property (TB,R,N,V_isB139OrB164Connected) isB139OrB164Connected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ACCTransportIOAccessorySharedManager sharedManager];
+[ACCTransportIOAccessorySharedManager IOAccessoryClassStringForIOAccessoryClassType:];
+[ACCTransportIOAccessorySharedManager IOAccessoryClassTypeForIOAccessoryClassString:];
```

## Instance methods

```
-[ACCTransportIOAccessorySharedManager setProperties:forManager:];
-[ACCTransportIOAccessorySharedManager _basePortForEndpointUUID:];
-[ACCTransportIOAccessorySharedManager rootOrionManager];
-[ACCTransportIOAccessorySharedManager handleOOBPairingEarlyInfoNotification:];
-[ACCTransportIOAccessorySharedManager setDeferAuthCPServiceArray:];
-[ACCTransportIOAccessorySharedManager IOAccessoryConfigStreamServiceTerminated:];
-[ACCTransportIOAccessorySharedManager setUSBCurrentOffset:forConnectionUUID:];
-[ACCTransportIOAccessorySharedManager USBChargingVoltageInmV:];
-[ACCTransportIOAccessorySharedManager IOAccessoryManagerServiceInfoSet:];
-[ACCTransportIOAccessorySharedManager _managerContainingBase:];
-[ACCTransportIOAccessorySharedManager IOAccessoryConfigStreamServiceArrived:];
-[ACCTransportIOAccessorySharedManager IOAccessoryManagerServiceDetached:];
-[ACCTransportIOAccessorySharedManager USBCurrentLimitBaseInmA:];
-[ACCTransportIOAccessorySharedManager handleOpenEASessionNotification:];
-[ACCTransportIOAccessorySharedManager _createEAEndpointForProtocol:andManager:];
-[ACCTransportIOAccessorySharedManager connectedThroughAdapter:];
-[ACCTransportIOAccessorySharedManager startIOACCTransportManager];
-[ACCTransportIOAccessorySharedManager IOAccessoryPortServiceTerminated:];
-[ACCTransportIOAccessorySharedManager closeEASession:];
-[ACCTransportIOAccessorySharedManager IOAccessoryPortDataArrived:endpointUUID:];
-[ACCTransportIOAccessorySharedManager setUSBMode:forEndpointUUID:];
-[ACCTransportIOAccessorySharedManager bIsWatch];
-[ACCTransportIOAccessorySharedManager deferEAServiceArray];
-[ACCTransportIOAccessorySharedManager _clearChildPortEndpointsForManagerDisconnection:];
-[ACCTransportIOAccessorySharedManager _managerForBase:];
-[ACCTransportIOAccessorySharedManager init];
-[ACCTransportIOAccessorySharedManager resetAccessoryBaseCurrent:];
-[ACCTransportIOAccessorySharedManager USBModeForConnectionUUID:];
-[ACCTransportIOAccessorySharedManager isB139OrB164Connected];
-[ACCTransportIOAccessorySharedManager dealloc];
-[ACCTransportIOAccessorySharedManager isPowerDuringSleepSupported:];
-[ACCTransportIOAccessorySharedManager _handleUSBHostPluginArrived:];
-[ACCTransportIOAccessorySharedManager _connectionWithUUIDHasActiveEndpoint:];
-[ACCTransportIOAccessorySharedManager IOAccessoryConfigStreamUpdateAccesssoryInfo:];
-[ACCTransportIOAccessorySharedManager _endpointTransportTypeForIOAccessoryPort:];
-[ACCTransportIOAccessorySharedManager IOAccessoryPortDetach:];
-[ACCTransportIOAccessorySharedManager resetLightningBusForEndpointWithUUID:];
-[ACCTransportIOAccessorySharedManager _shouldAllowDeviceSettings:];
-[ACCTransportIOAccessorySharedManager allIOAccessoryManagers];
-[ACCTransportIOAccessorySharedManager CableType:];
-[ACCTransportIOAccessorySharedManager accessoryChargingCurrentInmA:];
-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingServiceArrived:];
-[ACCTransportIOAccessorySharedManager managerForIOAccessoryManagerService:];
-[ACCTransportIOAccessorySharedManager _processDeferredEAServicesForManager:];
-[ACCTransportIOAccessorySharedManager USBModeForEndpointUUID:];
-[ACCTransportIOAccessorySharedManager USBCurrentLimitInmA:];
-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingDataStartedForEndpointUUID:];
-[ACCTransportIOAccessorySharedManager _handleRequestForIAPDPortB139B164Connected:];
-[ACCTransportIOAccessorySharedManager _portForManagerMatchingPrimaryPort:];
-[ACCTransportIOAccessorySharedManager _createBLEPairingEndpointForManager:publish:];
-[ACCTransportIOAccessorySharedManager rootIOAccessoryManagers];
-[ACCTransportIOAccessorySharedManager _IOAccessoryPortDetachInternal:];
-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingDataArrived:endpointUUID:];
-[ACCTransportIOAccessorySharedManager allIOAccessories];
-[ACCTransportIOAccessorySharedManager unlockAccessoryPorts];
-[ACCTransportIOAccessorySharedManager setDelegate:];
-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingInfoArrived:endpointUUID:];
-[ACCTransportIOAccessorySharedManager _managerForBaseEndpointUUID:];
-[ACCTransportIOAccessorySharedManager setUSBMode:forConnectionUUID:];
-[ACCTransportIOAccessorySharedManager _accPlatformPowerModeToIOAccessoryPowerMode:];
-[ACCTransportIOAccessorySharedManager _managerForInductiveOOBPairingEndpointUUID:];
-[ACCTransportIOAccessorySharedManager handleCloseEASessionNotification:];
-[ACCTransportIOAccessorySharedManager listQ];
-[ACCTransportIOAccessorySharedManager shouldEnableDirectAWCAuth];
-[ACCTransportIOAccessorySharedManager setListQ:];
-[ACCTransportIOAccessorySharedManager IOAccessoryPortPublish:];
-[ACCTransportIOAccessorySharedManager accessoryPortLock];
-[ACCTransportIOAccessorySharedManager _addIOAccessoryManagerWithIOService:];
-[ACCTransportIOAccessorySharedManager enableDirectAWCAuth];
-[ACCTransportIOAccessorySharedManager _processEAService:andPublish:];
-[ACCTransportIOAccessorySharedManager IOAccessoryManagerServiceArrived:];
-[ACCTransportIOAccessorySharedManager configureAccessoryPowerMode:forConnectionUUID:];
-[ACCTransportIOAccessorySharedManager deferAuthCPServiceArray];
-[ACCTransportIOAccessorySharedManager setRootIOAccessoryManagers:];
-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingDataFinishedForEndpointUUID:];
-[ACCTransportIOAccessorySharedManager delegate];
-[ACCTransportIOAccessorySharedManager _connectionTypeForIOAccessoryPort:];
-[ACCTransportIOAccessorySharedManager stopIOACCTransportManager];
-[ACCTransportIOAccessorySharedManager setBatteryPackMode:forConnectionUUID:forceResponse:];
-[ACCTransportIOAccessorySharedManager setAccessoryUsedCurrent:forConnectionUUID:];
-[ACCTransportIOAccessorySharedManager _managerForConnectionUUID:];
-[ACCTransportIOAccessorySharedManager setIoAccessoryListener:];
-[ACCTransportIOAccessorySharedManager sleepPowerCurrentLimitInmA:];
-[ACCTransportIOAccessorySharedManager lockAccessoryPorts];
-[ACCTransportIOAccessorySharedManager _managerForIOService:shouldCreateNewService:];
-[ACCTransportIOAccessorySharedManager IOAccessoryManagerServiceTerminated:];
-[ACCTransportIOAccessorySharedManager digitalIDDataForUpstreamConnection:];
-[ACCTransportIOAccessorySharedManager _handleInductiveOOBPairingTransmitData:forEndpointUUID:manager:];
-[ACCTransportIOAccessorySharedManager ioAccessoryListener];
-[ACCTransportIOAccessorySharedManager setAccessoryPortLock:];
-[ACCTransportIOAccessorySharedManager transmitData:forEndpointUUID:];
-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceAuthStatusChanged:authType:authCert:certType:authCTA:service:];
-[ACCTransportIOAccessorySharedManager setDeferEAServiceArray:];
-[ACCTransportIOAccessorySharedManager openEASession:withEAEndpointUUID:];
-[ACCTransportIOAccessorySharedManager IOAccessoryPortArrived:withEndpointProtocol:publish:];
-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:];
-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:];
-[ACCTransportIOAccessorySharedManager _createModuleConnectionAndEndpoint:];
-[ACCTransportIOAccessorySharedManager setEnableDirectAWCAuth:];
-[ACCTransportIOAccessorySharedManager basePortForService:];
-[ACCTransportIOAccessorySharedManager USBCurrentLimitOffsetInmA:];
-[ACCTransportIOAccessorySharedManager _addACCTransportToManager:];
-[ACCTransportIOAccessorySharedManager _handleRequestForPrimaryPort:];
-[ACCTransportIOAccessorySharedManager setFeaturesFromAuthStatus:andAuthCert:certType:forConnectionUUID:withConnectionType:];
-[ACCTransportIOAccessorySharedManager setUSBCurrentLimitBase:forConnectionUUID:forceResponse:];
-[ACCTransportIOAccessorySharedManager isPowerDuringSleepEnabled:];
-[ACCTransportIOAccessorySharedManager IOAccessoryEAServiceArrived:];
-[ACCTransportIOAccessorySharedManager _createEAProtocolsForManager:];
-[ACCTransportIOAccessorySharedManager IOAccessoryManagerSupervisedTransportsRestrictedDidChange:forManager:];
-[ACCTransportIOAccessorySharedManager _blePairingTransportTypeForConnectionType:];
-[ACCTransportIOAccessorySharedManager setPowerDuringSleepEnabled:forConnectionUUID:];
-[ACCTransportIOAccessorySharedManager IOAccessoryEAServiceTerminated:];
-[ACCTransportIOAccessorySharedManager setAllIOAccessoryManagers:];
-[ACCTransportIOAccessorySharedManager accessoryPowerModeCurrentLimitInmA:forConnectionUUID:];
-[ACCTransportIOAccessorySharedManager isBatteryPackModeEnabled:];
-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingServiceTerminated:];
-[ACCTransportIOAccessorySharedManager IOAccessoryEADataArrived:eaEndpointUUID:];
-[ACCTransportIOAccessorySharedManager processDeferredEAServicesForConnectionUUID:];
-[ACCTransportIOAccessorySharedManager IOAccessoryPortPropertyChanged:];
-[ACCTransportIOAccessorySharedManager IOAccessoryConfigStreamMessageArrived:endpointUUID:];
-[ACCTransportIOAccessorySharedManager _destroyBLEPairingEndpointForManager:];
-[ACCTransportIOAccessorySharedManager IOAccessoryManagerResistorIDChanged:forManager:];
-[ACCTransportIOAccessorySharedManager IOAccessoryPortServiceArrived:];
-[ACCTransportIOAccessorySharedManager setAllIOAccessories:];
-[ACCTransportIOAccessorySharedManager rootE75Manager];
-[ACCTransportIOAccessorySharedManager _basePortForConnectionUUID:];
-[ACCTransportIOAccessorySharedManager setAccessoryRequestedCurrent:forConnectionUUID:];
```
