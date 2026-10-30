# `CTCellularPlanQRCodeAction`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSString" _title;
@"NSString" _message;
@"NSString" _smdpAddress;
@"NSString" _matchingId;
@"NSString" _OID;
```

## Properties

```
@property (T@"NSString",&,N,V_smdpAddress) smdpAddress;
@property (T@"NSString",&,N,V_matchingId) matchingId;
@property (T@"NSString",&,N,V_OID) OID;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_message) message;
```

## Class methods

```
+[CTCellularPlanQRCodeAction supportsSecureCoding];
```

## Instance methods

```
-[CTCellularPlanQRCodeAction setMessage:];
-[CTCellularPlanQRCodeAction message];
-[CTCellularPlanQRCodeAction OID];
-[CTCellularPlanQRCodeAction setOID:];
-[CTCellularPlanQRCodeAction title];
-[CTCellularPlanQRCodeAction encodeWithCoder:];
-[CTCellularPlanQRCodeAction description];
-[CTCellularPlanQRCodeAction initWithCoder:];
-[CTCellularPlanQRCodeAction setTitle:];
-[CTCellularPlanQRCodeAction copyWithZone:];
-[CTCellularPlanQRCodeAction performWithCompletionHandler:];
-[CTCellularPlanQRCodeAction setSmdpAddress:];
-[CTCellularPlanQRCodeAction matchingId];
-[CTCellularPlanQRCodeAction setMatchingId:];
-[CTCellularPlanQRCodeAction smdpAddress];
```
