# `_UIRemoteKeyboardPlaceholderView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UISplittableInputView`, `_UIRemoteKeyboardInputViewPlaceholder`
- 7 instance variables, 9 properties, 30 instance methods, 3 class methods

## Instance variables

```
@"UIView" _mirroredView;
{CGSize="width"d"height"d} _fixedSize;
@? _sizeBlock;
@"UIWindowScene" _sceneForHeight;
B _isLocalMinimumHeight;
@"UIView" _fallbackView;
@"UIView" _associatedView;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGSize=dd},N) fixedSize;
@property (T@"UIView",R) placeheldView;
@property (T@"UIView",&,N,V_fallbackView) fallbackView;
@property (T@"UIView",&,N,V_associatedView) associatedView;
@property (TB,R,N) isLocalMinimumHeightPlaceholder;
```

## Class methods

```
+[_UIRemoteKeyboardPlaceholderView placeholderWithWidth:height:];
+[_UIRemoteKeyboardPlaceholderView placeholderWithWidthSizer:heightWithScene:];
+[_UIRemoteKeyboardPlaceholderView placeholderForView:];
```

## Instance methods

```
-[_UIRemoteKeyboardPlaceholderView setFixedSize:];
-[_UIRemoteKeyboardPlaceholderView fixedSize];
-[_UIRemoteKeyboardPlaceholderView placeheldView];
-[_UIRemoteKeyboardPlaceholderView intrinsicContentSize];
-[_UIRemoteKeyboardPlaceholderView _isPlaceholderViewSelector];
-[_UIRemoteKeyboardPlaceholderView _setLeftOffset:gapWidth:];
-[_UIRemoteKeyboardPlaceholderView _beginSplitTransitionIfNeeded:gapWidth:];
-[_UIRemoteKeyboardPlaceholderView setFallbackView:];
-[_UIRemoteKeyboardPlaceholderView hitTest:withEvent:];
-[_UIRemoteKeyboardPlaceholderView didEndSplitTransition];
-[_UIRemoteKeyboardPlaceholderView _compatibleBounds];
-[_UIRemoteKeyboardPlaceholderView updateSplitSubviewContraintsWithLeftContentSize:rightContentSize:];
-[_UIRemoteKeyboardPlaceholderView initWithPlaceholderSize:];
-[_UIRemoteKeyboardPlaceholderView layoutMergedSubviews];
-[_UIRemoteKeyboardPlaceholderView associatedView];
-[_UIRemoteKeyboardPlaceholderView setAssociatedView:];
-[_UIRemoteKeyboardPlaceholderView willBeginSplitTransition];
-[_UIRemoteKeyboardPlaceholderView leftContentViewSize];
-[_UIRemoteKeyboardPlaceholderView description];
-[_UIRemoteKeyboardPlaceholderView updateMergedSubviewConstraints];
-[_UIRemoteKeyboardPlaceholderView _setProgress:boundedBy:];
-[_UIRemoteKeyboardPlaceholderView fallbackView];
-[_UIRemoteKeyboardPlaceholderView pointInside:withEvent:];
-[_UIRemoteKeyboardPlaceholderView _endSplitTransitionIfNeeded:];
-[_UIRemoteKeyboardPlaceholderView isLocalMinimumHeightPlaceholder];
-[_UIRemoteKeyboardPlaceholderView isEqual:];
-[_UIRemoteKeyboardPlaceholderView layoutSplitSubviewsWithLeftContentSize:rightContentSize:];
-[_UIRemoteKeyboardPlaceholderView rightContentViewSize];
-[_UIRemoteKeyboardPlaceholderView refreshPlaceholder];
-[_UIRemoteKeyboardPlaceholderView _configureDebugOverlayIfNecessary];
```
