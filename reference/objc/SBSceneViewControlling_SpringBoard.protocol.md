# `SBSceneViewControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"SBSceneHandle",R,N) sceneHandle;
@property (Tq,R,N) displayMode;
@property (T@"<SBScenePlaceholderContentContext>",&,N) placeholderContentContext;
@property (T@"UIView",&,N) customContentView;
@property (T{CGSize=dd},R,N) contentReferenceSize;
@property (Tq,R,N) contentOrientation;
@property (Tq,R,N) containerOrientation;
```

## Instance methods

```
-[SBSceneViewControlling customContentView];
-[SBSceneViewControlling setCustomContentView:];
-[SBSceneViewControlling containerOrientation];
-[SBSceneViewControlling sceneHandle];
-[SBSceneViewControlling setPlaceholderContentContext:];
-[SBSceneViewControlling beginInteractiveDisplayModeTransitionToMode:];
-[SBSceneViewControlling contentOrientation];
-[SBSceneViewControlling displayMode];
-[SBSceneViewControlling containerContentWrapperInterfaceOrientationChangedTo:];
-[SBSceneViewControlling setContentReferenceSize:withContentOrientation:andContainerOrientation:];
-[SBSceneViewControlling invalidate];
-[SBSceneViewControlling endInteractiveDisplayModeTransitionAtMode:];
-[SBSceneViewControlling setDisplayMode:animationFactory:completion:];
-[SBSceneViewControlling contentReferenceSize];
-[SBSceneViewControlling placeholderContentContext];
-[SBSceneViewControlling updateInteractiveDisplayModeTransitionProgress:];
```
