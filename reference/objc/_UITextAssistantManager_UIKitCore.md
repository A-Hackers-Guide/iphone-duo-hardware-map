# `_UITextAssistantManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIWritingToolsCoordinatorInternalDelegate`
- 14 instance variables, 6 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"<_UIAssertion>" _grabberSuppression;
@"<_UIInvalidatable>" _selectionUIHiddenAssertion;
@"UITextRange" _initialSelectedRangeInDocument;
q _externalEditAction;
@"<NSObject>" _viewportLayoutObservationToken;
Q _offsetToContextualRange;
@"UIWritingToolsCoordinatorContext" _activeContext;
@"UITextRange" _pasteRangeInProgress;
@"NSString" _pasteStringInProgress;
B _isInitializingSession;
@"UITextRange" _lastAnimatingReplacementRange;
@"NSMutableDictionary" _textAnimationContextsByAnimationType;
B _isReplacingTextByRequest;
@"UITextView" _textView;
```

## Properties

```
@property (T@"UITextView",R,W,N,V_textView) textView;
@property (TB,R,N,V_isReplacingTextByRequest) isReplacingTextByRequest;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextAssistantManager textView];
-[_UITextAssistantManager initWithTextView:];
-[_UITextAssistantManager dealloc];
-[_UITextAssistantManager description];
-[_UITextAssistantManager paragraphRangeForRange:];
-[_UITextAssistantManager contextForWritingToolsForScope:];
-[_UITextAssistantManager _invalidateViewportLayoutForTextRange:];
-[_UITextAssistantManager _writingToolsCoordinator:didReceiveContexts:];
-[_UITextAssistantManager _writingToolsCoordinator:textHighlightColorForScheme:inHighlightStyle:];
-[_UITextAssistantManager cleanUpAnimatedTextLayoutInfoIfNecessary];
-[_UITextAssistantManager finishUndoRedoChanges];
-[_UITextAssistantManager isReplacingTextByRequest];
-[_UITextAssistantManager performExternalEditsForWritingToolsSessionIdentifier:action:usingBlock:];
-[_UITextAssistantManager removeTextAnimationAttributesAtRange:];
-[_UITextAssistantManager replaceRange:withWritingToolsReplacement:];
-[_UITextAssistantManager reportTextChunkVisibilityUpdateForDelivery:textRange:visible:];
-[_UITextAssistantManager sessionCleanup];
-[_UITextAssistantManager setUpTextAnimationContextForRange:animation:];
-[_UITextAssistantManager tearDownTextAnimationContextForAnimation:];
-[_UITextAssistantManager textViewDidReflowLayout];
-[_UITextAssistantManager updateForCharactersInRange:withReplacement:isUndoRedo:];
-[_UITextAssistantManager updateForPasteDelegateDidPasteText:toTextRange:];
-[_UITextAssistantManager updateForPasteDelegateWillPasteText:toTextRange:];
-[_UITextAssistantManager writingToolsCoordinator:adjustForUpdatedRange:forTextAnimation:inContext:completion:];
-[_UITextAssistantManager writingToolsCoordinator:finishTextAnimation:forRange:inContext:completion:];
-[_UITextAssistantManager writingToolsCoordinator:prepareForTextAnimation:forRange:inContext:completion:];
-[_UITextAssistantManager writingToolsCoordinator:replaceRange:inContext:proposedText:reason:animationParameters:completion:];
-[_UITextAssistantManager writingToolsCoordinator:requestsBoundingBezierPathsForRange:inContext:completion:];
-[_UITextAssistantManager writingToolsCoordinator:requestsContextsForScope:completion:];
-[_UITextAssistantManager writingToolsCoordinator:requestsPreviewForTextAnimation:ofRange:inContext:completion:];
-[_UITextAssistantManager writingToolsCoordinator:requestsRangeInContextWithIdentifierForPoint:completion:];
-[_UITextAssistantManager writingToolsCoordinator:requestsUnderlinePathsForRange:inContext:completion:];
-[_UITextAssistantManager writingToolsCoordinator:selectRanges:inContext:completion:];
-[_UITextAssistantManager writingToolsCoordinator:willChangeToState:completion:];
```
