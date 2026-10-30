# `ACCTransportIOAccessoryEA`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ACCTransportIOAccessoryBase`
- 14 instance variables, 12 properties, 32 instance methods, 0 class methods

## Instance variables

```
* _eaDataReadBuffer;
Q _eaDataReadBufferDataLength;
B _sessionOpen;
@"<ACCTransportIOAccessoryEAProtocol>" _delegate;
@"NSString" _eaProtocol;
@"NSString" _deviceVendorName;
@"NSString" _deviceName;
@"NSString" _deviceModelNumber;
@"NSString" _deviceHardwareRevision;
@"NSString" _deviceFirmwareRevision;
@"NSString" _deviceSerialNumber;
@"NSString" _deviceDockType;
@"NSString" _endpointUUID;
@"NSString" _parentConnectionUUID;
```

## Properties

```
@property (T@"NSString",&,N,V_eaProtocol) eaProtocol;
@property (T@"NSString",&,N,V_deviceVendorName) deviceVendorName;
@property (T@"NSString",&,N,V_deviceName) deviceName;
@property (T@"NSString",&,N,V_deviceModelNumber) deviceModelNumber;
@property (T@"NSString",&,N,V_deviceHardwareRevision) deviceHardwareRevision;
@property (T@"NSString",&,N,V_deviceFirmwareRevision) deviceFirmwareRevision;
@property (T@"NSString",&,N,V_deviceSerialNumber) deviceSerialNumber;
@property (T@"NSString",&,N,V_deviceDockType) deviceDockType;
@property (T@"<ACCTransportIOAccessoryEAProtocol>",W,N,V_delegate) delegate;
@property (T@"NSString",&,N,V_endpointUUID) endpointUUID;
@property (T@"NSString",W,N,V_parentConnectionUUID) parentConnectionUUID;
@property (TB,R,N,V_sessionOpen) sessionOpen;
```

## Instance methods

```
-[ACCTransportIOAccessoryEA deviceSerialNumber];
-[ACCTransportIOAccessoryEA dealloc];
-[ACCTransportIOAccessoryEA setDeviceFirmwareRevision:];
-[ACCTransportIOAccessoryEA setDeviceHardwareRevision:];
-[ACCTransportIOAccessoryEA setDelegate:];
-[ACCTransportIOAccessoryEA setDeviceVendorName:];
-[ACCTransportIOAccessoryEA deviceFirmwareRevision];
-[ACCTransportIOAccessoryEA setEndpointUUID:];
-[ACCTransportIOAccessoryEA setDeviceName:];
-[ACCTransportIOAccessoryEA endpointUUID];
-[ACCTransportIOAccessoryEA setDeviceModelNumber:];
-[ACCTransportIOAccessoryEA delegate];
-[ACCTransportIOAccessoryEA description];
-[ACCTransportIOAccessoryEA deviceHardwareRevision];
-[ACCTransportIOAccessoryEA setDeviceSerialNumber:];
-[ACCTransportIOAccessoryEA deviceName];
-[ACCTransportIOAccessoryEA deviceVendorName];
-[ACCTransportIOAccessoryEA deviceModelNumber];
-[ACCTransportIOAccessoryEA _checkEAInfo];
-[ACCTransportIOAccessoryEA _handleIncomingEAData];
-[ACCTransportIOAccessoryEA _registerEAReadCallback];
-[ACCTransportIOAccessoryEA closeEAServiceSession];
-[ACCTransportIOAccessoryEA deviceDockType];
-[ACCTransportIOAccessoryEA eaProtocol];
-[ACCTransportIOAccessoryEA initWithDelegate:andIOService:];
-[ACCTransportIOAccessoryEA openEAServiceSession];
-[ACCTransportIOAccessoryEA parentConnectionUUID];
-[ACCTransportIOAccessoryEA sessionOpen];
-[ACCTransportIOAccessoryEA setDeviceDockType:];
-[ACCTransportIOAccessoryEA setEaProtocol:];
-[ACCTransportIOAccessoryEA setParentConnectionUUID:];
-[ACCTransportIOAccessoryEA transmitData:];
```
