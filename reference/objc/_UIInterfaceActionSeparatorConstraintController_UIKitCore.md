# `_UIInterfaceActionSeparatorConstraintController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
d _constantAxisDimension;
@"UIView<UIInterfaceActionVisualSeparatorDisplaying><UIInterfaceActionVisualSectionSeparatorDisplaying>" _separatorView;
@"NSLayoutConstraint" _fixedHeightConstraint;
@"NSLayoutConstraint" _fixedWidthConstraint;
q _constantSizedAxis;
```

## Properties

```
@property (T@"UIView<UIInterfaceActionVisualSeparatorDisplaying><UIInterfaceActionVisualSectionSeparatorDisplaying>",R,W,N,V_separatorView) separatorView;
@property (T@"NSLayoutConstraint",R,N,V_fixedHeightConstraint) fixedHeightConstraint;
@property (T@"NSLayoutConstraint",R,N,V_fixedWidthConstraint) fixedWidthConstraint;
@property (Tq,N,V_constantSizedAxis) constantSizedAxis;
@property (Td,N,V_constantAxisDimension) constantAxisDimension;
```

## Instance methods

```
-[_UIInterfaceActionSeparatorConstraintController separatorView];
-[_UIInterfaceActionSeparatorConstraintController _updateConstantSizedConstraints];
-[_UIInterfaceActionSeparatorConstraintController _isFixedWidth];
-[_UIInterfaceActionSeparatorConstraintController constantAxisDimension];
-[_UIInterfaceActionSeparatorConstraintController constantSizedAxis];
-[_UIInterfaceActionSeparatorConstraintController fixedHeightConstraint];
-[_UIInterfaceActionSeparatorConstraintController fixedWidthConstraint];
-[_UIInterfaceActionSeparatorConstraintController initWithSeparatorView:];
-[_UIInterfaceActionSeparatorConstraintController separatorViewDidUpdateConstraints];
-[_UIInterfaceActionSeparatorConstraintController setConstantAxisDimension:];
-[_UIInterfaceActionSeparatorConstraintController setConstantSizedAxis:];
```
