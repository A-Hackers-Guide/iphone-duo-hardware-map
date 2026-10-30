# `ULLabelMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 13 properties, 1 instance methods, 3 class methods

## Properties

```
@property (T@"NSString",&,D,N) labelID;
@property (Td,D,N) receivedTimestamp;
@property (Ts,D,N) contextLayerType;
@property (Ts,D,N) deviceClass;
@property (T@"NSString",&,D,N) uuid;
@property (T@"ULScanningEventMO",&,D,N) scanningEvent;
@property (T@"ULServiceMO",&,D,N) service;
@property (T@"NSSet",&,D,N) mapLabels;
@property (T@"ULLoiMO",&,D,N) loi;
@property (T@"NSData",&,D,N) data;
@property (T@"NSDictionary",&,D,N) metadata;
@property (T@"NSString",&,D,N) serviceUUID_deprecated;
@property (T@"NSString",&,D,N) triggerUUID_deprecated;
```

## Class methods

```
+[ULLabelMO fetchRequest];
+[ULLabelMO createFromDO:withLoi:inManagedObjectContext:];
+[ULLabelMO createFromDO:withScanningEventMO:serviceMO:inManagedObjectContext:];
```

## Instance methods

```
-[ULLabelMO convertToDO];
```
