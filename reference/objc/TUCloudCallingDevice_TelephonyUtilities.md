# `TUCloudCallingDevice`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _defaultPairedDevice;
B _supportsRestrictingSecondaryCalling;
@"NSString" _name;
@"NSString" _modelIdentifier;
@"NSString" _uniqueID;
@"NSArray" _linkedUserURIs;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",C,N,V_modelIdentifier) modelIdentifier;
@property (T@"NSString",C,N,V_uniqueID) uniqueID;
@property (T@"NSArray",C,N,V_linkedUserURIs) linkedUserURIs;
@property (TB,N,GisDefaultPairedDevice,V_defaultPairedDevice) defaultPairedDevice;
@property (TB,N,V_supportsRestrictingSecondaryCalling) supportsRestrictingSecondaryCalling;
```

## Class methods

```
+[TUCloudCallingDevice supportsSecureCoding];
```

## Instance methods

```
-[TUCloudCallingDevice modelIdentifier];
-[TUCloudCallingDevice uniqueID];
-[TUCloudCallingDevice encodeWithCoder:];
-[TUCloudCallingDevice description];
-[TUCloudCallingDevice setName:];
-[TUCloudCallingDevice initWithCoder:];
-[TUCloudCallingDevice setModelIdentifier:];
-[TUCloudCallingDevice copyWithZone:];
-[TUCloudCallingDevice isEqual:];
-[TUCloudCallingDevice setUniqueID:];
-[TUCloudCallingDevice name];
-[TUCloudCallingDevice isDefaultPairedDevice];
-[TUCloudCallingDevice linkedUserURIs];
-[TUCloudCallingDevice setDefaultPairedDevice:];
-[TUCloudCallingDevice setLinkedUserURIs:];
-[TUCloudCallingDevice setSupportsRestrictingSecondaryCalling:];
-[TUCloudCallingDevice supportsRestrictingSecondaryCalling];
```
