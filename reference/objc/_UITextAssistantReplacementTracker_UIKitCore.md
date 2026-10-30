# `_UITextAssistantReplacementTracker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 23 properties, 37 instance methods, 0 class methods

## Instance variables

```
Q _offsetForSessionRange;
{_NSRange="location"Q"length"Q} _sessionContextRange;
@"WTContext" _originalContext;
@"NSWritingToolsEditTracker" _editTracker;
@"NSMutableArray" _replacementDeliveryUUIDs;
@"NSMutableDictionary" _replacementChunksByUUID;
@"NSMutableDictionary" _initialReplacementChunksByUUID;
@"NSUUID" _fallbackDeliveryID;
q _selectedRewriteIndex;
@"NSMutableArray" _previousRewrites;
@"NSMutableArray" _previousRewrittenTexts;
B _proofreading;
B _finished;
q _compositionSessionState;
@"NSAttributedString" _processedOriginalText;
@"NSAttributedString" _unprocessedOriginalText;
@"NSUUID" _contextUUID;
@"NSWritingToolsProofreadingController" _proofreadingController;
@"NSAttributedString" _originalText;
@"NSAttributedString" _rewrittenText;
```

## Properties

```
@property (T@"NSAttributedString",R,N) assembledRewrittenText;
@property (T{_NSRange=QQ},R,N) rewrittenCharacterRange;
@property (T{_NSRange=QQ},R,N) activeFullCharacterRange;
@property (T@"NSUUID",R,N,V_contextUUID) contextUUID;
@property (T@"NSWritingToolsProofreadingController",R,N,V_proofreadingController) proofreadingController;
@property (TQ,N,V_offsetForSessionRange) offsetForSessionRange;
@property (TB,R,N,GisProofreading,V_proofreading) proofreading;
@property (TB,R,N,GisRewriting) rewriting;
@property (TB,R,N) hasProcessedOriginalRange;
@property (Tq,N,V_compositionSessionState) compositionSessionState;
@property (TB,R,N,GisFinished,V_finished) finished;
@property (T@"NSAttributedString",R,N,V_originalText) originalText;
@property (T@"NSAttributedString",R,N,V_processedOriginalText) processedOriginalText;
@property (T@"NSAttributedString",R,N,V_unprocessedOriginalText) unprocessedOriginalText;
@property (T@"NSAttributedString",R,N,V_rewrittenText) rewrittenText;
@property (T@"NSAttributedString",R,N) activeText;
@property (T{_NSRange=QQ},R,N) originalCharacterRange;
@property (T{_NSRange=QQ},R,N) processedOriginalCharacterRange;
@property (T{_NSRange=QQ},R,N) initialCurrentChunkCharacterRange;
@property (T{_NSRange=QQ},R,N) finalCurrentChunkCharacterRange;
@property (T{_NSRange=QQ},R,N) activeCharacterRange;
@property (T{_NSRange=QQ},R,N) activeUnprocessedCharacterRange;
@property (TQ,R,N) numberOfPreviousRewrittenTexts;
```

## Instance methods

```
-[_UITextAssistantReplacementTracker isFinished];
-[_UITextAssistantReplacementTracker description];
-[_UITextAssistantReplacementTracker activeUnprocessedCharacterRange];
-[_UITextAssistantReplacementTracker processedOriginalCharacterRange];
-[_UITextAssistantReplacementTracker finalCurrentChunkCharacterRange];
-[_UITextAssistantReplacementTracker activeCharacterRange];
-[_UITextAssistantReplacementTracker activeFullCharacterRange];
-[_UITextAssistantReplacementTracker activeText];
-[_UITextAssistantReplacementTracker assembledRewrittenText];
-[_UITextAssistantReplacementTracker assembledRewrittenTextToDelivery:matchingInitialDeliveries:];
-[_UITextAssistantReplacementTracker compositionSessionState];
-[_UITextAssistantReplacementTracker contextUUID];
-[_UITextAssistantReplacementTracker hasProcessedOriginalRange];
-[_UITextAssistantReplacementTracker initFromSessionContext:offsetForSessionRange:withProofreadingController:];
-[_UITextAssistantReplacementTracker initialCurrentChunkCharacterRange];
-[_UITextAssistantReplacementTracker isProofreading];
-[_UITextAssistantReplacementTracker isRewriting];
-[_UITextAssistantReplacementTracker newEditTracker];
-[_UITextAssistantReplacementTracker nextDeliveryForDelivery:];
-[_UITextAssistantReplacementTracker numberOfPreviousRewrittenTexts];
-[_UITextAssistantReplacementTracker offsetForSessionRange];
-[_UITextAssistantReplacementTracker originalCharacterRange];
-[_UITextAssistantReplacementTracker originalChunkTextForDelivery:];
-[_UITextAssistantReplacementTracker originalText];
-[_UITextAssistantReplacementTracker processedOriginalText];
-[_UITextAssistantReplacementTracker proofreadingController];
-[_UITextAssistantReplacementTracker recordRewrittenText:forRange:withContext:finished:];
-[_UITextAssistantReplacementTracker rewrittenCharacterRange];
-[_UITextAssistantReplacementTracker rewrittenChunkTextForDelivery:];
-[_UITextAssistantReplacementTracker rewrittenText];
-[_UITextAssistantReplacementTracker selectRewriteMatchingUndoRedoReplacementText:];
-[_UITextAssistantReplacementTracker setCompositionSessionState:];
-[_UITextAssistantReplacementTracker setOffsetForSessionRange:];
-[_UITextAssistantReplacementTracker sourceRangeForChunkFromDelivery:];
-[_UITextAssistantReplacementTracker targetRangeForChunkFromDelivery:];
-[_UITextAssistantReplacementTracker unprocessedOriginalText];
-[_UITextAssistantReplacementTracker updateReplacementChunkForDeliveryID:newText:];
```
