# `SBDropShadowSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 5 instance variables, 5 properties, 11 instance methods, 2 class methods

## Instance variables

```
d _radius;
d _opacity;
d _offsetX;
d _offsetY;
d _continuousCornerRadius;
```

## Properties

```
@property (Td,N,V_radius) radius;
@property (Td,N,V_opacity) opacity;
@property (Td,N,V_offsetX) offsetX;
@property (Td,N,V_offsetY) offsetY;
@property (Td,N,V_continuousCornerRadius) continuousCornerRadius;
```

## Class methods

```
+[SBDropShadowSettings settingsControllerModule];
+[SBDropShadowSettings moduleWithSectionTitle:];
```

## Instance methods

```
-[SBDropShadowSettings setContinuousCornerRadius:];
-[SBDropShadowSettings opacity];
-[SBDropShadowSettings setRadius:];
-[SBDropShadowSettings setOpacity:];
-[SBDropShadowSettings continuousCornerRadius];
-[SBDropShadowSettings radius];
-[SBDropShadowSettings setDefaultValues];
-[SBDropShadowSettings offsetY];
-[SBDropShadowSettings offsetX];
-[SBDropShadowSettings setOffsetX:];
-[SBDropShadowSettings setOffsetY:];
```
