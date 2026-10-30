# `_UISystemBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 2 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"UIView" _colorView;
@"UIVisualEffectView" _visualEffectView;
@"UIImageView" _imageView;
@"_UISystemBackgroundStrokeView" _strokeView;
@"UIView" _shadowView;
d _currentlyAppliedCornerRadius;
[7C] _subviewInsertionIndices;
{?="currentlyAppliedCornersAreContinuous"b1"didSetCustomViewMasking"b1"didSetContentViewMasking"b1"isAddingOrRemovingInternalSubview"b1} _systemBackgroundViewFlags;
@"<_UIBackgroundConfigurationInternal>" _configuration;
@"UIView" _flexInteractionGestureView;
```

## Properties

```
@property (T@"<_UIBackgroundConfigurationInternal>",C,N,V_configuration) configuration;
@property (T@"UIView",W,N,V_flexInteractionGestureView) flexInteractionGestureView;
```

## Class methods

```
+[_UISystemBackgroundView _supportsInvalidatingFocusCache];
```

## Instance methods

```
-[_UISystemBackgroundView _isEligibleForFocusInteraction];
-[_UISystemBackgroundView didAddSubview:];
-[_UISystemBackgroundView currentVisiblePathInContainerView:];
-[_UISystemBackgroundView willRemoveSubview:];
-[_UISystemBackgroundView _dynamicUserInterfaceTraitDidChange];
-[_UISystemBackgroundView focusItemsInRect:];
-[_UISystemBackgroundView shapeInContainerView:];
-[_UISystemBackgroundView outlinePathInContainerView:];
-[_UISystemBackgroundView setConfiguration:];
-[_UISystemBackgroundView layoutSubviews];
-[_UISystemBackgroundView frameInContainerView:];
-[_UISystemBackgroundView initWithConfiguration:];
-[_UISystemBackgroundView setBounds:];
-[_UISystemBackgroundView _encodableSubviews];
-[_UISystemBackgroundView effectiveInsetsInContainerView:];
-[_UISystemBackgroundView tintColorDidChange];
-[_UISystemBackgroundView flexInteractionGestureView];
-[_UISystemBackgroundView configuration];
-[_UISystemBackgroundView initWithConfiguration:containerView:];
-[_UISystemBackgroundView encodeWithCoder:];
-[_UISystemBackgroundView _flexInteractionGestureView];
-[_UISystemBackgroundView setFrame:];
-[_UISystemBackgroundView currentBackgroundColor];
-[_UISystemBackgroundView description];
-[_UISystemBackgroundView setFlexInteractionGestureView:];
-[_UISystemBackgroundView initWithCoder:];
```
