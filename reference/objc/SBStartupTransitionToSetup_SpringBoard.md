# `SBStartupTransitionToSetup`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBBaseStartupTransition`
- 5 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"SBBannerManager" _bannerManager;
@"SBFUserAuthenticationController" _authController;
@"SBApplicationController" _appController;
@"SBSetupManager" _setupManager;
@"SBInitialRestartState" _initialRestartState;
```

## Instance methods

```
-[SBStartupTransitionToSetup _activateSetupWithCompletion:underLock:fromSnapshot:];
-[SBStartupTransitionToSetup initWithDestination:context:];
-[SBStartupTransitionToSetup initWithDestination:context:initialRestartState:];
-[SBStartupTransitionToSetup performTransitionWithCompletionBlock:];
```
