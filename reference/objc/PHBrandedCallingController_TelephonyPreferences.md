# `PHBrandedCallingController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUConfigurationProviderDelegate`
- 5 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"PSListController" _parentListController;
@"CoreTelephonyClient" _ctClient;
@"NSArray" _contexts;
@"TUConfigurationProvider" _configurationProvider;
@"TUFeatureFlags" _featureFlags;
```

## Properties

```
@property (T@"CoreTelephonyClient",&,N,V_ctClient) ctClient;
@property (T@"NSArray",&,N,V_contexts) contexts;
@property (T@"TUConfigurationProvider",R,N,V_configurationProvider) configurationProvider;
@property (T@"TUFeatureFlags",R,N,V_featureFlags) featureFlags;
@property (T@"PSListController",W,N,V_parentListController) parentListController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PHBrandedCallingController ctClient];
-[PHBrandedCallingController contexts];
-[PHBrandedCallingController configurationProvider];
-[PHBrandedCallingController setContexts:];
-[PHBrandedCallingController featureFlags];
-[PHBrandedCallingController configurationChanged];
-[PHBrandedCallingController fetchSubscriptionsInUse];
-[PHBrandedCallingController setCtClient:];
-[PHBrandedCallingController parentListController];
-[PHBrandedCallingController fetchCarrierBundleValue:context:];
-[PHBrandedCallingController activeContextsSupportingBrandedCalling];
-[PHBrandedCallingController featureEnabledForAtLeastOneContext];
-[PHBrandedCallingController getBrandedCallingCapabilityEnabledForContext:];
-[PHBrandedCallingController getBrandedCallingEnabled];
-[PHBrandedCallingController getBrandedCallingStateForContext:];
-[PHBrandedCallingController initWithCoreTelephonyClient:parentListController:];
-[PHBrandedCallingController setBrandedCallingEnabled:];
-[PHBrandedCallingController setParentListController:];
-[PHBrandedCallingController updateBrandedCallingState];
```
