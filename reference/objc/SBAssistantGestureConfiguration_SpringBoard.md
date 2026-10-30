# `SBAssistantGestureConfiguration`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAssistantGestureConfigurationObserving`
- 5 instance variables, 15 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
B _siriWantsToShowHomeAffordance;
@"UIGestureRecognizer" _statusBarActionGestureRecognizer;
@"SiriPresentationSpringBoardMainScreenViewController" _siriPresentationViewController;
q _siriWantsHomeAffordanceSuppression;
```

## Properties

```
@property (T@"SiriPresentationSpringBoardMainScreenViewController",R,N,V_siriPresentationViewController) siriPresentationViewController;
@property (T@"NSHashTable",R,N,V_observers) observers;
@property (TB,N,V_siriWantsToShowHomeAffordance) siriWantsToShowHomeAffordance;
@property (Tq,N,V_siriWantsHomeAffordanceSuppression) siriWantsHomeAffordanceSuppression;
@property (T@"UIGestureRecognizer",&,N,V_statusBarActionGestureRecognizer) statusBarActionGestureRecognizer;
@property (TB,R,N) shouldDismissForSwipesOutsideContent;
@property (TB,R,N) shouldDismissForTapsOutsideContent;
@property (TB,R,N) shouldShareHomeGesture;
@property (TB,R,N) shouldPassTouchesThroughToSpringBoard;
@property (TB,R,N) shouldShowHomeAffordance;
@property (Tq,R,N) homeAffordanceSuppression;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAssistantGestureConfiguration shouldDismissForTapsOutsideContent];
-[SBAssistantGestureConfiguration removeObserver:];
-[SBAssistantGestureConfiguration shouldDismissForSwipesOutsideContent];
-[SBAssistantGestureConfiguration shouldPassTouchesThroughToSpringBoard];
-[SBAssistantGestureConfiguration addObserver:];
-[SBAssistantGestureConfiguration observers];
-[SBAssistantGestureConfiguration _makeObserversPerformBlock:];
-[SBAssistantGestureConfiguration assistantGestureConfiguration:didUpdateHomeAffordanceSuppression:];
-[SBAssistantGestureConfiguration assistantGestureConfiguration:didUpdateHomeGestureSharing:];
-[SBAssistantGestureConfiguration assistantGestureConfiguration:didUpdateShouldDismissForSwipesOutsideContent:];
-[SBAssistantGestureConfiguration assistantGestureConfiguration:didUpdateShouldDismissForTapsOutsideContent:];
-[SBAssistantGestureConfiguration assistantGestureConfiguration:didUpdateShouldPassTouchesThroughToSpringBoard:];
-[SBAssistantGestureConfiguration assistantGestureConfiguration:didUpdateShouldShowHomeAffordance:];
-[SBAssistantGestureConfiguration assistantGestureConfiguration:didUpdateStatusBarActionGestureRecognizer:];
-[SBAssistantGestureConfiguration homeAffordanceSuppression];
-[SBAssistantGestureConfiguration initWithSiriPresentationViewController:];
-[SBAssistantGestureConfiguration notifyPanBeganAtPoint:];
-[SBAssistantGestureConfiguration notifyTapAtPoint:];
-[SBAssistantGestureConfiguration setSiriWantsHomeAffordanceSuppression:];
-[SBAssistantGestureConfiguration setSiriWantsToShowHomeAffordance:];
-[SBAssistantGestureConfiguration setStatusBarActionGestureRecognizer:];
-[SBAssistantGestureConfiguration shouldDismissForGestureAtLocation:completion:];
-[SBAssistantGestureConfiguration shouldShareHomeGesture];
-[SBAssistantGestureConfiguration shouldShowHomeAffordance];
-[SBAssistantGestureConfiguration siriPresentationViewController];
-[SBAssistantGestureConfiguration siriWantsHomeAffordanceSuppression];
-[SBAssistantGestureConfiguration siriWantsToShowHomeAffordance];
-[SBAssistantGestureConfiguration statusBarActionGestureRecognizer];
```
