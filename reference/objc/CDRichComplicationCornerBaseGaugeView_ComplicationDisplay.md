# `CDRichComplicationCornerBaseGaugeView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CDRichComplicationCornerView`
- 3 instance variables, 0 properties, 21 instance methods, 2 class methods

## Instance variables

```
@"CLKUICurvedColoringLabel" _leftLabel;
@"CDRichComplicationCurvedProgressView" _progressView;
@"CLKUICurvedColoringLabel" _rightLabel;
```

## Class methods

```
+[CDRichComplicationCornerBaseGaugeView isMeteredProgressView];
+[CDRichComplicationCornerBaseGaugeView progressFillStyle];
```

## Instance methods

```
-[CDRichComplicationCornerBaseGaugeView layoutSubviews];
-[CDRichComplicationCornerBaseGaugeView progressView];
-[CDRichComplicationCornerBaseGaugeView leftLabel];
-[CDRichComplicationCornerBaseGaugeView rightLabel];
-[CDRichComplicationCornerBaseGaugeView _editingDidEnd];
-[CDRichComplicationCornerBaseGaugeView _enumerateLabelsWithBlock:];
-[CDRichComplicationCornerBaseGaugeView _progressViewHorizontalPaddingInRadius];
-[CDRichComplicationCornerBaseGaugeView _setFontConfiguration:];
-[CDRichComplicationCornerBaseGaugeView handleGaugeProvider:leftTextProvider:rightTextProvider:];
-[CDRichComplicationCornerBaseGaugeView initWithFontFallback:];
-[CDRichComplicationCornerBaseGaugeView setCornerComplicationPosition:];
-[CDRichComplicationCornerBaseGaugeView transitionToMonochromeWithFraction:];
-[CDRichComplicationCornerBaseGaugeView updateMonochromeColor];
-[CDRichComplicationCornerBaseGaugeView _layoutSubviewsWithoutAnimation];
-[CDRichComplicationCornerBaseGaugeView _calculateLabel:center:widthInRadius:];
-[CDRichComplicationCornerBaseGaugeView _calculateProgressWidthWithLeftLabelWidth:rightLabelWidth:];
-[CDRichComplicationCornerBaseGaugeView _layoutLabel:withLabelCenter:labelWidthInRadius:leftInRadius:];
-[CDRichComplicationCornerBaseGaugeView _layoutProgressViewWithBeginAngle:widthInRadius:bottomPadding:];
-[CDRichComplicationCornerBaseGaugeView _replaceProgressView:];
-[CDRichComplicationCornerBaseGaugeView _updateLabelMaxWidths];
-[CDRichComplicationCornerBaseGaugeView handleGaugeProvider:leftLabelProvider:rightLabelProvider:];
```
