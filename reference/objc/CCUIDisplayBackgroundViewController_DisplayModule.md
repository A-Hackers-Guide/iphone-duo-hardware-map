# `CCUIDisplayBackgroundViewController`

- Image: [`/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule`](../userland/System__Library__ControlCenter__Bundles__DisplayModule.bundle__DisplayModule.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CCUISliderModuleBackgroundViewController`
- 9 instance variables, 3 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"CBClient" _brightnessClient;
@"CBAdaptationClient" _trueToneClient;
@"CBBlueLightClient" _nightShiftClient;
{?="active"B"enabled"B"sunSchedulePermitted"B"mode"i"schedule"{?="fromTime"{?="hour"i"minute"i}"toTime"{?="hour"i"minute"i}}"disableFlags"Q"available"B} _currentStatus;
@"UIAlertController" _presentedAlertController;
@"NSMutableArray" _buttons;
@"CCUILabeledRoundButtonViewController" _styleModeButton;
@"CCUILabeledRoundButtonViewController" _nightShiftButton;
@"CCUILabeledRoundButtonViewController" _trueToneButton;
```

## Properties

```
@property (T@"CCUILabeledRoundButtonViewController",&,N,V_styleModeButton) styleModeButton;
@property (T@"CCUILabeledRoundButtonViewController",&,N,V_nightShiftButton) nightShiftButton;
@property (T@"CCUILabeledRoundButtonViewController",&,N,V_trueToneButton) trueToneButton;
```

## Instance methods

```
-[CCUIDisplayBackgroundViewController _updateState];
-[CCUIDisplayBackgroundViewController _subtitleForBlueLightStatus:];
-[CCUIDisplayBackgroundViewController _setupTrueTone];
-[CCUIDisplayBackgroundViewController _nightShiftButtonPressed:];
-[CCUIDisplayBackgroundViewController setNightShiftButton:];
-[CCUIDisplayBackgroundViewController _setupStyleMode];
-[CCUIDisplayBackgroundViewController setStyleModeButton:];
-[CCUIDisplayBackgroundViewController _styleModeButtonPressed:];
-[CCUIDisplayBackgroundViewController _formattedHourForHour:];
-[CCUIDisplayBackgroundViewController dealloc];
-[CCUIDisplayBackgroundViewController _toggleTrueTone];
-[CCUIDisplayBackgroundViewController _toggleStyleMode];
-[CCUIDisplayBackgroundViewController _styleModeDidChange];
-[CCUIDisplayBackgroundViewController _timeStringForHour:minute:];
-[CCUIDisplayBackgroundViewController viewDidLoad];
-[CCUIDisplayBackgroundViewController _setupNightShift];
-[CCUIDisplayBackgroundViewController _formattedHourForTransitionTime:];
-[CCUIDisplayBackgroundViewController _timeStringForBlueLightTransitionTime:];
-[CCUIDisplayBackgroundViewController nightShiftButton];
-[CCUIDisplayBackgroundViewController viewWillAppear:];
-[CCUIDisplayBackgroundViewController _subtitleForUserInterfaceStyle:nextTransition:];
-[CCUIDisplayBackgroundViewController _canShowWhileLocked];
-[CCUIDisplayBackgroundViewController _subtitleFormatStringForBlueLightEnabled:transitionTime:];
-[CCUIDisplayBackgroundViewController _timeFormatter];
-[CCUIDisplayBackgroundViewController trueToneButton];
-[CCUIDisplayBackgroundViewController _trueToneButtonPressed:];
-[CCUIDisplayBackgroundViewController _alertControllerForDisablingAccessibilityScreenFilter:cancelBlock:];
-[CCUIDisplayBackgroundViewController _subtitleForTrueToneEnabled:];
-[CCUIDisplayBackgroundViewController _getBlueLightStatus:];
-[CCUIDisplayBackgroundViewController _toggleNightShift];
-[CCUIDisplayBackgroundViewController _setNightShiftEnabled:];
-[CCUIDisplayBackgroundViewController _uses24HourTime];
-[CCUIDisplayBackgroundViewController styleModeButton];
-[CCUIDisplayBackgroundViewController setTrueToneButton:];
```
