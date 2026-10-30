# `UIKeyboardSliceSet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSString" _ssid;
@"NSMutableSet" _slices;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _startRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endRect;
d _leftWidth;
d _rightWidth;
d _mergePoint;
@"NSMutableDictionary" _controlKeys;
```

## Properties

```
@property (T@"NSMutableSet",R,V_slices) slices;
@property (T@"NSString",&,V_ssid) sliceSetID;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_startRect) startRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_endRect) endRect;
@property (Td,V_leftWidth) leftWidth;
@property (Td,V_rightWidth) rightWidth;
@property (Td,V_mergePoint) mergePoint;
@property (T@"NSMutableDictionary",&,V_controlKeys) controlKeys;
```

## Class methods

```
+[UIKeyboardSliceSet sliceSetWithDictionaryRepresenation:];
```

## Instance methods

```
-[UIKeyboardSliceSet slices];
-[UIKeyboardSliceSet description];
-[UIKeyboardSliceSet endRect];
-[UIKeyboardSliceSet setControlKeys:];
-[UIKeyboardSliceSet addSlice:];
-[UIKeyboardSliceSet controlKeys];
-[UIKeyboardSliceSet initWithSliceID:];
-[UIKeyboardSliceSet leftWidth];
-[UIKeyboardSliceSet mergePoint];
-[UIKeyboardSliceSet rightWidth];
-[UIKeyboardSliceSet setEndRect:];
-[UIKeyboardSliceSet setLeftWidth:];
-[UIKeyboardSliceSet setMergePoint:];
-[UIKeyboardSliceSet setRightWidth:];
-[UIKeyboardSliceSet setSliceSetID:];
-[UIKeyboardSliceSet setStartRect:];
-[UIKeyboardSliceSet sliceSetID];
-[UIKeyboardSliceSet startRect];
```
