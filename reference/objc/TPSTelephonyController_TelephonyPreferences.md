# `TPSTelephonyController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPSController`
- Protocols: `CoreTelephonyClientDelegate`
- 6 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accessorLock;
@"NSOrderedSet" _activeSubscriptions;
@"NSOrderedSet" _subscriptions;
@"NSDictionary" _systemCapabilities;
@"CoreTelephonyClient" _telephonyClient;
@"NSObject<OS_dispatch_queue>" _serialDispatchQueue;
```

## Properties

```
@property (T{os_unfair_lock_s=I},N,V_accessorLock) accessorLock;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_serialDispatchQueue) serialDispatchQueue;
@property (T@"NSOrderedSet",C,N,V_activeSubscriptions) activeSubscriptions;
@property (T@"NSOrderedSet",C,N,V_subscriptions) subscriptions;
@property (T@"NSDictionary",C,N,V_systemCapabilities) systemCapabilities;
@property (T@"CoreTelephonyClient",R,N,V_telephonyClient) telephonyClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSTelephonyController accessorLock];
-[TPSTelephonyController subscriptions];
-[TPSTelephonyController init];
-[TPSTelephonyController context:capabilitiesChanged:];
-[TPSTelephonyController performAtomicAccessorBlock:];
-[TPSTelephonyController setSubscriptions:];
-[TPSTelephonyController telephonyClient];
-[TPSTelephonyController activeSubscriptions];
-[TPSTelephonyController fetchSubscriptionsInUse];
-[TPSTelephonyController supportsSystemCapabilityWithName:subscriptionContext:];
-[TPSTelephonyController systemCapabilitiesForSubscriptionContext:];
-[TPSTelephonyController serialDispatchQueue];
-[TPSTelephonyController setActiveSubscriptions:];
-[TPSTelephonyController fetchNonHiddenSubscriptions];
-[TPSTelephonyController fetchSubscriptions];
-[TPSTelephonyController fetchSystemCapabilitiesForSubscriptions:];
-[TPSTelephonyController isSubscriptionOrderedSet:equivalentToSubscriptionOrderedSet:];
-[TPSTelephonyController setAccessorLock:];
-[TPSTelephonyController setSystemCapabilities:];
-[TPSTelephonyController supportsCellularNetworkSelectionForSubscriptionContext:];
-[TPSTelephonyController supportsSystemCapabilityCallForwardingForSubscriptionContext:];
-[TPSTelephonyController supportsSystemCapabilityCallWaitingForSubscriptionContext:];
-[TPSTelephonyController supportsSystemCapabilityCallerIDForSubscriptionContext:];
-[TPSTelephonyController systemCapabilities];
-[TPSTelephonyController systemCapabilitiesForSubscriptionContext:error:];
```
