# `DBSColorTemperatureController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `PSTimeRangeCellDelegate`
- 10 instance variables, 5 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"NSDateFormatter" _timeFormatter;
B _temperatureSliderWasTracking;
@"NSTimer" _blueLightReductionLabelRefreshTimer;
B _showColorTemperature;
B _showingScheduleRange;
@"CBClient" __brightnessClient;
@"PSSpecifier" __scheduleRangeSpecifier;
@"PSSpecifier" __scheduleSwitchSpecifier;
@"PSSpecifier" __manualSwitchSpecifier;
@"PSSpecifier" __temperatureSlider;
```

## Properties

```
@property (T@"CBClient",&,N,V__brightnessClient) _brightnessClient;
@property (T@"PSSpecifier",&,N,V__scheduleRangeSpecifier) _scheduleRangeSpecifier;
@property (T@"PSSpecifier",&,N,V__scheduleSwitchSpecifier) _scheduleSwitchSpecifier;
@property (T@"PSSpecifier",&,N,V__manualSwitchSpecifier) _manualSwitchSpecifier;
@property (T@"PSSpecifier",&,N,V__temperatureSlider) _temperatureSlider;
```

## Instance methods

```
-[DBSColorTemperatureController dealloc];
-[DBSColorTemperatureController initWithNibName:bundle:];
-[DBSColorTemperatureController viewDidAppear:];
-[DBSColorTemperatureController specifiers];
-[DBSColorTemperatureController fromDetailForCell:];
-[DBSColorTemperatureController toDetailForCell:];
-[DBSColorTemperatureController colorTemperatureSliderDidChange];
-[DBSColorTemperatureController _brightnessClient];
-[DBSColorTemperatureController _manualSwitchSpecifier];
-[DBSColorTemperatureController _printBlueLightStatus:];
-[DBSColorTemperatureController _scheduleRangeSpecifier];
-[DBSColorTemperatureController _scheduleSwitchSpecifier];
-[DBSColorTemperatureController _setBlueLightReductionEnabled:forSpecifier:];
-[DBSColorTemperatureController _temperatureSlider];
-[DBSColorTemperatureController blueLightReductionFooter];
-[DBSColorTemperatureController getBlueLightReductionManualEnabled:];
-[DBSColorTemperatureController getBlueLightReductionScheduleEnabled:];
-[DBSColorTemperatureController handleBlueLightStatusChanged:];
-[DBSColorTemperatureController localizedTimeForTime:];
-[DBSColorTemperatureController setBlueLightReductionManualEnabled:forSpecifier:];
-[DBSColorTemperatureController setBlueLightReductionSchedule:forSpecifier:];
-[DBSColorTemperatureController setTemperatureStrength:specifier:];
-[DBSColorTemperatureController set_brightnessClient:];
-[DBSColorTemperatureController set_manualSwitchSpecifier:];
-[DBSColorTemperatureController set_scheduleRangeSpecifier:];
-[DBSColorTemperatureController set_scheduleSwitchSpecifier:];
-[DBSColorTemperatureController set_temperatureSlider:];
-[DBSColorTemperatureController showAlertToDisableAccessibilityFiltersForBlueLightReduction:cancel:];
-[DBSColorTemperatureController showScheduleRange:animated:];
-[DBSColorTemperatureController temperatureStrength:];
```
