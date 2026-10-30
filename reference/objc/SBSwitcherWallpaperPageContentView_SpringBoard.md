# `SBSwitcherWallpaperPageContentView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBAppSwitcherPageContentView`
- 10 instance variables, 14 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"BSUIOrientationTransformWrapperView" _wallpaperWrapperView;
B _active;
B _visible;
d _cornerRadius;
q _orientation;
q _desiredWallpaperOrientation;
q _wallpaperStyle;
@"SBWallpaperEffectView" _wallpaperEffectView;
Q _maskedCorners;
{CACornerRadii="minXMaxY"{CGSize="width"d"height"d}"maxXMaxY"{CGSize="width"d"height"d}"maxXMinY"{CGSize="width"d"height"d}"minXMinY"{CGSize="width"d"height"d}} _cornerRadii;
```

## Properties

```
@property (Tq,N,V_desiredWallpaperOrientation) desiredWallpaperOrientation;
@property (Tq,N,V_wallpaperStyle) wallpaperStyle;
@property (T@"SBWallpaperEffectView",R,N,V_wallpaperEffectView) wallpaperEffectView;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (TQ,N,V_maskedCorners) maskedCorners;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N,V_cornerRadii) cornerRadii;
@property (Tq,N,V_orientation) orientation;
@property (TB,R,N) contentRequiresGroupOpacity;
@property (TB,N,GisActive,V_active) active;
@property (TB,N,GisVisible,V_visible) visible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSwitcherWallpaperPageContentView cornerRadii];
-[SBSwitcherWallpaperPageContentView setOrientation:];
-[SBSwitcherWallpaperPageContentView _updateCornerRadius];
-[SBSwitcherWallpaperPageContentView setVisible:];
-[SBSwitcherWallpaperPageContentView contentRequiresGroupOpacity];
-[SBSwitcherWallpaperPageContentView orientation];
-[SBSwitcherWallpaperPageContentView wallpaperEffectView];
-[SBSwitcherWallpaperPageContentView wallpaperStyle];
-[SBSwitcherWallpaperPageContentView setCornerRadii:];
-[SBSwitcherWallpaperPageContentView isVisible];
-[SBSwitcherWallpaperPageContentView layoutSubviews];
-[SBSwitcherWallpaperPageContentView maskedCorners];
-[SBSwitcherWallpaperPageContentView setActive:];
-[SBSwitcherWallpaperPageContentView setCornerRadius:];
-[SBSwitcherWallpaperPageContentView invalidate];
-[SBSwitcherWallpaperPageContentView setMaskedCorners:];
-[SBSwitcherWallpaperPageContentView cornerRadius];
-[SBSwitcherWallpaperPageContentView isActive];
-[SBSwitcherWallpaperPageContentView setWallpaperStyle:];
-[SBSwitcherWallpaperPageContentView initWithFrame:];
-[SBSwitcherWallpaperPageContentView _wallpaperFrame];
-[SBSwitcherWallpaperPageContentView setDesiredWallpaperOrientation:];
-[SBSwitcherWallpaperPageContentView _updateWallpaperOrientation];
-[SBSwitcherWallpaperPageContentView _viewForWallpaperWrapper];
-[SBSwitcherWallpaperPageContentView desiredWallpaperOrientation];
```
