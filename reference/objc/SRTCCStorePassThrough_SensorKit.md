# `SRTCCStorePassThrough`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRTCCStore`
- 0 instance variables, 4 properties, 11 instance methods, 1 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRTCCStorePassThrough initialize];
```

## Instance methods

```
-[SRTCCStorePassThrough bundleIdentifiersDisabledForService:];
-[SRTCCStorePassThrough bundleIdentifiersForService:];
-[SRTCCStorePassThrough checkAccessForService:auditToken:];
-[SRTCCStorePassThrough informationForBundleId:];
-[SRTCCStorePassThrough isOverriddenForService:];
-[SRTCCStorePassThrough preflightAuthorizationStatusForService:];
-[SRTCCStorePassThrough requestAccessForService:completion:];
-[SRTCCStorePassThrough resetService:];
-[SRTCCStorePassThrough resetService:forBundleId:];
-[SRTCCStorePassThrough setOverride:forService:];
-[SRTCCStorePassThrough setValue:forService:bundleId:];
```
