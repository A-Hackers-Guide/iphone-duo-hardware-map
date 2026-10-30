# `UIKBRenderConfig`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `BSXPCCoding`
- 19 instance variables, 25 properties, 47 instance methods, 17 class methods

## Instance variables

```
B _useEmojiStyles;
@"NSMutableDictionary" _customSymbolImages;
Q _classFromEnvironment;
B _lightKeyboard;
B _isFloating;
B _emptyBackground;
B _animatedBackground;
B _colorAdaptiveBackground;
B _usesCompactKeycapsFont;
q _forceQuality;
d _blurRadius;
d _blurSaturation;
d _keycapOpacity;
d _lightKeycapOpacity;
@"NSString" _controlKeyBackgroundName;
@"NSString" _activatedKeyplaneSwitchControlKeyBackgroundName;
@"_UIButtonBarButtonVisualProvider" _buttonBarVisualProvider;
@"NSString" _preferredContentSizeCategory;
Q _currentLayoutClass;
```

## Properties

```
@property (TB,N,V_lightKeyboard) lightKeyboard;
@property (Tq,N,V_forceQuality) forceQuality;
@property (Td,N,V_blurRadius) blurRadius;
@property (Td,N,V_blurSaturation) blurSaturation;
@property (Td,N,V_keycapOpacity) keycapOpacity;
@property (Td,N,V_lightKeycapOpacity) lightKeycapOpacity;
@property (T@"NSString",C,N,V_controlKeyBackgroundName) controlKeyBackgroundName;
@property (T@"NSString",C,N,V_activatedKeyplaneSwitchControlKeyBackgroundName) activatedKeyplaneSwitchControlKeyBackgroundName;
@property (TB,N,V_isFloating) isFloating;
@property (TB,R,N) whiteText;
@property (Tq,R,N) backdropStyle;
@property (Tq,R,N) keyBackdropStyle;
@property (Tq,R,N) blurEffectStyle;
@property (T@"_UIButtonBarButtonVisualProvider",R,N,V_buttonBarVisualProvider) buttonBarVisualProvider;
@property (TB,N,V_emptyBackground) emptyBackground;
@property (TB,N,V_animatedBackground) animatedBackground;
@property (TB,N,V_colorAdaptiveBackground) colorAdaptiveBackground;
@property (TB,N,V_usesCompactKeycapsFont) usesCompactKeycapsFont;
@property (T@"NSString",C,N,V_preferredContentSizeCategory) preferredContentSizeCategory;
@property (TQ,R,N) defaultLayoutClass;
@property (TQ,N,V_currentLayoutClass) currentLayoutClass;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBRenderConfig supportsSecureCoding];
+[UIKBRenderConfig preferredVisualProviderClass];
+[UIKBRenderConfig _graphicsQuality];
+[UIKBRenderConfig clearConfigLightKeys];
+[UIKBRenderConfig darkConfig];
+[UIKBRenderConfig animatedConfigLight];
+[UIKBRenderConfig defaultConfig];
+[UIKBRenderConfig lowQualityDarkConfig];
+[UIKBRenderConfig colorAdaptiveConfigDark];
+[UIKBRenderConfig colorAdaptiveConfigLight];
+[UIKBRenderConfig clearConfigDarkKeys];
+[UIKBRenderConfig backdropStyleForStyle:quality:];
+[UIKBRenderConfig configForAppearance:inputMode:traitEnvironment:];
+[UIKBRenderConfig animatedConfigDark];
+[UIKBRenderConfig clearConfigWithLightKeys:];
+[UIKBRenderConfig configForAnimatedBackgroundWithLightKeys:];
+[UIKBRenderConfig defaultEmojiConfig];
```

## Instance methods

```
-[UIKBRenderConfig setIsFloating:];
-[UIKBRenderConfig isFloating];
-[UIKBRenderConfig blurEffectStyle];
-[UIKBRenderConfig backdropStyle];
-[UIKBRenderConfig preferredContentSizeCategory];
-[UIKBRenderConfig setKeycapOpacity:];
-[UIKBRenderConfig whiteText];
-[UIKBRenderConfig defaultLayoutClass];
-[UIKBRenderConfig initWithXPCDictionary:];
-[UIKBRenderConfig setColorAdaptiveBackground:];
-[UIKBRenderConfig activatedKeyplaneSwitchControlKeyBackgroundName];
-[UIKBRenderConfig currentLayoutClass];
-[UIKBRenderConfig usesCompactKeycapsFont];
-[UIKBRenderConfig defaultLayoutClassIsRegularWidth];
-[UIKBRenderConfig setForceQuality:];
-[UIKBRenderConfig keycapOpacity];
-[UIKBRenderConfig blurSaturation];
-[UIKBRenderConfig keyBackdropStyle];
-[UIKBRenderConfig setEmptyBackground:];
-[UIKBRenderConfig setCurrentLayoutClass:];
-[UIKBRenderConfig setControlKeyBackgroundName:];
-[UIKBRenderConfig overrideKeycapWithSymbol:forDisplayType:];
-[UIKBRenderConfig setPreferredContentSizeCategory:];
-[UIKBRenderConfig setLightKeyboard:];
-[UIKBRenderConfig emptyBackground];
-[UIKBRenderConfig encodeWithXPCDictionary:];
-[UIKBRenderConfig blurRadius];
-[UIKBRenderConfig buttonBarVisualProvider];
-[UIKBRenderConfig imageNameForType:];
-[UIKBRenderConfig encodeWithCoder:];
-[UIKBRenderConfig setBlurSaturation:];
-[UIKBRenderConfig animatedBackground];
-[UIKBRenderConfig forceQuality];
-[UIKBRenderConfig description];
-[UIKBRenderConfig setLightKeycapOpacity:];
-[UIKBRenderConfig initWithCoder:];
-[UIKBRenderConfig lightKeyboard];
-[UIKBRenderConfig setBlurRadius:];
-[UIKBRenderConfig copyWithZone:];
-[UIKBRenderConfig setAnimatedBackground:];
-[UIKBRenderConfig setActivatedKeyplaneSwitchControlKeyBackgroundName:];
-[UIKBRenderConfig isEqual:];
-[UIKBRenderConfig controlKeyBackgroundName];
-[UIKBRenderConfig setUsesCompactKeycapsFont:];
-[UIKBRenderConfig currentLayoutClassIsRegularWidth];
-[UIKBRenderConfig lightKeycapOpacity];
-[UIKBRenderConfig colorAdaptiveBackground];
```
