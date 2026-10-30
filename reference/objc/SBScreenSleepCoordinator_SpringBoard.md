# `SBScreenSleepCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"SBWindowSceneManager" _windowSceneManager;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBFUserAuthenticationController" _userAuthenticationController;
B _hasPlayedSoundForLock;
```

## Instance methods

```
-[SBScreenSleepCoordinator _shouldPlayLockSound];
-[SBScreenSleepCoordinator initWithWindowSceneManager:lockScreenCoordinator:userAuthenticationController:];
-[SBScreenSleepCoordinator playLockSoundIfPermitted];
-[SBScreenSleepCoordinator sleepAndLockUIFromSource:completion:];
-[SBScreenSleepCoordinator sleepAndLockUIFromSource:lockOptions:completion:];
```
