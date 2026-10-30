# `SBAppSwitcherWallpaperGradientView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBackdropView`
- 3 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"CAGradientLayer" _gradientLayer;
{CACornerRadii="minXMaxY"{CGSize="width"d"height"d}"maxXMaxY"{CGSize="width"d"height"d}"maxXMinY"{CGSize="width"d"height"d}"minXMinY"{CGSize="width"d"height"d}} _cornerRadii;
{SBSwitcherWallpaperGradientAttributes="leadingAlpha"d"trailingAlpha"d} _attributes;
```

## Properties

```
@property (T{SBSwitcherWallpaperGradientAttributes=dd},N,V_attributes) attributes;
```

## Instance methods

```
-[SBAppSwitcherWallpaperGradientView setAttributes:];
-[SBAppSwitcherWallpaperGradientView setCornerRadii:];
-[SBAppSwitcherWallpaperGradientView layoutSubviews];
-[SBAppSwitcherWallpaperGradientView setBounds:];
-[SBAppSwitcherWallpaperGradientView _updateGradientColors];
-[SBAppSwitcherWallpaperGradientView initWithPrivateStyle:];
-[SBAppSwitcherWallpaperGradientView attributes];
```
