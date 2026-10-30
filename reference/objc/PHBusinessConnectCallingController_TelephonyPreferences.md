# `PHBusinessConnectCallingController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `TPSCarrierBundleControllerDelegate`, `TUConfigurationProviderDelegate`
- 3 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"TPSCarrierBundleController" _carrierBundleController;
@"TUConfigurationProvider" _configurationProvider;
@"TUFeatureFlags" _featureFlags;
```

## Properties

```
@property (T@"TPSCarrierBundleController",R,N,V_carrierBundleController) carrierBundleController;
@property (T@"TUConfigurationProvider",R,N,V_configurationProvider) configurationProvider;
@property (T@"TUFeatureFlags",R,N,V_featureFlags) featureFlags;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PHBusinessConnectCallingController setBusinessConnectCallingEnabled:];
-[PHBusinessConnectCallingController init];
-[PHBusinessConnectCallingController getBooleanFromUserDefaults:default:];
-[PHBusinessConnectCallingController configurationProvider];
-[PHBusinessConnectCallingController objectForKeyHierarchy:subscriptionContext:error:];
-[PHBusinessConnectCallingController setValueInUserDefaults:forKey:];
-[PHBusinessConnectCallingController featureFlags];
-[PHBusinessConnectCallingController specifiers];
-[PHBusinessConnectCallingController carrierBundleController];
-[PHBusinessConnectCallingController configurationChanged];
-[PHBusinessConnectCallingController stringForKeyHierarchy:subscriptionContext:error:];
-[PHBusinessConnectCallingController supportsBusinessConnectCallingForSubscriptionContext:];
-[PHBusinessConnectCallingController getBusinessConnectCallingEnabled];
```
