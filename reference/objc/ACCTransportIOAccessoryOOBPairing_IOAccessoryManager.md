# `ACCTransportIOAccessoryOOBPairing`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ACCTransportIOAccessoryBase`
- 19 instance variables, 15 properties, 41 instance methods, 0 class methods

## Instance variables

```
* _oobPairingInfoReadBuffer;
Q _oobPairingInfoReadBufferLength;
* _oobPairingDataReadBuffer;
Q _oobPairingDataReadBufferLength;
i _activeType;
@"<ACCTransportIOAccessoryOOBPairingProtocol>" _delegate;
@"NSString" _deviceVendorName;
@"NSString" _deviceName;
@"NSString" _deviceModelNumber;
@"NSString" _deviceHardwareRevision;
@"NSString" _deviceFirmwareRevision;
@"NSString" _deviceSerialNumber;
@"NSString" _deviceDockType;
@"NSString" _deviceUID;
@"NSNumber" _devicePlatformID;
@"NSMutableData" _deviceSupportedTypes;
@"NSNumber" _supports2way;
@"NSString" _endpointUUID;
@"NSString" _parentConnectionUUID;
```

## Properties

```
@property (T@"NSString",&,N,V_deviceVendorName) deviceVendorName;
@property (T@"NSString",&,N,V_deviceName) deviceName;
@property (T@"NSString",&,N,V_deviceModelNumber) deviceModelNumber;
@property (T@"NSString",&,N,V_deviceHardwareRevision) deviceHardwareRevision;
@property (T@"NSString",&,N,V_deviceFirmwareRevision) deviceFirmwareRevision;
@property (T@"NSString",&,N,V_deviceSerialNumber) deviceSerialNumber;
@property (T@"NSString",&,N,V_deviceDockType) deviceDockType;
@property (T@"NSString",&,N,V_deviceUID) deviceUID;
@property (T@"NSNumber",&,N,V_devicePlatformID) devicePlatformID;
@property (T@"NSMutableData",&,N,V_deviceSupportedTypes) deviceSupportedTypes;
@property (Ti,N,V_activeType) activeType;
@property (T@"NSNumber",&,N,V_supports2way) supports2way;
@property (T@"<ACCTransportIOAccessoryOOBPairingProtocol>",W,N,V_delegate) delegate;
@property (T@"NSString",&,N,V_endpointUUID) endpointUUID;
@property (T@"NSString",W,N,V_parentConnectionUUID) parentConnectionUUID;
```

## Instance methods

```
-[ACCTransportIOAccessoryOOBPairing deviceUID];
-[ACCTransportIOAccessoryOOBPairing deviceSerialNumber];
-[ACCTransportIOAccessoryOOBPairing dealloc];
-[ACCTransportIOAccessoryOOBPairing setDeviceFirmwareRevision:];
-[ACCTransportIOAccessoryOOBPairing setDeviceHardwareRevision:];
-[ACCTransportIOAccessoryOOBPairing setDelegate:];
-[ACCTransportIOAccessoryOOBPairing setDeviceVendorName:];
-[ACCTransportIOAccessoryOOBPairing deviceFirmwareRevision];
-[ACCTransportIOAccessoryOOBPairing setDeviceUID:];
-[ACCTransportIOAccessoryOOBPairing setEndpointUUID:];
-[ACCTransportIOAccessoryOOBPairing setDeviceName:];
-[ACCTransportIOAccessoryOOBPairing endpointUUID];
-[ACCTransportIOAccessoryOOBPairing setDeviceModelNumber:];
-[ACCTransportIOAccessoryOOBPairing delegate];
-[ACCTransportIOAccessoryOOBPairing description];
-[ACCTransportIOAccessoryOOBPairing deviceHardwareRevision];
-[ACCTransportIOAccessoryOOBPairing setDeviceSerialNumber:];
-[ACCTransportIOAccessoryOOBPairing deviceName];
-[ACCTransportIOAccessoryOOBPairing deviceVendorName];
-[ACCTransportIOAccessoryOOBPairing supportsType:];
-[ACCTransportIOAccessoryOOBPairing deviceModelNumber];
-[ACCTransportIOAccessoryOOBPairing _checkAccInfo];
-[ACCTransportIOAccessoryOOBPairing _convertOOBPairingTypeFromIOAccessory:];
-[ACCTransportIOAccessoryOOBPairing _handleIncomingOOBPairingInfoData:];
-[ACCTransportIOAccessoryOOBPairing _registerReadCallback];
-[ACCTransportIOAccessoryOOBPairing activeType];
-[ACCTransportIOAccessoryOOBPairing closeServiceSession];
-[ACCTransportIOAccessoryOOBPairing deviceDockType];
-[ACCTransportIOAccessoryOOBPairing devicePlatformID];
-[ACCTransportIOAccessoryOOBPairing deviceSupportedTypes];
-[ACCTransportIOAccessoryOOBPairing initWithDelegate:andIOService:];
-[ACCTransportIOAccessoryOOBPairing openServiceSession];
-[ACCTransportIOAccessoryOOBPairing parentConnectionUUID];
-[ACCTransportIOAccessoryOOBPairing setActiveType:];
-[ACCTransportIOAccessoryOOBPairing setDeviceDockType:];
-[ACCTransportIOAccessoryOOBPairing setDevicePlatformID:];
-[ACCTransportIOAccessoryOOBPairing setDeviceSupportedTypes:];
-[ACCTransportIOAccessoryOOBPairing setParentConnectionUUID:];
-[ACCTransportIOAccessoryOOBPairing setSupports2way:];
-[ACCTransportIOAccessoryOOBPairing supports2way];
-[ACCTransportIOAccessoryOOBPairing transmitData:];
```
