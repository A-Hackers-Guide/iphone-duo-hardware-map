# `CDRichComplicationView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CDComplicationDisplay`, `CLKUITimeTravel`, `CLKMonochromeComplicationView`, `CLKMonochromeFilterProvider`
- 13 instance variables, 18 properties, 45 instance methods, 0 class methods

## Instance variables

```
q _family;
B _editing;
B _highlighted;
@"NSDate" _timeTravelDate;
B _paused;
@"<CLKMonochromeFilterProvider>" _filterProvider;
@"<CDComplicationDisplayObserver>" displayObserver;
Q textLayoutStyle;
@"CLKDevice" _device;
@"UIColor" _foregroundColor;
q _fontStyle;
@"UIFontDescriptor" _fontDescriptor;
d _fontSizeFactor;
```

## Properties

```
@property (T@"NSDate",R,N) complicationDate;
@property (T@"NSDate",R,N) timeTravelDate;
@property (T@"UIFontDescriptor",R,N,V_fontDescriptor) fontDescriptor;
@property (Td,R,N,V_fontSizeFactor) fontSizeFactor;
@property (T@"CLKDevice",R,N,V_device) device;
@property (Tq,R,N,V_family) family;
@property (TB,N,V_paused) paused;
@property (T@"UIColor",&,N,V_foregroundColor) foregroundColor;
@property (Tq,N,V_fontStyle) fontStyle;
@property (T@"<CDComplicationDisplayObserver>",W,N,VdisplayObserver) displayObserver;
@property (TQ,N,VtextLayoutStyle) textLayoutStyle;
@property (TB,?,N,GisHighlighted) highlighted;
@property (TB,?,N) shouldUseTemplateColors;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<CLKMonochromeFilterProvider>",W,N,V_filterProvider) filterProvider;
```

## Instance methods

```
-[CDRichComplicationView setFontStyle:];
-[CDRichComplicationView setForegroundColor:];
-[CDRichComplicationView fontStyle];
-[CDRichComplicationView device];
-[CDRichComplicationView paused];
-[CDRichComplicationView setPaused:];
-[CDRichComplicationView setEditing:];
-[CDRichComplicationView setHighlighted:];
-[CDRichComplicationView family];
-[CDRichComplicationView fontDescriptor];
-[CDRichComplicationView traitCollectionDidChange:];
-[CDRichComplicationView foregroundColor];
-[CDRichComplicationView initWithFamily:];
-[CDRichComplicationView complicationDate];
-[CDRichComplicationView textLayoutStyle];
-[CDRichComplicationView setTextLayoutStyle:];
-[CDRichComplicationView renderSynchronouslyWithImageQueueDiscard:inGroup:];
-[CDRichComplicationView displayObserver];
-[CDRichComplicationView _applyPausedUpdate];
-[CDRichComplicationView _editingDidEnd];
-[CDRichComplicationView _enumerateLabelsWithBlock:];
-[CDRichComplicationView _setFontConfiguration:];
-[CDRichComplicationView _transitThemeFromTheme:toTheme:fraction:];
-[CDRichComplicationView _transitToHighlightState:fraction:];
-[CDRichComplicationView _updateColoringLabel:withFontDescriptor:andSizeFactor:];
-[CDRichComplicationView backgroundColorForView:];
-[CDRichComplicationView colorForView:accented:];
-[CDRichComplicationView filterForView:style:];
-[CDRichComplicationView filterForView:style:fraction:];
-[CDRichComplicationView filterProvider];
-[CDRichComplicationView filtersForView:style:];
-[CDRichComplicationView filtersForView:style:fraction:];
-[CDRichComplicationView fontSizeFactor];
-[CDRichComplicationView interpolatedColorForView:];
-[CDRichComplicationView setDisplayObserver:];
-[CDRichComplicationView setFilterProvider:];
-[CDRichComplicationView setTimeTravelDate:animated:];
-[CDRichComplicationView timeTravelDate];
-[CDRichComplicationView transitThemeFromTheme:toTheme:fraction:];
-[CDRichComplicationView transitionToMonochromeWithFraction:];
-[CDRichComplicationView tritiumUpdateMode];
-[CDRichComplicationView updateMonochromeColor];
-[CDRichComplicationView viewShouldIgnoreTwoPieceImage:];
-[CDRichComplicationView _fontWithSize:withFontDescriptor:];
-[CDRichComplicationView _setWhistlerAnalogEditingAlphaTransitonFraction:direction:position:];
```
