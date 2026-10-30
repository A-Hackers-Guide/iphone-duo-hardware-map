# `SBWalletPrearmRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<SBWalletPrearmRecognizerDelegate>" _delegate;
d _timeout;
@"BSAbsoluteMachTimer" _timer;
B _invalidated;
```

## Instance methods

```
-[SBWalletPrearmRecognizer initWithDelegate:];
-[SBWalletPrearmRecognizer _invalidate];
-[SBWalletPrearmRecognizer dealloc];
-[SBWalletPrearmRecognizer invalidate];
-[SBWalletPrearmRecognizer _computeDoubleTapTimeout];
-[SBWalletPrearmRecognizer _invalidateForFailureReason:];
-[SBWalletPrearmRecognizer _invalidateForSuccess];
-[SBWalletPrearmRecognizer startRecognizing];
-[SBWalletPrearmRecognizer triggerButtonDoublePress];
-[SBWalletPrearmRecognizer triggerButtonSinglePress];
```
