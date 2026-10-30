# `CBTDSServiceElement`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `CUXPCCodable`, `NSCopying`
- 3 instance variables, 3 properties, 15 instance methods, 2 class methods

## Instance variables

```
C _operation;
C _dataLinkId;
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (TC,N,V_operation) operation;
@property (TC,N,V_dataLinkId) dataLinkId;
```

## Class methods

```
+[CBTDSServiceElement supportsSecureCoding];
+[CBTDSServiceElement CBTDSServiceHashFrom:operation:interface:address:];
```

## Instance methods

```
-[CBTDSServiceElement encodeWithXPCObject:];
-[CBTDSServiceElement setOperation:];
-[CBTDSServiceElement initWithXPCObject:error:];
-[CBTDSServiceElement operation];
-[CBTDSServiceElement descriptionWithLevel:];
-[CBTDSServiceElement encodeWithCoder:];
-[CBTDSServiceElement hash];
-[CBTDSServiceElement description];
-[CBTDSServiceElement setName:];
-[CBTDSServiceElement initWithCoder:];
-[CBTDSServiceElement copyWithZone:];
-[CBTDSServiceElement isEqual:];
-[CBTDSServiceElement name];
-[CBTDSServiceElement dataLinkId];
-[CBTDSServiceElement setDataLinkId:];
```
