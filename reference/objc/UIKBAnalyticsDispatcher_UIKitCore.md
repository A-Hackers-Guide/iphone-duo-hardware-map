# `UIKBAnalyticsDispatcher`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 20 instance methods, 34 class methods

## Instance variables

```
B _analyticsShouldCallDidKeyPress;
B _analyticsShouldCallDidKeyPressForDeleteKey;
Q _nextCandidateReplacementSource;
@"NSString" _nextCandidateReplacementRemovedText;
@"NSString" _nextCandidateReplacementInsertedText;
@"NSString" _nextCandidateReplacementPostCandidateInsertedText;
Q _nextCommitTextSource;
@"NSString" _updatedInputMode;
@"NSString" _glomojiTitle;
```

## Properties

```
@property (TQ,N,V_nextCandidateReplacementSource) nextCandidateReplacementSource;
@property (T@"NSString",C,N,V_nextCandidateReplacementRemovedText) nextCandidateReplacementRemovedText;
@property (T@"NSString",C,N,V_nextCandidateReplacementInsertedText) nextCandidateReplacementInsertedText;
@property (T@"NSString",C,N,V_nextCandidateReplacementPostCandidateInsertedText) nextCandidateReplacementPostCandidateInsertedText;
@property (TB,N,V_analyticsShouldCallDidKeyPress) analyticsShouldCallDidKeyPress;
@property (TB,N,V_analyticsShouldCallDidKeyPressForDeleteKey) analyticsShouldCallDidKeyPressForDeleteKey;
@property (TQ,N,V_nextCommitTextSource) nextCommitTextSource;
@property (T@"NSString",C,N,V_updatedInputMode) updatedInputMode;
@property (T@"NSString",C,N,V_glomojiTitle) glomojiTitle;
```

## Class methods

```
+[UIKBAnalyticsDispatcher sharedInstance];
+[UIKBAnalyticsDispatcher dispatchFloatingKeyboardEventOfType:trigger:pinnedToEdge:position:touchUpPosition:];
+[UIKBAnalyticsDispatcher emojiPopoverSummoned:appendsEmoji:];
+[UIKBAnalyticsDispatcher globeKeyLongPress];
+[UIKBAnalyticsDispatcher setKeyboardTrialParameters:];
+[UIKBAnalyticsDispatcher allowedValuesForType:];
+[UIKBAnalyticsDispatcher didCommitText:];
+[UIKBAnalyticsDispatcher didInsertText:relativeRangeBefore:selectedTextBefore:withLanguage:];
+[UIKBAnalyticsDispatcher handwritingResized:];
+[UIKBAnalyticsDispatcher keyboardCameraSessionEndedForTextContentType:didFindText:didInsertText:sender:];
+[UIKBAnalyticsDispatcher editingSessionEnded:];
+[UIKBAnalyticsDispatcher currentInputMode];
+[UIKBAnalyticsDispatcher keyboardShortcutInvokedWithKeyboardShortcutLeaf:keyEvent:keyboardProperties:];
+[UIKBAnalyticsDispatcher globeKeySelected];
+[UIKBAnalyticsDispatcher analyticsDispatchEventTextEditingOperation:trigger:];
+[UIKBAnalyticsDispatcher incrementAllowCursorMovementCount];
+[UIKBAnalyticsDispatcher sessionAnalyticsEnded:];
+[UIKBAnalyticsDispatcher decrementAllowCursorMovementCount];
+[UIKBAnalyticsDispatcher allowedValuesForTextEditingPreferredFieldName:];
+[UIKBAnalyticsDispatcher didRevisionBubbleTap];
+[UIKBAnalyticsDispatcher keyboardAnalyticsDispatchWithSelector:withTrigger:];
+[UIKBAnalyticsDispatcher didCandidateReplacement];
+[UIKBAnalyticsDispatcher didCandidateBarAction];
+[UIKBAnalyticsDispatcher keyplaneSwitched:];
+[UIKBAnalyticsDispatcher floatingKeyboardMoved:toPosition:touchPosition:];
+[UIKBAnalyticsDispatcher preferredEventName:];
+[UIKBAnalyticsDispatcher didDeleteBackwardText:];
+[UIKBAnalyticsDispatcher candidateViewExtended:direction:];
+[UIKBAnalyticsDispatcher didCandidateReplacementWithRemovedText:insertedText:];
+[UIKBAnalyticsDispatcher emojiInsertedByMethod:inputType:];
+[UIKBAnalyticsDispatcher globeKeyEducationShown:];
+[UIKBAnalyticsDispatcher floatingKeyboardSummonedEvent:trigger:finalPosition:];
+[UIKBAnalyticsDispatcher deleteKeySelected:];
+[UIKBAnalyticsDispatcher hapticEventEngineDuration:startCount:actionCount:];
```

## Instance methods

```
-[UIKBAnalyticsDispatcher resetCandidateReplacementVariables];
-[UIKBAnalyticsDispatcher setNextCandidateReplacementRemovedText:];
-[UIKBAnalyticsDispatcher init];
-[UIKBAnalyticsDispatcher nextCandidateReplacementInsertedText];
-[UIKBAnalyticsDispatcher setNextCommitTextSource:];
-[UIKBAnalyticsDispatcher setNextCandidateReplacementPostCandidateInsertedText:];
-[UIKBAnalyticsDispatcher nextCandidateReplacementPostCandidateInsertedText];
-[UIKBAnalyticsDispatcher nextCandidateReplacementSource];
-[UIKBAnalyticsDispatcher glomojiTitle];
-[UIKBAnalyticsDispatcher nextCandidateReplacementRemovedText];
-[UIKBAnalyticsDispatcher setAnalyticsShouldCallDidKeyPress:];
-[UIKBAnalyticsDispatcher setUpdatedInputMode:];
-[UIKBAnalyticsDispatcher setNextCandidateReplacementInsertedText:];
-[UIKBAnalyticsDispatcher setGlomojiTitle:];
-[UIKBAnalyticsDispatcher analyticsShouldCallDidKeyPressForDeleteKey];
-[UIKBAnalyticsDispatcher updatedInputMode];
-[UIKBAnalyticsDispatcher setNextCandidateReplacementSource:];
-[UIKBAnalyticsDispatcher analyticsShouldCallDidKeyPress];
-[UIKBAnalyticsDispatcher setAnalyticsShouldCallDidKeyPressForDeleteKey:];
-[UIKBAnalyticsDispatcher nextCommitTextSource];
```
