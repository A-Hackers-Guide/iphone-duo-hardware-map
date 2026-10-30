# `LACDTOFeatureController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOFeatureControlling`, `LACDTOEventProducer`
- 8 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOKVStore>" _kvStore;
@"<LACDTOFeatureRequirementsDataSource>" _dataSource;
@"<LACFeatureFlagsProviderDTO>" _featureFlags;
@"<LACBootArgParsing>" _bootArgParser;
@"<LACDTOAnalyticsReporting>" _analytics;
@"LACDTOFeatureEnablementModeCoder" _enablementModeCoder;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"<LACDTOEventBus>" eventBus;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LACDTOEventBus>",&,N,VeventBus) eventBus;
```

## Instance methods

```
-[LACDTOFeatureController fetchStateWithCompletion:];
-[LACDTOFeatureController checkCanEnableFeatureWithCompletion:];
-[LACDTOFeatureController disableExtendedPolicyProtectionWithContext:completion:];
-[LACDTOFeatureController disableFeatureStrictModeWithContext:completion:];
-[LACDTOFeatureController disableFeatureWithContext:completion:];
-[LACDTOFeatureController enableExtendedPolicyProtectionWithCompletion:];
-[LACDTOFeatureController enableFeatureStrictModeWithCompletion:];
-[LACDTOFeatureController _checkIsAutoEnablementAllowedWithCompletion:];
-[LACDTOFeatureController _enableFeatureWithOptions:completion:];
-[LACDTOFeatureController _setExtendedPolicyProtectionEnabled:context:connection:completion:];
-[LACDTOFeatureController _setFeatureEnablementMode:context:connection:completion:];
-[LACDTOFeatureController _setFeatureStrictModeEnabled:context:connection:completion:];
-[LACDTOFeatureController _setValue:forKey:contextUUID:connection:completion:];
-[LACDTOFeatureController checkIsAutoEnablementAllowedWithCompletion:];
-[LACDTOFeatureController checkIsExtendedPolicyProtectionAvailableWithCompletion:];
-[LACDTOFeatureController checkIsExtendedPolicyProtectionEnabledWithCompletion:];
-[LACDTOFeatureController checkIsFeatureAvailableWithCompletion:];
-[LACDTOFeatureController checkIsFeatureEnabledWithCompletion:];
-[LACDTOFeatureController checkIsFeatureStrictModeEnabledWithCompletion:];
-[LACDTOFeatureController checkIsFeatureSupportedWithCompletion:];
-[LACDTOFeatureController enableFeatureWithOptions:completion:];
-[LACDTOFeatureController eventBus];
-[LACDTOFeatureController fetchEnablementModeWithCompletion:];
-[LACDTOFeatureController fetchRequirements:completion:];
-[LACDTOFeatureController initWithKVStore:dataSource:featureFlags:bootArgParser:analytics:workQueue:];
-[LACDTOFeatureController setEventBus:];
```
