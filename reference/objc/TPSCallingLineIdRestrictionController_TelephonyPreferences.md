# `TPSCallingLineIdRestrictionController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TPSRequestControllerDelegate`
- 5 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _editable;
@"<TPSCallingLineIdRestrictionControllerDelegate>" _delegate;
q _state;
@"TPSCallingLineIdRestrictionRequestController" _requestController;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
```

## Properties

```
@property (T@"TPSCallingLineIdRestrictionRequestController",R,N,V_requestController) requestController;
@property (TB,N,GisEditable,V_editable) editable;
@property (Tq,N,V_state) state;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (T@"<TPSCallingLineIdRestrictionControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSCallingLineIdRestrictionController isEditable];
-[TPSCallingLineIdRestrictionController setState:];
-[TPSCallingLineIdRestrictionController init];
-[TPSCallingLineIdRestrictionController setDelegate:];
-[TPSCallingLineIdRestrictionController delegate];
-[TPSCallingLineIdRestrictionController setEditable:];
-[TPSCallingLineIdRestrictionController state];
-[TPSCallingLineIdRestrictionController initWithSubscriptionContext:];
-[TPSCallingLineIdRestrictionController requestController];
-[TPSCallingLineIdRestrictionController subscriptionContext];
-[TPSCallingLineIdRestrictionController requestStateChange:];
-[TPSCallingLineIdRestrictionController requestController:didReceiveResponse:];
-[TPSCallingLineIdRestrictionController requestStateForSubscriptionContext:];
```
