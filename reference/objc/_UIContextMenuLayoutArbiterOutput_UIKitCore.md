# `_UIContextMenuLayoutArbiterOutput`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _type;
d _maximumMenuHeight;
@"NSMapTable" _accessoryPositions;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentBounds;
{?="attachment"Q"alignment"Q"attachmentOffset"d"alignmentOffset"d"gravity"q} _anchor;
{?="bounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"center"{CAPoint3D="x"d"y"d"z"d}"anchorPoint"{CGPoint="x"d"y"d}"transform"{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d}"alpha"d} _preview;
{?="bounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"center"{CAPoint3D="x"d"y"d"z"d}"anchorPoint"{CGPoint="x"d"y"d}"transform"{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d}"alpha"d} _menu;
```

## Properties

```
@property (TQ,N,V_type) type;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_contentBounds) contentBounds;
@property (Td,N,V_maximumMenuHeight) maximumMenuHeight;
@property (T{?={CGRect={CGPoint=dd}{CGSize=dd}}{CAPoint3D=ddd}{CGPoint=dd}{CGAffineTransform=dddddd}d},N,V_preview) preview;
@property (T{?={CGRect={CGPoint=dd}{CGSize=dd}}{CAPoint3D=ddd}{CGPoint=dd}{CGAffineTransform=dddddd}d},N,V_menu) menu;
@property (T{?=QQddq},N,V_anchor) anchor;
@property (T@"NSMapTable",&,N,V_accessoryPositions) accessoryPositions;
```

## Instance methods

```
-[_UIContextMenuLayoutArbiterOutput menu];
-[_UIContextMenuLayoutArbiterOutput setContentBounds:];
-[_UIContextMenuLayoutArbiterOutput preview];
-[_UIContextMenuLayoutArbiterOutput setAnchor:];
-[_UIContextMenuLayoutArbiterOutput contentBounds];
-[_UIContextMenuLayoutArbiterOutput setAccessoryPositions:];
-[_UIContextMenuLayoutArbiterOutput anchor];
-[_UIContextMenuLayoutArbiterOutput setPreview:];
-[_UIContextMenuLayoutArbiterOutput setType:];
-[_UIContextMenuLayoutArbiterOutput type];
-[_UIContextMenuLayoutArbiterOutput setMaximumMenuHeight:];
-[_UIContextMenuLayoutArbiterOutput maximumMenuHeight];
-[_UIContextMenuLayoutArbiterOutput accessoryPositions];
-[_UIContextMenuLayoutArbiterOutput setMenu:];
```
