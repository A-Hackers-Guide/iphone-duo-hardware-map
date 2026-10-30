# `TPSPhonebookTelephonyController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPSTelephonyController`
- Protocols: `CoreTelephonyClientSuppServicesDelegate`
- 5 instance variables, 9 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"CTPhoneNumberInfo" _phoneNumberInfo;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
q _phoneBookEntryCount;
@"NSString" _updatePhoneNumber;
@? _updatePhoneNumberInfoCompletion;
```

## Properties

```
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (Tq,N,V_phoneBookEntryCount) phoneBookEntryCount;
@property (T@"CTPhoneNumberInfo",&,N,V_phoneNumberInfo) phoneNumberInfo;
@property (T@"NSString",C,N,V_updatePhoneNumber) updatePhoneNumber;
@property (T@?,C,N,V_updatePhoneNumberInfoCompletion) updatePhoneNumberInfoCompletion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSPhonebookTelephonyController phoneNumberChanged:];
-[TPSPhonebookTelephonyController init];
-[TPSPhonebookTelephonyController phoneBookSelected:];
-[TPSPhonebookTelephonyController initWithSubscriptionContext:];
-[TPSPhonebookTelephonyController subscriptionContext];
-[TPSPhonebookTelephonyController phoneNumberInfo];
-[TPSPhonebookTelephonyController updatePhoneNumberInfoCompletion];
-[TPSPhonebookTelephonyController fetchPhoneNumberInfo];
-[TPSPhonebookTelephonyController fetchPhoneNumberInfoWithCompletion:];
-[TPSPhonebookTelephonyController getPhoneNumberInfo];
-[TPSPhonebookTelephonyController getPhoneNumberInfoWithError:];
-[TPSPhonebookTelephonyController phoneBookEntryCount];
-[TPSPhonebookTelephonyController savePhoneBookEntryAtIndex:withContactName:contactNumber:];
-[TPSPhonebookTelephonyController savePhoneBookEntryAtIndex:withContactName:contactNumber:completion:];
-[TPSPhonebookTelephonyController selectPhoneBookWithName:password:completion:];
-[TPSPhonebookTelephonyController setPhoneBookEntryCount:];
-[TPSPhonebookTelephonyController setPhoneNumberInfo:];
-[TPSPhonebookTelephonyController setUpdatePhoneNumber:];
-[TPSPhonebookTelephonyController setUpdatePhoneNumberInfoCompletion:];
-[TPSPhonebookTelephonyController updatePhoneNumber];
-[TPSPhonebookTelephonyController updatePhoneNumberInfo:label:number:completion:];
```
