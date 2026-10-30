# `PHSilenceJunkCallingController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TPSCarrierBundleControllerDelegate`
- 7 instance variables, 11 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _hasSpamEnabledSim;
@"TUFeatureFlags" _featureFlags;
@"TUConfigurationProvider" _configurationProvider;
@"CoreTelephonyClient" _ctClient;
@"PHCallBlockingServiceProviderController" _serviceProviderController;
@"TPSCarrierBundleController" _carrierBundleController;
@"NSArray" _specifiers;
```

## Properties

```
@property (T@"TUFeatureFlags",R,N,V_featureFlags) featureFlags;
@property (T@"TUConfigurationProvider",R,N,V_configurationProvider) configurationProvider;
@property (T@"CoreTelephonyClient",R,N,V_ctClient) ctClient;
@property (T@"PHCallBlockingServiceProviderController",R,N,V_serviceProviderController) serviceProviderController;
@property (T@"TPSCarrierBundleController",R,N,V_carrierBundleController) carrierBundleController;
@property (T@"NSArray",&,N,V_specifiers) specifiers;
@property (TB,N,V_hasSpamEnabledSim) hasSpamEnabledSim;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PHSilenceJunkCallingController ctClient];
-[PHSilenceJunkCallingController configurationProvider];
-[PHSilenceJunkCallingController objectForKeyHierarchy:subscriptionContext:error:];
-[PHSilenceJunkCallingController featureFlags];
-[PHSilenceJunkCallingController specifiers];
-[PHSilenceJunkCallingController carrierBundleController];
-[PHSilenceJunkCallingController stringForKeyHierarchy:subscriptionContext:error:];
-[PHSilenceJunkCallingController supportsCallBlockingForSubscriptionContext:];
-[PHSilenceJunkCallingController setSpecifiers:];
-[PHSilenceJunkCallingController getSilenceJunkCallingEnabled:];
-[PHSilenceJunkCallingController hasSpamEnabledSim];
-[PHSilenceJunkCallingController informationalUrlForSubscriptionContext:];
-[PHSilenceJunkCallingController initWithCoreTelephonyClient:queue:];
-[PHSilenceJunkCallingController serviceProviderController];
-[PHSilenceJunkCallingController setHasSpamEnabledSim:];
-[PHSilenceJunkCallingController setSilenceJunkCallingEnabled:specifier:];
-[PHSilenceJunkCallingController shouldUseConfigurationProviderForSilenceJunkCalling];
```
