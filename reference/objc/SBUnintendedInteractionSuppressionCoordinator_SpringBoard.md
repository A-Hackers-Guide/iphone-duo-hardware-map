# `SBUnintendedInteractionSuppressionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowSceneAttachmentObserving`
- 6 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _unintendedInteractionLikelyAssertion;
@"NSHashTable" _observers;
@"NSHashTable" _windowScenes;
@"NSMapTable" _systemGestureSuppressionAssertions;
@"NSMapTable" _touchSuppressionAssertions;
B _unintendedInteractionLikely;
```

## Properties

```
@property (TB,N,G_isUnintendedInteractionLikely,S_setUnintendedInteractionLikely:,V_unintendedInteractionLikely) unintendedInteractionLikely;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUnintendedInteractionSuppressionCoordinator removeObserver:];
-[SBUnintendedInteractionSuppressionCoordinator init];
-[SBUnintendedInteractionSuppressionCoordinator windowSceneDidDisconnect:];
-[SBUnintendedInteractionSuppressionCoordinator dealloc];
-[SBUnintendedInteractionSuppressionCoordinator addObserver:];
-[SBUnintendedInteractionSuppressionCoordinator windowSceneDidConnect:];
-[SBUnintendedInteractionSuppressionCoordinator _configureWindowScene:forUnintendedInteractionLikely:];
-[SBUnintendedInteractionSuppressionCoordinator _isUnintendedInteractionLikely];
-[SBUnintendedInteractionSuppressionCoordinator _notifyObserversDidChangeInteractionDisablement:];
-[SBUnintendedInteractionSuppressionCoordinator _notifyObserversWillChangeInteractionDisablement:];
-[SBUnintendedInteractionSuppressionCoordinator _setUnintendedInteractionLikely:];
-[SBUnintendedInteractionSuppressionCoordinator acquireUnintendedInteractionLikelyAssertionForReason:];
```
