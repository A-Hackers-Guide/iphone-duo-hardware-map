# `UIAsyncTextInputClient` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIAsyncTextInput`
- 0 instance variables, 1 properties, 26 instance methods, 0 class methods

## Properties

```
@property (TB,?,R,N) shouldSuppressEditMenu;
```

## Instance methods

```
-[UIAsyncTextInputClient cancelAutoscroll];
-[UIAsyncTextInputClient selectPositionAtPoint:completionHandler:];
-[UIAsyncTextInputClient adjustSelection:completionHandler:];
-[UIAsyncTextInputClient shouldSuppressUpdateCandidateView];
-[UIAsyncTextInputClient selectTextWithGranularity:atPoint:completionHandler:];
-[UIAsyncTextInputClient requestPreferredArrowDirectionForEditMenuWithCompletionHandler:];
-[UIAsyncTextInputClient _cancelLongPressGestureRecognizer];
-[UIAsyncTextInputClient autoscrollToPoint:];
-[UIAsyncTextInputClient beginSelectionInDirection:completionHandler:];
-[UIAsyncTextInputClient changeSelectionWithGestureAt:withGesture:withState:];
-[UIAsyncTextInputClient changeSelectionWithTouchAt:withSelectionTouch:baseIsStart:withFlags:];
-[UIAsyncTextInputClient changeSelectionWithTouchesFrom:to:withGesture:withState:];
-[UIAsyncTextInputClient moveByOffset:];
-[UIAsyncTextInputClient moveSelectionAtBoundary:inDirection:completionHandler:];
-[UIAsyncTextInputClient pasteWithCompletionHandler:];
-[UIAsyncTextInputClient removeAnnotation:forSelectionOffset:length:];
-[UIAsyncTextInputClient selectPositionAtBoundary:inDirection:fromPoint:completionHandler:];
-[UIAsyncTextInputClient selectPositionAtPoint:withContextRequest:completionHandler:];
-[UIAsyncTextInputClient selectTextForContextMenuWithLocationInView:completionHandler:];
-[UIAsyncTextInputClient selectWordForReplacement];
-[UIAsyncTextInputClient shouldAllowHidingSelectionCommands];
-[UIAsyncTextInputClient shouldSuppressEditMenu];
-[UIAsyncTextInputClient textInteractionGesture:shouldBeginAtPoint:];
-[UIAsyncTextInputClient updateSelectionWithExtentPoint:completionHandler:];
-[UIAsyncTextInputClient updateSelectionWithExtentPoint:withBoundary:completionHandler:];
-[UIAsyncTextInputClient willFinishIgnoringCalloutBarFadeAfterPerformingAction];
```
