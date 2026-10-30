# `UIDictationTipPresentationHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _isShowingTip;
B _tipPresentedInCurrentDictationSession;
q _dictationTipSignaled;
```

## Properties

```
@property (Tq,N,V_dictationTipSignaled) dictationTipSignaled;
@property (TB,N,V_tipPresentedInCurrentDictationSession) tipPresentedInCurrentDictationSession;
@property (TB,N,V_isShowingTip) isShowingTip;
```

## Instance methods

```
-[UIDictationTipPresentationHandler init];
-[UIDictationTipPresentationHandler resetHandler];
-[UIDictationTipPresentationHandler dictationCommandTipsEnabled];
-[UIDictationTipPresentationHandler dictationTipDisplayCount:];
-[UIDictationTipPresentationHandler dictationTipShownOverLimit:];
-[UIDictationTipPresentationHandler dictationTipSignaled];
-[UIDictationTipPresentationHandler getDictationTipSignaled];
-[UIDictationTipPresentationHandler isShowingTip];
-[UIDictationTipPresentationHandler resetDictationTipSignal];
-[UIDictationTipPresentationHandler setDictationTipSignaled:];
-[UIDictationTipPresentationHandler setIsShowingTip:];
-[UIDictationTipPresentationHandler setTipPresentedInCurrentDictationSession:];
-[UIDictationTipPresentationHandler shouldSignalDictationTip:];
-[UIDictationTipPresentationHandler signalTipPresentedInCurrentDictationSession];
-[UIDictationTipPresentationHandler tipPresentedInCurrentDictationSession];
-[UIDictationTipPresentationHandler tipShownLastWeek];
```
