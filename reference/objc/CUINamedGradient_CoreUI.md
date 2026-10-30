# `CUINamedGradient`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedLookup`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _colorStops;
@"NSArray" _colors;
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
@property (T@"NSArray",R,N,V_colors) colors;
```

## Instance methods

```
-[CUINamedGradient colors];
-[CUINamedGradient gradientType];
-[CUINamedGradient _setGradientType:];
-[CUINamedGradient _setColors:andStops:];
-[CUINamedGradient colorStops];
-[CUINamedGradient dealloc];
-[CUINamedGradient gradientEndPoint];
-[CUINamedGradient _setGradientStartPoint:];
-[CUINamedGradient initWithName:usingRenditionKey:fromTheme:];
-[CUINamedGradient mutableCopy];
-[CUINamedGradient _updateFromCatalog:displayGamut:deviceIdiom:appearanceName:];
-[CUINamedGradient gradientStartPoint];
-[CUINamedGradient _setGradientEndPoint:];
```
