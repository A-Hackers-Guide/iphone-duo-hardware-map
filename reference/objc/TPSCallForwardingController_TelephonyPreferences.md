# `TPSCallForwardingController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TPSCarrierBundleControllerDelegate`, `TPSRequestControllerDelegate`
- 14 instance variables, 33 properties, 56 instance methods, 0 class methods

## Instance variables

```
B _unloading;
@"NSArray" _conditionalServiceRequests;
@"NSString" _subscriptionISOCountryCode;
@"NSArray" _unconditionalServiceRequests;
@"<TPSCallForwardingControllerDelegate>" _delegate;
@"TPSCarrierBundleController" _carrierBundleController;
@"TPSCallForwardingRequestController" _requestController;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
q _currentServiceType;
q _pendingServiceType;
@"CTCallForwardingValue" _conditionalServiceBusyValue;
@"CTCallForwardingValue" _conditionalServiceUnansweredValue;
@"CTCallForwardingValue" _conditionalServiceUnreachableValue;
@"CTCallForwardingValue" _unconditionalServiceValue;
```

## Properties

```
@property (TB,N,GisUnloading,V_unloading) unloading;
@property (T@"TPSCarrierBundleController",R,N,V_carrierBundleController) carrierBundleController;
@property (T@"TPSCallForwardingRequestController",R,N,V_requestController) requestController;
@property (T@"NSDictionary",R,C,N) carrierBundleLocalizedStringKeys;
@property (T@"NSString",R,C,N,V_subscriptionISOCountryCode) subscriptionISOCountryCode;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (Tq,N,V_currentServiceType) currentServiceType;
@property (Tq,N,V_pendingServiceType) pendingServiceType;
@property (TB,R,N,GisConditionalServiceLoading) conditionalServiceLoading;
@property (T@"NSArray",R,C,N,V_conditionalServiceRequests) conditionalServiceRequests;
@property (T@"CTCallForwardingValue",&,N,V_conditionalServiceBusyValue) conditionalServiceBusyValue;
@property (T@"CTCallForwardingValue",&,N,V_conditionalServiceUnansweredValue) conditionalServiceUnansweredValue;
@property (T@"CTCallForwardingValue",&,N,V_conditionalServiceUnreachableValue) conditionalServiceUnreachableValue;
@property (TB,R,N,GisUnconditionalServiceLoading) unconditionalServiceLoading;
@property (T@"NSArray",R,C,N,V_unconditionalServiceRequests) unconditionalServiceRequests;
@property (T@"CTCallForwardingValue",&,N,V_unconditionalServiceValue) unconditionalServiceValue;
@property (TB,R,N,GisLoading) loading;
@property (T@"<TPSCallForwardingControllerDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N) serviceType;
@property (TB,R,N,GisConditionalServiceAvailable) conditionalServiceAvailable;
@property (Tq,R,N) conditionalServiceState;
@property (T@"NSString",C,N) conditionalServiceBusyPhoneNumber;
@property (T@"NSString",C,N) conditionalServiceUnansweredPhoneNumber;
@property (T@"NSString",C,N) conditionalServiceUnreachablePhoneNumber;
@property (T@"NSString",R,C,N) localizedConditionalBusyTitle;
@property (T@"NSString",R,C,N) localizedConditionalUnansweredTitle;
@property (T@"NSString",R,C,N) localizedConditionalUnreachableTitle;
@property (Tq,R,N) unconditionalServiceState;
@property (T@"NSString",C,N) unconditionalServicePhoneNumber;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSCallForwardingController init];
-[TPSCallForwardingController setDelegate:];
-[TPSCallForwardingController delegate];
-[TPSCallForwardingController isLoading];
-[TPSCallForwardingController serviceType];
-[TPSCallForwardingController initWithSubscriptionContext:];
-[TPSCallForwardingController carrierBundleController];
-[TPSCallForwardingController requestController];
-[TPSCallForwardingController subscriptionContext];
-[TPSCallForwardingController unconditionalServicePhoneNumber];
-[TPSCallForwardingController setConditionalServiceBusyValue:];
-[TPSCallForwardingController carrierBundleLocalizedStringKeys];
-[TPSCallForwardingController conditionalServiceBusyPhoneNumber];
-[TPSCallForwardingController conditionalServiceBusyValue];
-[TPSCallForwardingController conditionalServiceRequests];
-[TPSCallForwardingController conditionalServiceState];
-[TPSCallForwardingController conditionalServiceUnansweredPhoneNumber];
-[TPSCallForwardingController conditionalServiceUnansweredValue];
-[TPSCallForwardingController conditionalServiceUnreachablePhoneNumber];
-[TPSCallForwardingController conditionalServiceUnreachableValue];
-[TPSCallForwardingController currentServiceType];
-[TPSCallForwardingController enableConditionalServiceIfNeeded];
-[TPSCallForwardingController enableUnconditionalServiceIfNeeded];
-[TPSCallForwardingController isConditionalServiceAvailable];
-[TPSCallForwardingController isConditionalServiceLoading];
-[TPSCallForwardingController isUnconditionalServiceLoading];
-[TPSCallForwardingController isUnloading];
-[TPSCallForwardingController localizedCarrierBundleStringForKey:];
-[TPSCallForwardingController localizedConditionalBusyTitle];
-[TPSCallForwardingController localizedConditionalUnansweredTitle];
-[TPSCallForwardingController localizedConditionalUnreachableTitle];
-[TPSCallForwardingController pendingServiceType];
-[TPSCallForwardingController requestController:didReceiveResponse:];
-[TPSCallForwardingController resetPendingServiceType];
-[TPSCallForwardingController sendConditionalServicesRequest];
-[TPSCallForwardingController sendEnableSetRequestForValue:];
-[TPSCallForwardingController sendServicesRequest];
-[TPSCallForwardingController sendSetAllServicesDisabledRequest];
-[TPSCallForwardingController sendSetRequestForValue:];
-[TPSCallForwardingController sendSetUnconditionalServiceDisabledRequest];
-[TPSCallForwardingController sendUnconditionalServicesRequest];
-[TPSCallForwardingController setConditionalServiceBusyPhoneNumber:];
-[TPSCallForwardingController setConditionalServiceUnansweredPhoneNumber:];
-[TPSCallForwardingController setConditionalServiceUnansweredValue:];
-[TPSCallForwardingController setConditionalServiceUnreachablePhoneNumber:];
-[TPSCallForwardingController setConditionalServiceUnreachableValue:];
-[TPSCallForwardingController setCurrentServiceType:];
-[TPSCallForwardingController setPendingServiceType:];
-[TPSCallForwardingController setUnconditionalServicePhoneNumber:];
-[TPSCallForwardingController setUnconditionalServiceValue:];
-[TPSCallForwardingController setUnloading:];
-[TPSCallForwardingController subscriptionISOCountryCode];
-[TPSCallForwardingController unconditionalServiceRequests];
-[TPSCallForwardingController unconditionalServiceState];
-[TPSCallForwardingController unconditionalServiceValue];
-[TPSCallForwardingController updateServiceType:];
```
