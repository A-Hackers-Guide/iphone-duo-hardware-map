# `UITextHighlightView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 9 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _padding;
@"UIPreviewParameters" _overriddenPreviewParameters;
B _contentViewValid;
@"_UITextHighlightBackgroundView" _backgroundView;
@"UIVisualEffectView" _contentClippingEffectView;
@"CAShapeLayer" _contentClippingMaskLayer;
@"UIView" _contentView;
@? _previewProvider;
@"UIColor" _fillColor;
```

## Properties

```
@property (T@?,R,C,N,V_previewProvider) previewProvider;
@property (T@"UIPreviewParameters",&,N,V_overriddenPreviewParameters) overriddenPreviewParameters;
@property (T@"UIColor",&,N,V_fillColor) fillColor;
```

## Class methods

```
+[UITextHighlightView preferredPreviewParametersForTextLineRects:];
```

## Instance methods

```
-[UITextHighlightView setFillColor:];
-[UITextHighlightView fillColor];
-[UITextHighlightView layoutSubviews];
-[UITextHighlightView previewProvider];
-[UITextHighlightView setOverriddenPreviewParameters:];
-[UITextHighlightView _fillEffect];
-[UITextHighlightView _updateWithPreviewParameters:];
-[UITextHighlightView animateWithCompletion:];
-[UITextHighlightView fadeAwayWithCompletion:];
-[UITextHighlightView initWithPreviewProvider:];
-[UITextHighlightView invalidateContentView];
-[UITextHighlightView overriddenPreviewParameters];
```
