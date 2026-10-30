# `CBDescriptor`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBAttribute`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"CBCharacteristic" _characteristic;
@ _value;
@"CBPeripheral" _peripheral;
@"NSNumber" _handle;
```

## Properties

```
@property (T@"CBCharacteristic",W,N,V_characteristic) characteristic;
@property (T@,&,V_value) value;
@property (T@"CBPeripheral",R,N,V_peripheral) peripheral;
@property (T@"NSNumber",R,N,V_handle) handle;
```

## Instance methods

```
-[CBDescriptor value];
-[CBDescriptor invalidate];
-[CBDescriptor handle];
-[CBDescriptor setValue:];
-[CBDescriptor description];
-[CBDescriptor peripheral];
-[CBDescriptor characteristic];
-[CBDescriptor setCharacteristic:];
-[CBDescriptor handleValueUpdated:];
-[CBDescriptor handleValueWritten:];
-[CBDescriptor initWithCharacteristic:dictionary:];
```
