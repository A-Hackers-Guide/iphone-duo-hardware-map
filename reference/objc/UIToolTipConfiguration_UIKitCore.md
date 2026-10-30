# `UIToolTipConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"NSString" _toolTip;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
```

## Properties

```
@property (T@"NSString",C,N,V_toolTip) toolTip;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceRect) sourceRect;
```

## Class methods

```
+[UIToolTipConfiguration configurationWithToolTip:];
+[UIToolTipConfiguration configurationWithToolTip:inRect:];
```

## Instance methods

```
-[UIToolTipConfiguration setSourceRect:];
-[UIToolTipConfiguration sourceRect];
-[UIToolTipConfiguration toolTip];
-[UIToolTipConfiguration setToolTip:];
```
