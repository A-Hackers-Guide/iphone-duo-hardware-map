# `UIDictationTipDeletionHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDictationTipRecordingProtocol`
- 7 instance variables, 11 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<UIDictationTipHandlerDelegate>" _delegate;
@"NSMutableString" _deletionText;
@"UIDelayedAction" _finalizeAction;
q _textRecorderStatus;
q _deletionEventCount;
@"NSMutableString" _cachedDeletedText;
{_NSRange="location"Q"length"Q} _lastSelectedDeletionRange;
```

## Properties

```
@property (T@"NSMutableString",&,N,V_deletionText) deletionText;
@property (T@"UIDelayedAction",&,N,V_finalizeAction) finalizeAction;
@property (Tq,N,V_textRecorderStatus) textRecorderStatus;
@property (T{_NSRange=QQ},N,V_lastSelectedDeletionRange) lastSelectedDeletionRange;
@property (Tq,N,V_deletionEventCount) deletionEventCount;
@property (T@"NSMutableString",&,N,V_cachedDeletedText) cachedDeletedText;
@property (T@"<UIDictationTipHandlerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDictationTipDeletionHandler initWithDelegate:];
-[UIDictationTipDeletionHandler resetHandler];
-[UIDictationTipDeletionHandler setDelegate:];
-[UIDictationTipDeletionHandler delegate];
-[UIDictationTipDeletionHandler recordDictationTipDeletionText:];
-[UIDictationTipDeletionHandler addDeletionEventCount:deletedTextRange:];
-[UIDictationTipDeletionHandler cachedDeletedText];
-[UIDictationTipDeletionHandler currentDeletionEventCount];
-[UIDictationTipDeletionHandler deletionEventCount];
-[UIDictationTipDeletionHandler deletionText];
-[UIDictationTipDeletionHandler finalizeAction];
-[UIDictationTipDeletionHandler finalizeRecordedText];
-[UIDictationTipDeletionHandler lastSelectedDeletionRange];
-[UIDictationTipDeletionHandler recordDictationTipText:];
-[UIDictationTipDeletionHandler resetDeletionEventCount];
-[UIDictationTipDeletionHandler resetRecorder];
-[UIDictationTipDeletionHandler setCachedDeletedText:];
-[UIDictationTipDeletionHandler setDeletionEventCount:];
-[UIDictationTipDeletionHandler setDeletionText:];
-[UIDictationTipDeletionHandler setFinalizeAction:];
-[UIDictationTipDeletionHandler setLastSelectedDeletionRange:];
-[UIDictationTipDeletionHandler setTextRecorderStatus:];
-[UIDictationTipDeletionHandler setlastDeletionRange:];
-[UIDictationTipDeletionHandler startRecodingDeletionText:];
-[UIDictationTipDeletionHandler startRecodingText:];
-[UIDictationTipDeletionHandler textRecorderStatus];
```
