# `DBSColorScheduleController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `PSDateTimePickerCellDelegate`
- 11 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"CBClient" _brightnessClient;
@"PSSpecifier" _radioGroup;
@"PSSpecifier" _sunsetToSunriseRadioSpecifier;
@"PSSpecifier" _scheduleRadioSpecifier;
@"PSSpecifier" _timeGroup;
@"PSSpecifier" _startTimePickerSpecifier;
@"PSSpecifier" _endTimePickerSpecifier;
@"NSDateFormatter" _timeFormatter;
B _showingScheduleSpecifiers;
@"UIDatePicker" _startTimePicker;
@"UIDatePicker" _endTimePicker;
```

## Instance methods

```
-[DBSColorScheduleController endTime];
-[DBSColorScheduleController willResignActive];
-[DBSColorScheduleController startTime];
-[DBSColorScheduleController dealloc];
-[DBSColorScheduleController initWithNibName:bundle:];
-[DBSColorScheduleController viewDidAppear:];
-[DBSColorScheduleController tableView:didSelectRowAtIndexPath:];
-[DBSColorScheduleController specifiers];
-[DBSColorScheduleController datePickerChanged:];
-[DBSColorScheduleController datePickerForSpecifier:];
-[DBSColorScheduleController blueLightMode];
-[DBSColorScheduleController handleBlueLightStatusChanged:];
-[DBSColorScheduleController showScheduleSpecifiers:animated:];
```
