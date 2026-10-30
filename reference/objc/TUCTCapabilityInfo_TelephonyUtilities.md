# `TUCTCapabilityInfo`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`, `TUPubliclyAccessibleCopying`
- 7 instance variables, 12 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _canEnable;
B _enabled;
B _canEnableRoaming;
B _roamingEnabled;
i _provisioningStatus;
@"NSURL" _provisioningURL;
@"NSData" _provisioningPostData;
```

## Properties

```
@property (Ti,N,V_provisioningStatus) provisioningStatus;
@property (T@"NSURL",C,N,V_provisioningURL) provisioningURL;
@property (T@"NSData",C,N,V_provisioningPostData) provisioningPostData;
@property (TB,N,V_canEnable) canEnable;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,N,V_canEnableRoaming) canEnableRoaming;
@property (TB,N,GisRoamingEnabled,V_roamingEnabled) roamingEnabled;
@property (TB,R,N,GisProvisioningURLInvalid) provisioningURLInvalid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCTCapabilityInfo supportsSecureCoding];
```

## Instance methods

```
-[TUCTCapabilityInfo setProvisioningURL:];
-[TUCTCapabilityInfo setRoamingEnabled:];
-[TUCTCapabilityInfo isRoamingEnabled];
-[TUCTCapabilityInfo publiclyAccessibleCopyWithZone:];
-[TUCTCapabilityInfo publiclyAccessibleCopy];
-[TUCTCapabilityInfo isProvisioningURLInvalid];
-[TUCTCapabilityInfo setProvisioningStatus:];
-[TUCTCapabilityInfo provisioningPostData];
-[TUCTCapabilityInfo provisioningStatus];
-[TUCTCapabilityInfo setCanEnableRoaming:];
-[TUCTCapabilityInfo setProvisioningPostData:];
-[TUCTCapabilityInfo provisioningURL];
-[TUCTCapabilityInfo canEnable];
-[TUCTCapabilityInfo isEnabled];
-[TUCTCapabilityInfo setEnabled:];
-[TUCTCapabilityInfo encodeWithCoder:];
-[TUCTCapabilityInfo canEnableRoaming];
-[TUCTCapabilityInfo setCanEnable:];
-[TUCTCapabilityInfo description];
-[TUCTCapabilityInfo initWithCoder:];
-[TUCTCapabilityInfo invalidateProvisioningURL];
-[TUCTCapabilityInfo copyWithZone:];
```
