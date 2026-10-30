# `LACDTORatchetManager`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDarwinNotificationCenterObserver`
- 3 instance variables, 12 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"<LACDTOServiceXPCClient>" _remoteObjectProxy;
@"<LACDarwinNotificationCenter>" _notificationCenter;
```

## Properties

```
@property (TB,R,N) isFeatureEnabled;
@property (TB,R,N) isFeatureSupported;
@property (TB,R,N) isFeatureAvailable;
@property (TB,R,N) isFeatureStrictModeEnabled;
@property (TB,R,N) isExtendedPolicyProtectionAvailable;
@property (TB,R,N) isExtendedPolicyProtectionEnabled;
@property (TB,R,N) isSensorTrusted;
@property (T@"LACDTORatchetState",R,N) ratchetState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTORatchetManager removeObserver:];
-[LACDTORatchetManager reset];
-[LACDTORatchetManager addObserver:];
-[LACDTORatchetManager isFeatureSupported];
-[LACDTORatchetManager isExtendedPolicyProtectionEnabled];
-[LACDTORatchetManager initWithContextProvider:];
-[LACDTORatchetManager isExtendedPolicyProtectionAvailable];
-[LACDTORatchetManager isFeatureEnabled];
-[LACDTORatchetManager _remoteObjectProxyWithErrorHandler:];
-[LACDTORatchetManager ratchetState];
-[LACDTORatchetManager isFeatureAvailable];
-[LACDTORatchetManager stateWithCompletion:];
-[LACDTORatchetManager enableFeatureWithOptions:reply:];
-[LACDTORatchetManager isSensorTrusted];
-[LACDTORatchetManager cancelArmRequestWithIdentifier:reason:completion:];
-[LACDTORatchetManager checkCanEnableFeatureWithCompletion:];
-[LACDTORatchetManager disableExtendedPolicyProtectionWithContext:completion:];
-[LACDTORatchetManager disableFeatureStrictModeWithContext:completion:];
-[LACDTORatchetManager disableFeatureWithContext:completion:];
-[LACDTORatchetManager enableExtendedPolicyProtectionWithCompletion:];
-[LACDTORatchetManager enableFeatureStrictModeWithCompletion:];
-[LACDTORatchetManager isAutoEnablementAllowed:];
-[LACDTORatchetManager isFeatureStrictModeEnabled];
-[LACDTORatchetManager performArmRequestWithContext:options:completion:];
-[LACDTORatchetManager resetRatchetWithReason:completion:];
-[LACDTORatchetManager stateInContext:completion:];
-[LACDTORatchetManager _armPolicy];
-[LACDTORatchetManager _performArmRequestWithContext:options:completion:];
-[LACDTORatchetManager notificationCenter:didReceiveNotification:];
-[LACDTORatchetManager stateCompositeInContext:completion:];
-[LACDTORatchetManager stateCompositeWithCompletion:];
```
