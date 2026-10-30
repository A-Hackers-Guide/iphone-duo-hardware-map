# `TPNumberPadButton`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `TPNumberPadButtonProtocol`
- 8 instance variables, 13 properties, 30 instance methods, 32 class methods

## Instance variables

```
q character;
@"UIColor" _color;
@"CALayer" _glyphLayer;
@"CALayer" _highlightedGlyphLayer;
@"_TPNumberPadCircleBackgroundView" _circleView;
@"UIColor" _buttonColor;
@"TPRevealingRingView" _revealingRingView;
@"UIVisualEffectView" _backDropVisualEffectView;
```

## Properties

```
@property (T@"CALayer",&,V_glyphLayer) glyphLayer;
@property (T@"CALayer",&,V_highlightedGlyphLayer) highlightedGlyphLayer;
@property (T@"_TPNumberPadCircleBackgroundView",&,V_circleView) circleView;
@property (T@"UIColor",R,N,V_buttonColor) buttonColor;
@property (T@"UIColor",R,N) highlightedButtonColor;
@property (T@"TPRevealingRingView",R,N,V_revealingRingView) revealingRingView;
@property (T@"UIVisualEffectView",&,N,V_backDropVisualEffectView) backDropVisualEffectView;
@property (T@"UIColor",&,N,V_color) color;
@property (Tq,Vcharacter) character;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TPNumberPadButton horizontalPadding];
+[TPNumberPadButton verticalPadding];
+[TPNumberPadButton isCarPlay];
+[TPNumberPadButton defaultSize];
+[TPNumberPadButton highlightedCircleViewAlpha];
+[TPNumberPadButton isUsingGlass];
+[TPNumberPadButton outerCircleDiameter];
+[TPNumberPadButton paddingOutsideRing];
+[TPNumberPadButton unhighlightedCircleViewAlpha];
+[TPNumberPadButton usesTelephonyGlyphsWhereAvailable];
+[TPNumberPadButton buttonColorMatrix];
+[TPNumberPadButton circleBounds];
+[TPNumberPadButton containerLayoutHeight];
+[TPNumberPadButton disabledImageForCharacter:];
+[TPNumberPadButton effectiveScreenSizeCategory];
+[TPNumberPadButton imageForCharacter:];
+[TPNumberPadButton imageForCharacter:highlighted:];
+[TPNumberPadButton imageForCharacter:highlighted:whiteVersion:];
+[TPNumberPadButton imageForCharacter:highlighted:whiteVersion:digitFontSizeOverride:letterFontSizeOverride:];
+[TPNumberPadButton isUsingClearGlass];
+[TPNumberPadButton loadNumberPadKeyPrototypeView];
+[TPNumberPadButton localizedLettersForCharacter:];
+[TPNumberPadButton localizedLettersForCharacter:featureFlags:];
+[TPNumberPadButton resetLocale];
+[TPNumberPadButton resetLocaleIfNeeded];
+[TPNumberPadButton scriptKey];
+[TPNumberPadButton updatePrototypeView:];
+[TPNumberPadButton usesBoldAssets];
+[TPNumberPadButton usesButtonBlurEffect];
+[TPNumberPadButton usesButtonColorMatrixFilters];
+[TPNumberPadButton usesButtonSaturationFilters];
+[TPNumberPadButton usesEmergencyCallButtonColorMatrixFilters];
```

## Instance methods

```
-[TPNumberPadButton setColor:];
-[TPNumberPadButton buttonColor];
-[TPNumberPadButton hitTest:withEvent:];
-[TPNumberPadButton defaultColor];
-[TPNumberPadButton color];
-[TPNumberPadButton setHighlighted:];
-[TPNumberPadButton touchDown];
-[TPNumberPadButton character];
-[TPNumberPadButton initForCharacter:];
-[TPNumberPadButton initForCharacter:style:];
-[TPNumberPadButton loadImagesForCurrentCharacter];
-[TPNumberPadButton revealingRingView];
-[TPNumberPadButton setCharacter:];
-[TPNumberPadButton updateBackgroundMaterial:];
-[TPNumberPadButton reloadImagesForCurrentCharacter];
-[TPNumberPadButton touchUp];
-[TPNumberPadButton backDropVisualEffectView];
-[TPNumberPadButton circleView];
-[TPNumberPadButton glyphLayer];
-[TPNumberPadButton highlightCircleView:animated:];
-[TPNumberPadButton highlightedButtonColor];
-[TPNumberPadButton highlightedGlyphLayer];
-[TPNumberPadButton overriddenDigitFontSize];
-[TPNumberPadButton overriddenLetterFontSize];
-[TPNumberPadButton setBackDropVisualEffectView:];
-[TPNumberPadButton setCircleView:];
-[TPNumberPadButton setGlyphLayer:];
-[TPNumberPadButton setGreyedOut:];
-[TPNumberPadButton setHighlightedGlyphLayer:];
-[TPNumberPadButton touchCancelled];
```
