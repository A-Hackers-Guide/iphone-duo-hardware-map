# `SBRingerPillView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 12 instance variables, 12 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _activatedForPreviewing;
f _sliderValue;
Q _state;
@"BSUICAPackageView" _glyphView;
@"UILabel" _silentModeLabel;
@"UILabel" _ringerLabel;
@"UILabel" _onLabel;
@"UILabel" _offLabel;
@"SBRingerVolumeSliderView" _slider;
@"UIColor" _glyphTintColor;
@"NSArray" _glyphTintBackgroundLayers;
@"NSArray" _glyphTintShapeLayers;
```

## Properties

```
@property (T@"BSUICAPackageView",&,N,V_glyphView) glyphView;
@property (T@"UILabel",&,N,V_silentModeLabel) silentModeLabel;
@property (T@"UILabel",&,N,V_ringerLabel) ringerLabel;
@property (T@"UILabel",&,N,V_onLabel) onLabel;
@property (T@"UILabel",&,N,V_offLabel) offLabel;
@property (T@"SBRingerVolumeSliderView",&,N,V_slider) slider;
@property (T@"UIColor",&,N,V_glyphTintColor) glyphTintColor;
@property (T@"NSArray",C,N,V_glyphTintBackgroundLayers) glyphTintBackgroundLayers;
@property (T@"NSArray",C,N,V_glyphTintShapeLayers) glyphTintShapeLayers;
@property (TB,N,GisActivatedForPreviewing,V_activatedForPreviewing) activatedForPreviewing;
@property (TQ,N,V_state) state;
@property (Tf,N,V_sliderValue) sliderValue;
```

## Instance methods

```
-[SBRingerPillView setState:];
-[SBRingerPillView setSlider:];
-[SBRingerPillView layoutSubviews];
-[SBRingerPillView sizeThatFits:];
-[SBRingerPillView setGlyphTintColor:];
-[SBRingerPillView glyphView];
-[SBRingerPillView slider];
-[SBRingerPillView glyphTintColor];
-[SBRingerPillView setGlyphView:];
-[SBRingerPillView state];
-[SBRingerPillView setSliderValue:];
-[SBRingerPillView sliderValue];
-[SBRingerPillView _subtitleLabelColor];
-[SBRingerPillView _titleLabelColor];
-[SBRingerPillView initWithActivatedForPreviewing:];
-[SBRingerPillView onLabel];
-[SBRingerPillView setRingerLabel:];
-[SBRingerPillView silentModeLabel];
-[SBRingerPillView _setGlyphTintColor:animationDuration:];
-[SBRingerPillView _updateGlyphWithStaticColor:animationSettings:];
-[SBRingerPillView _updateGlyphWithTintColor];
-[SBRingerPillView _visibleViewsForState:];
-[SBRingerPillView glyphTintBackgroundLayers];
-[SBRingerPillView glyphTintShapeLayers];
-[SBRingerPillView isActivatedForPreviewing];
-[SBRingerPillView offLabel];
-[SBRingerPillView ringerLabel];
-[SBRingerPillView setActivatedForPreviewing:];
-[SBRingerPillView setGlyphTintBackgroundLayers:];
-[SBRingerPillView setGlyphTintShapeLayers:];
-[SBRingerPillView setOffLabel:];
-[SBRingerPillView setOnLabel:];
-[SBRingerPillView setSilentModeLabel:];
-[SBRingerPillView setSliderValue:animated:];
```
