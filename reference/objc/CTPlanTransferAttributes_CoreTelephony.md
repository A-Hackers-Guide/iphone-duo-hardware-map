# `CTPlanTransferAttributes`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _isSecuredFlow;
Q _transferCapability;
Q _transferStatus;
Q _installRestriction;
@"NSString" _transferEndpoint;
```

## Properties

```
@property (TQ,N,V_transferCapability) transferCapability;
@property (TQ,N,V_transferStatus) transferStatus;
@property (TQ,N,V_installRestriction) installRestriction;
@property (TB,N,V_isSecuredFlow) isSecuredFlow;
@property (T@"NSString",&,N,V_transferEndpoint) transferEndpoint;
```

## Class methods

```
+[CTPlanTransferAttributes supportsSecureCoding];
```

## Instance methods

```
-[CTPlanTransferAttributes init];
-[CTPlanTransferAttributes encodeWithCoder:];
-[CTPlanTransferAttributes description];
-[CTPlanTransferAttributes initWithCoder:];
-[CTPlanTransferAttributes isEqual:];
-[CTPlanTransferAttributes initWithTransferCapability:transferStatus:installRestriction:isSecuredFlow:transferEndpoint:];
-[CTPlanTransferAttributes installRestriction];
-[CTPlanTransferAttributes isSecuredFlow];
-[CTPlanTransferAttributes setInstallRestriction:];
-[CTPlanTransferAttributes setIsSecuredFlow:];
-[CTPlanTransferAttributes setTransferCapability:];
-[CTPlanTransferAttributes setTransferEndpoint:];
-[CTPlanTransferAttributes setTransferStatus:];
-[CTPlanTransferAttributes transferCapability];
-[CTPlanTransferAttributes transferEndpoint];
-[CTPlanTransferAttributes transferStatus];
```
