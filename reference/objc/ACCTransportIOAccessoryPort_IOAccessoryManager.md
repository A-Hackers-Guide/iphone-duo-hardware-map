# `ACCTransportIOAccessoryPort`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ACCTransportIOAccessoryBase`
- 9 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
^{__CFRunLoopSource=} _notificationRunLoopSource;
B _isAuthenticated;
i _portIDNumber;
i _portTransportType;
i _resistorID;
i _portStreamType;
@"<ACCTransportIOAccessoryPortProtocol>" _delegate;
@"NSString" _ioAccPortEndpointUUID;
@"NSString" _ioAccPortParentConnectionUUID;
```

## Properties

```
@property (T@"<ACCTransportIOAccessoryPortProtocol>",W,N,V_delegate) delegate;
@property (TB,N,V_isAuthenticated) isAuthenticated;
@property (Ti,R,N,V_portIDNumber) portIDNumber;
@property (Ti,R,N,V_portTransportType) portTransportType;
@property (Ti,R,N,V_resistorID) resistorID;
@property (Ti,R,N,V_portStreamType) portStreamType;
@property (T@"NSString",&,N,V_ioAccPortEndpointUUID) ioAccPortEndpointUUID;
@property (T@"NSString",W,N,V_ioAccPortParentConnectionUUID) ioAccPortParentConnectionUUID;
```

## Instance methods

```
-[ACCTransportIOAccessoryPort isAuthenticated];
-[ACCTransportIOAccessoryPort setIsAuthenticated:];
-[ACCTransportIOAccessoryPort dealloc];
-[ACCTransportIOAccessoryPort setDelegate:];
-[ACCTransportIOAccessoryPort resistorID];
-[ACCTransportIOAccessoryPort delegate];
-[ACCTransportIOAccessoryPort portServiceRegistrationComplete];
-[ACCTransportIOAccessoryPort _handleAccessoryPortDetach];
-[ACCTransportIOAccessoryPort _handleIncomingData:];
-[ACCTransportIOAccessoryPort _handlePropertyChange];
-[ACCTransportIOAccessoryPort _handleResistorIDChange:];
-[ACCTransportIOAccessoryPort _registerForIOAccessoryPortInterestNotifications];
-[ACCTransportIOAccessoryPort initWithDelegate:andIOService:];
-[ACCTransportIOAccessoryPort ioAccPortEndpointUUID];
-[ACCTransportIOAccessoryPort ioAccPortParentConnectionUUID];
-[ACCTransportIOAccessoryPort portIDNumber];
-[ACCTransportIOAccessoryPort portStreamType];
-[ACCTransportIOAccessoryPort portTransportType];
-[ACCTransportIOAccessoryPort setIoAccPortEndpointUUID:];
-[ACCTransportIOAccessoryPort setIoAccPortParentConnectionUUID:];
-[ACCTransportIOAccessoryPort transmitData:];
```
