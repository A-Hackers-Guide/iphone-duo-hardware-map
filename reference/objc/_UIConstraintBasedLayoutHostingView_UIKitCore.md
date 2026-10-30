# `_UIConstraintBasedLayoutHostingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 2 instance variables, 1 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"UIView" _hostedView;
B _hasAddedConstraints;
```

## Properties

```
@property (T@"UIView",&,N,V_hostedView) hostedView;
```

## Class methods

```
+[_UIConstraintBasedLayoutHostingView requiresConstraintBasedLayout];
```

## Instance methods

```
-[_UIConstraintBasedLayoutHostingView _setFrameWithAlignmentRect:];
-[_UIConstraintBasedLayoutHostingView _intrinsicContentSizeInvalidatedForChildView:];
-[_UIConstraintBasedLayoutHostingView willRemoveSubview:];
-[_UIConstraintBasedLayoutHostingView constraintsDidChangeInEngine:];
-[_UIConstraintBasedLayoutHostingView initWithHostedView:];
-[_UIConstraintBasedLayoutHostingView alignmentRectInsets];
-[_UIConstraintBasedLayoutHostingView setHostedView:];
-[_UIConstraintBasedLayoutHostingView hostedView];
-[_UIConstraintBasedLayoutHostingView sizeThatFits:];
-[_UIConstraintBasedLayoutHostingView _scheduleUpdateConstraintsPassAsEngineHostNeedingLayout:];
-[_UIConstraintBasedLayoutHostingView updateConstraints];
-[_UIConstraintBasedLayoutHostingView _layoutHeightDependsOnWidth];
-[_UIConstraintBasedLayoutHostingView _layoutSizeThatFits:fixedAxes:];
-[_UIConstraintBasedLayoutHostingView _layoutMetricsInvalidatedForHostedView];
-[_UIConstraintBasedLayoutHostingView _baselineOffsetsAtSize:];
```
