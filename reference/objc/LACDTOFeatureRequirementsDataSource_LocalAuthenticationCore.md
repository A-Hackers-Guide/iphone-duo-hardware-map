# `LACDTOFeatureRequirementsDataSource`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOFeatureRequirementsDataSource`
- 6 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"<LACDTODeviceInfoProvider>" _device;
@"<LACDTOKVStoreReader>" _kvStore;
@"<LACGlobalDomainDTO>" _globalDomain;
@"<LACDTOAppleAccountInfoProviding>" _accountProvider;
@"<LACDTOLocationServicesInfoProviding>" _locationServicesProvider;
@"NSObject<OS_dispatch_queue>" _replyQueue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOFeatureRequirementsDataSource _hasBiometricLivenessWithQuery:completion:];
-[LACDTOFeatureRequirementsDataSource _hasNeverBeenDisabledByUserWithQuery:completion:];
-[LACDTOFeatureRequirementsDataSource fetchRequirements:completion:];
-[LACDTOFeatureRequirementsDataSource initWithDevice:kvStore:accountProvider:locationServicesProvider:globalDomain:replyQueue:];
```
