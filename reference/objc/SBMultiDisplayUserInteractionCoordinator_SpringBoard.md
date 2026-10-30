# `SBMultiDisplayUserInteractionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBPointerTouchDownEventSnifferDelegate`, `_SBTouchInteractionEventSnifferDelegate`, `_SBPointerInteractionEventSnifferDelegate`, `_SBScrollEventSnifferDelegate`, `_SBContinuityTouchEventSnifferDelegate`, `SBDisplayContentModeTransitionObserver`, `SBActiveWindowSceneTracking`, `SBWindowSceneAttachmentObserving`
- 7 instance variables, 11 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _activeDisplayWindowScene;
@"SBWindowScene" _activePointerWindowScene;
@"<SBMultiDisplayUserInteractionCoordinatorDelegate>" _delegate;
@"SBWindowScene" _activeTouchDownOriginatedWindowScene;
@"NSMapTable" _sceneToEventSniffers;
@"NSHashTable" _activeWindowSceneObservers;
@"NSHashTable" _pointerInteractionObservers;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_sceneToEventSniffers) sceneToEventSniffers;
@property (T@"NSHashTable",&,N,V_activeWindowSceneObservers) activeWindowSceneObservers;
@property (T@"NSHashTable",&,N,V_pointerInteractionObservers) pointerInteractionObservers;
@property (T@"SBWindowScene",R,W,N) activePointerWindowScene;
@property (T@"<SBMultiDisplayUserInteractionCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (T@"SBWindowScene",R,W,N,V_activeTouchDownOriginatedWindowScene) activeTouchDownOriginatedWindowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBWindowScene",R,W,N) activeWindowScene;
```

## Instance methods

```
-[SBMultiDisplayUserInteractionCoordinator activeWindowScene];
-[SBMultiDisplayUserInteractionCoordinator init];
-[SBMultiDisplayUserInteractionCoordinator windowSceneDidDisconnect:];
-[SBMultiDisplayUserInteractionCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBMultiDisplayUserInteractionCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBMultiDisplayUserInteractionCoordinator setDelegate:];
-[SBMultiDisplayUserInteractionCoordinator delegate];
-[SBMultiDisplayUserInteractionCoordinator windowSceneDidConnect:];
-[SBMultiDisplayUserInteractionCoordinator updateActiveWindowScene:reason:];
-[SBMultiDisplayUserInteractionCoordinator setPointerInteractionObservers:];
-[SBMultiDisplayUserInteractionCoordinator _handleActiveDisplayQualifyingEventInWindowScene:reason:];
-[SBMultiDisplayUserInteractionCoordinator _windowSceneForEvent:];
-[SBMultiDisplayUserInteractionCoordinator activePointerWindowScene];
-[SBMultiDisplayUserInteractionCoordinator activeTouchDownOriginatedWindowScene];
-[SBMultiDisplayUserInteractionCoordinator activeWindowSceneObservers];
-[SBMultiDisplayUserInteractionCoordinator addActiveDisplayWindowSceneObserver:];
-[SBMultiDisplayUserInteractionCoordinator addPointerInteractionObserver:];
-[SBMultiDisplayUserInteractionCoordinator eventSnifferHandledPointerInteractionQualifyingEvent:];
-[SBMultiDisplayUserInteractionCoordinator eventSnifferHandledPointerTouchDown:];
-[SBMultiDisplayUserInteractionCoordinator eventSnifferHandledPointerTouchUp:];
-[SBMultiDisplayUserInteractionCoordinator eventSnifferHandledQualifyingContinuityTouch:];
-[SBMultiDisplayUserInteractionCoordinator eventSnifferHandledQualifyingScroll:];
-[SBMultiDisplayUserInteractionCoordinator eventSnifferHandledTouchInteractionQualifyingEvent:];
-[SBMultiDisplayUserInteractionCoordinator handleSendEvent:];
-[SBMultiDisplayUserInteractionCoordinator pointerInteractionObservers];
-[SBMultiDisplayUserInteractionCoordinator removeActiveDisplayWindowSceneObserver:];
-[SBMultiDisplayUserInteractionCoordinator removePointerInteractionObserver:];
-[SBMultiDisplayUserInteractionCoordinator sceneToEventSniffers];
-[SBMultiDisplayUserInteractionCoordinator setActiveWindowSceneObservers:];
-[SBMultiDisplayUserInteractionCoordinator setSceneToEventSniffers:];
```
