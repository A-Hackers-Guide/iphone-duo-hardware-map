# `ACCTransportIOAccessoryConfigStream`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ACCTransportIOAccessoryBase`
- 17 instance variables, 17 properties, 50 instance methods, 0 class methods

## Instance variables

```
B _categoriesAvailable;
B _requestPending;
C _requestedPropertyID;
B _accInfoValid;
S _requestedCategoryID;
@"<ACCTransportIOAccessoryConfigStreamProtocol>" _delegate;
@"NSString" _deviceIdentifier;
@"NSString" _deviceName;
@"NSString" _deviceManufacturer;
@"NSString" _deviceModel;
@"NSString" _deviceHardwareVersion;
@"NSString" _deviceFirmwareVersion;
@"NSString" _deviceSerialNumber;
@"NSString" _devicePPID;
@"NSString" _endpointUUID;
@"NSString" _parentConnectionUUID;
@"NSObject<OS_dispatch_source>" _requestTimer;
```

## Properties

```
@property (T@"NSString",&,N,V_deviceIdentifier) deviceIdentifier;
@property (T@"NSString",&,N,V_deviceName) deviceName;
@property (T@"NSString",&,N,V_deviceManufacturer) deviceManufacturer;
@property (T@"NSString",&,N,V_deviceModel) deviceModel;
@property (T@"NSString",&,N,V_deviceHardwareVersion) deviceHardwareVersion;
@property (T@"NSString",&,N,V_deviceFirmwareVersion) deviceFirmwareVersion;
@property (T@"NSString",&,N,V_deviceSerialNumber) deviceSerialNumber;
@property (T@"NSString",&,N,V_devicePPID) devicePPID;
@property (TB,N,V_accInfoValid) accInfoValid;
@property (TB,N,V_requestPending) requestPending;
@property (TB,N,V_categoriesAvailable) categoriesAvailable;
@property (TS,N,V_requestedCategoryID) requestedCategoryID;
@property (TC,N,V_requestedPropertyID) requestedPropertyID;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_requestTimer) requestTimer;
@property (T@"<ACCTransportIOAccessoryConfigStreamProtocol>",W,N,V_delegate) delegate;
@property (T@"NSString",&,N,V_endpointUUID) endpointUUID;
@property (T@"NSString",W,N,V_parentConnectionUUID) parentConnectionUUID;
```

## Instance methods

```
-[ACCTransportIOAccessoryConfigStream deviceModel];
-[ACCTransportIOAccessoryConfigStream setDeviceIdentifier:];
-[ACCTransportIOAccessoryConfigStream setRequestPending:];
-[ACCTransportIOAccessoryConfigStream requestPending];
-[ACCTransportIOAccessoryConfigStream deviceSerialNumber];
-[ACCTransportIOAccessoryConfigStream dealloc];
-[ACCTransportIOAccessoryConfigStream setDelegate:];
-[ACCTransportIOAccessoryConfigStream deviceIdentifier];
-[ACCTransportIOAccessoryConfigStream setEndpointUUID:];
-[ACCTransportIOAccessoryConfigStream setDeviceName:];
-[ACCTransportIOAccessoryConfigStream deviceHardwareVersion];
-[ACCTransportIOAccessoryConfigStream endpointUUID];
-[ACCTransportIOAccessoryConfigStream delegate];
-[ACCTransportIOAccessoryConfigStream description];
-[ACCTransportIOAccessoryConfigStream setDeviceSerialNumber:];
-[ACCTransportIOAccessoryConfigStream setDeviceHardwareVersion:];
-[ACCTransportIOAccessoryConfigStream deviceName];
-[ACCTransportIOAccessoryConfigStream setDeviceModel:];
-[ACCTransportIOAccessoryConfigStream requestTimer];
-[ACCTransportIOAccessoryConfigStream setRequestTimer:];
-[ACCTransportIOAccessoryConfigStream deviceManufacturer];
-[ACCTransportIOAccessoryConfigStream setDeviceManufacturer:];
-[ACCTransportIOAccessoryConfigStream IOAccessoryConfigStreamCopyCategories];
-[ACCTransportIOAccessoryConfigStream IOAccessoryConfigStreamSetPropertyData:categoryID:propertyID:];
-[ACCTransportIOAccessoryConfigStream IOAccessoryConfigStreamCopyDataForCategoryID:propertyID:];
-[ACCTransportIOAccessoryConfigStream IOAccessoryConfigStreamRequestGetPropertyForCategoryID:propertyID:];
-[ACCTransportIOAccessoryConfigStream _getStringProperty:forCategory:];
-[ACCTransportIOAccessoryConfigStream _checkAccInfo];
-[ACCTransportIOAccessoryConfigStream _getCategories];
-[ACCTransportIOAccessoryConfigStream _getPropertyData:forCategory:];
-[ACCTransportIOAccessoryConfigStream _registerForInterestNotifications];
-[ACCTransportIOAccessoryConfigStream accInfoValid];
-[ACCTransportIOAccessoryConfigStream categoriesAvailable];
-[ACCTransportIOAccessoryConfigStream closeServiceSession];
-[ACCTransportIOAccessoryConfigStream deviceFirmwareVersion];
-[ACCTransportIOAccessoryConfigStream devicePPID];
-[ACCTransportIOAccessoryConfigStream handlePropertyDataReceived];
-[ACCTransportIOAccessoryConfigStream initWithDelegate:andIOService:];
-[ACCTransportIOAccessoryConfigStream openServiceSession];
-[ACCTransportIOAccessoryConfigStream parentConnectionUUID];
-[ACCTransportIOAccessoryConfigStream requestedCategoryID];
-[ACCTransportIOAccessoryConfigStream requestedPropertyID];
-[ACCTransportIOAccessoryConfigStream setAccInfoValid:];
-[ACCTransportIOAccessoryConfigStream setCategoriesAvailable:];
-[ACCTransportIOAccessoryConfigStream setDeviceFirmwareVersion:];
-[ACCTransportIOAccessoryConfigStream setDevicePPID:];
-[ACCTransportIOAccessoryConfigStream setParentConnectionUUID:];
-[ACCTransportIOAccessoryConfigStream setRequestedCategoryID:];
-[ACCTransportIOAccessoryConfigStream setRequestedPropertyID:];
-[ACCTransportIOAccessoryConfigStream transmitData:];
```
