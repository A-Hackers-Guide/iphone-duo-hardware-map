# `UIWKInteractionViewProtocol` (protocol)

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 53 instance methods, 0 class methods

## Instance methods

```
-[UIWKInteractionViewProtocol hasMarkedText];
-[UIWKInteractionViewProtocol selectedText];
-[UIWKInteractionViewProtocol textFirstRect];
-[UIWKInteractionViewProtocol applyAutocorrection:toString:withCompletionHandler:];
-[UIWKInteractionViewProtocol markedText];
-[UIWKInteractionViewProtocol selectPositionAtPoint:completionHandler:];
-[UIWKInteractionViewProtocol textLastRect];
-[UIWKInteractionViewProtocol selectTextWithGranularity:atPoint:completionHandler:];
-[UIWKInteractionViewProtocol _cancelLongPressGestureRecognizer];
-[UIWKInteractionViewProtocol beginSelectionInDirection:completionHandler:];
-[UIWKInteractionViewProtocol changeSelectionWithGestureAt:withGesture:withState:];
-[UIWKInteractionViewProtocol changeSelectionWithTouchesFrom:to:withGesture:withState:];
-[UIWKInteractionViewProtocol hasSelectablePositionAtPoint:];
-[UIWKInteractionViewProtocol requestAutocorrectionContextWithCompletionHandler:];
-[UIWKInteractionViewProtocol requestAutocorrectionRectsForString:withCompletionHandler:];
-[UIWKInteractionViewProtocol selectWordForReplacement];
-[UIWKInteractionViewProtocol textInteractionGesture:shouldBeginAtPoint:];
-[UIWKInteractionViewProtocol updateSelectionWithExtentPoint:completionHandler:];
-[UIWKInteractionViewProtocol updateSelectionWithExtentPoint:withBoundary:completionHandler:];
-[UIWKInteractionViewProtocol webSelectionRects];
-[UIWKInteractionViewProtocol clearSelection];
-[UIWKInteractionViewProtocol applyAutocorrection:toString:shouldUnderline:withCompletionHandler:];
-[UIWKInteractionViewProtocol attributedMarkedText];
-[UIWKInteractionViewProtocol unobscuredContentRect];
-[UIWKInteractionViewProtocol shouldSuppressUpdateCandidateView];
-[UIWKInteractionViewProtocol requestDocumentContext:completionHandler:];
-[UIWKInteractionViewProtocol requestPreferredArrowDirectionForEditMenuWithCompletionHandler:];
-[UIWKInteractionViewProtocol adjustSelectionWithDelta:completionHandler:];
-[UIWKInteractionViewProtocol alternativesForSelectedText];
-[UIWKInteractionViewProtocol changeSelectionWithTouchAt:withSelectionTouch:baseIsStart:withFlags:];
-[UIWKInteractionViewProtocol didInsertFinalDictationResult];
-[UIWKInteractionViewProtocol insertTextPlaceholderWithSize:completionHandler:];
-[UIWKInteractionViewProtocol inverseScale];
-[UIWKInteractionViewProtocol isReplaceAllowed];
-[UIWKInteractionViewProtocol moveByOffset:];
-[UIWKInteractionViewProtocol moveSelectionAtBoundary:inDirection:completionHandler:];
-[UIWKInteractionViewProtocol pasteWithCompletionHandler:];
-[UIWKInteractionViewProtocol pointIsNearMarkedText:];
-[UIWKInteractionViewProtocol prepareSelectionForContextMenuWithLocationInView:completionHandler:];
-[UIWKInteractionViewProtocol removeAnnotation:forSelectionOffset:length:];
-[UIWKInteractionViewProtocol removeTextPlaceholder:willInsertText:completionHandler:];
-[UIWKInteractionViewProtocol replaceDictatedText:withText:];
-[UIWKInteractionViewProtocol replaceSelectionOffset:length:withAnnotatedString:relativeReplacementRange:];
-[UIWKInteractionViewProtocol replaceText:withText:];
-[UIWKInteractionViewProtocol requestDictationContext:];
-[UIWKInteractionViewProtocol requestRVItemInSelectedRangeWithCompletionHandler:];
-[UIWKInteractionViewProtocol selectPositionAtBoundary:inDirection:fromPoint:completionHandler:];
-[UIWKInteractionViewProtocol selectPositionAtPoint:withContextRequest:completionHandler:];
-[UIWKInteractionViewProtocol selectWordBackward];
-[UIWKInteractionViewProtocol shouldAllowHidingSelectionCommands];
-[UIWKInteractionViewProtocol unscaledView];
-[UIWKInteractionViewProtocol willFinishIgnoringCalloutBarFadeAfterPerformingAction];
-[UIWKInteractionViewProtocol willInsertFinalDictationResult];
```
