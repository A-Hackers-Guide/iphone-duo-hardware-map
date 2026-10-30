# `_UIDatePickerDataModel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 20 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"NSLocale" _effectiveLocale;
@"NSCalendar" _effectiveCalendar;
@"_UIDatePickerChineseCalendar" _chineseWrapperCalendar;
@"NSCalendar" _lastSelectedDateComponentsCalendar;
B _roundsToMinuteInterval;
q _datePickerStyle;
q _datePickerMode;
@"NSLocale" _locale;
@"NSCalendar" _calendar;
@"NSTimeZone" _timeZone;
@"NSDate" _date;
@"NSDateComponents" _lastSelectedDateComponents;
@"_UIDatePickerDateRange" _dateRange;
q _minuteInterval;
@"NSString" _customFontDesign;
@"UIColor" _customTextColor;
```

## Properties

```
@property (Tq,N,V_datePickerStyle) datePickerStyle;
@property (Tq,N,V_datePickerMode) datePickerMode;
@property (T@"NSLocale",&,N,V_locale) locale;
@property (T@"NSCalendar",C,N,V_calendar) calendar;
@property (T@"NSLocale",R,N) effectiveLocale;
@property (T@"NSCalendar",R,N) effectiveCalendar;
@property (T@"NSCalendar",R,N) formattingCalendar;
@property (T@"NSTimeZone",&,N,V_timeZone) timeZone;
@property (T@"NSDate",&,N,V_date) date;
@property (T@"NSDateComponents",&,N,V_lastSelectedDateComponents) lastSelectedDateComponents;
@property (T@"NSDate",R,N) effectiveDate;
@property (T@"_UIDatePickerDateRange",R,N,V_dateRange) dateRange;
@property (T@"NSDateComponents",R,C,N) effectiveDateComponents;
@property (T@"NSDate",&,N) minimumDate;
@property (T@"NSDate",&,N) maximumDate;
@property (Tq,N,V_minuteInterval) minuteInterval;
@property (TB,N,V_roundsToMinuteInterval) roundsToMinuteInterval;
@property (TB,R,N) followsSystemHourCycle;
@property (T@"NSString",&,N,V_customFontDesign) customFontDesign;
@property (T@"UIColor",&,N,V_customTextColor) customTextColor;
```

## Instance methods

```
-[_UIDatePickerDataModel effectiveDate];
-[_UIDatePickerDataModel setTimeZone:];
-[_UIDatePickerDataModel setCalendar:];
-[_UIDatePickerDataModel effectiveCalendar];
-[_UIDatePickerDataModel _setupDerivedLocaleAndCalendars];
-[_UIDatePickerDataModel resetForCurrentLocaleOrCalendarChange];
-[_UIDatePickerDataModel formattingCalendar];
-[_UIDatePickerDataModel setDatePickerStyle:];
-[_UIDatePickerDataModel setMinuteInterval:];
-[_UIDatePickerDataModel setDate:];
-[_UIDatePickerDataModel init];
-[_UIDatePickerDataModel createDatePickerRepresentingDataModelForMode:style:];
-[_UIDatePickerDataModel datePickerStyle];
-[_UIDatePickerDataModel setLocale:];
-[_UIDatePickerDataModel setCustomTextColor:];
-[_UIDatePickerDataModel roundsToMinuteInterval];
-[_UIDatePickerDataModel calendar];
-[_UIDatePickerDataModel effectiveDateComponents];
-[_UIDatePickerDataModel date];
-[_UIDatePickerDataModel timeZone];
-[_UIDatePickerDataModel customFontDesign];
-[_UIDatePickerDataModel _dateForRoundingDateToMinuteInterval:];
-[_UIDatePickerDataModel locale];
-[_UIDatePickerDataModel createDatePickerRepresentingDataModel];
-[_UIDatePickerDataModel minimumDate];
-[_UIDatePickerDataModel minuteInterval];
-[_UIDatePickerDataModel followsSystemHourCycle];
-[_UIDatePickerDataModel setDatePickerMode:];
-[_UIDatePickerDataModel lastSelectedDateComponents];
-[_UIDatePickerDataModel dateRange];
-[_UIDatePickerDataModel setMaximumDate:];
-[_UIDatePickerDataModel customTextColor];
-[_UIDatePickerDataModel setMinimumDate:];
-[_UIDatePickerDataModel effectiveLocale];
-[_UIDatePickerDataModel setCustomFontDesign:];
-[_UIDatePickerDataModel datePickerMode];
-[_UIDatePickerDataModel setRoundsToMinuteInterval:];
-[_UIDatePickerDataModel setLastSelectedDateComponents:];
-[_UIDatePickerDataModel maximumDate];
```
