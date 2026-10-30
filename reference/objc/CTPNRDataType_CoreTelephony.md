# `CTPNRDataType`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
q _pnrMechanism;
@"NSString" _svcCenterAddr;
@"NSString" _destAddr;
```

## Properties

```
@property (Tq,N,V_pnrMechanism) pnrMechanism;
@property (T@"NSString",&,N,V_svcCenterAddr) svcCenterAddr;
@property (T@"NSString",&,N,V_destAddr) destAddr;
```

## Class methods

```
+[CTPNRDataType supportsSecureCoding];
```

## Instance methods

```
-[CTPNRDataType init];
-[CTPNRDataType encodeWithCoder:];
-[CTPNRDataType description];
-[CTPNRDataType initWithCoder:];
-[CTPNRDataType copyWithZone:];
-[CTPNRDataType isEqual:];
-[CTPNRDataType pnrMechanism];
-[CTPNRDataType setDestAddr:];
-[CTPNRDataType setPnrMechanism:];
-[CTPNRDataType setSvcCenterAddr:];
-[CTPNRDataType destAddr];
-[CTPNRDataType isEqualToCTPNRDataType:];
-[CTPNRDataType svcCenterAddr];
```
