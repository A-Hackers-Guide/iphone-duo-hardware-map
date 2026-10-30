# `UIDictationTipInsertionHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDictationTipRecordingProtocol`
- 4 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<UIDictationTipHandlerDelegate>" _delegate;
@"NSMutableString" _insertionText;
@"UIDelayedAction" _finalizeAction;
q _textRecorderStatus;
```

## Properties

```
@property (T@"NSMutableString",&,N,V_insertionText) insertionText;
@property (T@"UIDelayedAction",&,N,V_finalizeAction) finalizeAction;
@property (Tq,N,V_textRecorderStatus) textRecorderStatus;
@property (T@"<UIDictationTipHandlerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDictationTipInsertionHandler initWithDelegate:];
-[UIDictationTipInsertionHandler resetHandler];
-[UIDictationTipInsertionHandler setDelegate:];
-[UIDictationTipInsertionHandler delegate];
-[UIDictationTipInsertionHandler finalizeAction];
-[UIDictationTipInsertionHandler finalizeRecordedText];
-[UIDictationTipInsertionHandler insertionText];
-[UIDictationTipInsertionHandler recordDictationTipText:];
-[UIDictationTipInsertionHandler setFinalizeAction:];
-[UIDictationTipInsertionHandler setInsertionText:];
-[UIDictationTipInsertionHandler setTextRecorderStatus:];
-[UIDictationTipInsertionHandler startRecodingText:];
-[UIDictationTipInsertionHandler textRecorderStatus];
```
