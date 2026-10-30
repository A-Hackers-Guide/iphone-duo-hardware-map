# `SBPearlInterlockObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIBiometricResourceObserver`
- 2 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<SBUIBiometricResource>" _biometricResource;
B _fired;
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
-[SBPearlInterlockObserver deactivate];
-[SBPearlInterlockObserver activate];
-[SBPearlInterlockObserver _fire];
-[SBPearlInterlockObserver biometricResource:observeEvent:];
-[SBPearlInterlockObserver biometricResource:matchingEnabledDidChange:];
-[SBPearlInterlockObserver initWithBiometricResource:];
-[SBPearlInterlockObserver _checkForLockout];
```
