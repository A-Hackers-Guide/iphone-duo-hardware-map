# `_UIBarBackground`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 14 instance variables, 4 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"UIVisualEffectView" _effectView1;
@"UIImageView" _colorAndImageView1;
@"_UIBarBackgroundShadowView" _shadowView1;
@"UIVisualEffectView" _effectView2;
@"UIImageView" _colorAndImageView2;
@"_UIBarBackgroundShadowView" _shadowView2;
@"UIView" _topInsetView;
d _bg1LastLayoutHeight;
d _bg2LastLayoutHeight;
{?="needsTopInsetView"b1"needsEffectView1"b1"needsColorAndImageView1"b1"needsShadowView1"b1"needsEffectView2"b1"needsColorAndImageView2"b1"needsShadowView2"b1} _backgroundFlags;
B _topAligned;
@"NSString" _groupName;
@"_UIBarBackgroundLayout" _layout;
@"UIView" _customBackgroundView;
```

## Properties

```
@property (T@"NSString",C,N,V_groupName) groupName;
@property (TB,N,V_topAligned) topAligned;
@property (T@"_UIBarBackgroundLayout",&,N,V_layout) layout;
@property (T@"UIView",&,N,V_customBackgroundView) customBackgroundView;
```

## Instance methods

```
-[_UIBarBackground _orderSubviews];
-[_UIBarBackground _shadowView];
-[_UIBarBackground transition:toLayout:];
-[_UIBarBackground setCustomBackgroundView:];
-[_UIBarBackground set_backgroundEffectView:];
-[_UIBarBackground set_shadowView:];
-[_UIBarBackground setGroupName:];
-[_UIBarBackground layoutSubviews];
-[_UIBarBackground _updateBackgroundViewVisiblity];
-[_UIBarBackground prepareBackgroundViews];
-[_UIBarBackground _encodableSubviews];
-[_UIBarBackground customBackgroundView];
-[_UIBarBackground transitionBackgroundViewsAnimated:];
-[_UIBarBackground setTopAligned:];
-[_UIBarBackground updateBackground];
-[_UIBarBackground encodeWithCoder:];
-[_UIBarBackground cleanupBackgroundViews];
-[_UIBarBackground groupName];
-[_UIBarBackground _setupShadowView:effect:image:shadowColor:shadowTint:alpha:];
-[_UIBarBackground initWithCoder:];
-[_UIBarBackground layout];
-[_UIBarBackground frameForYOrigin:height:];
-[_UIBarBackground _backgroundEffectView];
-[_UIBarBackground transitionBackgroundViews];
-[_UIBarBackground topAligned];
-[_UIBarBackground initWithFrame:];
-[_UIBarBackground setLayout:];
-[_UIBarBackground _setupBackgroundValues];
```
