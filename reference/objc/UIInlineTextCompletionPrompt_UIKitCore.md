# `UIInlineTextCompletionPrompt`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIView" _textCompletionView;
@"NSMutableArray" _typedTextViews;
B _touchDown;
@"<UITextCompletionAcceptanceDelegate>" _delegate;
@"TIKeyboardCandidate" _textCompletionCandidate;
@"NSString" _textCompletion;
@"NSString" _typedText;
```

## Properties

```
@property (T@"TIKeyboardCandidate",R,N,V_textCompletionCandidate) textCompletionCandidate;
@property (T@"NSString",R,N,V_textCompletion) textCompletion;
@property (T@"NSString",R,N,V_typedText) typedText;
@property (T@"<UITextCompletionAcceptanceDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[UIInlineTextCompletionPrompt touchesEnded:withEvent:];
-[UIInlineTextCompletionPrompt pointInside:forEvent:];
-[UIInlineTextCompletionPrompt touchesCancelled:withEvent:];
-[UIInlineTextCompletionPrompt typedText];
-[UIInlineTextCompletionPrompt dealloc];
-[UIInlineTextCompletionPrompt touchesBegan:withEvent:];
-[UIInlineTextCompletionPrompt touchesMoved:withEvent:];
-[UIInlineTextCompletionPrompt setDelegate:];
-[UIInlineTextCompletionPrompt gestureRecognizerShouldBegin:];
-[UIInlineTextCompletionPrompt delegate];
-[UIInlineTextCompletionPrompt textCompletion];
-[UIInlineTextCompletionPrompt pointInside:withEvent:];
-[UIInlineTextCompletionPrompt initWithFrame:];
-[UIInlineTextCompletionPrompt textEffectsVisibilityLevel];
-[UIInlineTextCompletionPrompt accept];
-[UIInlineTextCompletionPrompt removePromptSubviews];
-[UIInlineTextCompletionPrompt setTextCompletion:inRect:];
-[UIInlineTextCompletionPrompt textCompletionCandidate];
-[UIInlineTextCompletionPrompt textEffectsVisibilityLevelInKeyboardWindow];
```
