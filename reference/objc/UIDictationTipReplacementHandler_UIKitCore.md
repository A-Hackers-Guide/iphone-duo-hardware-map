# `UIDictationTipReplacementHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDictationTipRecordingProtocol`
- 5 instance variables, 9 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"<UIDictationTipHandlerDelegate>" _delegate;
@"NSString" _replacementTargetText;
@"NSMutableString" _replacementText;
@"UIDelayedAction" _finalizeAction;
q _textRecorderStatus;
```

## Properties

```
@property (T@"NSString",&,N,V_replacementTargetText) replacementTargetText;
@property (T@"NSMutableString",&,N,V_replacementText) replacementText;
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
-[UIDictationTipReplacementHandler initWithDelegate:];
-[UIDictationTipReplacementHandler resetHandler];
-[UIDictationTipReplacementHandler setDelegate:];
-[UIDictationTipReplacementHandler delegate];
-[UIDictationTipReplacementHandler replacementText];
-[UIDictationTipReplacementHandler setReplacementText:];
-[UIDictationTipReplacementHandler finalizeAction];
-[UIDictationTipReplacementHandler finalizeRecordedText];
-[UIDictationTipReplacementHandler recordDictationTipReplacementText:];
-[UIDictationTipReplacementHandler recordDictationTipText:];
-[UIDictationTipReplacementHandler replacementTargetText];
-[UIDictationTipReplacementHandler setFinalizeAction:];
-[UIDictationTipReplacementHandler setReplacementTargetText:];
-[UIDictationTipReplacementHandler setTextRecorderStatus:];
-[UIDictationTipReplacementHandler startRecodingReplacementText:];
-[UIDictationTipReplacementHandler startRecodingText:];
-[UIDictationTipReplacementHandler textRecorderStatus];
```
