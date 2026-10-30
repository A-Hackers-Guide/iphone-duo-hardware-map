# `PHCallBlockingServiceProviderController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TPSCarrierBundleControllerDelegate`
- 4 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _serviceProviders;
@"<PHCallBlockingServiceProviderControllerDelegate>" _delegate;
@"TPSCarrierBundleController" _carrierBundleController;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"TPSCarrierBundleController",R,N,V_carrierBundleController) carrierBundleController;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSArray",C,N,V_serviceProviders) serviceProviders;
@property (T@"<PHCallBlockingServiceProviderControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,C,N) serviceProvidersSupportingSpamBlocking;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PHCallBlockingServiceProviderController init];
-[PHCallBlockingServiceProviderController queue];
-[PHCallBlockingServiceProviderController setDelegate:];
-[PHCallBlockingServiceProviderController delegate];
-[PHCallBlockingServiceProviderController objectForKeyHierarchy:subscriptionContext:error:];
-[PHCallBlockingServiceProviderController carrierBundleController];
-[PHCallBlockingServiceProviderController stringForKeyHierarchy:subscriptionContext:error:];
-[PHCallBlockingServiceProviderController supportsCallBlockingForSubscriptionContext:];
-[PHCallBlockingServiceProviderController carrierBundleController:carrierBundleDidChangeForSubscriptionContext:];
-[PHCallBlockingServiceProviderController fetchServiceProviders];
-[PHCallBlockingServiceProviderController serviceProviders];
-[PHCallBlockingServiceProviderController serviceProvidersSupportingSpamBlocking];
-[PHCallBlockingServiceProviderController setServiceProviders:];
```
