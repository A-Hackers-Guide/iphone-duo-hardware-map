# `SBLowBatteryAlertElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAlertProvidedContentElement`
- Protocols: `SBSystemApertureContextProviding`
- 9 instance variables, 20 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"UIColor" _keyColor;
B _lowPowerModeEnabled;
d _batteryPercentage;
Q _style;
@"BSUICAPackageView" _trailingLowBatteryStyleIconPackageView;
@"BSUICAPackageView" _minimalBatteryIconPackageView;
@"SBUISystemApertureTextContentProvider" _secondaryContent;
@? _action;
@"NSTimer" _dismissalTimer;
```

## Properties

```
@property (TQ,N,V_style) style;
@property (TB,N,GisLowPowerModeEnabled,V_lowPowerModeEnabled) lowPowerModeEnabled;
@property (T@"BSUICAPackageView",&,N,V_trailingLowBatteryStyleIconPackageView) trailingLowBatteryStyleIconPackageView;
@property (T@"BSUICAPackageView",&,N,V_minimalBatteryIconPackageView) minimalBatteryIconPackageView;
@property (T@"SBUISystemApertureTextContentProvider",&,N,V_secondaryContent) secondaryContent;
@property (T@?,C,N,V_action) action;
@property (T@"NSTimer",&,N,V_dismissalTimer) dismissalTimer;
@property (Td,N,V_batteryPercentage) batteryPercentage;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLowBatteryAlertElement keyColor];
-[SBLowBatteryAlertElement isLowPowerModeEnabled];
-[SBLowBatteryAlertElement preferredAlertingDuration:];
-[SBLowBatteryAlertElement dealloc];
-[SBLowBatteryAlertElement handleElementViewEvent:];
-[SBLowBatteryAlertElement setAction:];
-[SBLowBatteryAlertElement action];
-[SBLowBatteryAlertElement setBatteryPercentage:];
-[SBLowBatteryAlertElement supportsLimitedSize];
-[SBLowBatteryAlertElement style];
-[SBLowBatteryAlertElement batteryPercentage];
-[SBLowBatteryAlertElement setStyle:];
-[SBLowBatteryAlertElement shouldSuppressElementWhileProximityReaderPresent];
-[SBLowBatteryAlertElement setLowPowerModeEnabled:];
-[SBLowBatteryAlertElement dismissalTimer];
-[SBLowBatteryAlertElement setDismissalTimer:];
-[SBLowBatteryAlertElement _extendDismissalTimer];
-[SBLowBatteryAlertElement _prefersLargeScreenMetrics];
-[SBLowBatteryAlertElement _primaryTextFontSize];
-[SBLowBatteryAlertElement _secondaryTextColorForStyle];
-[SBLowBatteryAlertElement _secondaryTextForStyle];
-[SBLowBatteryAlertElement _updateBatteryContent];
-[SBLowBatteryAlertElement _updateLowPowerMode];
-[SBLowBatteryAlertElement customEdgeSpacing];
-[SBLowBatteryAlertElement dodgeSensorAreaOnIntrinsicContentSize];
-[SBLowBatteryAlertElement horizontalSpacingBetweenLeadingAndCenter];
-[SBLowBatteryAlertElement horizontalSpacingBetweenTrailingAndCenter];
-[SBLowBatteryAlertElement initWithIdentifier:style:batteryPercentage:lowPowerModeEnabled:action:];
-[SBLowBatteryAlertElement minimalBatteryIconPackageView];
-[SBLowBatteryAlertElement secondaryContent];
-[SBLowBatteryAlertElement setMinimalBatteryIconPackageView:];
-[SBLowBatteryAlertElement setSecondaryContent:];
-[SBLowBatteryAlertElement setTrailingLowBatteryStyleIconPackageView:];
-[SBLowBatteryAlertElement trailingLowBatteryStyleIconPackageView];
-[SBLowBatteryAlertElement verticalItemSpacing];
-[SBLowBatteryAlertElement verticalSpacingBetweenPrimaryAndSecondary];
```
