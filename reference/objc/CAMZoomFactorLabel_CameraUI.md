# `CAMZoomFactorLabel`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 9 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _showZoomFactorSymbol;
B _useLeadingZero;
B _preferDefaultSizing;
B _minimized;
d _zoomFactor;
q _shadowStrength;
@"UILabel" __label;
@"UIImageView" __minimizedGlyph;
```

## Properties

```
@property (T@"UILabel",R,N,V__label) _label;
@property (T@"UIImageView",&,N,V__minimizedGlyph) _minimizedGlyph;
@property (Td,N,V_zoomFactor) zoomFactor;
@property (TB,N,V_showZoomFactorSymbol) showZoomFactorSymbol;
@property (T@"UIColor",&,N) textColor;
@property (Tq,N,V_shadowStrength) shadowStrength;
@property (TB,N,V_useLeadingZero) useLeadingZero;
@property (TB,N,V_preferDefaultSizing) preferDefaultSizing;
@property (TB,N,V_minimized) minimized;
```

## Class methods

```
+[CAMZoomFactorLabel _minimizedImageWithScale:];
```

## Instance methods

```
-[CAMZoomFactorLabel _label];
-[CAMZoomFactorLabel _updateLabelText];
-[CAMZoomFactorLabel zoomFactor];
-[CAMZoomFactorLabel setZoomFactor:];
-[CAMZoomFactorLabel intrinsicContentSize];
-[CAMZoomFactorLabel setPreferDefaultSizing:];
-[CAMZoomFactorLabel _updateFont];
-[CAMZoomFactorLabel minimized];
-[CAMZoomFactorLabel setShadowStrength:];
-[CAMZoomFactorLabel textColor];
-[CAMZoomFactorLabel _minimizedGlyph];
-[CAMZoomFactorLabel useLeadingZero];
-[CAMZoomFactorLabel setTextColor:];
-[CAMZoomFactorLabel shadowStrength];
-[CAMZoomFactorLabel layoutSubviews];
-[CAMZoomFactorLabel _updateShadow];
-[CAMZoomFactorLabel _updateMinimizedGlyph];
-[CAMZoomFactorLabel showZoomFactorSymbol];
-[CAMZoomFactorLabel set_minimizedGlyph:];
-[CAMZoomFactorLabel preferDefaultSizing];
-[CAMZoomFactorLabel _labelInsets];
-[CAMZoomFactorLabel setShowZoomFactorSymbol:];
-[CAMZoomFactorLabel description];
-[CAMZoomFactorLabel setUseLeadingZero:];
-[CAMZoomFactorLabel _preferredContentSizeCategoryChanged];
-[CAMZoomFactorLabel setMinimized:];
-[CAMZoomFactorLabel initWithFrame:];
```
