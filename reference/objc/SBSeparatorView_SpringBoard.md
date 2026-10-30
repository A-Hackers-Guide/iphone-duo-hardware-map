# `SBSeparatorView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 3 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
Q _nubStyle;
d _keyboardHeight;
@"SBSeparatorNubView" _nubView;
```

## Properties

```
@property (T@"SBSeparatorNubView",&,N,V_nubView) nubView;
@property (TQ,N,V_nubStyle) nubStyle;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) nubRect;
@property (Td,N,V_keyboardHeight) keyboardHeight;
```

## Class methods

```
+[SBSeparatorView nubHitTestSize];
```

## Instance methods

```
-[SBSeparatorView setKeyboardHeight:];
-[SBSeparatorView keyboardHeight];
-[SBSeparatorView layoutSubviews];
-[SBSeparatorView setBounds:];
-[SBSeparatorView setFrame:];
-[SBSeparatorView initWithFrame:];
-[SBSeparatorView nubRect];
-[SBSeparatorView nubView];
-[SBSeparatorView _updateNubViewFrame];
-[SBSeparatorView nubStyle];
-[SBSeparatorView setNubStyle:];
-[SBSeparatorView setNubView:];
```
