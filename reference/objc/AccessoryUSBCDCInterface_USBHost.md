# `AccessoryUSBCDCInterface`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](../userland/System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSString" _endpointUUID;
@"NSString" _eaSessionUUID;
I _cdcDataService;
I _usbService;
I _cdcConnect;
^{IONotificationPort=} _notiPort;
^{SerialPortInterface=II[30I]II[30I]IICC[118C]} arena;
* rxBuf;
* txBuf;
Q _deviceID;
@"NSString" _protocolName;
I _locationID;
Q _registryEntryID;
Q _parentDeviceRegistryEntryID;
@"NSDictionary" _ioregProperties;
@? _dataInHandler;
```

## Properties

```
@property (TQ,R,N,V_registryEntryID) registryEntryID;
@property (TI,R,N,V_locationID) locationID;
@property (TQ,R,N,V_parentDeviceRegistryEntryID) parentDeviceRegistryEntryID;
@property (T@"NSDictionary",R,N,V_ioregProperties) ioregProperties;
@property (T@?,C,N,V_dataInHandler) dataInHandler;
```

## Class methods

```
+[AccessoryUSBCDCInterface getRegistryEntryIDFromService:];
```

## Instance methods

```
-[AccessoryUSBCDCInterface init];
-[AccessoryUSBCDCInterface dealloc];
-[AccessoryUSBCDCInterface description];
-[AccessoryUSBCDCInterface writeData:];
-[AccessoryUSBCDCInterface registryEntryID];
-[AccessoryUSBCDCInterface locationID];
-[AccessoryUSBCDCInterface ioregProperties];
-[AccessoryUSBCDCInterface _handleReadDataCallback:revent:t_look:];
-[AccessoryUSBCDCInterface _poll:txCommitted:];
-[AccessoryUSBCDCInterface _processInterface:];
-[AccessoryUSBCDCInterface closeCDCInterface];
-[AccessoryUSBCDCInterface dataInHandler];
-[AccessoryUSBCDCInterface initWithInterface:protocol:endpointUUID:andDataInHandler:];
-[AccessoryUSBCDCInterface openCDCInterface];
-[AccessoryUSBCDCInterface parentDeviceRegistryEntryID];
-[AccessoryUSBCDCInterface setDataInHandler:];
-[AccessoryUSBCDCInterface shuttingDownSession];
```
