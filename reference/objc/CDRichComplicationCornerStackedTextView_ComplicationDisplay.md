# `CDRichComplicationCornerStackedTextView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CDRichComplicationCornerBaseTextView`
- 2 instance variables, 1 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"CLKUICurvedColoringLabel" _outerLabel;
@"NSArray" _outerLabelProviders;
```

## Properties

```
@property (T@"NSArray",&,N,V_outerLabelProviders) outerLabelProviders;
```

## Class methods

```
+[CDRichComplicationCornerStackedTextView handlesComplicationTemplate:];
+[CDRichComplicationCornerStackedTextView supportsComplicationFamily:];
```

## Instance methods

```
-[CDRichComplicationCornerStackedTextView layoutSubviews];
-[CDRichComplicationCornerStackedTextView _editingDidEnd];
-[CDRichComplicationCornerStackedTextView _enumerateLabelsWithBlock:];
-[CDRichComplicationCornerStackedTextView _handleTemplate:reason:];
-[CDRichComplicationCornerStackedTextView _setFontConfiguration:];
-[CDRichComplicationCornerStackedTextView initWithFontFallback:];
-[CDRichComplicationCornerStackedTextView transitionToMonochromeWithFraction:];
-[CDRichComplicationCornerStackedTextView updateMonochromeColor];
-[CDRichComplicationCornerStackedTextView outerLabel];
-[CDRichComplicationCornerStackedTextView outerLabelProviders];
-[CDRichComplicationCornerStackedTextView setOuterLabelProviders:];
```
