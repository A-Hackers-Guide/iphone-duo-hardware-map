# `_UIFeedbackGeneratorGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIDragEventRespondable`
- 9 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _trackedTouches;
@"UIScrollEvent" _trackedScrollEvent;
@"UITransformEvent" _trackedTransformEvent;
@"NSHashTable" _feedbackGenerators;
@"NSMutableSet" _completedInteractions;
@"NSSet" _potentialDragTouches;
B _trackingDragEvent;
@"_UIFeedbackGeneratorGestureRecognizerCompletedEvent" _completedScrollEvent;
@"_UIFeedbackGeneratorGestureRecognizerCompletedEvent" _completedTransformEvent;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFeedbackGeneratorGestureRecognizer canPreventGestureRecognizer:];
-[_UIFeedbackGeneratorGestureRecognizer touchesEnded:withEvent:];
-[_UIFeedbackGeneratorGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIFeedbackGeneratorGestureRecognizer _scrollingChangedWithEvent:];
-[_UIFeedbackGeneratorGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UIFeedbackGeneratorGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIFeedbackGeneratorGestureRecognizer _canCancelGestureRecognizer:];
-[_UIFeedbackGeneratorGestureRecognizer touchesCancelled:withEvent:];
-[_UIFeedbackGeneratorGestureRecognizer _transformChangedWithEvent:];
-[_UIFeedbackGeneratorGestureRecognizer _draggingEnteredWithEvent:];
-[_UIFeedbackGeneratorGestureRecognizer _draggingExitedWithEvent:];
-[_UIFeedbackGeneratorGestureRecognizer touchesBegan:withEvent:];
-[_UIFeedbackGeneratorGestureRecognizer touchesMoved:withEvent:];
-[_UIFeedbackGeneratorGestureRecognizer initWithTarget:action:];
-[_UIFeedbackGeneratorGestureRecognizer _draggingEndedWithEvent:];
-[_UIFeedbackGeneratorGestureRecognizer _draggingUpdatedWithEvent:];
-[_UIFeedbackGeneratorGestureRecognizer __completeIfNecessary];
-[_UIFeedbackGeneratorGestureRecognizer __moveEventToCompleted:];
-[_UIFeedbackGeneratorGestureRecognizer __removeCompletedInteractionsAfterDelay:];
-[_UIFeedbackGeneratorGestureRecognizer _wantsPartialTouchSequences];
```
