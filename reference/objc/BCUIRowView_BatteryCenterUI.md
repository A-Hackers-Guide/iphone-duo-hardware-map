# `BCUIRowView`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI`](../userland/System__Library__PrivateFrameworks__BatteryCenterUI.framework__BatteryCenterUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `MTVisualStylingRequiring`, `BCUIBatteryDeviceDisplaying`
- 15 instance variables, 15 properties, 44 instance methods, 1 class methods

## Instance variables

```
@"UIImageView" _glyphImageView;
@"UILabel" _nameLabel;
@"UILabel" _percentChargeLabel;
@"NSNumberFormatter" _percentChargeFormatter;
@"_UIStaticBatteryView" _batteryView;
@"UIView" _separator;
@"NSMutableDictionary" _categoriesToVisualStylingProvider;
B _charging;
B _lowCharge;
B _lowPowerModeEnabled;
B _empty;
q _percentCharge;
@"UIImage" _glyph;
d _scaleFactor;
@"NSString" _name;
```

## Properties

```
@property (TB,N,GisSeparatorVisible) separatorVisible;
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
@property (T@"NSString",?,C,N,V_name) name;
@property (TB,?,N,GisEmpty,V_empty) empty;
@property (T@"<UIViewControllerTransitionCoordinator>",?,W,N) transitionCoordinator;
```

## Class methods

```
+[BCUIRowView isAX3PlusLayoutRequiredForContentSizeCategory:];
```

## Instance methods

```
-[BCUIRowView isCharging];
-[BCUIRowView isLowPowerModeEnabled];
-[BCUIRowView didMoveToWindow];
-[BCUIRowView setGlyph:];
-[BCUIRowView glyph];
-[BCUIRowView _configureGlyphImageViewIfNecessary];
-[BCUIRowView init];
-[BCUIRowView setScaleFactor:];
-[BCUIRowView layoutSubviews];
-[BCUIRowView setVisualStylingProvider:forCategory:];
-[BCUIRowView setLowPowerModeEnabled:];
-[BCUIRowView isEmpty];
-[BCUIRowView scaleFactor];
-[BCUIRowView setCharging:];
-[BCUIRowView setName:];
-[BCUIRowView requiredVisualStyleCategories];
-[BCUIRowView setPercentCharge:];
-[BCUIRowView setEmpty:];
-[BCUIRowView didMoveToSuperview];
-[BCUIRowView percentCharge];
-[BCUIRowView name];
-[BCUIRowView isSeparatorVisible];
-[BCUIRowView setSeparatorVisible:];
-[BCUIRowView _batteryViewFrameforContentSize:percentChargeLabelFrame:];
-[BCUIRowView _beginAutomaticallyUpdatingVisualStylingForCategory:];
-[BCUIRowView _configureBatteryViewIfNecessary];
-[BCUIRowView _configureNameLabelIfNecessary];
-[BCUIRowView _configurePercentChargeLabelIfNecessary];
-[BCUIRowView _configureSeparatorIfNecessary];
-[BCUIRowView _glyphImageViewFrameForContentSizeCategory:];
-[BCUIRowView _lazyPercentChargeFormatter];
-[BCUIRowView _nameLabelFrameForContentSize:percentChargeLabelFrame:];
-[BCUIRowView _percentChargeLabelFrameForContentSizeCategory:];
-[BCUIRowView _percentChargeString:];
-[BCUIRowView _sepatorFrameForContentSize:];
-[BCUIRowView _stopAutomaticallyUpdatingVisualStylingForCategory:];
-[BCUIRowView _updateBatteryViewIfNeccessary];
-[BCUIRowView _updateGlyphImageViewIfNecessary:];
-[BCUIRowView _updateNameLabelIfNecessary:];
-[BCUIRowView _updatePercentChargeLabelIfNecessary:];
-[BCUIRowView _updateVisualStylingWithProvidersFromStylingProvider:];
-[BCUIRowView _visualStylingProviderForCategory:];
-[BCUIRowView isLowCharge];
-[BCUIRowView setLowCharge:];
```
