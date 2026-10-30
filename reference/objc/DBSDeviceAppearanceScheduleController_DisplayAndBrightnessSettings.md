# `DBSDeviceAppearanceScheduleController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `PSDateTimePickerCellDelegate`
- 9 instance variables, 9 properties, 29 instance methods, 0 class methods

## Instance variables

```
B __showingScheduleSpecifiers;
@"PSSpecifier" __radioGroup;
@"PSSpecifier" __timeGroup;
@"PSSpecifier" __lightAppearanceTimePickerSpecifier;
@"PSSpecifier" __darkAppearanceTimePickerSpecifier;
@"UISUserInterfaceStyleMode" __styleMode;
@"NSDateFormatter" __timeFormatter;
@"UIDatePicker" __lightAppearanceTimePicker;
@"UIDatePicker" __darkAppearanceTimePicker;
```

## Properties

```
@property (T@"PSSpecifier",&,N,V__radioGroup) _radioGroup;
@property (T@"PSSpecifier",&,N,V__timeGroup) _timeGroup;
@property (T@"PSSpecifier",&,N,V__lightAppearanceTimePickerSpecifier) _lightAppearanceTimePickerSpecifier;
@property (T@"PSSpecifier",&,N,V__darkAppearanceTimePickerSpecifier) _darkAppearanceTimePickerSpecifier;
@property (TB,N,V__showingScheduleSpecifiers) _showingScheduleSpecifiers;
@property (T@"UISUserInterfaceStyleMode",W,N,V__styleMode) _styleMode;
@property (T@"NSDateFormatter",&,N,V__timeFormatter) _timeFormatter;
@property (T@"UIDatePicker",&,N,V__lightAppearanceTimePicker) _lightAppearanceTimePicker;
@property (T@"UIDatePicker",&,N,V__darkAppearanceTimePicker) _darkAppearanceTimePicker;
```

## Instance methods

```
-[DBSDeviceAppearanceScheduleController willResignActive];
-[DBSDeviceAppearanceScheduleController initWithNibName:bundle:];
-[DBSDeviceAppearanceScheduleController setSpecifier:];
-[DBSDeviceAppearanceScheduleController _timeFormatter];
-[DBSDeviceAppearanceScheduleController viewDidAppear:];
-[DBSDeviceAppearanceScheduleController tableView:didSelectRowAtIndexPath:];
-[DBSDeviceAppearanceScheduleController specifiers];
-[DBSDeviceAppearanceScheduleController datePickerChanged:];
-[DBSDeviceAppearanceScheduleController datePickerForSpecifier:];
-[DBSDeviceAppearanceScheduleController set_radioGroup:];
-[DBSDeviceAppearanceScheduleController _darkAppearanceTimePicker];
-[DBSDeviceAppearanceScheduleController _darkAppearanceTimePickerSpecifier];
-[DBSDeviceAppearanceScheduleController _darkAppearanceTimeString];
-[DBSDeviceAppearanceScheduleController _lightAppearanceTimePicker];
-[DBSDeviceAppearanceScheduleController _lightAppearanceTimePickerSpecifier];
-[DBSDeviceAppearanceScheduleController _lightAppearanceTimeString];
-[DBSDeviceAppearanceScheduleController _radioGroup];
-[DBSDeviceAppearanceScheduleController _showingScheduleSpecifiers];
-[DBSDeviceAppearanceScheduleController _styleMode];
-[DBSDeviceAppearanceScheduleController _timeGroup];
-[DBSDeviceAppearanceScheduleController set_darkAppearanceTimePicker:];
-[DBSDeviceAppearanceScheduleController set_darkAppearanceTimePickerSpecifier:];
-[DBSDeviceAppearanceScheduleController set_lightAppearanceTimePicker:];
-[DBSDeviceAppearanceScheduleController set_lightAppearanceTimePickerSpecifier:];
-[DBSDeviceAppearanceScheduleController set_showingScheduleSpecifiers:];
-[DBSDeviceAppearanceScheduleController set_styleMode:];
-[DBSDeviceAppearanceScheduleController set_timeFormatter:];
-[DBSDeviceAppearanceScheduleController set_timeGroup:];
-[DBSDeviceAppearanceScheduleController showScheduleSpecifiers:animated:];
```
