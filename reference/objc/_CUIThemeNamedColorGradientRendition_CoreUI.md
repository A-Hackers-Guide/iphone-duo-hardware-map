# `_CUIThemeNamedColorGradientRendition`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUIThemeRendition`
- 5 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _colorNames;
@"NSArray" _colorStops;
q _gradientType;
{CGPoint="x"d"y"d} _gradientStart;
{CGPoint="x"d"y"d} _gradientEnd;
```

## Properties

```
@property (Tq,R,N,V_gradientType) gradientType;
@property (T{CGPoint=dd},R,N,V_gradientStart) gradientStartPoint;
@property (T{CGPoint=dd},R,N,V_gradientEnd) gradientEndPoint;
@property (T@"NSArray",R,N,V_colorStops) colorStops;
@property (T@"NSArray",R,N,V_colorNames) colorNames;
```

## Instance methods

```
-[_CUIThemeNamedColorGradientRendition gradientType];
-[_CUIThemeNamedColorGradientRendition colorStops];
-[_CUIThemeNamedColorGradientRendition dealloc];
-[_CUIThemeNamedColorGradientRendition gradientEndPoint];
-[_CUIThemeNamedColorGradientRendition colorNames];
-[_CUIThemeNamedColorGradientRendition _initWithCSIHeader:version:];
-[_CUIThemeNamedColorGradientRendition gradientStartPoint];
-[_CUIThemeNamedColorGradientRendition initWithCSIData:forKey:version:];
```
