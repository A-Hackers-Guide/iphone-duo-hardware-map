# `UITextSearchingDimmingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"CAShapeLayer" _brighteningLayer;
@"CALayer" _dimmingLayer;
@"CAShapeLayer" _punchoutLayer;
B _punchoutPathIsValid;
@"NSArray" _textRects;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInset;
```

## Properties

```
@property (T{UIEdgeInsets=dddd},N,V_contentInset) contentInset;
@property (T@"NSArray",&,N,V_textRects) textRects;
```

## Instance methods

```
-[UITextSearchingDimmingView setContentInset:];
-[UITextSearchingDimmingView layoutSubviews];
-[UITextSearchingDimmingView traitCollectionDidChange:];
-[UITextSearchingDimmingView initWithFrame:];
-[UITextSearchingDimmingView contentInset];
-[UITextSearchingDimmingView _updatePunchoutPathForVisibleRect:];
-[UITextSearchingDimmingView _wantsTargetOfKeyboardEventDeferringEnvironment];
-[UITextSearchingDimmingView setTextRects:];
-[UITextSearchingDimmingView textRects];
```
