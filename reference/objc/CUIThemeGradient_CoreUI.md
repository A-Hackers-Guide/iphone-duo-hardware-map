# `CUIThemeGradient`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUIThemeGradientDrawing`
- 4 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
@ gradientEvaluator;
^{CGFunction=} colorShader;
^{CGColorSpace=} colorSpace;
^{CGImage=} _gradientImage;
```

## Instance methods

```
-[CUIThemeGradient colorStops];
-[CUIThemeGradient fillColor];
-[CUIThemeGradient dealloc];
-[CUIThemeGradient isDithered];
-[CUIThemeGradient blendMode];
-[CUIThemeGradient _createRadialGradientImageWithWidth:height:];
-[CUIThemeGradient _initWithGradientEvaluator:colorSpace:];
-[CUIThemeGradient colorLocations];
-[CUIThemeGradient drawAngleGradientInRect:relativeCenterPosition:withContext:];
-[CUIThemeGradient drawFromPoint:toPoint:options:withContext:];
-[CUIThemeGradient drawInRect:angle:];
-[CUIThemeGradient drawInRect:angle:options:withContext:];
-[CUIThemeGradient drawInRect:angle:withContext:];
-[CUIThemeGradient drawRadialGradientInRect:relativeCenterPosition:withContext:];
-[CUIThemeGradient gradientByApplyingEffects:];
-[CUIThemeGradient initWithColors:colorlocations:colorMidpoints:opacities:opacityLocations:opacityMidpoints:smoothingCoefficient:fillColor:colorSpace:];
-[CUIThemeGradient initWithColors:colorlocations:colorMidpoints:opacities:opacityLocations:opacityMidpoints:smoothingCoefficient:fillColor:colorSpace:dither:];
-[CUIThemeGradient interpolatedColorAtLocation:];
-[CUIThemeGradient opacityLocations];
-[CUIThemeGradient opacityStops];
-[CUIThemeGradient smoothingCoefficient];
```
