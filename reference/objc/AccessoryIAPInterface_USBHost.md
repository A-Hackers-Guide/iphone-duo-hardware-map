# `AccessoryIAPInterface`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](../userland/System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 29 instance variables, 29 properties, 64 instance methods, 1 class methods

## Instance variables

```
B _needOutZLP;
C _bulkOutPipeRef;
C _bulkInPipeRef;
C _interruptInPipeRef;
B _hasReadInterruptPipe;
B _interfaceConfigured;
S _vid;
S _pid;
S _bulkOutPipeMaxPacketSize;
S _bulkInPipeMaxPacketSize;
S _interruptInPipeMaxPacketSize;
I _locationID;
I _maxOutLength;
I _vidpid;
I _interruptBulkReadAllocCount;
I _interruptBulkReadReleaseCount;
Q _registryEntryID;
Q _parentDeviceRegistryEntryID;
@"NSDictionary" _ioregProperties;
@? _dataInHandler;
d _creationTime;
@"NSString" _identifier;
@"NSDictionary" _aidInfo;
^^{IOUSBInterfaceStruct942} _interface;
* _interruptInPipeBuffer;
@"NSMutableArray" _interfacePropertiesArray;
@"NSMutableArray" _inUseDataBufArray;
@"NSLock" _dataBufLock;
@"NSMutableArray" _interruptBulkReadList;
```

## Properties

```
@property (T^^{IOUSBInterfaceStruct942},N,V_interface) interface;
@property (TC,N,V_bulkOutPipeRef) bulkOutPipeRef;
@property (TS,N,V_bulkOutPipeMaxPacketSize) bulkOutPipeMaxPacketSize;
@property (TC,N,V_bulkInPipeRef) bulkInPipeRef;
@property (TS,N,V_bulkInPipeMaxPacketSize) bulkInPipeMaxPacketSize;
@property (TC,N,V_interruptInPipeRef) interruptInPipeRef;
@property (TS,N,V_interruptInPipeMaxPacketSize) interruptInPipeMaxPacketSize;
@property (T*,N,V_interruptInPipeBuffer) interruptInPipeBuffer;
@property (T@"NSMutableArray",&,N,V_interfacePropertiesArray) interfacePropertiesArray;
@property (T@"NSMutableArray",&,N,V_inUseDataBufArray) inUseDataBufArray;
@property (T@"NSLock",&,N,V_dataBufLock) dataBufLock;
@property (TB,N,V_hasReadInterruptPipe) hasReadInterruptPipe;
@property (T@"NSMutableArray",&,N,V_interruptBulkReadList) interruptBulkReadList;
@property (TI,N,V_interruptBulkReadAllocCount) interruptBulkReadAllocCount;
@property (TI,N,V_interruptBulkReadReleaseCount) interruptBulkReadReleaseCount;
@property (TB,N,V_interfaceConfigured) interfaceConfigured;
@property (TQ,R,N,V_registryEntryID) registryEntryID;
@property (TI,R,N,V_locationID) locationID;
@property (TQ,R,N,V_parentDeviceRegistryEntryID) parentDeviceRegistryEntryID;
@property (T@"NSDictionary",R,N,V_ioregProperties) ioregProperties;
@property (T@?,C,N,V_dataInHandler) dataInHandler;
@property (TB,N,V_needOutZLP) needOutZLP;
@property (TI,N,V_maxOutLength) maxOutLength;
@property (TS,R,N,V_vid) vid;
@property (TS,R,N,V_pid) pid;
@property (TI,R,N,V_vidpid) vidpid;
@property (Td,R,N,V_creationTime) creationTime;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSDictionary",&,N,V_aidInfo) aidInfo;
```

## Class methods

```
+[AccessoryIAPInterface getRegistryEntryIDFromService:];
```

## Instance methods

```
-[AccessoryIAPInterface creationTime];
-[AccessoryIAPInterface identifier];
-[AccessoryIAPInterface dealloc];
-[AccessoryIAPInterface setInterface:];
-[AccessoryIAPInterface pid];
-[AccessoryIAPInterface interface];
-[AccessoryIAPInterface description];
-[AccessoryIAPInterface writeData:];
-[AccessoryIAPInterface vid];
-[AccessoryIAPInterface registryEntryID];
-[AccessoryIAPInterface locationID];
-[AccessoryIAPInterface aidInfo];
-[AccessoryIAPInterface ioregProperties];
-[AccessoryIAPInterface setInterruptBulkReadAllocCount:];
-[AccessoryIAPInterface setDataBufLock:];
-[AccessoryIAPInterface bulkInPipeMaxPacketSize];
-[AccessoryIAPInterface bulkInPipeRef];
-[AccessoryIAPInterface bulkOutPipeMaxPacketSize];
-[AccessoryIAPInterface bulkOutPipeRef];
-[AccessoryIAPInterface clearUSBHostHIDInterfaces];
-[AccessoryIAPInterface configureInterface:skipPipeSetup:];
-[AccessoryIAPInterface configureNCMInterface:asCarPlay:];
-[AccessoryIAPInterface dataBufLock];
-[AccessoryIAPInterface dataInHandler];
-[AccessoryIAPInterface dismissNotSupportNotification];
-[AccessoryIAPInterface hasReadInterruptPipe];
-[AccessoryIAPInterface inUseDataBufArray];
-[AccessoryIAPInterface initWithInterface:andDataInHandler:];
-[AccessoryIAPInterface initWithInterface:vid:pid:aidInfo:andDataInHandler:];
-[AccessoryIAPInterface interfaceConfigured];
-[AccessoryIAPInterface interfacePropertiesArray];
-[AccessoryIAPInterface interruptBulkReadAllocCount];
-[AccessoryIAPInterface interruptBulkReadList];
-[AccessoryIAPInterface interruptBulkReadReleaseCount];
-[AccessoryIAPInterface interruptInPipeBuffer];
-[AccessoryIAPInterface interruptInPipeMaxPacketSize];
-[AccessoryIAPInterface interruptInPipeRef];
-[AccessoryIAPInterface lockOtherInterfaces];
-[AccessoryIAPInterface maxOutLength];
-[AccessoryIAPInterface needOutZLP];
-[AccessoryIAPInterface parentDeviceRegistryEntryID];
-[AccessoryIAPInterface presentNotSupportNotification];
-[AccessoryIAPInterface setAidInfo:];
-[AccessoryIAPInterface setBulkInPipeMaxPacketSize:];
-[AccessoryIAPInterface setBulkInPipeRef:];
-[AccessoryIAPInterface setBulkOutPipeMaxPacketSize:];
-[AccessoryIAPInterface setBulkOutPipeRef:];
-[AccessoryIAPInterface setDataInHandler:];
-[AccessoryIAPInterface setHasReadInterruptPipe:];
-[AccessoryIAPInterface setInUseDataBufArray:];
-[AccessoryIAPInterface setInterfaceConfigured:];
-[AccessoryIAPInterface setInterfaceProperties:];
-[AccessoryIAPInterface setInterfacePropertiesArray:];
-[AccessoryIAPInterface setInterruptBulkReadList:];
-[AccessoryIAPInterface setInterruptBulkReadReleaseCount:];
-[AccessoryIAPInterface setInterruptInPipeBuffer:];
-[AccessoryIAPInterface setInterruptInPipeMaxPacketSize:];
-[AccessoryIAPInterface setInterruptInPipeRef:];
-[AccessoryIAPInterface setMaxOutLength:];
-[AccessoryIAPInterface setNeedOutZLP:];
-[AccessoryIAPInterface setProperty:forInterfaceNum:];
-[AccessoryIAPInterface setUSBHostHIDInterface:withHIDFunction:];
-[AccessoryIAPInterface unlockOtherInterfaces];
-[AccessoryIAPInterface vidpid];
```
