# `CBATTRequest`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableData" _value;
B _ignoreResponse;
@"CBCentral" _central;
@"CBCharacteristic" _characteristic;
Q _offset;
@"NSNumber" _transactionID;
```

## Properties

```
@property (T@"CBCharacteristic",&,N,V_characteristic) characteristic;
@property (T@"NSNumber",R,N,V_transactionID) transactionID;
@property (TB,N,V_ignoreResponse) ignoreResponse;
@property (T@"CBCentral",R,N,V_central) central;
@property (TQ,R,N,V_offset) offset;
@property (T@"NSData",C,V_value) value;
```

## Instance methods

```
-[CBATTRequest transactionID];
-[CBATTRequest value];
-[CBATTRequest setValue:];
-[CBATTRequest description];
-[CBATTRequest offset];
-[CBATTRequest endOffset];
-[CBATTRequest characteristic];
-[CBATTRequest setCharacteristic:];
-[CBATTRequest central];
-[CBATTRequest appendValueData:];
-[CBATTRequest ignoreResponse];
-[CBATTRequest initWithCentral:characteristic:offset:transactionID:];
-[CBATTRequest setIgnoreResponse:];
```
