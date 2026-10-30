# `UIKBCacheToken_Keyplane`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBCacheToken`
- 17 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
{CGSize="width"d"height"d} _size;
(?="styling"{?="idiom"b6"landscape"b1"split"b1"appearance"b8"rendering"b8"padding"b8}"intValue"i) _style;
@"NSString" _geometrySetName;
@"NSString" _keySetName;
@"NSString" _cachedGestureKeySetName;
@"NSString" _annotations;
@"NSString" _locale;
B _colorAdaptiveBackground;
B _lightKeyboard;
B _animatedBackground;
B _usesCompactKeycapsFont;
i _controlKeyBackgroundName;
i _preferredContentSizeCategory;
i _appSpecificBackgroundContrastSetting;
i _appSpecificDarkenSystemColorsSetting;
i _appSpecificEnhanceTextLegibilitySetting;
i _appSpecificReduceHighlightingEffectsSetting;
```

## Class methods

```
+[UIKBCacheToken_Keyplane tokenForKeyplane:renderConfig:];
```

## Instance methods

```
-[UIKBCacheToken_Keyplane size];
-[UIKBCacheToken_Keyplane annotateWithBool:];
-[UIKBCacheToken_Keyplane isUsableForCacheToken:withRenderFlags:];
-[UIKBCacheToken_Keyplane _initWithKeyplane:keylayout:renderConfig:];
-[UIKBCacheToken_Keyplane stringForSplitState:handBias:];
-[UIKBCacheToken_Keyplane annotateWithInt:];
-[UIKBCacheToken_Keyplane styling];
-[UIKBCacheToken_Keyplane setStyling:];
-[UIKBCacheToken_Keyplane setSize:];
```
