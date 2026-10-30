# `PKPaletteToolPickerClippingView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteViewSizeScaling`
- 22 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"PKPaletteToolPickerBackgroundContentView" _backgroundContentView;
@"PKPalettePassthroughView" _contentOverlayView;
@"PKPaletteToolPickerClippingEdgeView" _leadingEdgeView;
@"PKPaletteToolPickerClippingEdgeView" _trailingEdgeView;
@"PKPaletteToolPickerClippingEdgeView" _topEdgeView;
@"PKPaletteToolPickerClippingEdgeView" _bottomEdgeView;
@"NSArray" _edgeViews;
@"NSArray" _edgeViewThicknessConstraints;
@"NSLayoutConstraint" _leadingEdgeViewTopConstraint;
@"NSLayoutConstraint" _trailingEdgeViewTopConstraint;
@"NSLayoutConstraint" _topEdgeViewLeadingConstraint;
@"NSLayoutConstraint" _topEdgeViewTrailingConstraint;
@"NSLayoutConstraint" _bottomEdgeViewLeadingConstraint;
@"NSLayoutConstraint" _bottomEdgeViewTrailingConstraint;
B _isVerticalRight;
B _leadingOrTopEdgeVisible;
B _trailingOrBottomEdgeVisible;
B _lassoToolEditingViewVisible;
B _scrollingEnabled;
d _scalingFactor;
@"UIView" _contentView;
q _layoutAxis;
```

## Properties

```
@property (Td,N,V_scalingFactor) scalingFactor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteToolPickerClippingView scalingFactor];
-[PKPaletteToolPickerClippingView init];
-[PKPaletteToolPickerClippingView layoutSubviews];
-[PKPaletteToolPickerClippingView setScalingFactor:];
```
