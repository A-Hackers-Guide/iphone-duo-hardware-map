# `SBHomeAffordanceInteractionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAssistantSceneControllingObserver`, `UIGestureRecognizerDelegate`, `SBFHomeAffordanceInteractionProviding`
- 14 instance variables, 6 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _gesturesEnabled;
@"UITapGestureRecognizer" _bounceTapRecognizer;
@"UITapGestureRecognizer" _bounceDoubleTapRecognizer;
@"UITapGestureRecognizer" _bounceDoubleTapFailureRecognizer;
@"UITapGestureRecognizer" _revealTapRecognizer;
@"UITapGestureRecognizer" _revealDoubleTapRecognizer;
@"UIScreenEdgePanGestureRecognizer" _revealEdgePanRecognizer;
@"NSHashTable" _registeredHomeAffordanceInteractions;
@"SBHomeAffordanceInteraction" _currentHomeAffordanceInteraction;
B _isTrackingPossibleDoubleTap;
@"SiriQuickTypeGestureSource" _quickTypeGestureSource;
@"<SiriAssertion>" _quickTypePrewarmAssertion;
@"SBWindowScene" _windowScene;
q _hitTestRectSize;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (Tq,N,V_hitTestRectSize) hitTestRectSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBHomeAffordanceInteractionManager _wantsModernRevealGestureRecognizerBehaviors];
```

## Instance methods

```
-[SBHomeAffordanceInteractionManager _updateBounceTapGestureRecognizers];
-[SBHomeAffordanceInteractionManager _systemGestureManager];
-[SBHomeAffordanceInteractionManager gestureRecognizer:shouldReceiveTouch:];
-[SBHomeAffordanceInteractionManager assistantDidChangeHomeAffordanceDoubleTapGestureEnablement:];
-[SBHomeAffordanceInteractionManager registerHomeAffordanceInteraction:];
-[SBHomeAffordanceInteractionManager _gestureRecognizer:didRecognizeSingleTapWithHomeAffordanceInteraction:];
-[SBHomeAffordanceInteractionManager unregisterHomeAffordanceInteraction:];
-[SBHomeAffordanceInteractionManager dealloc];
-[SBHomeAffordanceInteractionManager _bounceTapRecognized:];
-[SBHomeAffordanceInteractionManager _bounceDoubleTapRecognized:];
-[SBHomeAffordanceInteractionManager _revealEdgePanRecognized:];
-[SBHomeAffordanceInteractionManager updateHomeAffordanceHitTestRectForHomeAffordanceInteraction:];
-[SBHomeAffordanceInteractionManager _logShouldReceiveTouchIfNeeded:forGestureRecognizer:touch:];
-[SBHomeAffordanceInteractionManager initWithWindowScene:];
-[SBHomeAffordanceInteractionManager hitTestRectSize];
-[SBHomeAffordanceInteractionManager newHomeAffordanceInteraction];
-[SBHomeAffordanceInteractionManager _gestureRecognizer:didRecognizeSingleClickWithHomeAffordanceInteraction:];
-[SBHomeAffordanceInteractionManager _firstHomeAffordanceInteractionForGestureRecognizer:touch:];
-[SBHomeAffordanceInteractionManager setHitTestRectSize:];
-[SBHomeAffordanceInteractionManager _firstHomeAffordanceInteractionForGestureRecognizer:];
-[SBHomeAffordanceInteractionManager _bounceDoubleTapFailureRecognized:];
-[SBHomeAffordanceInteractionManager _revealTapRecognized:];
-[SBHomeAffordanceInteractionManager gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBHomeAffordanceInteractionManager _homeAffordanceHitTestRectOfSize:forHomeAffordanceInteraction:];
-[SBHomeAffordanceInteractionManager _assistantController];
-[SBHomeAffordanceInteractionManager windowScene];
-[SBHomeAffordanceInteractionManager acquireDisableHomeAffordanceDoubleTapGestureAssertionWithReason:];
-[SBHomeAffordanceInteractionManager _gestureRecognizer:didRecognizeDoubleTapWithHomeAffordanceInteraction:];
-[SBHomeAffordanceInteractionManager _gestureRecognizer:didFailToRecognizeDoubleTapWithHomeAffordanceInteraction:];
```
