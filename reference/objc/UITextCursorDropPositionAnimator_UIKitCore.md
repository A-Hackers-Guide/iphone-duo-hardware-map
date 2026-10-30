# `UITextCursorDropPositionAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _didPerformInitialUpdate;
B _isCursorVisible;
@"NSMutableArray" _alongsideAnimations;
@"NSMutableArray" _alongsideCompletions;
@"UIView<UITextCursorView>" _cursorView;
@"UIView<UITextInput>" _textInput;
```

## Properties

```
@property (T@"UIView<UITextCursorView>",R,N,V_cursorView) cursorView;
@property (T@"UIView<UITextInput>",R,N,V_textInput) textInput;
```

## Instance methods

```
-[UITextCursorDropPositionAnimator _hostView];
-[UITextCursorDropPositionAnimator cursorView];
-[UITextCursorDropPositionAnimator placeCursorAtPosition:animated:];
-[UITextCursorDropPositionAnimator _currentCaretRect];
-[UITextCursorDropPositionAnimator _cursorColor];
-[UITextCursorDropPositionAnimator _dismissalAnimatesBackToCurrentCursorPosition];
-[UITextCursorDropPositionAnimator _hasActiveCaretSelection];
-[UITextCursorDropPositionAnimator _performWithAnimation::];
-[UITextCursorDropPositionAnimator _performWithAnimation::completion:];
-[UITextCursorDropPositionAnimator animateAlongsideChanges:completion:];
-[UITextCursorDropPositionAnimator initWithTextCursorView:textInput:];
-[UITextCursorDropPositionAnimator setCursorVisible:animated:];
-[UITextCursorDropPositionAnimator textInput];
```
