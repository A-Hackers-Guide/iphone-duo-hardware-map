# `UIKBSplitTraits`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 1 class methods

## Instance variables

```
Q _corners;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leftFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rightFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_leftFrame) leftFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_rightFrame) rightFrame;
@property (TQ,R,N,V_corners) corners;
```

## Class methods

```
+[UIKBSplitTraits traitsWithLeftFrame:rightFrame:corners:];
```

## Instance methods

```
-[UIKBSplitTraits corners];
-[UIKBSplitTraits initWithLeftFrame:rightFrame:corners:];
-[UIKBSplitTraits leftFrame];
-[UIKBSplitTraits rightFrame];
```
