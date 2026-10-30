# `SBChargingAlertElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAElement`, `SAAlertBehavior`, `SAUILayoutSpecifying`, `SAUIElementViewProviding`, `SAUILayoutDirectionObserving`, `SBSystemApertureElement`, `SBSystemApertureSuppressible`, `SBSystemApertureContextProviding`, `SBSystemApertureLayoutCustomizing`
- 31 instance variables, 52 properties, 83 instance methods, 0 class methods

## Instance variables

```
@"UIColor" _keyColor;
B _displayedWithLimitedSize;
B _lowPowerModeEnabled;
@"NSString" _clientIdentifier;
@"NSString" _elementIdentifier;
@"<SAElementHosting>" _elementHost;
@"<SAAlertHosting>" _alertHost;
q _layoutMode;
q _minimumSupportedLayoutMode;
q _maximumSupportedLayoutMode;
q _preferredLayoutMode;
@"<SAUILayoutHosting>" _layoutHost;
@"UIView" _leadingView;
@"UIView" _trailingView;
@"UIView" _minimalView;
Q _layoutDirection;
@"<SBSystemAperturePlatformElementHosting>" _platformElementHost;
d _batteryPercentage;
@"UILabel" _leadingLabel;
@"BSUICAPackageView" _leadingBatteryIconPackageView;
@"UILabel" _trailingBatteryLabel;
@"BSUICAPackageView" _trailingBatteryIconPackageView;
@"BSUICAPackageView" _minimalBatteryIconPackageView;
@"NSArray" _defaultLeadingConstraints;
@"NSArray" _horizontalLimitedSizeLeadingConstraints;
@"NSArray" _verticalLimitedSizeLeadingConstraints;
@"NSArray" _defaultTrailingConstraints;
@"NSArray" _inflatedTrailingWidthConstraints;
@"NSArray" _contentSizedTrailingWidthConstraints;
@"NSArray" _horizontalLimitedSizeTrailingConstraints;
@"NSArray" _verticalLimitedSizeTrailingConstraints;
```

## Properties

```
@property (Tq,N,V_minimumSupportedLayoutMode) minimumSupportedLayoutMode;
@property (Tq,N,V_maximumSupportedLayoutMode) maximumSupportedLayoutMode;
@property (Tq,N,V_preferredLayoutMode) preferredLayoutMode;
@property (TB,N,GisLowPowerModeEnabled,V_lowPowerModeEnabled) lowPowerModeEnabled;
@property (T@"UILabel",&,N,V_leadingLabel) leadingLabel;
@property (T@"BSUICAPackageView",&,N,V_leadingBatteryIconPackageView) leadingBatteryIconPackageView;
@property (T@"UILabel",&,N,V_trailingBatteryLabel) trailingBatteryLabel;
@property (T@"BSUICAPackageView",&,N,V_trailingBatteryIconPackageView) trailingBatteryIconPackageView;
@property (T@"BSUICAPackageView",&,N,V_minimalBatteryIconPackageView) minimalBatteryIconPackageView;
@property (T@"NSArray",&,N,V_defaultLeadingConstraints) defaultLeadingConstraints;
@property (T@"NSArray",&,N,V_horizontalLimitedSizeLeadingConstraints) horizontalLimitedSizeLeadingConstraints;
@property (T@"NSArray",&,N,V_verticalLimitedSizeLeadingConstraints) verticalLimitedSizeLeadingConstraints;
@property (T@"NSArray",&,N,V_defaultTrailingConstraints) defaultTrailingConstraints;
@property (T@"NSArray",&,N,V_inflatedTrailingWidthConstraints) inflatedTrailingWidthConstraints;
@property (T@"NSArray",&,N,V_contentSizedTrailingWidthConstraints) contentSizedTrailingWidthConstraints;
@property (T@"NSArray",&,N,V_horizontalLimitedSizeTrailingConstraints) horizontalLimitedSizeTrailingConstraints;
@property (T@"NSArray",&,N,V_verticalLimitedSizeTrailingConstraints) verticalLimitedSizeTrailingConstraints;
@property (Td,N,V_batteryPercentage) batteryPercentage;
@property (T@"<SAElementHosting>",?,W,N,V_elementHost) elementHost;
@property (T@"NSString",R,C,N,V_clientIdentifier) clientIdentifier;
@property (T@"NSString",R,C,N,V_elementIdentifier) elementIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SAAlertHosting>",?,W,N,V_alertHost) alertHost;
@property (Tq,R,N,V_layoutMode) layoutMode;
@property (T@"<SAUILayoutHosting>",?,W,N,V_layoutHost) layoutHost;
@property (TB,?,R,N,GisInteractiveDismissalEnabled) interactiveDismissalEnabled;
@property (TB,?,R,N,GisMinimalPresentationPossible) minimalPresentationPossible;
@property (TB,?,R,N,GisRequestingMenuPresentation) requestingMenuPresentation;
@property (TB,?,N,GisDisplayedWithLimitedSize,V_displayedWithLimitedSize) displayedWithLimitedSize;
@property (T@"UIView",R,N,V_leadingView) leadingView;
@property (T@"UIView",R,N,V_trailingView) trailingView;
@property (T@"UIView",R,N,V_minimalView) minimalView;
@property (T@"UIView",?,R,N) detachedMinimalView;
@property (T@"<SAElement>",R,W,N) element;
@property (TQ,?,N) layoutAxis;
@property (TQ,?,N,V_layoutDirection) layoutDirection;
@property (T@"<SBSystemAperturePlatformElementHosting>",?,W,N,V_platformElementHost) platformElementHost;
@property (TB,?,N,GisSuppressed) suppressed;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (Tq,?,R,N) systemApertureCustomLayout;
@property (Tq,?,R,N) customLayoutRequestingSpecialFlowerBoundsResizingAnimation;
@property (Tq,?,R,N) systemApertureLayoutCustomizingOptions;
```

## Instance methods

```
-[SBChargingAlertElement setDisplayedWithLimitedSize:];
-[SBChargingAlertElement _windowScene];
-[SBChargingAlertElement layoutHost];
-[SBChargingAlertElement keyColor];
-[SBChargingAlertElement minimalView];
-[SBChargingAlertElement trailingView];
-[SBChargingAlertElement overridesConcentricPaddingForView:inLayoutMode:];
-[SBChargingAlertElement setLayoutMode:reason:];
-[SBChargingAlertElement concentricPaddingOverrideForView:inLayoutMode:];
-[SBChargingAlertElement layoutMode];
-[SBChargingAlertElement leadingView];
-[SBChargingAlertElement isLowPowerModeEnabled];
-[SBChargingAlertElement setLayoutHost:];
-[SBChargingAlertElement clientIdentifier];
-[SBChargingAlertElement isProvidedViewConcentric:inLayoutMode:];
-[SBChargingAlertElement element];
-[SBChargingAlertElement preferredLayoutMode];
-[SBChargingAlertElement preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBChargingAlertElement isDisplayedWithLimitedSize];
-[SBChargingAlertElement elementIdentifier];
-[SBChargingAlertElement viewProvider];
-[SBChargingAlertElement setLayoutDirection:];
-[SBChargingAlertElement layoutDirection];
-[SBChargingAlertElement handleElementViewEvent:];
-[SBChargingAlertElement setBatteryPercentage:];
-[SBChargingAlertElement batteryPercentage];
-[SBChargingAlertElement setAlertHost:];
-[SBChargingAlertElement shouldSuppressElementWhileProximityReaderPresent];
-[SBChargingAlertElement setPlatformElementHost:];
-[SBChargingAlertElement _canShowWhileLocked];
-[SBChargingAlertElement elementHost];
-[SBChargingAlertElement setLowPowerModeEnabled:];
-[SBChargingAlertElement description];
-[SBChargingAlertElement minimumSupportedLayoutMode];
-[SBChargingAlertElement hasAlertBehavior];
-[SBChargingAlertElement setElementHost:];
-[SBChargingAlertElement alertHost];
-[SBChargingAlertElement maximumSupportedLayoutMode];
-[SBChargingAlertElement _layoutMetrics];
-[SBChargingAlertElement platformElementHost];
-[SBChargingAlertElement setPreferredLayoutMode:];
-[SBChargingAlertElement leadingLabel];
-[SBChargingAlertElement _applyLayoutForLimitedSize:];
-[SBChargingAlertElement _buildContentViews];
-[SBChargingAlertElement _buildLeadingView];
-[SBChargingAlertElement _buildMinimalView];
-[SBChargingAlertElement _buildTrailingView];
-[SBChargingAlertElement _leadingViewFlanksSensor];
-[SBChargingAlertElement _platformLayoutMetrics];
-[SBChargingAlertElement _trailingViewFillsAvailableWidth];
-[SBChargingAlertElement _trailingViewWidth];
-[SBChargingAlertElement _updateBatteryContent];
-[SBChargingAlertElement _updateMinimalViewWithDelayToState:];
-[SBChargingAlertElement _usesVerticalLimitedLayout];
-[SBChargingAlertElement contentSizedTrailingWidthConstraints];
-[SBChargingAlertElement defaultLeadingConstraints];
-[SBChargingAlertElement defaultTrailingConstraints];
-[SBChargingAlertElement elementDescription];
-[SBChargingAlertElement horizontalLimitedSizeLeadingConstraints];
-[SBChargingAlertElement horizontalLimitedSizeTrailingConstraints];
-[SBChargingAlertElement inflatedTrailingWidthConstraints];
-[SBChargingAlertElement initWithIdentifier:batteryPercentage:lowPowerModeEnabled:];
-[SBChargingAlertElement leadingBatteryIconPackageView];
-[SBChargingAlertElement minimalBatteryIconPackageView];
-[SBChargingAlertElement setContentSizedTrailingWidthConstraints:];
-[SBChargingAlertElement setDefaultLeadingConstraints:];
-[SBChargingAlertElement setDefaultTrailingConstraints:];
-[SBChargingAlertElement setHorizontalLimitedSizeLeadingConstraints:];
-[SBChargingAlertElement setHorizontalLimitedSizeTrailingConstraints:];
-[SBChargingAlertElement setInflatedTrailingWidthConstraints:];
-[SBChargingAlertElement setLeadingBatteryIconPackageView:];
-[SBChargingAlertElement setLeadingLabel:];
-[SBChargingAlertElement setMaximumSupportedLayoutMode:];
-[SBChargingAlertElement setMinimalBatteryIconPackageView:];
-[SBChargingAlertElement setMinimumSupportedLayoutMode:];
-[SBChargingAlertElement setTrailingBatteryIconPackageView:];
-[SBChargingAlertElement setTrailingBatteryLabel:];
-[SBChargingAlertElement setVerticalLimitedSizeLeadingConstraints:];
-[SBChargingAlertElement setVerticalLimitedSizeTrailingConstraints:];
-[SBChargingAlertElement trailingBatteryIconPackageView];
-[SBChargingAlertElement trailingBatteryLabel];
-[SBChargingAlertElement verticalLimitedSizeLeadingConstraints];
-[SBChargingAlertElement verticalLimitedSizeTrailingConstraints];
```
