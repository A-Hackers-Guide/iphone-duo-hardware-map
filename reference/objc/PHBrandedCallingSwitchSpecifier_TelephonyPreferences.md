# `PHBrandedCallingSwitchSpecifier`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSSpecifier`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CoreTelephonyClient" _ctClient;
@"CTXPCServiceSubscriptionContext" _context;
@"TUFeatureFlags" _featureFlags;
@"TUConfigurationProvider" _configurationProvider;
```

## Properties

```
@property (T@"CoreTelephonyClient",&,N,V_ctClient) ctClient;
@property (T@"CTXPCServiceSubscriptionContext",&,N,V_context) context;
@property (T@"TUFeatureFlags",R,N,V_featureFlags) featureFlags;
@property (T@"TUConfigurationProvider",R,N,V_configurationProvider) configurationProvider;
```

## Instance methods

```
-[PHBrandedCallingSwitchSpecifier ctClient];
-[PHBrandedCallingSwitchSpecifier setContext:];
-[PHBrandedCallingSwitchSpecifier configurationProvider];
-[PHBrandedCallingSwitchSpecifier context];
-[PHBrandedCallingSwitchSpecifier featureFlags];
-[PHBrandedCallingSwitchSpecifier setCtClient:];
-[PHBrandedCallingSwitchSpecifier getBrandedCallingEnabled];
-[PHBrandedCallingSwitchSpecifier initWithCoreTelephonyClient:context:];
-[PHBrandedCallingSwitchSpecifier initWithCoreTelephonyClient:context:carrierName:];
-[PHBrandedCallingSwitchSpecifier setBrandedCallingEnabled:];
```
