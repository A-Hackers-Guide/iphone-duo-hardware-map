# `AccessoryUSBBillboardDevice`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](../userland/System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 8 instance methods, 2 class methods

## Instance variables

```
Q _registryEntryID;
S _vid;
S _pid;
@"NSDictionary" _ioregProperties;
@"NSString" _identifier;
```

## Properties

```
@property (TQ,R,N,V_registryEntryID) registryEntryID;
@property (TS,R,N,V_vid) vid;
@property (TS,R,N,V_pid) pid;
@property (T@"NSDictionary",R,N,V_ioregProperties) ioregProperties;
@property (T@"NSString",R,N,V_identifier) identifier;
```

## Class methods

```
+[AccessoryUSBBillboardDevice getRegistryEntryIDFromService:];
+[AccessoryUSBBillboardDevice parentServiceVidPid:];
```

## Instance methods

```
-[AccessoryUSBBillboardDevice identifier];
-[AccessoryUSBBillboardDevice pid];
-[AccessoryUSBBillboardDevice initWithService:];
-[AccessoryUSBBillboardDevice vid];
-[AccessoryUSBBillboardDevice registryEntryID];
-[AccessoryUSBBillboardDevice ioregProperties];
-[AccessoryUSBBillboardDevice dismissNotSupportNotification];
-[AccessoryUSBBillboardDevice presentNotSupportNotification];
```
