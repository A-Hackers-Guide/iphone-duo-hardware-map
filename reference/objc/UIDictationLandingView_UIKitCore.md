# `UIDictationLandingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIBasicAnimationFactory`
- 13 instance variables, 7 properties, 30 instance methods, 5 class methods

## Instance variables

```
@"UITextRange" _range;
@ _placeholder;
B _didHaveText;
B _willInsertResult;
d _angle;
d _diameter;
@"CADisplayLink" _displayLink;
d _startTime;
d _shrinkStartTime;
B _shrinking;
@"NSOperation" _afterShrinkCompletionInvocation;
B _didSkipLanding;
@"<UITextCursorAssertion>" _hideCursorAssertion;
```

## Properties

```
@property (TB,N,V_didSkipLanding) didSkipLanding;
@property (T@"<UITextCursorAssertion>",&,N,V_hideCursorAssertion) hideCursorAssertion;
@property (TB,N,V_willInsertResult) willInsertResult;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDictationLandingView sharedInstance];
+[UIDictationLandingView activeInstance];
+[UIDictationLandingView diameterForLineHeight:];
+[UIDictationLandingView fallbackPlaceholderLength];
+[UIDictationLandingView widthForLineHeight:];
```

## Instance methods

```
-[UIDictationLandingView dealloc];
-[UIDictationLandingView drawRect:];
-[UIDictationLandingView initWithFrame:];
-[UIDictationLandingView _basicAnimationForView:withKeyPath:];
-[UIDictationLandingView advanceLanding:];
-[UIDictationLandingView fadeOutDuration];
-[UIDictationLandingView _currentTextInputView];
-[UIDictationLandingView _invalidatDisplayLink];
-[UIDictationLandingView _timingFunctionForAnimation];
-[UIDictationLandingView canStopLanding];
-[UIDictationLandingView clearRotation];
-[UIDictationLandingView delegateWasEmpty];
-[UIDictationLandingView didSkipLanding];
-[UIDictationLandingView errorShakeDidFinish];
-[UIDictationLandingView hasActivePlaceholder];
-[UIDictationLandingView hideCursor];
-[UIDictationLandingView hideCursorAssertion];
-[UIDictationLandingView performRemoteSelector:];
-[UIDictationLandingView rotateBy:];
-[UIDictationLandingView setDidSkipLanding:];
-[UIDictationLandingView setHideCursorAssertion:];
-[UIDictationLandingView setWillInsertResult:];
-[UIDictationLandingView showCursor];
-[UIDictationLandingView shrinkWithCompletion:];
-[UIDictationLandingView startDisplayLinkIfNecessary];
-[UIDictationLandingView startLandingIfNecessary];
-[UIDictationLandingView stopLanding];
-[UIDictationLandingView stopLandingForError];
-[UIDictationLandingView updatePosition];
-[UIDictationLandingView willInsertResult];
```
