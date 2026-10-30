# `CBMutableCharacteristic`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBCharacteristic`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _subscribedCentrals;
Q _permissions;
@"NSNumber" _ID;
```

## Properties

```
@property (T@"NSNumber",&,V_ID) ID;
@property (TQ,N,V_permissions) permissions;
@property (T@"NSArray",R,&,V_subscribedCentrals) subscribedCentrals;
@property (TQ,D,N) properties;
@property (T@"NSData",&,D) value;
@property (T@"NSArray",&,D) descriptors;
```

## Instance methods

```
-[CBMutableCharacteristic setID:];
-[CBMutableCharacteristic ID];
-[CBMutableCharacteristic observeValueForKeyPath:ofObject:change:context:];
-[CBMutableCharacteristic setPermissions:];
-[CBMutableCharacteristic initWithType:properties:value:permissions:];
-[CBMutableCharacteristic dealloc];
-[CBMutableCharacteristic permissions];
-[CBMutableCharacteristic description];
-[CBMutableCharacteristic handleCentralUnsubscribed:];
-[CBMutableCharacteristic initWithService:dictionary:];
-[CBMutableCharacteristic handleCentralSubscribed:];
-[CBMutableCharacteristic handlePowerNotOn];
-[CBMutableCharacteristic subscribedCentrals];
```
