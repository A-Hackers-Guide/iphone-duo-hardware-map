# `SBAmbientProudLockViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBUIProudLockContainerViewControllerLockStatusProvider`
- 5 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBUIProudLockContainerViewController" _proudLockContainerViewController;
@"SBPropertyAnimatingView" _proudLockWrapperView;
@"SBUIBiometricResource" _biometricResource;
@"SBFUserAuthenticationController" _authenticationController;
@? _authenticationCompletion;
```

## Properties

```
@property (TB,R,N) hasPasscodeSet;
@property (TB,R,N) isBiometricLockedOut;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAmbientProudLockViewController init];
-[SBAmbientProudLockViewController viewDidLoad];
-[SBAmbientProudLockViewController _canShowWhileLocked];
-[SBAmbientProudLockViewController hasPasscodeSet];
-[SBAmbientProudLockViewController setAuthenticated:completion:];
-[SBAmbientProudLockViewController isBiometricLockedOut];
-[SBAmbientProudLockViewController _dismissTransientProudLockAnimated];
-[SBAmbientProudLockViewController _prepareBlurForWrapperView];
-[SBAmbientProudLockViewController initWithBiometricResource:authenticationController:];
```
