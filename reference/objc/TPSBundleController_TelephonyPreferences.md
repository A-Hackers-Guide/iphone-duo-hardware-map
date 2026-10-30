# `TPSBundleController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSBundleController`
- 4 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _supportsDisabledSubscriptions;
@"TPSTelephonyController" _telephonyController;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
@"NSArray" _specifiers;
```

## Properties

```
@property (T@"CTXPCServiceSubscriptionContext",&,N,V_subscriptionContext) subscriptionContext;
@property (T@"NSArray",C,N,V_specifiers) specifiers;
@property (T@"PSListController",R,W,N) parentListController;
@property (T@"TPSTelephonyController",R,N,V_telephonyController) telephonyController;
@property (T@"NSOrderedSet",R,C,N) subscriptions;
@property (T@"NSOrderedSet",R,C,N) supportedSubscriptions;
@property (TB,R,N,V_supportsDisabledSubscriptions) supportsDisabledSubscriptions;
@property (TB,R,N,GisHidden) hidden;
@property (TB,R,N,GisSubscriptionListHidden) subscriptionListHidden;
```

## Instance methods

```
-[TPSBundleController subscriptions];
-[TPSBundleController isHidden];
-[TPSBundleController specifiers];
-[TPSBundleController setSpecifiers:];
-[TPSBundleController initWithParentListController:];
-[TPSBundleController specifiersWithSpecifier:];
-[TPSBundleController setSubscriptionContext:];
-[TPSBundleController subscriptionContext];
-[TPSBundleController parentListController];
-[TPSBundleController telephonyController];
-[TPSBundleController telephonyController:didChangeActiveSubscriptions:];
-[TPSBundleController telephonyController:didChangeSubscriptions:];
-[TPSBundleController isSubscriptionListHidden];
-[TPSBundleController subscriptionContextForSpecifier:];
-[TPSBundleController supportedSubscriptions];
-[TPSBundleController supportsDisabledSubscriptions];
```
