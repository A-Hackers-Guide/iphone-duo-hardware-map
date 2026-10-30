# `UIKBWatch10KeyLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
@"NSArray" _leftControlKeyFrames;
@"NSArray" _rightControlKeyFrames;
@"NSMutableArray" _gridKeyFrames;
q _leftControlKeys;
q _gridRows;
q _gridColumns;
q _rightControlKeys;
d _controlKeyWidthRatio;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _leftControlKeysInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _rightControlKeysInsets;
```

## Properties

```
@property (Tq,N,V_leftControlKeys) leftControlKeys;
@property (T{UIEdgeInsets=dddd},N,V_leftControlKeysInsets) leftControlKeysInsets;
@property (Tq,N,V_gridRows) gridRows;
@property (Tq,N,V_gridColumns) gridColumns;
@property (Tq,N,V_rightControlKeys) rightControlKeys;
@property (T{UIEdgeInsets=dddd},N,V_rightControlKeysInsets) rightControlKeysInsets;
@property (Td,N,V_controlKeyWidthRatio) controlKeyWidthRatio;
```

## Instance methods

```
-[UIKBWatch10KeyLayout layout];
-[UIKBWatch10KeyLayout initWithFrame:];
-[UIKBWatch10KeyLayout setGridColumns:];
-[UIKBWatch10KeyLayout leftControlKeys];
-[UIKBWatch10KeyLayout controlKeyWidthRatio];
-[UIKBWatch10KeyLayout frameForGridKeyAt:inRow:];
-[UIKBWatch10KeyLayout frameForLeftControlKeyAt:];
-[UIKBWatch10KeyLayout frameForRightControlKeyAt:];
-[UIKBWatch10KeyLayout gridColumns];
-[UIKBWatch10KeyLayout gridRows];
-[UIKBWatch10KeyLayout layoutControlKeys:in:];
-[UIKBWatch10KeyLayout leftControlKeysInsets];
-[UIKBWatch10KeyLayout rightControlKeys];
-[UIKBWatch10KeyLayout rightControlKeysInsets];
-[UIKBWatch10KeyLayout setControlKeyWidthRatio:];
-[UIKBWatch10KeyLayout setGridRows:];
-[UIKBWatch10KeyLayout setLeftControlKeys:];
-[UIKBWatch10KeyLayout setLeftControlKeysInsets:];
-[UIKBWatch10KeyLayout setRightControlKeys:];
-[UIKBWatch10KeyLayout setRightControlKeysInsets:];
```
