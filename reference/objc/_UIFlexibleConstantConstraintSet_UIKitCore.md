# `_UIFlexibleConstantConstraintSet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIConstantConstraintSet`
- 7 instance variables, 3 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSLayoutConstraint" _minConstraint;
@"NSLayoutConstraint" _maxConstraint;
@"NSLayoutConstraint" _equalityConstraint;
B _equalityConstraintPrefersMin;
d _minConstant;
d _maxConstant;
d _equalityConstant;
```

## Properties

```
@property (Td,N,V_minConstant) minConstant;
@property (Td,N,V_maxConstant) maxConstant;
@property (Td,N,V_equalityConstant) equalityConstant;
```

## Class methods

```
+[_UIFlexibleConstantConstraintSet constraintSetWithCollapsableConstantPreferredEqualityConstraint:equalityPriority:];
+[_UIFlexibleConstantConstraintSet constraintSetWithRequiredEqualityConstraint:];
```

## Instance methods

```
-[_UIFlexibleConstantConstraintSet setMaxConstant:];
-[_UIFlexibleConstantConstraintSet equalityConstant];
-[_UIFlexibleConstantConstraintSet minConstant];
-[_UIFlexibleConstantConstraintSet _updateInequalityConstants];
-[_UIFlexibleConstantConstraintSet _equalityConstraintIsRequired];
-[_UIFlexibleConstantConstraintSet setMinConstant:];
-[_UIFlexibleConstantConstraintSet _preferredInequalityConstraint];
-[_UIFlexibleConstantConstraintSet _otherInequalityConstraint];
-[_UIFlexibleConstantConstraintSet _initWithEqualityConstraint:equalityPriority:prefersMin:];
-[_UIFlexibleConstantConstraintSet maxConstant];
-[_UIFlexibleConstantConstraintSet setEqualityConstant:];
```
