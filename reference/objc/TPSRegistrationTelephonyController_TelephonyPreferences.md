# `TPSRegistrationTelephonyController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPSTelephonyController`
- Protocols: `CoreTelephonyClientRegistrationDelegate`
- 3 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _networks;
@"CTNetworkSelectionInfo" _networkSelectionInfo;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
```

## Properties

```
@property (T@"NSArray",C,N,V_networks) networks;
@property (T@"CTNetworkSelectionInfo",&,N,V_networkSelectionInfo) networkSelectionInfo;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSRegistrationTelephonyController setNetworks:];
-[TPSRegistrationTelephonyController networkSelected:success:mode:];
-[TPSRegistrationTelephonyController init];
-[TPSRegistrationTelephonyController networks];
-[TPSRegistrationTelephonyController initWithSubscriptionContext:];
-[TPSRegistrationTelephonyController networkListAvailable:list:];
-[TPSRegistrationTelephonyController performDelegateSelector:];
-[TPSRegistrationTelephonyController subscriptionContext];
-[TPSRegistrationTelephonyController fetchNetworkList];
-[TPSRegistrationTelephonyController selectNetwork:];
-[TPSRegistrationTelephonyController fetchNetworkListWithCompletion:];
-[TPSRegistrationTelephonyController automaticallySelectNetwork];
-[TPSRegistrationTelephonyController automaticallySelectNetworkWithCompletion:];
-[TPSRegistrationTelephonyController copyNetworkSelectionInfo];
-[TPSRegistrationTelephonyController networkSelectionInfo];
-[TPSRegistrationTelephonyController networksWithCompletionHandler:];
-[TPSRegistrationTelephonyController selectNetwork:completion:];
-[TPSRegistrationTelephonyController setNetworkSelectionInfo:];
```
