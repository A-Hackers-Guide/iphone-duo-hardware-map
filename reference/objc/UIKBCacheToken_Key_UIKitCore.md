# `UIKBCacheToken_Key`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBCacheToken`
- 24 instance variables, 0 properties, 18 instance methods, 2 class methods

## Instance variables

```
(?="styling"{?="idiom"b6"landscape"b1"split"b1"appearance"b8"rendering"b8"padding"b8}"intValue"i) _style;
@"NSString" _cacheDisplayString;
@"NSString" _cacheSecondaryDisplayString;
@"NSString" _annotationString;
@"NSString" _layoutTag;
i _displayTypeHint;
i _state;
Q _clipCorners;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _displayInsets;
Q _groupNeighbors;
{CGSize="width"d"height"d} _size;
i _displayRowHint;
i _controlKeyBackgroundName;
i _preferredContentSizeCategory;
i _appSpecificBackgroundContrastSetting;
i _appSpecificDarkenSystemColorsSetting;
i _appSpecificEnhanceTextLegibilitySetting;
i _appSpecificReduceHighlightingEffectsSetting;
B _usesInsets;
B _lightKeyboard;
B _colorAdaptiveBackground;
B _animatedBackground;
B _usesCompactKeycapsFont;
B _differentDisplayStrings;
```

## Class methods

```
+[UIKBCacheToken_Key tokenForKey:style:renderConfig:];
+[UIKBCacheToken_Key tokenForKey:style:renderConfig:displayInsets:];
```

## Instance methods

```
-[UIKBCacheToken_Key rowHint];
-[UIKBCacheToken_Key setRowHint:];
-[UIKBCacheToken_Key displayHint];
-[UIKBCacheToken_Key stringForRenderFlags:lightKeyboard:];
-[UIKBCacheToken_Key string];
-[UIKBCacheToken_Key resetAnnotations];
-[UIKBCacheToken_Key size];
-[UIKBCacheToken_Key annotateWithBool:];
-[UIKBCacheToken_Key _stringWithAdditionalValues:];
-[UIKBCacheToken_Key annotateWithInt:];
-[UIKBCacheToken_Key styling];
-[UIKBCacheToken_Key setDisplayHint:];
-[UIKBCacheToken_Key annotateWithString:];
-[UIKBCacheToken_Key copyTokenWithoutContentProperties];
-[UIKBCacheToken_Key hasKey];
-[UIKBCacheToken_Key setStyling:];
-[UIKBCacheToken_Key setSize:];
-[UIKBCacheToken_Key _initWithKey:style:renderConfig:displayInsets:];
```
