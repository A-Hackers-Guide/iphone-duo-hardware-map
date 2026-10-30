# `_UINavigationBarTransitionAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 14 properties, 33 instance methods, 2 class methods

## Instance variables

```
q _animationCount;
@"NSMutableArray" _animationIDs;
B _interruptable;
B _interactive;
B _needsLifetimeExtended;
B _cancelledTransition;
B _shouldHideBackButtonDuringTransition;
B _shouldUpdatePromptAfterTransition;
@"<UIViewControllerTransitionCoordinator>" _transitionCoordinator;
@"UINavigationBar" _navigationBar;
@"<_UINavigationBarDelegatePrivate>" _delegate;
q _transition;
d _duration;
```

## Properties

```
@property (T@"<UIViewControllerTransitionCoordinator>",R,W,N,V_transitionCoordinator) transitionCoordinator;
@property (T@"UINavigationBar",R,W,N,V_navigationBar) navigationBar;
@property (T@"<_UINavigationBarDelegatePrivate>",R,W,N,V_delegate) delegate;
@property (Tq,R,N,V_transition) transition;
@property (Td,R,N,V_duration) duration;
@property (TB,R,N,V_interruptable) interruptable;
@property (TB,R,N,V_interactive) interactive;
@property (TB,N,V_needsLifetimeExtended) needsLifetimeExtended;
@property (TB,R,N) shouldAnimateAlongside;
@property (TB,R,N) shouldCrossfade;
@property (TB,R,N,V_cancelledTransition) cancelledTransition;
@property (TB,N,V_shouldHideBackButtonDuringTransition) shouldHideBackButtonDuringTransition;
@property (TB,N,V_shouldUpdatePromptAfterTransition) shouldUpdatePromptAfterTransition;
@property (T@"NSArray",R,N,V_animationIDs) animationIDs;
```

## Class methods

```
+[_UINavigationBarTransitionAssistant popTransitionAssistantForNavigationBar:delegate:crossfade:];
+[_UINavigationBarTransitionAssistant pushTransitionAssistantForNavigationBar:delegate:crossfade:];
```

## Instance methods

```
-[_UINavigationBarTransitionAssistant transitionCoordinator];
-[_UINavigationBarTransitionAssistant transition];
-[_UINavigationBarTransitionAssistant shouldCrossfade];
-[_UINavigationBarTransitionAssistant updateInteractiveTransitionPercent:];
-[_UINavigationBarTransitionAssistant navigationBar];
-[_UINavigationBarTransitionAssistant initWithNavigationBar:delegate:];
-[_UINavigationBarTransitionAssistant needsLifetimeExtended];
-[_UINavigationBarTransitionAssistant setNeedsLifetimeExtended:];
-[_UINavigationBarTransitionAssistant startInteractiveTransition];
-[_UINavigationBarTransitionAssistant setShouldUpdatePromptAfterTransition:];
-[_UINavigationBarTransitionAssistant finishInteractiveTransitionPercent:completionSpeed:completionCurve:];
-[_UINavigationBarTransitionAssistant _getTransitionCoordinator];
-[_UINavigationBarTransitionAssistant cancelInteractiveTransitionPercent:completionSpeed:completionCurve:];
-[_UINavigationBarTransitionAssistant duration];
-[_UINavigationBarTransitionAssistant _finishTrackingAnimations];
-[_UINavigationBarTransitionAssistant _transitionOverrideFrom:defaultingTo:];
-[_UINavigationBarTransitionAssistant delegate];
-[_UINavigationBarTransitionAssistant _startTrackingAnimations];
-[_UINavigationBarTransitionAssistant shouldHideBackButtonDuringTransition];
-[_UINavigationBarTransitionAssistant incrementAnimationCount];
-[_UINavigationBarTransitionAssistant interruptable];
-[_UINavigationBarTransitionAssistant _clearAnimationsWithDuration:curve:reverse:];
-[_UINavigationBarTransitionAssistant shouldUpdatePromptAfterTransition];
-[_UINavigationBarTransitionAssistant cancelledTransition];
-[_UINavigationBarTransitionAssistant _getPopDurationAndTransitionAlwaysCrossfade:];
-[_UINavigationBarTransitionAssistant animationIDs];
-[_UINavigationBarTransitionAssistant finishTrackingInteractiveTransition];
-[_UINavigationBarTransitionAssistant interactive];
-[_UINavigationBarTransitionAssistant _getPushDurationAndTransitionAlwaysCrossfade:];
-[_UINavigationBarTransitionAssistant shouldAnimateAlongside];
-[_UINavigationBarTransitionAssistant setShouldHideBackButtonDuringTransition:];
-[_UINavigationBarTransitionAssistant decrementAnimationCount];
-[_UINavigationBarTransitionAssistant _getInteractive];
```
