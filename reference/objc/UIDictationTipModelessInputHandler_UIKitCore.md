# `UIDictationTipModelessInputHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _modelessInputTipDictationStoppedSignal;
B _softwareKeyboardInteractionAfterDictationStoppedSignal;
B _shouldAttemptToShowModelessTip;
@"<UIDictationTipHandlerDelegate>" _delegate;
```

## Properties

```
@property (T@"<UIDictationTipHandlerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_modelessInputTipDictationStoppedSignal) modelessInputTipDictationStoppedSignal;
@property (TB,N,V_softwareKeyboardInteractionAfterDictationStoppedSignal) softwareKeyboardInteractionAfterDictationStoppedSignal;
@property (TB,N,V_shouldAttemptToShowModelessTip) shouldAttemptToShowModelessTip;
```

## Instance methods

```
-[UIDictationTipModelessInputHandler shouldShowModelessInputTip];
-[UIDictationTipModelessInputHandler initWithDelegate:];
-[UIDictationTipModelessInputHandler shouldAttemptToShowModelessTip];
-[UIDictationTipModelessInputHandler triggerAttemptToShowModelessTipFlag];
-[UIDictationTipModelessInputHandler processSoftwareKeyboardInteraction];
-[UIDictationTipModelessInputHandler modelessInputTipDictationStoppedSignal];
-[UIDictationTipModelessInputHandler showModelessInputTip];
-[UIDictationTipModelessInputHandler processUserInteractionEnded];
-[UIDictationTipModelessInputHandler userInteractionEndedDuringModelessInputTipDictationStoppedSignal];
-[UIDictationTipModelessInputHandler setDelegate:];
-[UIDictationTipModelessInputHandler setSoftwareKeyboardInteractionAfterDictationStoppedSignal:];
-[UIDictationTipModelessInputHandler delegate];
-[UIDictationTipModelessInputHandler softwareKeyboardInteractionAfterDictationStoppedSignal];
-[UIDictationTipModelessInputHandler resetDictationTipModelessHandlerSignalFlags];
-[UIDictationTipModelessInputHandler setShouldAttemptToShowModelessTip:];
-[UIDictationTipModelessInputHandler setModelessInputTipDictationStoppedSignal:];
```
