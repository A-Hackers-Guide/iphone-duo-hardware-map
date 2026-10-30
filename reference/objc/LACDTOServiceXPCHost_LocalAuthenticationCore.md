# `LACDTOServiceXPCHost`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOServiceXPC`
- 5 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOFeatureControlling>" _featureController;
@"<LACDTORatchetStateProvider>" _ratchetStateProvider;
@"<LACDTORatchetHandler>" _ratchetHandler;
@"<LACDTOSensorTrustStateProvider>" _trustStateProvider;
@"<LACDTOPendingPolicyEvaluationController>" _pendingEvaluationController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOServiceXPCHost checkCanEnableFeatureWithCompletion:];
-[LACDTOServiceXPCHost disableExtendedPolicyProtectionWithContext:completion:];
-[LACDTOServiceXPCHost disableFeatureStrictModeWithContext:completion:];
-[LACDTOServiceXPCHost disableFeatureWithContext:completion:];
-[LACDTOServiceXPCHost enableExtendedPolicyProtectionWithCompletion:];
-[LACDTOServiceXPCHost enableFeatureStrictModeWithCompletion:];
-[LACDTOServiceXPCHost resetRatchetWithReason:completion:];
-[LACDTOServiceXPCHost cancelPendingEvaluationWithRatchetIdentifier:reason:completion:];
-[LACDTOServiceXPCHost checkIsAutoEnablementAllowedWithCompletion:];
-[LACDTOServiceXPCHost checkIsExtendedPolicyProtectionAvailableWithCompletion:];
-[LACDTOServiceXPCHost checkIsExtendedPolicyProtectionEnabledWithCompletion:];
-[LACDTOServiceXPCHost checkIsFeatureAvailableWithCompletion:];
-[LACDTOServiceXPCHost checkIsFeatureEnabledWithCompletion:];
-[LACDTOServiceXPCHost checkIsFeatureStrictModeEnabledWithCompletion:];
-[LACDTOServiceXPCHost checkIsFeatureSupportedWithCompletion:];
-[LACDTOServiceXPCHost checkIsSensorTrustedWithCompletion:];
-[LACDTOServiceXPCHost enableFeatureWithOptions:completion:];
-[LACDTOServiceXPCHost initWithFeatureController:ratchetStateProvider:ratchetHandler:trustStateProvider:pendingEvaluationController:];
-[LACDTOServiceXPCHost ratchetStateCompositeWithCompletion:];
-[LACDTOServiceXPCHost ratchetStateWithCompletion:];
```
