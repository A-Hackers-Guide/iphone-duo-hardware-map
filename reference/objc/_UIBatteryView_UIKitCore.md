# `_UIBatteryView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIStatusBarView`, `_UIBatteryView`
- 19 instance variables, 34 properties, 116 instance methods, 8 class methods

## Instance variables

```
B _saverModeActive;
B _showsPercentage;
B _showsInlineChargingIndicator;
B _rounded;
d _chargePercent;
q _chargingState;
q _lowBatteryMode;
d _lowBatteryChargePercentThreshold;
q _iconSize;
@"UIColor" _fillColor;
@"UIColor" _inactiveColor;
@"UILabel" _percentageLabel;
@"_UIBatteryViewAXHUDImageCacheInfo" _accessibilityHUDImageCacheInfo;
@"CALayer" _bodyLayer;
@"CALayer" _pinLayer;
@"CALayer" _boltMaskLayer;
@"CALayer" _boltLayer;
@"CALayer" _percentFillLayer;
q _internalSizeCategory;
```

## Properties

```
@property (T@"CAShapeLayer",R,N) bodyShapeLayer;
@property (T@"CAShapeLayer",R,N) pinShapeLayer;
@property (T@"CAShapeLayer",R,N) boltMaskShapeLayer;
@property (T@"CAShapeLayer",R,N) boltShapeLayer;
@property (T@"CAShapeLayer",R,N) percentFillShapeLayer;
@property (T@"UILabel",&,N,V_percentageLabel) percentageLabel;
@property (T@"_UIBatteryViewAXHUDImageCacheInfo",&,N,V_accessibilityHUDImageCacheInfo) accessibilityHUDImageCacheInfo;
@property (T@"CALayer",&,N,V_bodyLayer) bodyLayer;
@property (T@"CALayer",&,N,V_pinLayer) pinLayer;
@property (T@"CALayer",&,N,V_boltMaskLayer) boltMaskLayer;
@property (T@"CALayer",&,N,V_boltLayer) boltLayer;
@property (T@"CALayer",&,N,V_percentFillLayer) percentFillLayer;
@property (Tq,N,V_internalSizeCategory) internalSizeCategory;
@property (TB,N,V_rounded) rounded;
@property (Td,N) bodyColorAlpha;
@property (Td,N) pinColorAlpha;
@property (TB,R,N) hasValidIconSize;
@property (T@"UIColor",C,N) bodyColor;
@property (T@"UIColor",C,N) pinColor;
@property (T@"UIColor",C,N) boltColor;
@property (T@"UIColor",C,N) boltInactiveColor;
@property (Tq,N,V_iconSize) iconSize;
@property (T@"UIAccessibilityHUDItem",R,N) accessibilityHUDRepresentation;
@property (Tq,N) sizeCategory;
@property (Td,N,V_chargePercent) chargePercent;
@property (Tq,N,V_chargingState) chargingState;
@property (TB,N,V_saverModeActive) saverModeActive;
@property (TB,N,V_showsPercentage) showsPercentage;
@property (Tq,N,V_lowBatteryMode) lowBatteryMode;
@property (Td,N,V_lowBatteryChargePercentThreshold) lowBatteryChargePercentThreshold;
@property (TB,R,N,GisLowBattery) lowBattery;
@property (TB,N,V_showsInlineChargingIndicator) showsInlineChargingIndicator;
@property (T@"UIColor",C,N,V_fillColor) fillColor;
@property (T@"UIColor",C,N,V_inactiveColor) inactiveColor;
```

## Class methods

```
+[_UIBatteryView _insideCornerRadiusForIconSize:];
+[_UIBatteryView _pinSizeForIconSize:];
+[_UIBatteryView _batterySizeForIconSize:];
+[_UIBatteryView _outsideCornerRadiusForIconSize:];
+[_UIBatteryView _lineWidthAndInterspaceForIconSize:];
+[_UIBatteryView _boltBezierPathForSize:];
+[_UIBatteryView _boltMaskBezierPath];
+[_UIBatteryView _pinBezierPathForSize:isComplex:];
```

## Instance methods

```
-[_UIBatteryView _commonInit];
-[_UIBatteryView setIconSize:];
-[_UIBatteryView iconSize];
-[_UIBatteryView _percentTextVerticalAdjustmentForIconSize:];
-[_UIBatteryView _percentageFontSizeForIconSize:];
-[_UIBatteryView accessibilityHUDRepresentation];
-[_UIBatteryView _percentageFontCondensedWhenChargingForIconSize:];
-[_UIBatteryView hasValidIconSize];
-[_UIBatteryView intrinsicContentSize];
-[_UIBatteryView setInactiveColor:];
-[_UIBatteryView _batteryBoltScaleFactorMultiplier];
-[_UIBatteryView setFillColor:];
-[_UIBatteryView fillColor];
-[_UIBatteryView _pinSizeForIconSize:];
-[_UIBatteryView dealloc];
-[_UIBatteryView sizeCategory];
-[_UIBatteryView inactiveColor];
-[_UIBatteryView layoutSubviews];
-[_UIBatteryView saverModeActive];
-[_UIBatteryView setSizeCategory:];
-[_UIBatteryView initWithCoder:];
-[_UIBatteryView _percentTextXAdjustmentWhenFullForIconSize:];
-[_UIBatteryView rounded];
-[_UIBatteryView setRounded:];
-[_UIBatteryView setChargingState:];
-[_UIBatteryView initWithFrame:];
-[_UIBatteryView chargingState];
-[_UIBatteryView _percentageBatteryBoltScaleFactorMultiplier];
-[_UIBatteryView _baselineOffsetsAtSize:];
-[_UIBatteryView _batterySizeForTraitCollection:];
-[_UIBatteryView _shouldShowBolt];
-[_UIBatteryView _boltIsInactive];
-[_UIBatteryView percentageLabel];
-[_UIBatteryView showsPercentage];
-[_UIBatteryView __resetBoltLayers];
-[_UIBatteryView __updateFillLayer];
-[_UIBatteryView _batteryBoltLargeScaleFactor];
-[_UIBatteryView _batteryBoltPositionOffsetForTraitCollection:];
-[_UIBatteryView _batteryBoltSmallScaleFactor];
-[_UIBatteryView _batteryTextIsCutout];
-[_UIBatteryView _bodyRectForTraitCollection:];
-[_UIBatteryView _createBodyLayers];
-[_UIBatteryView _createBoltLayersWithSize:];
-[_UIBatteryView _createFillLayer];
-[_UIBatteryView _didFinishAnimatingBoltToVisible:];
-[_UIBatteryView _fillLayerFrame:cornerRadius:];
-[_UIBatteryView _insideCornerRadiusForTraitCollection:];
-[_UIBatteryView _lineWidthAndInterspaceForTraitCollection:];
-[_UIBatteryView _nonPercentageBatteryBoltScaleFactor];
-[_UIBatteryView _notifyDidFinishAnimatingBoltToVisible:];
-[_UIBatteryView _notifyWillBeginAnimatingBoltToVisible:];
-[_UIBatteryView _outsideCornerRadiusForTraitCollection:];
-[_UIBatteryView _percentTextVerticalAdjustmentForTraitCollection:];
-[_UIBatteryView _percentTextXAdjustmentWhenFullForTraitCollection:];
-[_UIBatteryView _percentageFontCondensedWhenChargingForTraitCollection:];
-[_UIBatteryView _percentageFontSizeForTraitCollection:];
-[_UIBatteryView _pinSizeForTraitCollection:];
-[_UIBatteryView _roundedCornerRadiusFactor];
-[_UIBatteryView _unflipBoltIfNecessary];
-[_UIBatteryView _updateBatteryFillColor];
-[_UIBatteryView _updateBodyColors];
-[_UIBatteryView _updateBodyLayers];
-[_UIBatteryView _updateBolt];
-[_UIBatteryView _updateFillColor];
-[_UIBatteryView _updateFillLayer];
-[_UIBatteryView _updateForObservedTraitChange];
-[_UIBatteryView _updateLightningBoltAndPercentagePosition];
-[_UIBatteryView _updatePercentage];
-[_UIBatteryView _updatePercentageFont];
-[_UIBatteryView _updateTransform];
-[_UIBatteryView _willBeginAnimatingBoltToVisible:];
-[_UIBatteryView accessibilityHUDImageCacheInfo];
-[_UIBatteryView bodyColor];
-[_UIBatteryView bodyColorAlpha];
-[_UIBatteryView bodyLayer];
-[_UIBatteryView bodyShapeLayer];
-[_UIBatteryView boltColor];
-[_UIBatteryView boltInactiveColor];
-[_UIBatteryView boltLayer];
-[_UIBatteryView boltMaskLayer];
-[_UIBatteryView boltMaskShapeLayer];
-[_UIBatteryView boltShapeLayer];
-[_UIBatteryView chargePercent];
-[_UIBatteryView initWithSizeCategory:];
-[_UIBatteryView internalSizeCategory];
-[_UIBatteryView isLowBattery];
-[_UIBatteryView lowBatteryChargePercentThreshold];
-[_UIBatteryView lowBatteryMode];
-[_UIBatteryView percentFillLayer];
-[_UIBatteryView percentFillShapeLayer];
-[_UIBatteryView pinColor];
-[_UIBatteryView pinColorAlpha];
-[_UIBatteryView pinLayer];
-[_UIBatteryView pinShapeLayer];
-[_UIBatteryView setAccessibilityHUDImageCacheInfo:];
-[_UIBatteryView setBodyColor:];
-[_UIBatteryView setBodyColorAlpha:];
-[_UIBatteryView setBodyLayer:];
-[_UIBatteryView setBoltColor:];
-[_UIBatteryView setBoltInactiveColor:];
-[_UIBatteryView setBoltLayer:];
-[_UIBatteryView setBoltMaskLayer:];
-[_UIBatteryView setChargePercent:];
-[_UIBatteryView setInternalSizeCategory:];
-[_UIBatteryView setLowBatteryChargePercentThreshold:];
-[_UIBatteryView setLowBatteryMode:];
-[_UIBatteryView setPercentFillLayer:];
-[_UIBatteryView setPercentageLabel:];
-[_UIBatteryView setPinColor:];
-[_UIBatteryView setPinColorAlpha:];
-[_UIBatteryView setPinLayer:];
-[_UIBatteryView setRounded:iconSize:];
-[_UIBatteryView setSaverModeActive:];
-[_UIBatteryView setShowsInlineChargingIndicator:];
-[_UIBatteryView setShowsPercentage:];
-[_UIBatteryView showsInlineChargingIndicator];
```
