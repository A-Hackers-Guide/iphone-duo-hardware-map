# `_UIContentUnavailableView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 18 instance variables, 5 properties, 45 instance methods, 1 class methods

## Instance variables

```
Q _style;
@"NSString" _title;
@"_UIBackdropView" _backdrop;
@"UIView" _containerView;
@"UIScrollView" _scrollView;
@"UILabel" _titleLabel;
@"UILabel" _messageLabel;
@"UIButton" _actionButton;
@"NSLayoutConstraint" titleToMessageConstraint;
@"NSLayoutConstraint" messageToButtonConstraint;
@"UIView" _fromSnapshot;
@"UIView" _toSnapshot;
{CGSize="width"d"height"d} _fromSnapshotSize;
@"NSMutableArray" _containerViewContraints;
@"NSString" _message;
@"NSString" _buttonTitle;
@? _buttonAction;
Q _vibrantOptions;
```

## Properties

```
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_message) message;
@property (T@"NSString",C,N,V_buttonTitle) buttonTitle;
@property (T@?,C,N,V_buttonAction) buttonAction;
@property (TQ,N,V_vibrantOptions) vibrantOptions;
```

## Class methods

```
+[_UIContentUnavailableView allocWithZone:];
```

## Instance methods

```
-[_UIContentUnavailableView didMoveToWindow];
-[_UIContentUnavailableView setMessage:];
-[_UIContentUnavailableView message];
-[_UIContentUnavailableView _actionButtonPressed:];
-[_UIContentUnavailableView dealloc];
-[_UIContentUnavailableView layoutSubviews];
-[_UIContentUnavailableView _titleFont];
-[_UIContentUnavailableView _updateViewHierarchy];
-[_UIContentUnavailableView title];
-[_UIContentUnavailableView updateConstraints];
-[_UIContentUnavailableView setTitle:];
-[_UIContentUnavailableView preferredFocusedView];
-[_UIContentUnavailableView initWithFrame:];
-[_UIContentUnavailableView _hasVibrantText];
-[_UIContentUnavailableView setButtonTitle:];
-[_UIContentUnavailableView _actionButton];
-[_UIContentUnavailableView _buttonAlpha];
-[_UIContentUnavailableView _buttonBackgroundImageForStyle:controlState:];
-[_UIContentUnavailableView _buttonContentEdgeInsets];
-[_UIContentUnavailableView _buttonFont];
-[_UIContentUnavailableView _buttonSize];
-[_UIContentUnavailableView _buttonTextStyle];
-[_UIContentUnavailableView _buttonVerticalSpacing];
-[_UIContentUnavailableView _colorForButtonForStyle:controlState:];
-[_UIContentUnavailableView _flatTextColor];
-[_UIContentUnavailableView _hasVibrantButton];
-[_UIContentUnavailableView _labelAlpha];
-[_UIContentUnavailableView _labelVerticalSpacing];
-[_UIContentUnavailableView _messageLabel];
-[_UIContentUnavailableView _messageTextStyle];
-[_UIContentUnavailableView _rebuildConstraints];
-[_UIContentUnavailableView _titleLabel];
-[_UIContentUnavailableView _updateForCurrentContentSizeCategory];
-[_UIContentUnavailableView _vibrantBaseColor];
-[_UIContentUnavailableView buttonAction];
-[_UIContentUnavailableView buttonTitle];
-[_UIContentUnavailableView cleanupLingeringRotationState];
-[_UIContentUnavailableView initWithFrame:title:style:];
-[_UIContentUnavailableView initWithFrame:title:style:includeBackdrop:];
-[_UIContentUnavailableView setButtonAction:];
-[_UIContentUnavailableView setVibrantOptions:];
-[_UIContentUnavailableView vibrantOptions];
-[_UIContentUnavailableView windowDidRotateNotification:];
-[_UIContentUnavailableView windowWillAnimateRotateNotification:];
-[_UIContentUnavailableView windowWillRotateNotification:];
```
