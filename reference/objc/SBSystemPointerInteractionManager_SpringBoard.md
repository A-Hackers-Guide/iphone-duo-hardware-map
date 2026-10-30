# `SBSystemPointerInteractionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBMultiDisplayPointerInteractionObserver`, `UIPointerInteractionDelegate`
- 4 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _registeredViewsToDelegates;
@"NSHashTable" _observers;
@"SBMultiDisplayUserInteractionCoordinator" _multiDisplayUserInteractionCoordinator;
@"UIView" _activePointerRegionView;
```

## Properties

```
@property (T@"UIView",R,N,V_activePointerRegionView) activePointerRegionView;
@property (T@"SBWindowScene",R,W,N) activePointerWindowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemPointerInteractionManager removeObserver:];
-[SBSystemPointerInteractionManager dealloc];
-[SBSystemPointerInteractionManager unregisterView:];
-[SBSystemPointerInteractionManager addObserver:];
-[SBSystemPointerInteractionManager registerView:delegate:];
-[SBSystemPointerInteractionManager activePointerRegionView];
-[SBSystemPointerInteractionManager activePointerWindowScene];
-[SBSystemPointerInteractionManager initWithMultiDisplayUserInteractionCoordinator:];
-[SBSystemPointerInteractionManager isViewRegistered:];
-[SBSystemPointerInteractionManager pointerDidMoveToFromWindowScene:toWindowScene:];
-[SBSystemPointerInteractionManager pointerInteraction:window:regionForRequest:defaultRegion:];
-[SBSystemPointerInteractionManager pointerInteraction:window:styleForRegion:];
-[SBSystemPointerInteractionManager pointerInteraction:window:willEnterRegion:animator:];
-[SBSystemPointerInteractionManager pointerInteraction:window:willExitRegion:animator:];
```
