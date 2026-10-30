# `UIWKTextInteractionAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInteractionAssistant`
- Protocols: `UIResponderStandardEditActions`
- 20 instance variables, 11 properties, 85 instance methods, 0 class methods

## Instance variables

```
q _selectionOperation;
@"_UITextServiceSession" _definitionSession;
@"_UITextServiceSession" _learnSession;
@"_UITextServiceSession" _shareSession;
@"_UITextServiceSession" _lookupSession;
@"_UITextServiceSession" _translateSession;
@"UITextChecker" _textChecker;
Q _options;
@"_UIBurnableBlock" _prepareToInvalidateLoupeSessionBlock;
B _isEndingRangeAdjustmentInteraction;
@"<UITextCursorAssertion>" _blinkAssertion;
@"<UIWKTextInteractionAssistantDelegate>" _delegate;
@"UIProofreadingSuggestionList" _currentProofreadingSuggestionList;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentProofreadingSuggestionRect;
@? _currentWritingToolsAnchorCompletion;
@"WTSession" _currentWritingToolsSession;
@"WTContext" _currentWritingToolsContext;
B _shouldDelayActivatingSelectionView;
@"NSString" _wordBeforeTap;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _caretBeforeTap;
```

## Properties

```
@property (T@"NSString",&,N,V_wordBeforeTap) wordBeforeTap;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_caretBeforeTap) caretBeforeTap;
@property (T@"UITapGestureRecognizer",R,D,N) singleTapGesture;
@property (T@"UILongPressGestureRecognizer",R,D,N) loupeGesture;
@property (T@"UILongPressGestureRecognizer",R,D,N) forcePressGesture;
@property (TB,N,V_shouldDelayActivatingSelectionView) shouldDelayActivatingSelectionView;
@property (T@"<UIWKTextInteractionAssistantDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWKTextInteractionAssistant asyncWebKitInteractionDelegate];
-[UIWKTextInteractionAssistant selectAll:];
-[UIWKTextInteractionAssistant shouldSuppressSelectionCommands];
-[UIWKTextInteractionAssistant textChecker];
-[UIWKTextInteractionAssistant scheduleReplacementsWithOptions:];
-[UIWKTextInteractionAssistant beginSelectionChange];
-[UIWKTextInteractionAssistant endSelectionChange];
-[UIWKTextInteractionAssistant proofreadingDidUpdateState:forAlwaysOnSuggestionsWithUUIDs:];
-[UIWKTextInteractionAssistant proofreadingScrollToVisibleAlwaysOnSuggestionWithUUID:completion:];
-[UIWKTextInteractionAssistant showTextServiceFor:fromRect:];
-[UIWKTextInteractionAssistant lookup:withRange:fromRect:];
-[UIWKTextInteractionAssistant initWithView:];
-[UIWKTextInteractionAssistant selectionChanged];
-[UIWKTextInteractionAssistant dealloc];
-[UIWKTextInteractionAssistant showShareSheetFor:fromRect:];
-[UIWKTextInteractionAssistant showDictionaryFor:fromRect:];
-[UIWKTextInteractionAssistant proofreadingRetrieveResultOptionsForAlwaysOnSuggestionWithUUID:completion:];
-[UIWKTextInteractionAssistant translate:fromRect:];
-[UIWKTextInteractionAssistant setDelegate:];
-[UIWKTextInteractionAssistant proofreadingDidDismissSuggestions];
-[UIWKTextInteractionAssistant showSelectionView];
-[UIWKTextInteractionAssistant didEndScrollingOverflow];
-[UIWKTextInteractionAssistant scheduleReplacementsForText:];
-[UIWKTextInteractionAssistant delegate];
-[UIWKTextInteractionAssistant selectionChangedWithTouchAt:withSelectionTouch:withFlags:];
-[UIWKTextInteractionAssistant selectionChangedWithGestureAt:withGesture:withState:withFlags:];
-[UIWKTextInteractionAssistant scheduleChineseTransliterationForText:];
-[UIWKTextInteractionAssistant scrollSelectionToVisible:];
-[UIWKTextInteractionAssistant proofreadingSetCheckGrammarWhileTyping:];
-[UIWKTextInteractionAssistant selectWord];
-[UIWKTextInteractionAssistant _asText];
-[UIWKTextInteractionAssistant _findCurrentProofreadingSuggestionAndShow:category:grammarUUID:];
-[UIWKTextInteractionAssistant containerIsAtom];
-[UIWKTextInteractionAssistant addGestureRecognizersToView:];
-[UIWKTextInteractionAssistant alternativesForSelectedText];
-[UIWKTextInteractionAssistant asyncInteractionDelegate];
-[UIWKTextInteractionAssistant asyncTextInteractionDelegate];
-[UIWKTextInteractionAssistant caretBeforeTap];
-[UIWKTextInteractionAssistant changeSelectionWithTouchAt:withSelectionTouch:baseIsStart:withFlags:];
-[UIWKTextInteractionAssistant containerAllowsSelection];
-[UIWKTextInteractionAssistant containerAllowsSelectionTintOnly];
-[UIWKTextInteractionAssistant containerIsBrowserView];
-[UIWKTextInteractionAssistant currentCursorBehavior];
-[UIWKTextInteractionAssistant didEndSelectionInteraction];
-[UIWKTextInteractionAssistant generatorForRange:withOptions:];
-[UIWKTextInteractionAssistant lookup:fromRect:];
-[UIWKTextInteractionAssistant overrideGestureRecognizer:shouldReceiveTouch:];
-[UIWKTextInteractionAssistant overrideGestureRecognizerShouldBegin:];
-[UIWKTextInteractionAssistant proofreadingDidUpdateState:forAlwaysOnSuggestionWithUUID:];
-[UIWKTextInteractionAssistant proofreadingScrollToVisibleAlwaysOnSuggestionWithUUID:];
-[UIWKTextInteractionAssistant proofreadingSessionWithUUID:showDetailsForSuggestionWithUUID:relativeToRect:inView:];
-[UIWKTextInteractionAssistant rangeSelectionCanceled];
-[UIWKTextInteractionAssistant rangeSelectionEnded:];
-[UIWKTextInteractionAssistant rangeSelectionMoved:withTouchPoint:];
-[UIWKTextInteractionAssistant rangeSelectionStarted:];
-[UIWKTextInteractionAssistant requiresImmediateUpdate];
-[UIWKTextInteractionAssistant scheduleReplacementsForText:withOptions:];
-[UIWKTextInteractionAssistant selectProofreadingSuggestionRange:contextString:alternatives:];
-[UIWKTextInteractionAssistant selectTextForReplacement:withOptions:];
-[UIWKTextInteractionAssistant selectionInteractionClass];
-[UIWKTextInteractionAssistant setCaretBeforeTap:];
-[UIWKTextInteractionAssistant setShouldDelayActivatingSelectionView:];
-[UIWKTextInteractionAssistant setWordBeforeTap:];
-[UIWKTextInteractionAssistant shouldDelayActivatingSelectionView];
-[UIWKTextInteractionAssistant shouldDisplayProofreadingSuggestionCalloutBarItemWithCategory:grammarUUID:];
-[UIWKTextInteractionAssistant shouldTryReplacementsForText:withOptions:];
-[UIWKTextInteractionAssistant showProofreadingSuggestion];
-[UIWKTextInteractionAssistant showProofreadingSuggestionsForAlternatives:];
-[UIWKTextInteractionAssistant showReplacementsForText:withOptions:];
-[UIWKTextInteractionAssistant showReplacementsForText:withOptions:rects:];
-[UIWKTextInteractionAssistant textRangeAdjustmentInteraction:didBeginAtPoint:];
-[UIWKTextInteractionAssistant textRangeAdjustmentInteraction:didEndAtPoint:];
-[UIWKTextInteractionAssistant textRangeAdjustmentInteraction:prepareForInvalidation:];
-[UIWKTextInteractionAssistant textRangeAdjustmentInteraction:selectionMoved:withTouchPoint:];
-[UIWKTextInteractionAssistant textRangeAdjustmentInteractionWasCancelled:];
-[UIWKTextInteractionAssistant updateActivatingSelectionView];
-[UIWKTextInteractionAssistant updateSelectionWithPoint:];
-[UIWKTextInteractionAssistant updateWithMagnifierTerminalPoint:];
-[UIWKTextInteractionAssistant usesAsynchronousSelectionController];
-[UIWKTextInteractionAssistant wantsLinkInteraction];
-[UIWKTextInteractionAssistant webInteractionDelegate];
-[UIWKTextInteractionAssistant willBeginSelectionInteraction];
-[UIWKTextInteractionAssistant willChangeSelection];
-[UIWKTextInteractionAssistant willStartScrollingOverflow];
-[UIWKTextInteractionAssistant wordBeforeTap];
```
