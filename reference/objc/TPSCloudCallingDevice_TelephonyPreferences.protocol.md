# `TPSCloudCallingDevice` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) name;
@property (T@"NSString",R,C,N) modelIdentifier;
@property (T@"NSString",R,C,N) uniqueID;
@property (TB,R,N,GisDefaultPairedDevice) defaultPairedDevice;
@property (TB,R,N) supportsRestrictingSecondaryCalling;
@property (T@"NSString",R,C,N) tps_modelName;
```

## Instance methods

```
-[TPSCloudCallingDevice modelIdentifier];
-[TPSCloudCallingDevice uniqueID];
-[TPSCloudCallingDevice name];
-[TPSCloudCallingDevice isDefaultPairedDevice];
-[TPSCloudCallingDevice supportsRestrictingSecondaryCalling];
-[TPSCloudCallingDevice tps_modelName];
```
