# `CTCellularPlanTransferCrossPlatformRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSString" _phoneNumber;
@"NSString" _carrierName;
@"NSString" _mccMnc;
@"NSString" _gid1;
@"NSString" _gid2;
@"NSString" _carrierID;
```

## Properties

```
@property (T@"NSString",R,N,V_phoneNumber) phoneNumber;
@property (T@"NSString",R,N,V_carrierName) carrierName;
@property (T@"NSString",R,N,V_mccMnc) mccMnc;
@property (T@"NSString",R,N,V_gid1) gid1;
@property (T@"NSString",R,N,V_gid2) gid2;
@property (T@"NSString",R,N,V_carrierID) carrierID;
```

## Class methods

```
+[CTCellularPlanTransferCrossPlatformRequest supportsSecureCoding];
```

## Instance methods

```
-[CTCellularPlanTransferCrossPlatformRequest phoneNumber];
-[CTCellularPlanTransferCrossPlatformRequest carrierName];
-[CTCellularPlanTransferCrossPlatformRequest encodeWithCoder:];
-[CTCellularPlanTransferCrossPlatformRequest description];
-[CTCellularPlanTransferCrossPlatformRequest initWithCoder:];
-[CTCellularPlanTransferCrossPlatformRequest isEqual:];
-[CTCellularPlanTransferCrossPlatformRequest carrierID];
-[CTCellularPlanTransferCrossPlatformRequest gid1];
-[CTCellularPlanTransferCrossPlatformRequest gid2];
-[CTCellularPlanTransferCrossPlatformRequest initWithPhoneNumber:carrierName:mccMnc:gid1:gid2:];
-[CTCellularPlanTransferCrossPlatformRequest initWithPhoneNumber:carrierName:mccMnc:gid1:gid2:carrierID:];
-[CTCellularPlanTransferCrossPlatformRequest mccMnc];
```
