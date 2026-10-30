# `_UIPreviewInteractionClassicImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPreviewInteractionImpl`
- 15 instance variables, 8 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
{?="delegatePreviewInteractionShouldBegin"b1"delegateDidUpdateCommitTransition"b1"delegateShouldFinishTransitionToPreview"b1"delegateShouldAutomaticallyTransitionToPreviewAfterDelay"b1"delegateHighlighterForPreviewTransition"b1"delegateViewControllerPresentationForPresentingViewController"b1"interactive"b1"delegateDidPreventInteraction"b1"interactionRequiresRestart"b1"interactionWasCancelled"b1"previousProgressWasNegativeOrZero"b1"currentState"b3"nextUpdateShouldTransitionToPreview"b1"nextPreviewShouldPreventHapticFeedback"b1} _previewInteractionFlags;
@"<_UIPreviewInteractionTouchForceProviding>" _systemTouchForceProvider;
@"_UIPreviewInteractionStateRecognizer" _currentInteractionStateRecognizer;
{CGPoint="x"d"y"d} _sceneReferenceLocationFromLatestUpdate;
@"CADisplayLink" _continuousEvaluationDisplayLink;
@"_UIDeepPressAnalyzer" _deepPressAnalyzer;
@"_UIStatesFeedbackGenerator" _feedbackGenerator;
B _feedbackGeneratorTurnedOn;
@"_UIPreviewInteractionHighlighter" _highlighter;
@"_UIPreviewInteractionViewControllerHelper" _viewControllerHelper;
@ _viewControllerPresentationObserver;
@"<UIPreviewInteractionDelegate>" _delegate;
@"<_UIPreviewInteractionTouchForceProviding>" _touchForceProvider;
@"UIPreviewInteraction" _previewInteraction;
```

## Properties

```
@property (T@"<UIPreviewInteractionDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",R,W,N,V_view) view;
@property (T@"<_UIPreviewInteractionTouchForceProviding>",&,N,V_touchForceProvider) touchForceProvider;
@property (T@"UIPreviewInteraction",W,N,V_previewInteraction) previewInteraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewInteractionClassicImpl locationInCoordinateSpace:];
-[_UIPreviewInteractionClassicImpl cancelInteraction];
-[_UIPreviewInteractionClassicImpl observeValueForKeyPath:ofObject:change:context:];
-[_UIPreviewInteractionClassicImpl init];
-[_UIPreviewInteractionClassicImpl dealloc];
-[_UIPreviewInteractionClassicImpl view];
-[_UIPreviewInteractionClassicImpl setDelegate:];
-[_UIPreviewInteractionClassicImpl delegate];
-[_UIPreviewInteractionClassicImpl _shouldCancelTransitionToState:];
-[_UIPreviewInteractionClassicImpl _updateForContinuousEvaluation:];
-[_UIPreviewInteractionClassicImpl _endInteractiveStateTransitions];
-[_UIPreviewInteractionClassicImpl _actuateFeedbackForStateIfNeeded:];
-[_UIPreviewInteractionClassicImpl _dismissPreviewViewControllerIfNeeded];
-[_UIPreviewInteractionClassicImpl _endContinuousEvaluation];
-[_UIPreviewInteractionClassicImpl _endHighlightingIfNeeded];
-[_UIPreviewInteractionClassicImpl _endInteractionIfNeeded];
-[_UIPreviewInteractionClassicImpl _endUsingFeedbackIfNeeded];
-[_UIPreviewInteractionClassicImpl _endViewControllerPresentationObserving];
-[_UIPreviewInteractionClassicImpl _gestureRecognizerForExclusionRelationship];
-[_UIPreviewInteractionClassicImpl _prepareForInteractionIfNeeded];
-[_UIPreviewInteractionClassicImpl _prepareForViewControllerPresentationObserving];
-[_UIPreviewInteractionClassicImpl _prepareHighlighterIfNeeded];
-[_UIPreviewInteractionClassicImpl _prepareUsingFeedback];
-[_UIPreviewInteractionClassicImpl _prepareUsingFeedbackIfNeeded];
-[_UIPreviewInteractionClassicImpl _presentPreviewViewControllerIfNeeded];
-[_UIPreviewInteractionClassicImpl _resetAfterInteraction];
-[_UIPreviewInteractionClassicImpl _startPreviewAtLocation:inCoordinateSpace:];
-[_UIPreviewInteractionClassicImpl _turnOffFeedbackGenerator];
-[_UIPreviewInteractionClassicImpl _turnOnFeedbackGenerator];
-[_UIPreviewInteractionClassicImpl _updateFeedbackTowardNextState:progress:];
-[_UIPreviewInteractionClassicImpl _updateForCurrentTouchForceProvider];
-[_UIPreviewInteractionClassicImpl _updateHighlighter:];
-[_UIPreviewInteractionClassicImpl _updateInteractionStateRecognizerForTouchForce:atTimestamp:withCentroidAtLocation:];
-[_UIPreviewInteractionClassicImpl initWithView:previewInteraction:];
-[_UIPreviewInteractionClassicImpl previewInteraction];
-[_UIPreviewInteractionClassicImpl setPreviewInteraction:];
-[_UIPreviewInteractionClassicImpl setTouchForceProvider:];
-[_UIPreviewInteractionClassicImpl touchForceProvider];
```
