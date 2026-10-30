# `_UINavigationBarTitleViewOverlayRects`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 13 properties, 26 instance methods, 0 class methods

## Instance variables

```
q _titleLocation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leadingStaticItemRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _backButtonRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leadingItemsRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _titleRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _centerItemsRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _floatingTabBarRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _trailingItemsRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _trailingStaticItemRect;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_leadingStaticItemRect) leadingStaticItemRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_backButtonRect) backButtonRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_leadingItemsRect) leadingItemsRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_titleRect) titleRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_centerItemsRect) centerItemsRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_floatingTabBarRect) floatingTabBarRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_trailingItemsRect) trailingItemsRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_trailingStaticItemRect) trailingStaticItemRect;
@property (Tq,N,V_titleLocation) titleLocation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) leadingRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) centerRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) centerLine2Rect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) trailingRect;
```

## Instance methods

```
-[_UINavigationBarTitleViewOverlayRects leadingItemsRect];
-[_UINavigationBarTitleViewOverlayRects setTitleRect:];
-[_UINavigationBarTitleViewOverlayRects setTrailingItemsRect:];
-[_UINavigationBarTitleViewOverlayRects init];
-[_UINavigationBarTitleViewOverlayRects trailingRect];
-[_UINavigationBarTitleViewOverlayRects setTrailingStaticItemRect:];
-[_UINavigationBarTitleViewOverlayRects leadingStaticItemRect];
-[_UINavigationBarTitleViewOverlayRects reset];
-[_UINavigationBarTitleViewOverlayRects leadingRect];
-[_UINavigationBarTitleViewOverlayRects setFloatingTabBarRect:];
-[_UINavigationBarTitleViewOverlayRects setBackButtonRect:];
-[_UINavigationBarTitleViewOverlayRects asArray];
-[_UINavigationBarTitleViewOverlayRects titleLocation];
-[_UINavigationBarTitleViewOverlayRects centerLine2Rect];
-[_UINavigationBarTitleViewOverlayRects description];
-[_UINavigationBarTitleViewOverlayRects backButtonRect];
-[_UINavigationBarTitleViewOverlayRects setLeadingItemsRect:];
-[_UINavigationBarTitleViewOverlayRects trailingStaticItemRect];
-[_UINavigationBarTitleViewOverlayRects setLeadingStaticItemRect:];
-[_UINavigationBarTitleViewOverlayRects centerItemsRect];
-[_UINavigationBarTitleViewOverlayRects centerRect];
-[_UINavigationBarTitleViewOverlayRects titleRect];
-[_UINavigationBarTitleViewOverlayRects setCenterItemsRect:];
-[_UINavigationBarTitleViewOverlayRects setTitleLocation:];
-[_UINavigationBarTitleViewOverlayRects trailingItemsRect];
-[_UINavigationBarTitleViewOverlayRects floatingTabBarRect];
```
