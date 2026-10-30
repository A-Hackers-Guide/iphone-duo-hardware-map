# `TUThumperCTCapabilitiesState`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUCTCapabilitiesState`
- Protocols: `NSSecureCoding`, `NSCopying`, `TUPubliclyAccessibleCopying`
- 7 instance variables, 11 properties, 25 instance methods, 2 class methods

## Instance variables

```
B _approved;
B _associated;
B _supportsDefaultPairedDevice;
B _eligibleToEnable;
@"NSSet" _approvedSecondaryDeviceIDs;
@"NSString" _accountID;
@"NSString" _localDeviceID;
```

## Properties

```
@property (TB,N,GisApproved,V_approved) approved;
@property (T@"NSSet",C,N,V_approvedSecondaryDeviceIDs) approvedSecondaryDeviceIDs;
@property (T@"NSString",C,N,V_accountID) accountID;
@property (TB,N,GisAssociated,V_associated) associated;
@property (T@"NSString",C,N,V_localDeviceID) localDeviceID;
@property (TB,N,V_supportsDefaultPairedDevice) supportsDefaultPairedDevice;
@property (TB,N,V_eligibleToEnable) eligibleToEnable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUThumperCTCapabilitiesState supportsSecureCoding];
+[TUThumperCTCapabilitiesState unarchivedObjectClasses];
```

## Instance methods

```
-[TUThumperCTCapabilitiesState setApproved:];
-[TUThumperCTCapabilitiesState isApproved];
-[TUThumperCTCapabilitiesState setAccountID:];
-[TUThumperCTCapabilitiesState isAssociated];
-[TUThumperCTCapabilitiesState publiclyAccessibleCopyWithZone:];
-[TUThumperCTCapabilitiesState eligibleToEnable];
-[TUThumperCTCapabilitiesState publiclyAccessibleCopy];
-[TUThumperCTCapabilitiesState init];
-[TUThumperCTCapabilitiesState accountID];
-[TUThumperCTCapabilitiesState setApprovedSecondaryDeviceIDs:];
-[TUThumperCTCapabilitiesState supportsDefaultPairedDevice];
-[TUThumperCTCapabilitiesState setSupportsDefaultPairedDevice:];
-[TUThumperCTCapabilitiesState localDeviceID];
-[TUThumperCTCapabilitiesState setEligibleToEnable:];
-[TUThumperCTCapabilitiesState setAssociated:];
-[TUThumperCTCapabilitiesState setLocalDeviceID:];
-[TUThumperCTCapabilitiesState encodeWithCoder:];
-[TUThumperCTCapabilitiesState hash];
-[TUThumperCTCapabilitiesState description];
-[TUThumperCTCapabilitiesState initWithCoder:];
-[TUThumperCTCapabilitiesState copyWithZone:];
-[TUThumperCTCapabilitiesState initWithCapabilityInfo:];
-[TUThumperCTCapabilitiesState isEqual:];
-[TUThumperCTCapabilitiesState approvedSecondaryDeviceIDs];
-[TUThumperCTCapabilitiesState isEqualToCapabilitiesState:];
```
