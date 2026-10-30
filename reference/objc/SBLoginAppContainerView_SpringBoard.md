# `SBLoginAppContainerView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _contentHiddenRequesters;
@"UIView" _contentView;
@"CSBatteryChargingView" _batteryChargingView;
@"SBLoginAppContainerOverlayWrapperView" _thermalWarningView;
@"SBLockScreenDeviceInformationTextView" _deviceInformationTextView;
@"UIView" _pluginView;
@"_UILegibilitySettings" _legibilitySettings;
```

## Properties

```
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"CSBatteryChargingView",&,N,V_batteryChargingView) batteryChargingView;
@property (T@"SBLoginAppContainerOverlayWrapperView",&,N,V_thermalWarningView) thermalWarningView;
@property (T@"SBLockScreenDeviceInformationTextView",&,N,V_deviceInformationTextView) deviceInformationTextView;
@property (T@"UIView",&,N,V_pluginView) pluginView;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
```

## Instance methods

```
-[SBLoginAppContainerView setContentView:];
-[SBLoginAppContainerView layoutSubviews];
-[SBLoginAppContainerView contentView];
-[SBLoginAppContainerView legibilitySettings];
-[SBLoginAppContainerView setLegibilitySettings:];
-[SBLoginAppContainerView initWithFrame:];
-[SBLoginAppContainerView pluginView];
-[SBLoginAppContainerView setPluginView:];
-[SBLoginAppContainerView batteryChargingView];
-[SBLoginAppContainerView setBatteryChargingView:];
-[SBLoginAppContainerView _showOrHidePluginViewAppropriately];
-[SBLoginAppContainerView deviceInformationTextView];
-[SBLoginAppContainerView setContentHidden:forRequester:];
-[SBLoginAppContainerView setDeviceInformationTextView:];
-[SBLoginAppContainerView setThermalWarningView:];
-[SBLoginAppContainerView thermalWarningView];
```
