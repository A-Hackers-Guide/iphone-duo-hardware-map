# `BCUIRingItemView`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI`](../userland/System__Library__PrivateFrameworks__BatteryCenterUI.framework__BatteryCenterUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `MTVisualStylingRequiring`, `BCUIBatteryDeviceDisplaying`
- 9 instance variables, 17 properties, 43 instance methods, 3 class methods

## Instance variables

```
@"BCUIChargeRing" _chargeRing;
@"UILabel" _chargeLabel;
@"NSNumberFormatter" _percentChargeFormatter;
@"MTVisualStylingProvider" _visualStylingProvider;
B _empty;
d _ringScale;
d _scaleFactor;
@"<UIViewControllerTransitionCoordinator>" _transitionCoordinator;
q _ringItemViewStyle;
```

## Properties

```
@property (Tq,N,V_ringItemViewStyle) ringItemViewStyle;
@property (Td,N) ringLineWidth;
@property (Td,N,V_ringScale) ringScale;
@property (T@"NSArray",R,C,N) requiredVisualStyleCategories;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N) percentCharge;
@property (TB,N,GisCharging) charging;
@property (TB,N,GisLowCharge) lowCharge;
@property (TB,N,GisLowPowerModeEnabled) lowPowerModeEnabled;
@property (T@"UIImage",&,N) glyph;
@property (Td,N,V_scaleFactor) scaleFactor;
@property (T@"NSString",?,C,N) name;
@property (TB,?,N,GisEmpty,V_empty) empty;
@property (T@"<UIViewControllerTransitionCoordinator>",?,W,N,V_transitionCoordinator) transitionCoordinator;
```

## Class methods

```
+[BCUIRingItemView _ringLabelPaddingForContentSizeCategory:];
+[BCUIRingItemView isAX1PlusLayoutRequiredForContentSizeCategory:];
+[BCUIRingItemView isAX3PlusLayoutRequiredForContentSizeCategory:];
```

## Instance methods

```
-[BCUIRingItemView isCharging];
-[BCUIRingItemView transitionCoordinator];
-[BCUIRingItemView isLowPowerModeEnabled];
-[BCUIRingItemView didMoveToWindow];
-[BCUIRingItemView setGlyph:];
-[BCUIRingItemView glyph];
-[BCUIRingItemView setScaleFactor:];
-[BCUIRingItemView layoutSubviews];
-[BCUIRingItemView setVisualStylingProvider:forCategory:];
-[BCUIRingItemView setLowPowerModeEnabled:];
-[BCUIRingItemView isEmpty];
-[BCUIRingItemView scaleFactor];
-[BCUIRingItemView setCharging:];
-[BCUIRingItemView requiredVisualStyleCategories];
-[BCUIRingItemView setPercentCharge:];
-[BCUIRingItemView setEmpty:];
-[BCUIRingItemView didMoveToSuperview];
-[BCUIRingItemView initWithFrame:];
-[BCUIRingItemView percentCharge];
-[BCUIRingItemView setTransitionCoordinator:];
-[BCUIRingItemView _isPercentSymbolEnabledForRingItemStyle:andContentSizeCategory:];
-[BCUIRingItemView _beginAutomaticallyUpdatingChargeLabelVisualStyling];
-[BCUIRingItemView _chargeRing];
-[BCUIRingItemView _configureChargeLabelForStyle:];
-[BCUIRingItemView _frameForChargeLabelWithSize:baseLineOffsetFromBoundsTop:chargeRingSize:style:inBounds:scale:];
-[BCUIRingItemView _frameForChargeRingWithSize:chargeLabelSize:style:inBounds:scale:];
-[BCUIRingItemView _largestPossibleFrameForChargeLabelGivenBounds:chargeRingSize:andRingLabelPadding:];
-[BCUIRingItemView _lazyPercentChargeFormatter];
-[BCUIRingItemView _percentChargeString:];
-[BCUIRingItemView _sizeForChargeLabel:withStyle:inBounds:scale:];
-[BCUIRingItemView _sizeForChargeRingWithStyle:inBounds:withPreferredContentSizeCategory:];
-[BCUIRingItemView _stopAutomaticallyUpdatingVisualStyling];
-[BCUIRingItemView _updateFontForChargeLabelForStyle:andContentSizeCategory:];
-[BCUIRingItemView _updateVisualStylingWithProvidersFromStylingProvider:];
-[BCUIRingItemView _visualStylingProviderForCategory:];
-[BCUIRingItemView isLowCharge];
-[BCUIRingItemView ringItemViewStyle];
-[BCUIRingItemView ringLineWidth];
-[BCUIRingItemView ringScale];
-[BCUIRingItemView setLowCharge:];
-[BCUIRingItemView setRingItemViewStyle:];
-[BCUIRingItemView setRingLineWidth:];
-[BCUIRingItemView setRingScale:];
```
