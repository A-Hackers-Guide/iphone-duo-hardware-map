# `CBCharacteristic`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBAttribute`
- 10 instance variables, 10 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _isBroadcasted;
B _isNotifying;
@"CBService" _service;
Q _properties;
@"NSData" _value;
@"NSArray" _descriptors;
Q _valueTimestamp;
@"CBPeripheral" _peripheral;
@"NSNumber" _handle;
@"NSNumber" _valueHandle;
```

## Properties

```
@property (T@"CBService",W,N,V_service) service;
@property (TQ,N,V_properties) properties;
@property (T@"NSData",&,V_value) value;
@property (T@"NSArray",&,V_descriptors) descriptors;
@property (TB,V_isNotifying) isNotifying;
@property (TQ,R,N,V_valueTimestamp) valueTimestamp;
@property (T@"CBPeripheral",R,N,V_peripheral) peripheral;
@property (T@"NSNumber",R,N,V_handle) handle;
@property (T@"NSNumber",R,N,V_valueHandle) valueHandle;
@property (TB,R,V_isBroadcasted) isBroadcasted;
```

## Instance methods

```
-[CBCharacteristic properties];
-[CBCharacteristic setService:];
-[CBCharacteristic value];
-[CBCharacteristic setDescriptors:];
-[CBCharacteristic descriptors];
-[CBCharacteristic setProperties:];
-[CBCharacteristic invalidate];
-[CBCharacteristic handle];
-[CBCharacteristic setValue:];
-[CBCharacteristic service];
-[CBCharacteristic description];
-[CBCharacteristic initWithService:dictionary:];
-[CBCharacteristic peripheral];
-[CBCharacteristic setIsNotifying:];
-[CBCharacteristic handleDescriptorsDiscovered:];
-[CBCharacteristic handleValueBroadcasted:];
-[CBCharacteristic handleValueNotifying:];
-[CBCharacteristic handleValueUpdated:];
-[CBCharacteristic handleValueWritten:];
-[CBCharacteristic isBroadcasted];
-[CBCharacteristic isNotifying];
-[CBCharacteristic valueHandle];
-[CBCharacteristic valueTimestamp];
```
