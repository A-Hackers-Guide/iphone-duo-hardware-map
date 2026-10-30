# `TPSCallWaitingController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TPSRequestControllerDelegate`
- 4 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<TPSCallWaitingControllerDelegate>" _delegate;
q _state;
@"TPSCallWaitingRequestController" _requestController;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
```

## Properties

```
@property (T@"TPSCallWaitingRequestController",R,N,V_requestController) requestController;
@property (Tq,N,V_state) state;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (T@"<TPSCallWaitingControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSCallWaitingController setState:];
-[TPSCallWaitingController init];
-[TPSCallWaitingController setDelegate:];
-[TPSCallWaitingController delegate];
-[TPSCallWaitingController state];
-[TPSCallWaitingController initWithSubscriptionContext:];
-[TPSCallWaitingController requestController];
-[TPSCallWaitingController subscriptionContext];
-[TPSCallWaitingController requestStateChange:];
-[TPSCallWaitingController requestController:didReceiveResponse:];
```
