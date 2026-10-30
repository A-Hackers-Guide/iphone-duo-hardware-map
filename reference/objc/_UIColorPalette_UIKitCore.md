# `_UIColorPalette`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 9 instance methods, 13 class methods

## Instance variables

```
@"NSArray" _colors;
@"NSArray" _locations;
@"NSString" _colorSpaceName;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_colors) colors;
@property (T@"NSArray",R,C,N,V_locations) locations;
@property (T@"NSString",R,C,N,V_colorSpaceName) colorSpaceName;
@property (T^{CGGradient=},R,N) gradientRepresentation;
```

## Class methods

```
+[_UIColorPalette _coolColors];
+[_UIColorPalette _warmColors];
+[_UIColorPalette intelligenceAmbientPalette];
+[_UIColorPalette intelligenceColors];
+[_UIColorPalette intelligenceComputedPalette];
+[_UIColorPalette intelligenceDefaultPalette];
+[_UIColorPalette intelligenceProcessingPalette];
+[_UIColorPalette intelligenceSymbolLivingColorPalette];
+[_UIColorPalette textAssistantPonderingFillPalette];
+[_UIColorPalette textAssistantPonderingLightSheenPalette];
+[_UIColorPalette textAssistantReplacementBuildInPalette];
+[_UIColorPalette textAssistantReplacementBuildOutPalette];
+[_UIColorPalette textAssistantReplacementSheenPalette];
```

## Instance methods

```
-[_UIColorPalette colors];
-[_UIColorPalette colorSpaceName];
-[_UIColorPalette locations];
-[_UIColorPalette initWithColors:];
-[_UIColorPalette hash];
-[_UIColorPalette isEqual:];
-[_UIColorPalette gradientRepresentation];
-[_UIColorPalette initWithColors:locations:colorSpaceName:];
-[_UIColorPalette paletteByMergingPalette:];
```
