# `TPSResponse`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TPSSecureObject`
- 2 instance variables, 6 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"NSError" _error;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
```

## Properties

```
@property (T@"NSError",&,N,V_error) error;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TPSResponse supportsSecureCoding];
+[TPSResponse unarchivedObjectClasses];
+[TPSResponse unarchivedObjectFromData:error:];
```

## Instance methods

```
-[TPSResponse setError:];
-[TPSResponse debugDescription];
-[TPSResponse init];
-[TPSResponse archivedDataWithError:];
-[TPSResponse error];
-[TPSResponse encodeWithCoder:];
-[TPSResponse hash];
-[TPSResponse description];
-[TPSResponse initWithCoder:];
-[TPSResponse copyWithZone:];
-[TPSResponse isEqual:];
-[TPSResponse isEqualToResponse:];
-[TPSResponse subscriptionContext];
-[TPSResponse initWithSubscriptionContext:error:];
```
