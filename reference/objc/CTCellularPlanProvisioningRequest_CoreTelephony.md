# `CTCellularPlanProvisioningRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSString" _address;
@"NSString" _matchingID;
@"NSString" _OID;
@"NSString" _confirmationCode;
@"NSString" _ICCID;
@"NSString" _EID;
```

## Properties

```
@property (T@"NSString",&,N,V_address) address;
@property (T@"NSString",&,N,V_matchingID) matchingID;
@property (T@"NSString",&,N,V_OID) OID;
@property (T@"NSString",&,N,V_confirmationCode) confirmationCode;
@property (T@"NSString",&,N,V_ICCID) ICCID;
@property (T@"NSString",&,N,V_EID) EID;
```

## Class methods

```
+[CTCellularPlanProvisioningRequest supportsSecureCoding];
```

## Instance methods

```
-[CTCellularPlanProvisioningRequest address];
-[CTCellularPlanProvisioningRequest setAddress:];
-[CTCellularPlanProvisioningRequest init];
-[CTCellularPlanProvisioningRequest OID];
-[CTCellularPlanProvisioningRequest setOID:];
-[CTCellularPlanProvisioningRequest setICCID:];
-[CTCellularPlanProvisioningRequest encodeWithCoder:];
-[CTCellularPlanProvisioningRequest description];
-[CTCellularPlanProvisioningRequest initWithCoder:];
-[CTCellularPlanProvisioningRequest ICCID];
-[CTCellularPlanProvisioningRequest copyWithZone:];
-[CTCellularPlanProvisioningRequest isEqual:];
-[CTCellularPlanProvisioningRequest EID];
-[CTCellularPlanProvisioningRequest setEID:];
-[CTCellularPlanProvisioningRequest confirmationCode];
-[CTCellularPlanProvisioningRequest matchingID];
-[CTCellularPlanProvisioningRequest setConfirmationCode:];
-[CTCellularPlanProvisioningRequest setMatchingID:];
```
