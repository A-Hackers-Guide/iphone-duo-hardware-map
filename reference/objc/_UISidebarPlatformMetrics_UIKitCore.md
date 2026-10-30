# `_UISidebarPlatformMetrics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
d _fallbackCornerRadius;
@"<_UIViewMaterial>" _floatingBackground;
@"<_UIViewMaterial>" _abuttedBackground;
{_UISidebarWidths="minimum"d"preferred"d"maximum"d} _narrowWidthMetrics;
{_UISidebarWidths="minimum"d"preferred"d"maximum"d} _wideWidthMetrics;
{_UISidebarWidths="minimum"d"preferred"d"maximum"d} _inspectorWidthMetrics;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _platterInsets;
```

## Properties

```
@property (Td,N,V_fallbackCornerRadius) fallbackCornerRadius;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_platterInsets) platterInsets;
@property (T{_UISidebarWidths=ddd},N,V_narrowWidthMetrics) narrowWidthMetrics;
@property (T{_UISidebarWidths=ddd},N,V_wideWidthMetrics) wideWidthMetrics;
@property (T{_UISidebarWidths=ddd},N,V_inspectorWidthMetrics) inspectorWidthMetrics;
@property (T@"<_UIViewMaterial>",&,N,V_floatingBackground) floatingBackground;
@property (T@"<_UIViewMaterial>",&,N,V_abuttedBackground) abuttedBackground;
```

## Instance methods

```
-[_UISidebarPlatformMetrics platterInsets];
-[_UISidebarPlatformMetrics narrowWidthMetrics];
-[_UISidebarPlatformMetrics init];
-[_UISidebarPlatformMetrics setInspectorWidthMetrics:];
-[_UISidebarPlatformMetrics abuttedBackground];
-[_UISidebarPlatformMetrics fallbackCornerRadius];
-[_UISidebarPlatformMetrics setNarrowWidthMetrics:];
-[_UISidebarPlatformMetrics inspectorWidthMetrics];
-[_UISidebarPlatformMetrics setAbuttedBackground:];
-[_UISidebarPlatformMetrics setFallbackCornerRadius:];
-[_UISidebarPlatformMetrics floatingBackground];
-[_UISidebarPlatformMetrics wideWidthMetrics];
-[_UISidebarPlatformMetrics setPlatterInsets:];
-[_UISidebarPlatformMetrics setFloatingBackground:];
-[_UISidebarPlatformMetrics setWideWidthMetrics:];
```
