# `LACDTOServiceXPC` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance methods

```
-[LACDTOServiceXPC checkCanEnableFeatureWithCompletion:];
-[LACDTOServiceXPC disableExtendedPolicyProtectionWithContext:completion:];
-[LACDTOServiceXPC disableFeatureStrictModeWithContext:completion:];
-[LACDTOServiceXPC disableFeatureWithContext:completion:];
-[LACDTOServiceXPC enableExtendedPolicyProtectionWithCompletion:];
-[LACDTOServiceXPC enableFeatureStrictModeWithCompletion:];
-[LACDTOServiceXPC resetRatchetWithReason:completion:];
-[LACDTOServiceXPC cancelPendingEvaluationWithRatchetIdentifier:reason:completion:];
-[LACDTOServiceXPC checkIsAutoEnablementAllowedWithCompletion:];
-[LACDTOServiceXPC checkIsExtendedPolicyProtectionAvailableWithCompletion:];
-[LACDTOServiceXPC checkIsExtendedPolicyProtectionEnabledWithCompletion:];
-[LACDTOServiceXPC checkIsFeatureAvailableWithCompletion:];
-[LACDTOServiceXPC checkIsFeatureEnabledWithCompletion:];
-[LACDTOServiceXPC checkIsFeatureStrictModeEnabledWithCompletion:];
-[LACDTOServiceXPC checkIsFeatureSupportedWithCompletion:];
-[LACDTOServiceXPC checkIsSensorTrustedWithCompletion:];
-[LACDTOServiceXPC enableFeatureWithOptions:completion:];
-[LACDTOServiceXPC ratchetStateCompositeWithCompletion:];
-[LACDTOServiceXPC ratchetStateWithCompletion:];
```
