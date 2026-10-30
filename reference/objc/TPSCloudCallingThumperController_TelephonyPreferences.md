# `TPSCloudCallingThumperController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"<TPSCloudCallingThumperControllerDelegate>" _delegate;
@"TUSenderIdentityCapabilities" _subscriptionCapabilities;
@"TPSCarrierBundleController" _carrierBundleController;
@"NSDictionary" _encryptedIdentityInfo;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
```

## Properties

```
@property (T@"TPSCarrierBundleController",&,N,V_carrierBundleController) carrierBundleController;
@property (T@"NSDictionary",C,N,V_encryptedIdentityInfo) encryptedIdentityInfo;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (T@"TUSenderIdentityCapabilities",&,N,V_subscriptionCapabilities) subscriptionCapabilities;
@property (T@"<TPSCloudCallingThumperControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisThumperCallingEnabled) thumperCallingEnabled;
@property (T@"NSString",R,C,N) localizedCarrierName;
```

## Instance methods

```
-[TPSCloudCallingThumperController init];
-[TPSCloudCallingThumperController setDelegate:];
-[TPSCloudCallingThumperController delegate];
-[TPSCloudCallingThumperController setThumperCallingEnabled:];
-[TPSCloudCallingThumperController isThumperCallingEnabled];
-[TPSCloudCallingThumperController initWithSubscriptionContext:];
-[TPSCloudCallingThumperController carrierBundleController];
-[TPSCloudCallingThumperController subscriptionContext];
-[TPSCloudCallingThumperController subscriptionCapabilities];
-[TPSCloudCallingThumperController encryptedIdentityInfo];
-[TPSCloudCallingThumperController localizedCarrierName];
-[TPSCloudCallingThumperController setCarrierBundleController:];
-[TPSCloudCallingThumperController setEncryptedIdentityInfo:];
-[TPSCloudCallingThumperController setSubscriptionCapabilities:];
```
