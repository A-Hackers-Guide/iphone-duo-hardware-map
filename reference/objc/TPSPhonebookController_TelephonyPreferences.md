# `TPSPhonebookController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TPSPhonebookTelephonyControllerDelegate`
- 4 instance variables, 10 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _subscriptionISOCountryCode;
@"<TPSPhonebookControllerDelegate>" _delegate;
@"TPSPhonebookTelephonyController" _telephonyClient;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
```

## Properties

```
@property (T@"TPSPhonebookTelephonyController",R,N,V_telephonyClient) telephonyClient;
@property (T@"NSString",R,C,N,V_subscriptionISOCountryCode) subscriptionISOCountryCode;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (T@"<TPSPhonebookControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisSubscriptionEditable) subscriptionEditable;
@property (T@"NSString",R,C,N) localizedSubscriptionTelephoneNumber;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSPhonebookController init];
-[TPSPhonebookController setDelegate:];
-[TPSPhonebookController delegate];
-[TPSPhonebookController telephonyClient];
-[TPSPhonebookController initWithSubscriptionContext:];
-[TPSPhonebookController subscriptionContext];
-[TPSPhonebookController isSubscriptionEditable];
-[TPSPhonebookController localizedSubscriptionTelephoneNumber];
-[TPSPhonebookController phonebookController:didChangePhoneNumberInfo:];
-[TPSPhonebookController subscriptionISOCountryCode];
-[TPSPhonebookController updateSubscriptionTelephoneNumber:completion:];
```
