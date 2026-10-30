# `UIKBSystemLayoutViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 5 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _constraints;
Q _horizontalLayoutType;
Q _verticalLayoutType;
{CGSize="width"d"height"d} _centeredOffsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _minimumInsets;
```

## Properties

```
@property (TQ,N,V_horizontalLayoutType) horizontalLayoutType;
@property (TQ,N,V_verticalLayoutType) verticalLayoutType;
@property (T{UIEdgeInsets=dddd},N,V_minimumInsets) minimumInsets;
@property (T{CGSize=dd},N,V_centeredOffsets) centeredOffsets;
```

## Class methods

```
+[UIKBSystemLayoutViewController systemLayoutViewControllerWithViewController:];
```

## Instance methods

```
-[UIKBSystemLayoutViewController updateViewConstraints];
-[UIKBSystemLayoutViewController centeredOffsets];
-[UIKBSystemLayoutViewController horizontalLayoutType];
-[UIKBSystemLayoutViewController minimumInsets];
-[UIKBSystemLayoutViewController setCenteredOffsets:];
-[UIKBSystemLayoutViewController setHorizontalLayoutType:];
-[UIKBSystemLayoutViewController setMinimumInsets:];
-[UIKBSystemLayoutViewController setVerticalLayoutType:];
-[UIKBSystemLayoutViewController verticalLayoutType];
```
