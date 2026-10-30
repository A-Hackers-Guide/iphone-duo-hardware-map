# `CDRichComplicationTemplateView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CDRichComplicationView`
- Protocols: `CDTemplateComplicationDisplay`
- 2 instance variables, 11 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _templateWantsPlatter;
@"CLKComplicationTemplate" _complicationTemplate;
```

## Properties

```
@property (T@"CLKComplicationTemplate",R,N,V_complicationTemplate) complicationTemplate;
@property (T@"CLKComplicationTemplate",R,N) template;
@property (TB,N,V_templateWantsPlatter) templateWantsPlatter;
@property (T@"<CDComplicationDisplayObserver>",W,N) displayObserver;
@property (TQ,N) textLayoutStyle;
@property (TB,?,N,GisHighlighted) highlighted;
@property (TB,?,N) shouldUseTemplateColors;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CDRichComplicationTemplateView handlesComplicationTemplate:];
```

## Instance methods

```
-[CDRichComplicationTemplateView template];
-[CDRichComplicationTemplateView complicationTemplate];
-[CDRichComplicationTemplateView setComplicationTemplate:reason:];
-[CDRichComplicationTemplateView _handleTemplate:reason:];
-[CDRichComplicationTemplateView setTimeTravelDate:animated:];
-[CDRichComplicationTemplateView templateWantsPlatter];
-[CDRichComplicationTemplateView timelineAnimationFadeTypeOverride];
-[CDRichComplicationTemplateView tritiumUpdateMode];
-[CDRichComplicationTemplateView setTemplateWantsPlatter:];
```
