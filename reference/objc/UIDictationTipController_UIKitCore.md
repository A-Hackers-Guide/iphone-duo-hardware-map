# `UIDictationTipController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDictationTipHandlerDelegate`
- 9 instance variables, 14 properties, 51 instance methods, 1 class methods

## Instance variables

```
Q _dismissalReasonType;
@"UIDictationTipPresentationHandler" _dictationTipPresentationHandler;
@"UIDictationTipReplacementHandler" _dictationReplacementTipHandler;
@"UIDictationTipDeletionHandler" _dictationDeletionTipHandler;
@"UIDictationTipEmojiHandler" _dictationEmojiTipHandler;
@"UIDictationTipSelectionHandler" _dictationSelectionTipHandler;
@"UIDictationTipInsertionHandler" _dictationInsertionTipHandler;
@"UIDictationTipModelessInputHandler" _dictationTipModelessInputHandler;
@? _delayedTip;
```

## Properties

```
@property (T@"UIDictationTipPresentationHandler",&,N,V_dictationTipPresentationHandler) dictationTipPresentationHandler;
@property (T@"UIDictationTipReplacementHandler",&,N,V_dictationReplacementTipHandler) dictationReplacementTipHandler;
@property (T@"UIDictationTipDeletionHandler",&,N,V_dictationDeletionTipHandler) dictationDeletionTipHandler;
@property (T@"UIDictationTipEmojiHandler",&,N,V_dictationEmojiTipHandler) dictationEmojiTipHandler;
@property (T@"UIDictationTipSelectionHandler",&,N,V_dictationSelectionTipHandler) dictationSelectionTipHandler;
@property (T@"UIDictationTipInsertionHandler",&,N,V_dictationInsertionTipHandler) dictationInsertionTipHandler;
@property (T@"UIDictationTipModelessInputHandler",&,N,V_dictationTipModelessInputHandler) dictationTipModelessInputHandler;
@property (T@?,C,N,V_delayedTip) delayedTip;
@property (TQ,N,V_dismissalReasonType) dismissalReasonType;
@property (Tq,R,N) activeTipType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDictationTipController dictationTipPreferenceKey:];
```

## Instance methods

```
-[UIDictationTipController init];
-[UIDictationTipController reset];
-[UIDictationTipController signalDictationSelectionTip:];
-[UIDictationTipController processSoftwareKeyboardInteraction];
-[UIDictationTipController processUserInteractionEnded];
-[UIDictationTipController dictationTipPresentationHandler];
-[UIDictationTipController recordDictationTipDeletionText:];
-[UIDictationTipController setDictationDeletionTipHandler:];
-[UIDictationTipController activeTipType];
-[UIDictationTipController addDeletionEventCount:deletedTextRange:];
-[UIDictationTipController currentDeletionEventCount];
-[UIDictationTipController delayedTip];
-[UIDictationTipController dictationCommandUsed:firstTargetString:secondTargetString:];
-[UIDictationTipController dictationDeletionTipHandler];
-[UIDictationTipController dictationEmojiTipHandler];
-[UIDictationTipController dictationInsertionTipHandler];
-[UIDictationTipController dictationReplacementTipHandler];
-[UIDictationTipController dictationSelectionTipHandler];
-[UIDictationTipController dictationTipModelessInputHandler];
-[UIDictationTipController dictationTipShown:];
-[UIDictationTipController dismissalReasonType];
-[UIDictationTipController emitTipShowingInstrumentation:];
-[UIDictationTipController finalizeSelectionTip];
-[UIDictationTipController finalizeTextWithTipType:title:andTipDescription:];
-[UIDictationTipController getDictationTipSignaled];
-[UIDictationTipController incrementDictationTipDisplayCount:stopFutureShowing:];
-[UIDictationTipController logDictationTipDimissialInstrumentation];
-[UIDictationTipController markDictationTipPreferenceToShown:];
-[UIDictationTipController modelessTipShown];
-[UIDictationTipController presentDelayedTipIfNeeded];
-[UIDictationTipController recordDictationTipReplacementText:];
-[UIDictationTipController replaceEmojiInStringWithEmojiDictationCommand:];
-[UIDictationTipController resetDeletionEventCount];
-[UIDictationTipController resetShowModelessTipSignal];
-[UIDictationTipController setDelayedTip:];
-[UIDictationTipController setDictationEmojiTipHandler:];
-[UIDictationTipController setDictationInsertionTipHandler:];
-[UIDictationTipController setDictationReplacementTipHandler:];
-[UIDictationTipController setDictationSelectionTipHandler:];
-[UIDictationTipController setDictationTipModelessInputHandler:];
-[UIDictationTipController setDictationTipPresentationHandler:];
-[UIDictationTipController setDismissalReasonType:];
-[UIDictationTipController showDictationTipWithTitle:description:dictationTipType:];
-[UIDictationTipController signalDictationClearAllTip];
-[UIDictationTipController signalDictationDeletionTip:];
-[UIDictationTipController signalDictationEmojiTip:];
-[UIDictationTipController signalDictationInsertionTip:];
-[UIDictationTipController signalDictationReplacementTip:];
-[UIDictationTipController signalDictationSendMessageTip];
-[UIDictationTipController signalShowModelessTipIfNeeded];
-[UIDictationTipController triggerModelessInputTipDictationStoppedSignal];
```
