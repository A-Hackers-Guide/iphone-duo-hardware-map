# `CDRichComplicationImageView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CLKMonochromeFilterProvider`, `CLKMonochromeComplicationView`, `CDRichComplicationTintedPlatterColorOverridable`
- 14 instance variables, 18 properties, 45 instance methods, 0 class methods

## Instance variables

```
B _useAccentColor;
B _hostingOverrideView;
B _paused;
B _prefersFilterOverTransition;
@"<CLKMonochromeFilterProvider>" _filterProvider;
@"CLKDevice" _device;
@"NSNumber" _tritiumUpdateMode;
@"UIFontDescriptor" _fontDescriptor;
d _fontSizeFactor;
@"CLKFullColorImageProvider" _imageProvider;
@"UIView" _richComplicationImageView;
@"CDStackedImagesComplicationImageView" _monochromeImageView;
q _monochromeFilterType;
d _inMonochromeModeFraction;
```

## Properties

```
@property (T@"CLKFullColorImageProvider",&,N,V_imageProvider) imageProvider;
@property (T@"UIView",W,N,V_richComplicationImageView) richComplicationImageView;
@property (T@"CDStackedImagesComplicationImageView",W,N,V_monochromeImageView) monochromeImageView;
@property (TB,N,GisHostingOverrideView,V_hostingOverrideView) hostingOverrideView;
@property (TB,N,GisPaused,V_paused) paused;
@property (Tq,N,V_monochromeFilterType) monochromeFilterType;
@property (Td,N,V_inMonochromeModeFraction) inMonochromeModeFraction;
@property (TB,N,V_prefersFilterOverTransition) prefersFilterOverTransition;
@property (T@"CLKDevice",R,N,V_device) device;
@property (TB,R,N,V_useAccentColor) useAccentColor;
@property (T@"NSNumber",R,N,V_tritiumUpdateMode) tritiumUpdateMode;
@property (T@"UIFontDescriptor",C,N,V_fontDescriptor) fontDescriptor;
@property (Td,N,V_fontSizeFactor) fontSizeFactor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<CLKMonochromeFilterProvider>",W,N,V_filterProvider) filterProvider;
```

## Instance methods

```
-[CDRichComplicationImageView isPaused];
-[CDRichComplicationImageView device];
-[CDRichComplicationImageView layoutSubviews];
-[CDRichComplicationImageView setPaused:];
-[CDRichComplicationImageView imageProvider];
-[CDRichComplicationImageView fontDescriptor];
-[CDRichComplicationImageView setFontDescriptor:];
-[CDRichComplicationImageView setImageProvider:];
-[CDRichComplicationImageView setPrefersFilterOverTransition:];
-[CDRichComplicationImageView monochromeFilterType];
-[CDRichComplicationImageView prefersFilterOverTransition];
-[CDRichComplicationImageView setMonochromeFilterType:];
-[CDRichComplicationImageView renderSynchronouslyWithImageQueueDiscard:inGroup:];
-[CDRichComplicationImageView backgroundColorForView:];
-[CDRichComplicationImageView colorForView:accented:];
-[CDRichComplicationImageView filterForView:style:];
-[CDRichComplicationImageView filterForView:style:fraction:];
-[CDRichComplicationImageView filterProvider];
-[CDRichComplicationImageView filtersForView:style:];
-[CDRichComplicationImageView filtersForView:style:fraction:];
-[CDRichComplicationImageView fontSizeFactor];
-[CDRichComplicationImageView initWithDevice:useAccentColor:];
-[CDRichComplicationImageView interpolatedColorForView:];
-[CDRichComplicationImageView setFilterProvider:];
-[CDRichComplicationImageView setFontSizeFactor:];
-[CDRichComplicationImageView setImageProvider:reason:];
-[CDRichComplicationImageView setTintedFraction:];
-[CDRichComplicationImageView setTintedPlatterColor:];
-[CDRichComplicationImageView transitionToMonochromeWithFraction:];
-[CDRichComplicationImageView tritiumUpdateMode];
-[CDRichComplicationImageView updateMonochromeColor];
-[CDRichComplicationImageView viewShouldIgnoreTwoPieceImage:];
-[CDRichComplicationImageView _createMonochromeImageView];
-[CDRichComplicationImageView _filterStyle];
-[CDRichComplicationImageView _isSymbolImageProvider];
-[CDRichComplicationImageView _isSymbolImageProviderWithoutSpecificSize];
-[CDRichComplicationImageView inMonochromeModeFraction];
-[CDRichComplicationImageView isHostingOverrideView];
-[CDRichComplicationImageView monochromeImageView];
-[CDRichComplicationImageView richComplicationImageView];
-[CDRichComplicationImageView setHostingOverrideView:];
-[CDRichComplicationImageView setInMonochromeModeFraction:];
-[CDRichComplicationImageView setMonochromeImageView:];
-[CDRichComplicationImageView setRichComplicationImageView:];
-[CDRichComplicationImageView useAccentColor];
```
