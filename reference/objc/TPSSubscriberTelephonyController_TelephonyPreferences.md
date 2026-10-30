# `TPSSubscriberTelephonyController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPSTelephonyController`
- Protocols: `CoreTelephonyClientSubscriberDelegate`
- 4 instance variables, 8 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _SIMPasscodeLockEnabled;
q _SIMPasscodeRemainingAttempts;
@"NSString" _SIMStatus;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
```

## Properties

```
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (TB,N,GisSIMPasscodeLockEnabled,V_SIMPasscodeLockEnabled) SIMPasscodeLockEnabled;
@property (Tq,N,V_SIMPasscodeRemainingAttempts) SIMPasscodeRemainingAttempts;
@property (T@"NSString",C,N,V_SIMStatus) SIMStatus;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSSubscriberTelephonyController simStatusDidChange:status:];
-[TPSSubscriberTelephonyController init];
-[TPSSubscriberTelephonyController SIMStatus];
-[TPSSubscriberTelephonyController setSIMStatus:];
-[TPSSubscriberTelephonyController initWithSubscriptionContext:];
-[TPSSubscriberTelephonyController simLockSaveRequestDidComplete:success:];
-[TPSSubscriberTelephonyController simPinChangeRequestDidComplete:success:];
-[TPSSubscriberTelephonyController simPinEntryErrorDidOccur:status:];
-[TPSSubscriberTelephonyController simPukEntryErrorDidOccur:status:];
-[TPSSubscriberTelephonyController subscriptionContext];
-[TPSSubscriberTelephonyController SIMPasscodeRemainingAttempts];
-[TPSSubscriberTelephonyController changePIN:newPin:];
-[TPSSubscriberTelephonyController changePIN:newPin:completion:];
-[TPSSubscriberTelephonyController fetchSIMPasscodeLockEnabled];
-[TPSSubscriberTelephonyController fetchSIMPasscodeLockEnabledWithCompletion:];
-[TPSSubscriberTelephonyController fetchSIMPasscodeRemainingAttempts];
-[TPSSubscriberTelephonyController fetchSIMPasscodeRemainingAttemptsWithCompletion:];
-[TPSSubscriberTelephonyController fetchSIMStatus];
-[TPSSubscriberTelephonyController fetchSIMStatusWithCompletion:];
-[TPSSubscriberTelephonyController getSIMPasscodeLockEnabledValue];
-[TPSSubscriberTelephonyController getSIMPasscodeLockEnabledValueWithError:];
-[TPSSubscriberTelephonyController getSIMPasscodeRemainingAttemptsValue];
-[TPSSubscriberTelephonyController getSIMPasscodeRemainingAttemptsValueWithError:];
-[TPSSubscriberTelephonyController getSIMStatus];
-[TPSSubscriberTelephonyController getSIMStatusWithError:];
-[TPSSubscriberTelephonyController isSIMPasscodeLockEnabled];
-[TPSSubscriberTelephonyController presentSIMPasscodeAlert];
-[TPSSubscriberTelephonyController setSIMLockEnabled:pin:];
-[TPSSubscriberTelephonyController setSIMLockEnabled:pin:completion:];
-[TPSSubscriberTelephonyController setSIMPasscodeLockEnabled:];
-[TPSSubscriberTelephonyController setSIMPasscodeRemainingAttempts:];
```
