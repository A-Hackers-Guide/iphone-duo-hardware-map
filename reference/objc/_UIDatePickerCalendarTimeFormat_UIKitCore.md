# `_UIDatePickerCalendarTimeFormat`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 19 instance variables, 19 properties, 28 instance methods, 2 class methods

## Instance variables

```
B _wantsDoubleDigitHours;
B _forceDoubleDigitHours;
B _hasLeadingLiteral;
B _hasTrailingLiteral;
B _displaysTimeZone;
@"NSString" _timeFormat;
@"NSString" _hourFormat;
@"NSString" _dayPeriodFormat;
@"NSArray" _dayPeriods;
@"NSDictionary" _dayPeriodsRanges;
q _clock;
q _clockLayout;
@"NSNumberFormatter" _hourFormatter;
@"NSNumberFormatter" _minuteFormatter;
@"NSString" _extendedHoursFormat;
@"NSNumberFormatter" _strictHourFormatter;
@"NSDate" _timeZoneReferenceDate;
@"NSTimeZone" _timeZone;
@"NSLocale" _locale;
```

## Properties

```
@property (T@"NSString",R,N,V_timeFormat) timeFormat;
@property (T@"NSString",R,N,V_hourFormat) hourFormat;
@property (T@"NSString",R,N,V_dayPeriodFormat) dayPeriodFormat;
@property (T@"NSArray",R,N,V_dayPeriods) dayPeriods;
@property (T@"NSDictionary",R,N,V_dayPeriodsRanges) dayPeriodsRanges;
@property (TB,R,N,V_wantsDoubleDigitHours) wantsDoubleDigitHours;
@property (TB,R,N,V_forceDoubleDigitHours) forceDoubleDigitHours;
@property (Tq,R,N,V_clock) clock;
@property (Tq,R,N,V_clockLayout) clockLayout;
@property (TB,R,N,V_hasLeadingLiteral) hasLeadingLiteral;
@property (TB,R,N,V_hasTrailingLiteral) hasTrailingLiteral;
@property (T@"NSNumberFormatter",R,N,V_hourFormatter) hourFormatter;
@property (T@"NSNumberFormatter",R,N,V_minuteFormatter) minuteFormatter;
@property (T@"NSString",R,N,V_extendedHoursFormat) extendedHoursFormat;
@property (T@"NSNumberFormatter",R,N,V_strictHourFormatter) strictHourFormatter;
@property (T@"NSDate",&,N,V_timeZoneReferenceDate) timeZoneReferenceDate;
@property (T@"NSTimeZone",R,N,V_timeZone) timeZone;
@property (T@"NSLocale",R,N,V_locale) locale;
@property (TB,R,N,V_displaysTimeZone) displaysTimeZone;
```

## Class methods

```
+[_UIDatePickerCalendarTimeFormat formatWithCalendar:locale:];
+[_UIDatePickerCalendarTimeFormat formatWithCalendar:locale:followsSystemHourCycle:];
```

## Instance methods

```
-[_UIDatePickerCalendarTimeFormat clock];
-[_UIDatePickerCalendarTimeFormat timeZone];
-[_UIDatePickerCalendarTimeFormat locale];
-[_UIDatePickerCalendarTimeFormat timeFormat];
-[_UIDatePickerCalendarTimeFormat copyWithZone:];
-[_UIDatePickerCalendarTimeFormat minuteFormatter];
-[_UIDatePickerCalendarTimeFormat dayPeriodFormat];
-[_UIDatePickerCalendarTimeFormat initWithCalendar:locale:forceDoubleDigitHours:displaysTimeZone:];
-[_UIDatePickerCalendarTimeFormat clockLayout];
-[_UIDatePickerCalendarTimeFormat dayPeriods];
-[_UIDatePickerCalendarTimeFormat dayPeriodsRanges];
-[_UIDatePickerCalendarTimeFormat displaysTimeZone];
-[_UIDatePickerCalendarTimeFormat extendedHoursFormat];
-[_UIDatePickerCalendarTimeFormat forceDoubleDigitHours];
-[_UIDatePickerCalendarTimeFormat hasLeadingLiteral];
-[_UIDatePickerCalendarTimeFormat hasTrailingLiteral];
-[_UIDatePickerCalendarTimeFormat hourFormat];
-[_UIDatePickerCalendarTimeFormat hourFormatter];
-[_UIDatePickerCalendarTimeFormat initWithCalendar:locale:followsSystemHourCycle:forceDoubleDigitHours:displaysTimeZone:];
-[_UIDatePickerCalendarTimeFormat localizedTimeStringWithHours:minutes:dayPeriod:];
-[_UIDatePickerCalendarTimeFormat localizedTimeStringWithHours:minutes:dayPeriod:ranges:];
-[_UIDatePickerCalendarTimeFormat setTimeZoneReferenceDate:];
-[_UIDatePickerCalendarTimeFormat strictHourFormatter];
-[_UIDatePickerCalendarTimeFormat timeZoneReferenceDate];
-[_UIDatePickerCalendarTimeFormat wantsDoubleDigitHours];
-[_UIDatePickerCalendarTimeFormat withDisplaysTimeZone:];
-[_UIDatePickerCalendarTimeFormat withForceDoubleDigitHours:];
-[_UIDatePickerCalendarTimeFormat withTimeZone:];
```
