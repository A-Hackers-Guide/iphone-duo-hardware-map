# `CTCellularPlanProvisioningOnDeviceActivationRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 14 instance variables, 14 properties, 38 instance methods, 1 class methods

## Instance variables

```
B _useDS;
B _isESim;
B _portIn;
@"NSString" _eid;
@"NSString" _iccid;
@"NSString" _sourceIccid;
@"NSString" _unusableIccid;
@"NSString" _phoneNumber;
@"NSString" _mcc;
@"NSString" _mnc;
@"NSString" _gid1;
@"NSString" _gid2;
@"NSString" _smdpAddress;
@"NSString" _flowType;
```

## Properties

```
@property (T@"NSString",&,N,V_eid) eid;
@property (T@"NSString",&,N,V_iccid) iccid;
@property (T@"NSString",&,N,V_sourceIccid) sourceIccid;
@property (T@"NSString",&,N,V_unusableIccid) unusableIccid;
@property (T@"NSString",&,N,V_phoneNumber) phoneNumber;
@property (T@"NSString",&,N,V_mcc) mcc;
@property (T@"NSString",&,N,V_mnc) mnc;
@property (T@"NSString",&,N,V_gid1) gid1;
@property (T@"NSString",&,N,V_gid2) gid2;
@property (T@"NSString",&,N,V_smdpAddress) smdpAddress;
@property (TB,N,V_useDS) useDS;
@property (TB,N,V_isESim) isESim;
@property (T@"NSString",&,N,V_flowType) flowType;
@property (TB,N,V_portIn) portIn;
```

## Class methods

```
+[CTCellularPlanProvisioningOnDeviceActivationRequest supportsSecureCoding];
```

## Instance methods

```
-[CTCellularPlanProvisioningOnDeviceActivationRequest phoneNumber];
-[CTCellularPlanProvisioningOnDeviceActivationRequest init];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setPhoneNumber:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest iccid];
-[CTCellularPlanProvisioningOnDeviceActivationRequest mnc];
-[CTCellularPlanProvisioningOnDeviceActivationRequest encodeWithCoder:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest description];
-[CTCellularPlanProvisioningOnDeviceActivationRequest initWithCoder:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setMnc:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest mcc];
-[CTCellularPlanProvisioningOnDeviceActivationRequest flowType];
-[CTCellularPlanProvisioningOnDeviceActivationRequest copyWithZone:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setIccid:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest isEqual:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setMcc:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setEid:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setSourceIccid:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest eid];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setSmdpAddress:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest gid1];
-[CTCellularPlanProvisioningOnDeviceActivationRequest gid2];
-[CTCellularPlanProvisioningOnDeviceActivationRequest initWithDetails:installIccid:sourceIccid:unusableIccid:phoneNumber:mcc:mnc:gid1:gid2:smdp:useDS:esim:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest initWithDetails:installIccid:sourceIccid:unusableIccid:phoneNumber:mcc:mnc:gid1:gid2:smdp:useDS:esim:flowType:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest initWithDetails:installIccid:sourceIccid:unusableIccid:phoneNumber:mcc:mnc:gid1:gid2:smdp:useDS:esim:flowType:portIn:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest initWithEid:installIccid:sourceIccid:phoneNumber:mcc:mnc:gid1:gid2:smdp:useDS:esim:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest isESim];
-[CTCellularPlanProvisioningOnDeviceActivationRequest portIn];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setFlowType:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setGid1:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setGid2:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setIsESim:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setPortIn:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setUnusableIccid:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest setUseDS:];
-[CTCellularPlanProvisioningOnDeviceActivationRequest smdpAddress];
-[CTCellularPlanProvisioningOnDeviceActivationRequest sourceIccid];
-[CTCellularPlanProvisioningOnDeviceActivationRequest unusableIccid];
-[CTCellularPlanProvisioningOnDeviceActivationRequest useDS];
```
