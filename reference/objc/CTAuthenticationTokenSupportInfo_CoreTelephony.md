# `CTAuthenticationTokenSupportInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 13 instance methods, 2 class methods

## Instance variables

```
B _isLocal;
q _supportStatus;
@"NSString" _printFormattedPhoneNumber;
@"NSString" _carrier;
@"NSArray" _supportedAggregators;
@"NSString" _iccid;
@"NSString" _simPrintLabel;
@"NSString" _msisdnPublicKey;
```

## Properties

```
@property (Tq,R,N,V_supportStatus) supportStatus;
@property (T@"NSString",R,C,N,V_printFormattedPhoneNumber) printFormattedPhoneNumber;
@property (T@"NSString",R,C,N,V_carrier) carrier;
@property (T@"NSArray",R,C,N,V_supportedAggregators) supportedAggregators;
@property (T@"NSString",R,C,N,V_iccid) iccid;
@property (TB,R,N,V_isLocal) isLocal;
@property (T@"NSString",R,C,N,V_simPrintLabel) simPrintLabel;
@property (T@"NSString",R,C,N,V_msisdnPublicKey) msisdnPublicKey;
```

## Class methods

```
+[CTAuthenticationTokenSupportInfo supportsSecureCoding];
+[CTAuthenticationTokenSupportInfo infoFromDictionary:];
```

## Instance methods

```
-[CTAuthenticationTokenSupportInfo iccid];
-[CTAuthenticationTokenSupportInfo isLocal];
-[CTAuthenticationTokenSupportInfo encodeWithCoder:];
-[CTAuthenticationTokenSupportInfo description];
-[CTAuthenticationTokenSupportInfo initWithCoder:];
-[CTAuthenticationTokenSupportInfo dictionaryRepresentation];
-[CTAuthenticationTokenSupportInfo carrier];
-[CTAuthenticationTokenSupportInfo msisdnPublicKey];
-[CTAuthenticationTokenSupportInfo initWithSupportStatus:printFormattedPhoneNumber:carrier:supportedAggregators:iccid:isLocal:simPrintLabel:msisdnPublicKey:];
-[CTAuthenticationTokenSupportInfo printFormattedPhoneNumber];
-[CTAuthenticationTokenSupportInfo simPrintLabel];
-[CTAuthenticationTokenSupportInfo supportStatus];
-[CTAuthenticationTokenSupportInfo supportedAggregators];
```
