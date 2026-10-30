# `_TtC25LocalAuthenticationCoreUI21LACUIRatchetViewModel`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTORatchetObserver`, `LACUIRatchetViewModelType`
- 17 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
LocalAuthenticationCoreUI.LACUIRatchetViewModelConfiguration configuration;
Swift.Bool isInvalidated;
LocalAuthenticationCoreUI.LACUIRatchetViewModel.State state;
Swift.Bool isRunning;
Combine.CurrentValueSubject LocalAuthenticationCoreUI.LACUIRatchetViewModel.State Swift.Never ? $__lazy_storage_$_stateSubject;
Combine.PassthroughSubject _$syyt Swift.Never ? $__lazy_storage_$_learnMoreSubject;
Combine.PassthroughSubject _$syyt Swift.Never ? $__lazy_storage_$_tapToRadarSubject;
_$sSD -> Swift.AnyHashable Any options;
(objc_protocol 0x28d598910) contextProvider;
_$sSSSg $__lazy_storage_$_ratchetIdentifier;
_$sSo20LACDTORatchetManagerC ratchetManager;
(objc_protocol 0x28d598918) ? $__lazy_storage_$_context;
_$sSayScTyyt Swift.Never tasks;
_$sScCySD -> Swift.AnyHashable _$sypGSg Swift.Error ? uiContinuation;
Foundation.Date ? expirationDate;
Foundation.Date ? gracePeriodExpirationDate;
Swift.Bool isStrictModeEnabled;
```

## Properties

```
@property (TB,N,VisInvalidated) isInvalidated;
```

## Class methods

```
+[_TtC25LocalAuthenticationCoreUI21LACUIRatchetViewModel mapError:];
```

## Instance methods

```
-[_TtC25LocalAuthenticationCoreUI21LACUIRatchetViewModel init];
-[_TtC25LocalAuthenticationCoreUI21LACUIRatchetViewModel dealloc];
-[_TtC25LocalAuthenticationCoreUI21LACUIRatchetViewModel start];
-[_TtC25LocalAuthenticationCoreUI21LACUIRatchetViewModel isInvalidated];
-[_TtC25LocalAuthenticationCoreUI21LACUIRatchetViewModel setIsInvalidated:];
-[_TtC25LocalAuthenticationCoreUI21LACUIRatchetViewModel ratchetStateDidChange:];
-[_TtC25LocalAuthenticationCoreUI21LACUIRatchetViewModel stopWithReason:invalidate:];
```
