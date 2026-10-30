# `_UIPreviewInteractionClickImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIClickInteractionDelegate`, `UIInteraction_Private`, `UIGestureRecognizerDelegate`, `_UIPreviewInteractionImpl`, `UIInteraction`
- 14 instance variables, 16 properties, 40 instance methods, 0 class methods

## Instance variables

```
Q _currentState;
{?="shouldBegin"B"didUpdateCommitTransition"B"highlighterForPreviewTransition"B"viewControllerPresentationForPresentingViewController"B"shouldFinishTransitionToPreview"B"targetedPreviewForPreviewingAtLocation"B"overrideViewForCommitPhase"B} _delegateImplements;
@"<UIPreviewInteractionDelegate>" _delegate;
@"<UIPreviewInteractionDelegatePrivate>" _privateDelegate;
@"UIView" _view;
@"<_UIPreviewInteractionTouchForceProviding>" _touchForceProvider;
@"UIPreviewInteraction" _previewInteraction;
@"<UIInteractionEffect>" _interactionEffect;
@"_UIClickInteraction" _previewClickInteraction;
@"_UIClickInteraction" _commitClickInteraction;
@"_UIRelationshipGestureRecognizer" _exclusionRelationshipGestureRecognizer;
@"_UIPreviewInteractionPresentationAssistant" _presentationAssistant;
@"_UIPreviewInteractionHighlighter" _highlighter;
@"UIDragInteraction" _associatedDragInteraction;
```

## Properties

```
@property (T@"<UIPreviewInteractionDelegatePrivate>",R,W,N,V_privateDelegate) privateDelegate;
@property (T@"_UIClickInteraction",&,N,V_previewClickInteraction) previewClickInteraction;
@property (T@"_UIClickInteraction",&,N,V_commitClickInteraction) commitClickInteraction;
@property (T@"_UIRelationshipGestureRecognizer",&,N,V_exclusionRelationshipGestureRecognizer) exclusionRelationshipGestureRecognizer;
@property (T@"_UIPreviewInteractionPresentationAssistant",&,N,V_presentationAssistant) presentationAssistant;
@property (T@"_UIPreviewInteractionHighlighter",&,N,V_highlighter) highlighter;
@property (T@"UIDragInteraction",W,N,V_associatedDragInteraction) associatedDragInteraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIInteractionEffect>",?,&,N,V_interactionEffect) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
@property (T@"<UIPreviewInteractionDelegate>",W,N,V_delegate) delegate;
@property (T@"<_UIPreviewInteractionTouchForceProviding>",&,N,V_touchForceProvider) touchForceProvider;
@property (T@"UIPreviewInteraction",W,N,V_previewInteraction) previewInteraction;
```

## Instance methods

```
-[_UIPreviewInteractionClickImpl setExclusionRelationshipGestureRecognizer:];
-[_UIPreviewInteractionClickImpl locationInCoordinateSpace:];
-[_UIPreviewInteractionClickImpl interactionEffect];
-[_UIPreviewInteractionClickImpl cancelInteraction];
-[_UIPreviewInteractionClickImpl setInteractionEffect:];
-[_UIPreviewInteractionClickImpl privateDelegate];
-[_UIPreviewInteractionClickImpl associatedDragInteraction];
-[_UIPreviewInteractionClickImpl dealloc];
-[_UIPreviewInteractionClickImpl _prepareInteractionEffect];
-[_UIPreviewInteractionClickImpl setPresentationAssistant:];
-[_UIPreviewInteractionClickImpl clickInteractionDidEnd:];
-[_UIPreviewInteractionClickImpl clickInteractionDidClickUp:];
-[_UIPreviewInteractionClickImpl view];
-[_UIPreviewInteractionClickImpl exclusionRelationshipGestureRecognizer];
-[_UIPreviewInteractionClickImpl setDelegate:];
-[_UIPreviewInteractionClickImpl willMoveToView:];
-[_UIPreviewInteractionClickImpl gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIPreviewInteractionClickImpl delegate];
-[_UIPreviewInteractionClickImpl highlightEffectForClickInteraction:];
-[_UIPreviewInteractionClickImpl presentationAssistant];
-[_UIPreviewInteractionClickImpl setAssociatedDragInteraction:];
-[_UIPreviewInteractionClickImpl didMoveToView:];
-[_UIPreviewInteractionClickImpl _canPerformPresentation];
-[_UIPreviewInteractionClickImpl clickInteractionShouldBegin:];
-[_UIPreviewInteractionClickImpl setHighlighter:];
-[_UIPreviewInteractionClickImpl _endInteractionEffectIfNeeded];
-[_UIPreviewInteractionClickImpl _gestureRecognizerForExclusionRelationship];
-[_UIPreviewInteractionClickImpl _performPresentationIfPossible];
-[_UIPreviewInteractionClickImpl _startPreviewAtLocation:inCoordinateSpace:];
-[_UIPreviewInteractionClickImpl clickInteractionDidClickDown:];
-[_UIPreviewInteractionClickImpl commitClickInteraction];
-[_UIPreviewInteractionClickImpl highlighter];
-[_UIPreviewInteractionClickImpl initWithView:previewInteraction:];
-[_UIPreviewInteractionClickImpl previewClickInteraction];
-[_UIPreviewInteractionClickImpl previewInteraction];
-[_UIPreviewInteractionClickImpl setCommitClickInteraction:];
-[_UIPreviewInteractionClickImpl setPreviewClickInteraction:];
-[_UIPreviewInteractionClickImpl setPreviewInteraction:];
-[_UIPreviewInteractionClickImpl setTouchForceProvider:];
-[_UIPreviewInteractionClickImpl touchForceProvider];
```
