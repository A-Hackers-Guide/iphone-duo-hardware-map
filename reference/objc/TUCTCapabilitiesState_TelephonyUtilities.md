# `TUCTCapabilitiesState`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `TUPubliclyAccessibleCopying`, `TUSecureCoding`
- 11 instance variables, 16 properties, 35 instance methods, 3 class methods

## Instance variables

```
B _provisioningURLInvalid;
B _supported;
B _enabled;
B _currentlyAvailable;
B _roamingSupported;
B _roamingEnabled;
B _emergencySupported;
B _emergencyCurrentlyAvailable;
i _provisioningStatus;
@"NSURL" _provisioningURL;
@"NSData" _provisioningPostData;
```

## Properties

```
@property (T@"TUCTCapabilityInfo",R,C,N) ctCapabilityInfo;
@property (Ti,N,V_provisioningStatus) provisioningStatus;
@property (T@"NSURL",C,N,V_provisioningURL) provisioningURL;
@property (TB,N,GisProvisioningURLInvalid,V_provisioningURLInvalid) provisioningURLInvalid;
@property (T@"NSData",C,N,V_provisioningPostData) provisioningPostData;
@property (TB,N,GisSupported,V_supported) supported;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,N,GisCurrentlyAvailable,V_currentlyAvailable) currentlyAvailable;
@property (TB,N,GisRoamingSupported,V_roamingSupported) roamingSupported;
@property (TB,N,GisRoamingEnabled,V_roamingEnabled) roamingEnabled;
@property (TB,N,GisEmergencySupported,V_emergencySupported) emergencySupported;
@property (TB,N,GisEmergencyCurrentlyAvailable,V_emergencyCurrentlyAvailable) emergencyCurrentlyAvailable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCTCapabilitiesState supportsSecureCoding];
+[TUCTCapabilitiesState unarchivedObjectClasses];
+[TUCTCapabilitiesState unarchivedObjectFromData:error:];
```

## Instance methods

```
-[TUCTCapabilitiesState setSupported:];
-[TUCTCapabilitiesState isEmergencySupported];
-[TUCTCapabilitiesState setProvisioningURL:];
-[TUCTCapabilitiesState isRoamingSupported];
-[TUCTCapabilitiesState setRoamingEnabled:];
-[TUCTCapabilitiesState isRoamingEnabled];
-[TUCTCapabilitiesState publiclyAccessibleCopyWithZone:];
-[TUCTCapabilitiesState publiclyAccessibleCopy];
-[TUCTCapabilitiesState isProvisioningURLInvalid];
-[TUCTCapabilitiesState setProvisioningStatus:];
-[TUCTCapabilitiesState provisioningPostData];
-[TUCTCapabilitiesState isSupported];
-[TUCTCapabilitiesState provisioningStatus];
-[TUCTCapabilitiesState setProvisioningPostData:];
-[TUCTCapabilitiesState provisioningURL];
-[TUCTCapabilitiesState archivedDataWithError:];
-[TUCTCapabilitiesState setRoamingSupported:];
-[TUCTCapabilitiesState ctCapabilityInfo];
-[TUCTCapabilitiesState isEmergencyCurrentlyAvailable];
-[TUCTCapabilitiesState isEnabled];
-[TUCTCapabilitiesState setEnabled:];
-[TUCTCapabilitiesState setCurrentlyAvailable:];
-[TUCTCapabilitiesState encodeWithCoder:];
-[TUCTCapabilitiesState setEmergencyCurrentlyAvailable:];
-[TUCTCapabilitiesState hash];
-[TUCTCapabilitiesState description];
-[TUCTCapabilitiesState setEmergencySupported:];
-[TUCTCapabilitiesState initWithCoder:];
-[TUCTCapabilitiesState invalidateProvisioningURL];
-[TUCTCapabilitiesState copyWithZone:];
-[TUCTCapabilitiesState setProvisioningURLInvalid:];
-[TUCTCapabilitiesState initWithCapabilityInfo:];
-[TUCTCapabilitiesState isEqual:];
-[TUCTCapabilitiesState isCurrentlyAvailable];
-[TUCTCapabilitiesState isEqualToCapabilitiesState:];
```
