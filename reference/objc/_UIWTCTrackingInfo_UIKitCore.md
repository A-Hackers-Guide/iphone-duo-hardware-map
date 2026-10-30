# `_UIWTCTrackingInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 23 properties, 51 instance methods, 0 class methods

## Instance variables

```
B _streaming;
B _showingOriginal;
@"NSMutableDictionary" _anticipationAnimationPreviews;
@"NSMutableDictionary" _removalAnimationPreviews;
@"NSMutableDictionary" _insertionAnimationPreviews;
@"NSMutableDictionary" _customAnimationFillColorsBySubrangeIndex;
@"UIWritingToolsCoordinatorContext" _acceptedEvaluationContext;
@"UIWritingToolsCoordinatorContext" _proposedEvaluationContext;
@"_UITextAssistantReplacementTracker" _replacementTracker;
@"NSMutableArray" _anticipationAnimationSubranges;
@"NSMutableArray" _removalAnimationSubranges;
@"NSMutableArray" _insertionAnimationSubranges;
@"NSMutableIndexSet" _finishedAnticipationSubrangeIndexes;
@"NSMutableIndexSet" _finishedRemovalSubrangeIndexes;
@"NSMutableIndexSet" _finishedInsertionSubrangeIndexes;
@"NSMutableIndexSet" _landedReplacementSubrangeIndexes;
@"NSMutableAttributedString" _currentProofreadingText;
@"NSMutableDictionary" _proofreadingSuggestionIDsPerDeliveryID;
@"NSMutableDictionary" _backingProofreadingSuggestionStatePerSuggestionID;
@"NSUUID" _savedReviewingProofreadingSuggestionID;
@"NSMutableDictionary" _decorationContainerViewsPerRange;
@"_UIWTCUndoRoller" _undoRoller;
```

## Properties

```
@property (T@"NSUUID",R,N) contextID;
@property (T@"UIWritingToolsCoordinatorContext",&,N,V_acceptedEvaluationContext) acceptedEvaluationContext;
@property (T@"UIWritingToolsCoordinatorContext",&,N,V_proposedEvaluationContext) proposedEvaluationContext;
@property (T@"_UITextAssistantReplacementTracker",&,N,V_replacementTracker) replacementTracker;
@property (T@"NSMutableArray",&,N,V_anticipationAnimationSubranges) anticipationAnimationSubranges;
@property (T@"NSMutableArray",&,N,V_removalAnimationSubranges) removalAnimationSubranges;
@property (T@"NSMutableArray",&,N,V_insertionAnimationSubranges) insertionAnimationSubranges;
@property (T@"NSMutableIndexSet",&,N,V_finishedAnticipationSubrangeIndexes) finishedAnticipationSubrangeIndexes;
@property (T@"NSMutableIndexSet",&,N,V_finishedRemovalSubrangeIndexes) finishedRemovalSubrangeIndexes;
@property (T@"NSMutableIndexSet",&,N,V_finishedInsertionSubrangeIndexes) finishedInsertionSubrangeIndexes;
@property (T@"NSMutableIndexSet",&,N,V_landedReplacementSubrangeIndexes) landedReplacementSubrangeIndexes;
@property (T@"NSMutableDictionary",R,N,V_customAnimationFillColorsBySubrangeIndex) customAnimationFillColorsBySubrangeIndex;
@property (T@"NSMutableDictionary",R,N,V_anticipationAnimationPreviews) anticipationAnimationPreviews;
@property (T@"NSMutableDictionary",R,N,V_removalAnimationPreviews) removalAnimationPreviews;
@property (T@"NSMutableDictionary",R,N,V_insertionAnimationPreviews) insertionAnimationPreviews;
@property (TB,N,GisStreaming,V_streaming) streaming;
@property (TB,N,V_showingOriginal) showingOriginal;
@property (T@"NSMutableAttributedString",&,N,V_currentProofreadingText) currentProofreadingText;
@property (T@"NSMutableDictionary",&,N,V_proofreadingSuggestionIDsPerDeliveryID) proofreadingSuggestionIDsPerDeliveryID;
@property (T@"NSMutableDictionary",&,N,V_backingProofreadingSuggestionStatePerSuggestionID) backingProofreadingSuggestionStatePerSuggestionID;
@property (T@"NSUUID",C,N,V_savedReviewingProofreadingSuggestionID) savedReviewingProofreadingSuggestionID;
@property (T@"NSMutableDictionary",&,N,V_decorationContainerViewsPerRange) decorationContainerViewsPerRange;
@property (T@"_UIWTCUndoRoller",&,N,V_undoRoller) undoRoller;
```

## Instance methods

```
-[_UIWTCTrackingInfo isStreaming];
-[_UIWTCTrackingInfo contextID];
-[_UIWTCTrackingInfo setInsertionAnimationSubranges:];
-[_UIWTCTrackingInfo showingOriginal];
-[_UIWTCTrackingInfo acceptedEvaluationContext];
-[_UIWTCTrackingInfo anticipationAnimationPreviews];
-[_UIWTCTrackingInfo anticipationAnimationSubranges];
-[_UIWTCTrackingInfo backingProofreadingSuggestionStateForSuggestion:];
-[_UIWTCTrackingInfo backingProofreadingSuggestionStatePerSuggestionID];
-[_UIWTCTrackingInfo currentProofreadingText];
-[_UIWTCTrackingInfo customAnimationFillColorsBySubrangeIndex];
-[_UIWTCTrackingInfo customFillColorForSubrangeIndex:];
-[_UIWTCTrackingInfo decorationContainerViewsPerRange];
-[_UIWTCTrackingInfo finishedAnticipationSubrangeIndexes];
-[_UIWTCTrackingInfo finishedInsertionSubrangeIndexes];
-[_UIWTCTrackingInfo finishedRemovalSubrangeIndexes];
-[_UIWTCTrackingInfo finishedSubrangeIndexesForTextAnimation:];
-[_UIWTCTrackingInfo insertionAnimationPreviews];
-[_UIWTCTrackingInfo insertionAnimationSubranges];
-[_UIWTCTrackingInfo isMarkedForRemovalTargetedPreview:];
-[_UIWTCTrackingInfo landedReplacementSubrangeIndexes];
-[_UIWTCTrackingInfo markForRemovalTargetedPreviewForTextAnimation:subrangeIndex:];
-[_UIWTCTrackingInfo proofreadingSuggestionIDsForDelivery:];
-[_UIWTCTrackingInfo proofreadingSuggestionIDsPerDeliveryID];
-[_UIWTCTrackingInfo proposedEvaluationContext];
-[_UIWTCTrackingInfo removalAnimationPreviews];
-[_UIWTCTrackingInfo removalAnimationSubranges];
-[_UIWTCTrackingInfo replacementTracker];
-[_UIWTCTrackingInfo savedReviewingProofreadingSuggestionID];
-[_UIWTCTrackingInfo setAcceptedEvaluationContext:];
-[_UIWTCTrackingInfo setAnticipationAnimationSubranges:];
-[_UIWTCTrackingInfo setBackingProofreadingSuggestionStatePerSuggestionID:];
-[_UIWTCTrackingInfo setCurrentProofreadingText:];
-[_UIWTCTrackingInfo setCustomFillColor:forSubrangeIndex:];
-[_UIWTCTrackingInfo setDecorationContainerViewsPerRange:];
-[_UIWTCTrackingInfo setFinishedAnticipationSubrangeIndexes:];
-[_UIWTCTrackingInfo setFinishedInsertionSubrangeIndexes:];
-[_UIWTCTrackingInfo setFinishedRemovalSubrangeIndexes:];
-[_UIWTCTrackingInfo setLandedReplacementSubrangeIndexes:];
-[_UIWTCTrackingInfo setProofreadingSuggestionIDsPerDeliveryID:];
-[_UIWTCTrackingInfo setProposedEvaluationContext:];
-[_UIWTCTrackingInfo setRemovalAnimationSubranges:];
-[_UIWTCTrackingInfo setReplacementTracker:];
-[_UIWTCTrackingInfo setSavedReviewingProofreadingSuggestionID:];
-[_UIWTCTrackingInfo setShowingOriginal:];
-[_UIWTCTrackingInfo setStreaming:];
-[_UIWTCTrackingInfo setUndoRoller:];
-[_UIWTCTrackingInfo subrangesForTextAnimation:];
-[_UIWTCTrackingInfo targetedPreviewForTextAnimation:subrangeIndex:];
-[_UIWTCTrackingInfo targetedPreviewsForTextAnimation:];
-[_UIWTCTrackingInfo undoRoller];
```
