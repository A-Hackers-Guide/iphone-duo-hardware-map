# `CDRichComplicationCornerGaugeTextView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CDRichComplicationCornerBaseGaugeView`
- 2 instance variables, 2 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _outerLabelProviders;
@"CLKUICurvedColoringLabel" _outerLabel;
```

## Properties

```
@property (T@"CLKUICurvedColoringLabel",R,N,V_outerLabel) outerLabel;
@property (T@"NSArray",&,N,V_outerLabelProviders) outerLabelProviders;
```

## Class methods

```
+[CDRichComplicationCornerGaugeTextView handlesComplicationTemplate:];
+[CDRichComplicationCornerGaugeTextView supportsComplicationFamily:];
```

## Instance methods

```
-[CDRichComplicationCornerGaugeTextView setFontStyle:];
-[CDRichComplicationCornerGaugeTextView layoutSubviews];
-[CDRichComplicationCornerGaugeTextView _editingDidEnd];
-[CDRichComplicationCornerGaugeTextView _enumerateLabelsWithBlock:];
-[CDRichComplicationCornerGaugeTextView _handleTemplate:reason:];
-[CDRichComplicationCornerGaugeTextView _setFontConfiguration:];
-[CDRichComplicationCornerGaugeTextView initWithFontFallback:];
-[CDRichComplicationCornerGaugeTextView transitionToMonochromeWithFraction:];
-[CDRichComplicationCornerGaugeTextView updateMonochromeColor];
-[CDRichComplicationCornerGaugeTextView outerLabel];
-[CDRichComplicationCornerGaugeTextView outerLabelProviders];
-[CDRichComplicationCornerGaugeTextView setOuterLabelProviders:];
```
