# `_UICalendarDataModel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 9 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSCalendar" _effectiveCalendar;
@"NSLocale" _effectiveLocale;
@"NSLocale" _locale;
@"NSCalendar" _calendar;
@"NSTimeZone" _timeZone;
@"_UIDatePickerCalendarMonth" _visibleMonth;
@"NSDateInterval" _availableDateRange;
@"NSString" _fontDesign;
```

## Properties

```
@property (T@"NSLocale",C,N,V_locale) locale;
@property (T@"NSCalendar",C,N,V_calendar) calendar;
@property (T@"NSTimeZone",&,N,V_timeZone) timeZone;
@property (T@"NSCalendar",R,N,V_effectiveCalendar) effectiveCalendar;
@property (T@"NSLocale",R,N,V_effectiveLocale) effectiveLocale;
@property (T@"NSTimeZone",R,N) effectiveTimeZone;
@property (T@"_UIDatePickerCalendarMonth",&,N,V_visibleMonth) visibleMonth;
@property (T@"NSDateInterval",C,N,V_availableDateRange) availableDateRange;
@property (T@"NSString",&,N,V_fontDesign) fontDesign;
```

## Instance methods

```
-[_UICalendarDataModel setTimeZone:];
-[_UICalendarDataModel setCalendar:];
-[_UICalendarDataModel effectiveCalendar];
-[_UICalendarDataModel init];
-[_UICalendarDataModel setLocale:];
-[_UICalendarDataModel calendar];
-[_UICalendarDataModel timeZone];
-[_UICalendarDataModel locale];
-[_UICalendarDataModel effectiveLocale];
-[_UICalendarDataModel _deriveEffectiveLocaleAndCalendarIfNeeded];
-[_UICalendarDataModel availableDateRange];
-[_UICalendarDataModel effectiveTimeZone];
-[_UICalendarDataModel fontDesign];
-[_UICalendarDataModel setAvailableDateRange:];
-[_UICalendarDataModel setFontDesign:];
-[_UICalendarDataModel setVisibleMonth:];
-[_UICalendarDataModel visibleMonth];
```
