# `UIKeyboardAutomatic`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboard`
- 7 instance variables, 7 properties, 27 instance methods, 2 class methods

## Instance variables

```
B showsCandidateBar;
B showsCandidateInline;
B receivedCandidatesInCurrentInputMode;
@"<UITextCursorAssertion>" _blinkAssertion;
@"_UIStringAndPositionPair" _lastMatchedSupplementalCandidate;
@"_UIStringAndPositionPair" _pendingSupplementalCandidateToInsert;
Q _lastChooseSupplementalItemToInsertCallbackIdentifier;
```

## Properties

```
@property (T@"<UITextCursorAssertion>",&,N,V_blinkAssertion) blinkAssertion;
@property (T@"_UIStringAndPositionPair",&,N,V_lastMatchedSupplementalCandidate) lastMatchedSupplementalCandidate;
@property (T@"_UIStringAndPositionPair",&,N,V_pendingSupplementalCandidateToInsert) pendingSupplementalCandidateToInsert;
@property (TQ,N,V_lastChooseSupplementalItemToInsertCallbackIdentifier) lastChooseSupplementalItemToInsertCallbackIdentifier;
@property (TB,N,VshowsCandidateBar) showsCandidateBar;
@property (TB,N,VreceivedCandidatesInCurrentInputMode) receivedCandidatesInCurrentInputMode;
@property (TB,N,VshowsCandidateInline) showsCandidateInline;
```

## Class methods

```
+[UIKeyboardAutomatic sharedInstance];
+[UIKeyboardAutomatic activeInstance];
```

## Instance methods

```
-[UIKeyboardAutomatic setLastChooseSupplementalItemToInsertCallbackIdentifier:];
-[UIKeyboardAutomatic setPendingSupplementalCandidateToInsert:];
-[UIKeyboardAutomatic willResume:];
-[UIKeyboardAutomatic pendingSupplementalCandidateToInsert];
-[UIKeyboardAutomatic setLastMatchedSupplementalCandidate:];
-[UIKeyboardAutomatic receivedCandidatesInCurrentInputMode];
-[UIKeyboardAutomatic showsCandidateBar];
-[UIKeyboardAutomatic minimize];
-[UIKeyboardAutomatic setShowsCandidateBar:];
-[UIKeyboardAutomatic setReceivedCandidatesInCurrentInputMode:];
-[UIKeyboardAutomatic lastChooseSupplementalItemToInsertCallbackIdentifier];
-[UIKeyboardAutomatic maximize];
-[UIKeyboardAutomatic isAutomatic];
-[UIKeyboardAutomatic lastMatchedSupplementalCandidate];
-[UIKeyboardAutomatic showsCandidateInline];
-[UIKeyboardAutomatic didSuspend:];
-[UIKeyboardAutomatic setShowsCandidateInline:];
-[UIKeyboardAutomatic blinkAssertion];
-[UIKeyboardAutomatic dealloc];
-[UIKeyboardAutomatic prepareForImplBoundsHeightChange:suppressNotification:];
-[UIKeyboardAutomatic activate];
-[UIKeyboardAutomatic implBoundsHeightChangeDone:suppressNotification:];
-[UIKeyboardAutomatic setBlinkAssertion:];
-[UIKeyboardAutomatic _isAutomaticKeyboard];
-[UIKeyboardAutomatic isActive];
-[UIKeyboardAutomatic initWithFrame:];
-[UIKeyboardAutomatic geometryForHeightDelta:];
```
