# `SBUnintendedInteractionSuppressionSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"SBBiometricFailureStrictMatchingSettings" _biometricFailureStrictMatchingSettings;
@"SBDisplayTransitionBiometricSuppressionSettings" _displayTransitionBiometricSuppressionSettings;
@"SBHingeMotionDetectionSettings" _hingeMotionDetectionSettings;
```

## Properties

```
@property (T@"SBBiometricFailureStrictMatchingSettings",&,N,V_biometricFailureStrictMatchingSettings) biometricFailureStrictMatchingSettings;
@property (T@"SBDisplayTransitionBiometricSuppressionSettings",&,N,V_displayTransitionBiometricSuppressionSettings) displayTransitionBiometricSuppressionSettings;
@property (T@"SBHingeMotionDetectionSettings",&,N,V_hingeMotionDetectionSettings) hingeMotionDetectionSettings;
```

## Class methods

```
+[SBUnintendedInteractionSuppressionSettings settingsControllerModule];
```

## Instance methods

```
-[SBUnintendedInteractionSuppressionSettings setDefaultValues];
-[SBUnintendedInteractionSuppressionSettings biometricFailureStrictMatchingSettings];
-[SBUnintendedInteractionSuppressionSettings displayTransitionBiometricSuppressionSettings];
-[SBUnintendedInteractionSuppressionSettings hingeMotionDetectionSettings];
-[SBUnintendedInteractionSuppressionSettings setBiometricFailureStrictMatchingSettings:];
-[SBUnintendedInteractionSuppressionSettings setDisplayTransitionBiometricSuppressionSettings:];
-[SBUnintendedInteractionSuppressionSettings setHingeMotionDetectionSettings:];
```
