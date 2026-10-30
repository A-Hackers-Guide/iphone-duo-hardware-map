# `UIDynamicCaret`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIImageView`
- Protocols: `UIKeyboardCandidateList`, `_UIDynamicCaretDocumentContentDelegate`
- 8 instance variables, 10 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"<UIKeyboardCandidateListDelegate>" _candidateListDelegate;
q _selectedIndex;
B _justDeleted;
@"_UIDynamicCaretInput" _inputView;
@"_UIDynamicCaretAlternatives" _alternativesView;
@"_UIDynamicCaretNoContentView" _noContentView;
@"_UIDynamicCaretHelpLabel" _helpLabel;
@"TIKeyboardCandidateResultSet" _candidateSet;
```

## Properties

```
@property (T@"_UIDynamicCaretInput",&,N,V_inputView) inputView;
@property (T@"_UIDynamicCaretAlternatives",&,N,V_alternativesView) alternativesView;
@property (T@"_UIDynamicCaretNoContentView",&,N,V_noContentView) noContentView;
@property (T@"_UIDynamicCaretHelpLabel",&,N,V_helpLabel) helpLabel;
@property (T@"TIKeyboardCandidateResultSet",&,N,V_candidateSet) candidateSet;
@property (TB,N) isActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDynamicCaret setIsActive:];
-[UIDynamicCaret touchesEnded:withEvent:];
-[UIDynamicCaret currentCandidate];
-[UIDynamicCaret touchesCancelled:withEvent:];
-[UIDynamicCaret backgroundImage];
-[UIDynamicCaret setCandidates:inlineText:inlineRect:maxX:layout:];
-[UIDynamicCaret statisticsIdentifier];
-[UIDynamicCaret hasCandidates];
-[UIDynamicCaret setUIKeyboardCandidateListDelegate:];
-[UIDynamicCaret layoutSubviews];
-[UIDynamicCaret touchesBegan:withEvent:];
-[UIDynamicCaret touchesMoved:withEvent:];
-[UIDynamicCaret candidateAcceptedAtIndex:];
-[UIDynamicCaret selectedSortIndex];
-[UIDynamicCaret showCandidateInForwardDirection:granularity:];
-[UIDynamicCaret inputView];
-[UIDynamicCaret keyboardBehaviors];
-[UIDynamicCaret showCandidate:];
-[UIDynamicCaret setFrame:];
-[UIDynamicCaret setInputView:];
-[UIDynamicCaret isActive];
-[UIDynamicCaret currentIndex];
-[UIDynamicCaret didMoveToSuperview];
-[UIDynamicCaret isFloatingList];
-[UIDynamicCaret initWithFrame:];
-[UIDynamicCaret showCandidateAtIndex:];
-[UIDynamicCaret isExtendedList];
-[UIDynamicCaret alternativeTappedAtIndex:];
-[UIDynamicCaret alternativesView];
-[UIDynamicCaret candidateSet];
-[UIDynamicCaret displayAlternatives:];
-[UIDynamicCaret helpLabel];
-[UIDynamicCaret isDeleteCandidate:];
-[UIDynamicCaret noContentView];
-[UIDynamicCaret setAlternativesView:];
-[UIDynamicCaret setCandidateSet:];
-[UIDynamicCaret setDocumentHasContent:];
-[UIDynamicCaret setHelpLabel:];
-[UIDynamicCaret setNoContentView:];
```
