# `_UIKeyboardHandwritingLink`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIResponder`
- Protocols: `UIKeyboardCandidateListConsumer`
- 6 instance variables, 5 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"UIResponder" _previousResponder;
@"UIResponder" _fallbackResponder;
@"<UIKeyboardCandidateListDelegate>" _candidateListDelegate;
q _selectedIndex;
B _justDeleted;
@"TIKeyboardCandidateResultSet" _candidateSet;
```

## Properties

```
@property (T@"TIKeyboardCandidateResultSet",&,N,V_candidateSet) candidateSet;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIKeyboardHandwritingLink currentCandidate];
-[_UIKeyboardHandwritingLink init];
-[_UIKeyboardHandwritingLink setCandidates:inlineText:inlineRect:maxX:layout:];
-[_UIKeyboardHandwritingLink statisticsIdentifier];
-[_UIKeyboardHandwritingLink hasCandidates];
-[_UIKeyboardHandwritingLink dealloc];
-[_UIKeyboardHandwritingLink becomeFirstResponder];
-[_UIKeyboardHandwritingLink setUIKeyboardCandidateListDelegate:];
-[_UIKeyboardHandwritingLink resignFirstResponder];
-[_UIKeyboardHandwritingLink candidateAcceptedAtIndex:];
-[_UIKeyboardHandwritingLink selectedSortIndex];
-[_UIKeyboardHandwritingLink showCandidateInForwardDirection:granularity:];
-[_UIKeyboardHandwritingLink keyboardBehaviors];
-[_UIKeyboardHandwritingLink showCandidate:];
-[_UIKeyboardHandwritingLink nextResponder];
-[_UIKeyboardHandwritingLink currentIndex];
-[_UIKeyboardHandwritingLink isFloatingList];
-[_UIKeyboardHandwritingLink canBecomeFirstResponder];
-[_UIKeyboardHandwritingLink showCandidateAtIndex:];
-[_UIKeyboardHandwritingLink isExtendedList];
-[_UIKeyboardHandwritingLink candidateOutput:];
-[_UIKeyboardHandwritingLink candidateSet];
-[_UIKeyboardHandwritingLink candidatesUpdated];
-[_UIKeyboardHandwritingLink isDeleteCandidate:];
-[_UIKeyboardHandwritingLink performOutput:];
-[_UIKeyboardHandwritingLink reloadInputViews];
-[_UIKeyboardHandwritingLink sendStrokes:];
-[_UIKeyboardHandwritingLink setCandidateSet:];
-[_UIKeyboardHandwritingLink shouldRestoreResponder];
```
