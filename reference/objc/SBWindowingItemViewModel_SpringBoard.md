# `SBWindowingItemViewModel`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowingItemViewModel`, `NSCopying`, `NSMutableCopying`
- 14 instance variables, 14 properties, 32 instance methods, 1 class methods

## Instance variables

```
B _supportsHomeAffordance;
d _opacity;
d _dimmingAlpha;
@"SBSwitcherAnimationAttributes" _animationAttributes;
@"SBWindowingItemViewModel" _spaceAccessoryViewModel;
Q _personalityDebugColorStyle;
@"<SBWindowingItem>" _item;
{SBWindowingItemShadow="shadowOpacity"d"shadowStyle"q} _shadow;
{SBSwitcherWallpaperGradientAttributes="leadingAlpha"d"trailingAlpha"d} _wallpaperGradientAttributes;
{CGPoint="x"d"y"d} _perspectiveAngle;
{SBWindowingItemCorners="cornerRadii"{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d}"cornerMask"Q} _corners;
{SBWindowingItemTitleStyle="headerStyle"q"titleAndIconOpacity"d"titleOpacity"d"iconOpacity"d"trailingIconOpacityBehavior"q"footerViewIconAlignment"Q} _titleStyle;
{SBWindowingItemFrame="bounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"position"{CGPoint="x"d"y"d}"anchorPoint"{CGPoint="x"d"y"d}"scale"{CGPoint="x"d"y"d}"translation"{CGPoint="x"d"y"d}} _frame;
{SBWindowingItemBorder="width"d"red"d"green"d"blue"d"alpha"d"colorMatrix"{CAColorMatrix="m11"f"m12"f"m13"f"m14"f"m15"f"m21"f"m22"f"m23"f"m24"f"m25"f"m31"f"m32"f"m33"f"m34"f"m35"f"m41"f"m42"f"m43"f"m44"f"m45"f}} _border;
```

## Properties

```
@property (T@"<SBWindowingItem>",&,N,V_item) item;
@property (T{SBWindowingItemFrame={CGRect={CGPoint=dd}{CGSize=dd}}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}},N,V_frame) frame;
@property (T{SBWindowingItemCorners={UIRectCornerRadii=dddd}Q},N,V_corners) corners;
@property (T{SBWindowingItemShadow=dq},N,V_shadow) shadow;
@property (T{SBWindowingItemTitleStyle=qdddqQ},N,V_titleStyle) titleStyle;
@property (T{SBWindowingItemBorder=ddddd{CAColorMatrix=ffffffffffffffffffff}},N,V_border) border;
@property (Td,N,V_opacity) opacity;
@property (T{SBSwitcherWallpaperGradientAttributes=dd},N,V_wallpaperGradientAttributes) wallpaperGradientAttributes;
@property (T{CGPoint=dd},N,V_perspectiveAngle) perspectiveAngle;
@property (Td,N,V_dimmingAlpha) dimmingAlpha;
@property (T@"SBSwitcherAnimationAttributes",&,N,V_animationAttributes) animationAttributes;
@property (TB,N,V_supportsHomeAffordance) supportsHomeAffordance;
@property (T@"SBWindowingItemViewModel",&,N,V_spaceAccessoryViewModel) spaceAccessoryViewModel;
@property (TQ,N,V_personalityDebugColorStyle) personalityDebugColorStyle;
```

## Class methods

```
+[SBWindowingItemViewModel viewModelWithItem:fromViewModel:];
```

## Instance methods

```
-[SBWindowingItemViewModel wallpaperGradientAttributes];
-[SBWindowingItemViewModel setBorder:];
-[SBWindowingItemViewModel shadow];
-[SBWindowingItemViewModel mutableCopyWithZone:];
-[SBWindowingItemViewModel setShadow:];
-[SBWindowingItemViewModel setTitleStyle:];
-[SBWindowingItemViewModel setWallpaperGradientAttributes:];
-[SBWindowingItemViewModel setItem:];
-[SBWindowingItemViewModel opacity];
-[SBWindowingItemViewModel item];
-[SBWindowingItemViewModel setOpacity:];
-[SBWindowingItemViewModel setFrame:];
-[SBWindowingItemViewModel border];
-[SBWindowingItemViewModel setAnimationAttributes:];
-[SBWindowingItemViewModel dimmingAlpha];
-[SBWindowingItemViewModel copyWithZone:];
-[SBWindowingItemViewModel corners];
-[SBWindowingItemViewModel mutableCopy];
-[SBWindowingItemViewModel setDimmingAlpha:];
-[SBWindowingItemViewModel frame];
-[SBWindowingItemViewModel titleStyle];
-[SBWindowingItemViewModel setCorners:];
-[SBWindowingItemViewModel perspectiveAngle];
-[SBWindowingItemViewModel setPerspectiveAngle:];
-[SBWindowingItemViewModel animationAttributes];
-[SBWindowingItemViewModel initWithItem:frame:corners:shadow:titleStyle:border:opacity:wallpaperGradientAttributes:perspectiveAngle:dimmingAlpha:animationAttributes:supportsHomeAffordance:spaceAccessoryViewModel:personalityDebugColorStyle:];
-[SBWindowingItemViewModel personalityDebugColorStyle];
-[SBWindowingItemViewModel setPersonalityDebugColorStyle:];
-[SBWindowingItemViewModel setSpaceAccessoryViewModel:];
-[SBWindowingItemViewModel setSupportsHomeAffordance:];
-[SBWindowingItemViewModel spaceAccessoryViewModel];
-[SBWindowingItemViewModel supportsHomeAffordance];
```
