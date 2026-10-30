# `ULBluetoothIdentityMO`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 4 properties, 1 instance methods, 2 class methods

## Properties

```
@property (T@"NSString",&,D,N) bluetoothId;
@property (T@"NSString",&,D,N) deviceName;
@property (Td,D,N) lastSeenTimeStamp;
@property (T@"NSString",&,D,N) stableIdentifier;
```

## Class methods

```
+[ULBluetoothIdentityMO fetchRequest];
+[ULBluetoothIdentityMO createFromDO:inManagedObjectContext:];
```

## Instance methods

```
-[ULBluetoothIdentityMO convertToDO];
```
