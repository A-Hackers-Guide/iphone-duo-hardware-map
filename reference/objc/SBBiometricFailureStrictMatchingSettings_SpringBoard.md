# `SBBiometricFailureStrictMatchingSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
B _enabled;
q _failureThreshold;
```

## Properties

```
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (Tq,N,V_failureThreshold) failureThreshold;
```

## Class methods

```
+[SBBiometricFailureStrictMatchingSettings settingsControllerModule];
```

## Instance methods

```
-[SBBiometricFailureStrictMatchingSettings isEnabled];
-[SBBiometricFailureStrictMatchingSettings setDefaultValues];
-[SBBiometricFailureStrictMatchingSettings setEnabled:];
-[SBBiometricFailureStrictMatchingSettings failureThreshold];
-[SBBiometricFailureStrictMatchingSettings setFailureThreshold:];
```
