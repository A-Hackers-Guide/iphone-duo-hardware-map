# `BCUIChargeRing`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI`](../userland/System__Library__PrivateFrameworks__BatteryCenterUI.framework__BatteryCenterUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `MTVisualStylingRequiring`, `BCUIBatteryDeviceDisplaying`
- 18 instance variables, 16 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"BCUIRingView" _baseRing;
@"BCUIRingView" _chargeRing;
@"BCUIRingCapShadow" _ringCapShadow;
@"UIImageView" _boltMaskImageView;
@"UIImageView" _boltImageView;
@"CABackdropLayer" _captureBackdrop;
@"UIImageView" _glyphImageView;
@"MTVisualStylingProvider" _visualStylingProvider;
@"MTVisualStylingProvider" _baseRingVisualStylingProvider;
B _lowCharge;
B _charging;
B _lowPowerModeEnabled;
d _lineWidth;
d _ringScale;
q _percentCharge;
@"UIImage" _glyph;
d _scaleFactor;
@"<UIViewControllerTransitionCoordinator>" _transitionCoordinator;
```

## Properties

```
@property (Td,N,V_lineWidth) lineWidth;
@property (Td,N,V_ringScale) ringScale;
@property (T@"NSArray",R,C,N) requiredVisualStyleCategories;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N,V_percentCharge) percentCharge;
@property (TB,N,GisCharging,V_charging) charging;
@property (TB,N,GisLowCharge,V_lowCharge) lowCharge;
@property (TB,N,GisLowPowerModeEnabled,V_lowPowerModeEnabled) lowPowerModeEnabled;
@property (T@"UIImage",&,N,V_glyph) glyph;
@property (Td,N,V_scaleFactor) scaleFactor;
@property (T@"NSString",?,C,N) name;
@property (TB,?,N,GisEmpty) empty;
@property (T@"<UIViewControllerTransitionCoordinator>",?,W,N,V_transitionCoordinator) transitionCoordinator;
```

## Instance methods

```
-[BCUIChargeRing isCharging];
-[BCUIChargeRing transitionCoordinator];
-[BCUIChargeRing lineWidth];
-[BCUIChargeRing isLowPowerModeEnabled];
-[BCUIChargeRing setLineWidth:];
-[BCUIChargeRing didMoveToWindow];
-[BCUIChargeRing setGlyph:];
-[BCUIChargeRing glyph];
-[BCUIChargeRing _dynamicUserInterfaceTraitDidChange];
-[BCUIChargeRing init];
-[BCUIChargeRing setScaleFactor:];
-[BCUIChargeRing layoutSubviews];
-[BCUIChargeRing setVisualStylingProvider:forCategory:];
-[BCUIChargeRing sizeThatFits:];
-[BCUIChargeRing setLowPowerModeEnabled:];
-[BCUIChargeRing scaleFactor];
-[BCUIChargeRing setCharging:];
-[BCUIChargeRing requiredVisualStyleCategories];
-[BCUIChargeRing setPercentCharge:];
-[BCUIChargeRing didMoveToSuperview];
-[BCUIChargeRing percentCharge];
-[BCUIChargeRing setTransitionCoordinator:];
-[BCUIChargeRing _glyphImageView];
-[BCUIChargeRing _baseRing];
-[BCUIChargeRing _beginAutomaticallyUpdatingPrimaryVisualStylingForView:observerBlock:];
-[BCUIChargeRing _beginAutomaticallyUpdatingVisualStylingForCategory:];
-[BCUIChargeRing _chargeRing];
-[BCUIChargeRing _configureBoltImageViewIfNecessary];
-[BCUIChargeRing _configureBoltMaskImageViewIfNecessary];
-[BCUIChargeRing _configureCaptureBackdropIfNecessary];
-[BCUIChargeRing _configureRingCapShadowIfNecessary];
-[BCUIChargeRing _isPastThresholdForRingCapShadow];
-[BCUIChargeRing _ringVisualStylingProvider];
-[BCUIChargeRing _shouldShowRingCapShadow];
-[BCUIChargeRing _stopAutomaticallyUpdatingVisualStylingForCategory:];
-[BCUIChargeRing _updateVisualStylingForBaseRingIfNecessary];
-[BCUIChargeRing _updateVisualStylingForBolt];
-[BCUIChargeRing _updateVisualStylingWithProvidersFromStylingProvider:];
-[BCUIChargeRing _visualStylingProviderForCategory:];
-[BCUIChargeRing isLowCharge];
-[BCUIChargeRing ringScale];
-[BCUIChargeRing setLowCharge:];
-[BCUIChargeRing setRingScale:];
```
