# `CTXPCServiceSubscriptionInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTXPCLogging`, `NSCopying`, `NSSecureCoding`
- 3 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _subscriptions;
@"NSArray" _subscriptionsInUse;
@"NSArray" _subscriptionsValid;
```

## Properties

```
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
@property (T@"NSArray",&,N,V_subscriptions) subscriptions;
@property (T@"NSArray",&,N,V_subscriptionsInUse) subscriptionsInUse;
@property (T@"NSArray",&,N,V_subscriptionsValid) subscriptionsValid;
```

## Class methods

```
+[CTXPCServiceSubscriptionInfo supportsSecureCoding];
```

## Instance methods

```
-[CTXPCServiceSubscriptionInfo subscriptions];
-[CTXPCServiceSubscriptionInfo ct_shortDescription];
-[CTXPCServiceSubscriptionInfo setSubscriptionsValid:];
-[CTXPCServiceSubscriptionInfo ct_shortName];
-[CTXPCServiceSubscriptionInfo setSubscriptionsInUse:];
-[CTXPCServiceSubscriptionInfo subscriptionsInUse];
-[CTXPCServiceSubscriptionInfo redactedDescription];
-[CTXPCServiceSubscriptionInfo encodeWithCoder:];
-[CTXPCServiceSubscriptionInfo subscriptionsValid];
-[CTXPCServiceSubscriptionInfo description];
-[CTXPCServiceSubscriptionInfo initWithCoder:];
-[CTXPCServiceSubscriptionInfo setSubscriptions:];
-[CTXPCServiceSubscriptionInfo copyWithZone:];
-[CTXPCServiceSubscriptionInfo isEqual:];
```
