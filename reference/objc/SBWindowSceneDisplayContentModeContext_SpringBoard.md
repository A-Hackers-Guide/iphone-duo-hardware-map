# `SBWindowSceneDisplayContentModeContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBFDevicePoseProvider" _devicePoseProvider;
```

## Properties

```
@property (T@"SBDisplayContentModeCoordinator",W,N,V_displayContentModeCoordinator) displayContentModeCoordinator;
@property (T@"SBFDevicePoseProvider",W,N,V_devicePoseProvider) devicePoseProvider;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (Tq,R,N) currentContentMode;
```

## Instance methods

```
-[SBWindowSceneDisplayContentModeContext _windowScene];
-[SBWindowSceneDisplayContentModeContext phase];
-[SBWindowSceneDisplayContentModeContext isInteractive];
-[SBWindowSceneDisplayContentModeContext isTransitioning];
-[SBWindowSceneDisplayContentModeContext setDisplayContentModeCoordinator:];
-[SBWindowSceneDisplayContentModeContext devicePoseProvider];
-[SBWindowSceneDisplayContentModeContext windowScene];
-[SBWindowSceneDisplayContentModeContext displayContentModeCoordinator];
-[SBWindowSceneDisplayContentModeContext interactiveProgress];
-[SBWindowSceneDisplayContentModeContext continuousFoldPosition];
-[SBWindowSceneDisplayContentModeContext continuousFoldVelocity];
-[SBWindowSceneDisplayContentModeContext progressFromSwap];
-[SBWindowSceneDisplayContentModeContext progressToSwap];
-[SBWindowSceneDisplayContentModeContext _coordinator];
-[SBWindowSceneDisplayContentModeContext setDevicePoseProvider:];
-[SBWindowSceneDisplayContentModeContext _currentContext];
-[SBWindowSceneDisplayContentModeContext currentContentMode];
-[SBWindowSceneDisplayContentModeContext initWithWindowScene:displayContentModeCoordinator:devicePoseProvider:];
-[SBWindowSceneDisplayContentModeContext isAppliedDisplayContentModeUserInitiated];
-[SBWindowSceneDisplayContentModeContext isInvolvedInTransition];
-[SBWindowSceneDisplayContentModeContext swapTarget];
```
