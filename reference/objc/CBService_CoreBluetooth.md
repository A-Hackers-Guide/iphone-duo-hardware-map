# `CBService`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBAttribute`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isPrimary;
@"CBPeripheral" _peripheral;
@"NSArray" _includedServices;
@"NSArray" _characteristics;
@"NSNumber" _startHandle;
@"NSNumber" _endHandle;
```

## Properties

```
@property (TB,N,V_isPrimary) isPrimary;
@property (T@"NSArray",&,V_includedServices) includedServices;
@property (T@"NSArray",&,V_characteristics) characteristics;
@property (T@"NSNumber",R,N,V_startHandle) startHandle;
@property (T@"NSNumber",R,N,V_endHandle) endHandle;
@property (T@"CBPeripheral",R,W,N,V_peripheral) peripheral;
```

## Instance methods

```
-[CBService isPrimary];
-[CBService invalidate];
-[CBService description];
-[CBService setIsPrimary:];
-[CBService peripheral];
-[CBService characteristics];
-[CBService setCharacteristics:];
-[CBService includedServices];
-[CBService endHandle];
-[CBService handleCharacteristicsDiscovered:];
-[CBService handleIncludedServicesDiscovered:];
-[CBService initWithPeripheral:dictionary:];
-[CBService setIncludedServices:];
-[CBService startHandle];
```
