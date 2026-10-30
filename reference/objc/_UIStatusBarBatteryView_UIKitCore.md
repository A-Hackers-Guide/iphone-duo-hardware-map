# `_UIStatusBarBatteryView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIStatusBarDisplayable`
- 25 instance variables, 41 properties, 108 instance methods, 7 class methods

## Instance variables

```
B _saverModeActive;
B _showsInlineChargingIndicator;
B _rounded;
B _showsPercentage;
@"UIColor" _fillColor;
@"UIColor" _bodyColor;
@"UIColor" _pinColor;
@"UIColor" _boltColor;
@"UIColor" _inactiveColor;
d _chargePercent;
q _chargingState;
q _lowBatteryMode;
d _lowBatteryChargePercentThreshold;
q _iconSize;
@"UILabel" _percentageLabel;
@"_UIStatusBarBatteryViewAXHUDImageCacheInfo" _accessibilityHUDImageCacheInfo;
@"CALayer" _bodyLayer;
@"CALayer" _pinLayer;
@"CALayer" _boltMaskLayer;
@"CALayer" _boltLayer;
@"CALayer" _fillLayer;
@"CALayer" _percentFillLayer;
q _internalSizeCategory;
d _bodyColorAlpha;
d _pinColorAlpha;
```

## Properties

```
@property (Tq,N,V_iconSize) iconSize;
@property (T@"CAShapeLayer",R,N) bodyShapeLayer;
@property (T@"CAShapeLayer",R,N) pinShapeLayer;
@property (T@"CAShapeLayer",R,N) boltMaskShapeLayer;
@property (T@"CAShapeLayer",R,N) boltShapeLayer;
@property (T@"CAShapeLayer",R,N) percentFillShapeLayer;
@property (T@"UILabel",&,N,V_percentageLabel) percentageLabel;
@property (T@"_UIStatusBarBatteryViewAXHUDImageCacheInfo",&,N,V_accessibilityHUDImageCacheInfo) accessibilityHUDImageCacheInfo;
@property (TB,N,V_rounded) rounded;
@property (T@"CALayer",&,N,V_bodyLayer) bodyLayer;
@property (T@"CALayer",&,N,V_pinLayer) pinLayer;
@property (T@"CALayer",&,N,V_boltMaskLayer) boltMaskLayer;
@property (T@"CALayer",&,N,V_boltLayer) boltLayer;
@property (T@"CALayer",&,N,V_fillLayer) fillLayer;
@property (T@"CALayer",&,N,V_percentFillLayer) percentFillLayer;
@property (Tq,N,V_internalSizeCategory) internalSizeCategory;
@property (TB,N,V_showsPercentage) showsPercentage;
@property (Td,N,V_bodyColorAlpha) bodyColorAlpha;
@property (Td,N,V_pinColorAlpha) pinColorAlpha;
@property (T@"UIColor",C,N,V_inactiveColor) inactiveColor;
@property (Tq,N) sizeCategory;
@property (Td,N,V_chargePercent) chargePercent;
@property (Tq,N,V_chargingState) chargingState;
@property (TB,N,V_saverModeActive) saverModeActive;
@property (Tq,N,V_lowBatteryMode) lowBatteryMode;
@property (Td,N,V_lowBatteryChargePercentThreshold) lowBatteryChargePercentThreshold;
@property (TB,R,N,GisLowBattery) lowBattery;
@property (TB,N,V_showsInlineChargingIndicator) showsInlineChargingIndicator;
@property (T@"UIColor",C,N,V_fillColor) fillColor;
@property (T@"UIColor",C,N,V_bodyColor) bodyColor;
@property (T@"UIColor",C,N,V_pinColor) pinColor;
@property (T@"UIColor",C,N,V_boltColor) boltColor;
@property (TB,?,R,N) wantsCrossfade;
@property (TB,?,R,N) prefersBaselineAlignment;
@property (TB,?,R,N) prefersCenterVerticalAlignment;
@property (Tq,?,R,N) overriddenVerticalAlignment;
@property (T@"UIAccessibilityHUDItem",?,R,N) accessibilityHUDRepresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStatusBarBatteryView _pinSizeForIconSize:];
+[_UIStatusBarBatteryView _batterySizeForIconSize:];
+[_UIStatusBarBatteryView _lineWidthAndInterspaceForIconSize:];
+[_UIStatusBarBatteryView _boltBezierPathForSize:];
+[_UIStatusBarBatteryView _boltMaskBezierPath];
+[_UIStatusBarBatteryView _pinBezierPathForSize:isComplex:];
+[_UIStatusBarBatteryView _statusBarIntrinsicContentSizeForIconSize:];
```

## Instance methods

```
-[_UIStatusBarBatteryView _commonInit];
-[_UIStatusBarBatteryView setIconSize:];
-[_UIStatusBarBatteryView iconSize];
-[_UIStatusBarBatteryView accessibilityHUDRepresentation];
-[_UIStatusBarBatteryView applyStyleAttributes:];
-[_UIStatusBarBatteryView intrinsicContentSize];
-[_UIStatusBarBatteryView setInactiveColor:];
-[_UIStatusBarBatteryView _batteryBoltScaleFactorMultiplier];
-[_UIStatusBarBatteryView setFillColor:];
-[_UIStatusBarBatteryView fillColor];
-[_UIStatusBarBatteryView sizeCategory];
-[_UIStatusBarBatteryView inactiveColor];
-[_UIStatusBarBatteryView layoutSubviews];
-[_UIStatusBarBatteryView saverModeActive];
-[_UIStatusBarBatteryView setSizeCategory:];
-[_UIStatusBarBatteryView initWithCoder:];
-[_UIStatusBarBatteryView traitCollectionDidChange:];
-[_UIStatusBarBatteryView rounded];
-[_UIStatusBarBatteryView setRounded:];
-[_UIStatusBarBatteryView setChargingState:];
-[_UIStatusBarBatteryView initWithFrame:];
-[_UIStatusBarBatteryView chargingState];
-[_UIStatusBarBatteryView _percentageBatteryBoltScaleFactorMultiplier];
-[_UIStatusBarBatteryView _baselineOffsetsAtSize:];
-[_UIStatusBarBatteryView _batterySizeForTraitCollection:];
-[_UIStatusBarBatteryView _shouldShowBolt];
-[_UIStatusBarBatteryView percentageLabel];
-[_UIStatusBarBatteryView showsPercentage];
-[_UIStatusBarBatteryView __resetBoltLayers];
-[_UIStatusBarBatteryView __updateFillLayer];
-[_UIStatusBarBatteryView _batteryBoltLargeScaleFactor];
-[_UIStatusBarBatteryView _batteryBoltPositionOffsetForTraitCollection:];
-[_UIStatusBarBatteryView _batteryBoltSmallScaleFactor];
-[_UIStatusBarBatteryView _batteryFillColor];
-[_UIStatusBarBatteryView _batteryTextColor];
-[_UIStatusBarBatteryView _batteryTextIsCutout];
-[_UIStatusBarBatteryView _batteryUnfilledColor];
-[_UIStatusBarBatteryView _bodyRectForTraitCollection:];
-[_UIStatusBarBatteryView _createBodyLayers];
-[_UIStatusBarBatteryView _createBoltLayersWithSize:];
-[_UIStatusBarBatteryView _createFillLayer];
-[_UIStatusBarBatteryView _didFinishAnimatingBoltToVisible:];
-[_UIStatusBarBatteryView _fillLayerFrame:cornerRadius:];
-[_UIStatusBarBatteryView _insideCornerRadiusForTraitCollection:];
-[_UIStatusBarBatteryView _lineWidthAndInterspaceForTraitCollection:];
-[_UIStatusBarBatteryView _notifyDidFinishAnimatingBoltToVisible:];
-[_UIStatusBarBatteryView _notifyWillBeginAnimatingBoltToVisible:];
-[_UIStatusBarBatteryView _outsideCornerRadiusForTraitCollection:];
-[_UIStatusBarBatteryView _percentTextVerticalAdjustmentForTraitCollection:];
-[_UIStatusBarBatteryView _percentageFontCondensedWhenChargingForTraitCollection:];
-[_UIStatusBarBatteryView _percentageFontSizeForTraitCollection:];
-[_UIStatusBarBatteryView _pinSizeForTraitCollection:];
-[_UIStatusBarBatteryView _unflipBoltIfNecessary];
-[_UIStatusBarBatteryView _updateBatteryFillColor];
-[_UIStatusBarBatteryView _updateBodyColors];
-[_UIStatusBarBatteryView _updateBodyLayers];
-[_UIStatusBarBatteryView _updateBolt];
-[_UIStatusBarBatteryView _updateFillColor];
-[_UIStatusBarBatteryView _updateFillLayer];
-[_UIStatusBarBatteryView _updateLightningBoltAndPercentagePosition];
-[_UIStatusBarBatteryView _updatePercentage];
-[_UIStatusBarBatteryView _updatePercentageFont];
-[_UIStatusBarBatteryView _updateTransform];
-[_UIStatusBarBatteryView _willBeginAnimatingBoltToVisible:];
-[_UIStatusBarBatteryView accessibilityHUDImageCacheInfo];
-[_UIStatusBarBatteryView bodyColor];
-[_UIStatusBarBatteryView bodyColorAlpha];
-[_UIStatusBarBatteryView bodyLayer];
-[_UIStatusBarBatteryView bodyShapeLayer];
-[_UIStatusBarBatteryView boltColor];
-[_UIStatusBarBatteryView boltLayer];
-[_UIStatusBarBatteryView boltMaskLayer];
-[_UIStatusBarBatteryView boltMaskShapeLayer];
-[_UIStatusBarBatteryView boltShapeLayer];
-[_UIStatusBarBatteryView chargePercent];
-[_UIStatusBarBatteryView fillLayer];
-[_UIStatusBarBatteryView initWithSizeCategory:];
-[_UIStatusBarBatteryView internalSizeCategory];
-[_UIStatusBarBatteryView isLowBattery];
-[_UIStatusBarBatteryView lowBatteryChargePercentThreshold];
-[_UIStatusBarBatteryView lowBatteryMode];
-[_UIStatusBarBatteryView percentFillLayer];
-[_UIStatusBarBatteryView percentFillShapeLayer];
-[_UIStatusBarBatteryView pinColor];
-[_UIStatusBarBatteryView pinColorAlpha];
-[_UIStatusBarBatteryView pinLayer];
-[_UIStatusBarBatteryView pinShapeLayer];
-[_UIStatusBarBatteryView setAccessibilityHUDImageCacheInfo:];
-[_UIStatusBarBatteryView setBodyColor:];
-[_UIStatusBarBatteryView setBodyColorAlpha:];
-[_UIStatusBarBatteryView setBodyLayer:];
-[_UIStatusBarBatteryView setBoltColor:];
-[_UIStatusBarBatteryView setBoltLayer:];
-[_UIStatusBarBatteryView setBoltMaskLayer:];
-[_UIStatusBarBatteryView setChargePercent:];
-[_UIStatusBarBatteryView setFillLayer:];
-[_UIStatusBarBatteryView setInternalSizeCategory:];
-[_UIStatusBarBatteryView setLowBatteryChargePercentThreshold:];
-[_UIStatusBarBatteryView setLowBatteryMode:];
-[_UIStatusBarBatteryView setPercentFillLayer:];
-[_UIStatusBarBatteryView setPercentageLabel:];
-[_UIStatusBarBatteryView setPinColor:];
-[_UIStatusBarBatteryView setPinColorAlpha:];
-[_UIStatusBarBatteryView setPinLayer:];
-[_UIStatusBarBatteryView setSaverModeActive:];
-[_UIStatusBarBatteryView setShowsInlineChargingIndicator:];
-[_UIStatusBarBatteryView setShowsPercentage:];
-[_UIStatusBarBatteryView showsInlineChargingIndicator];
```
