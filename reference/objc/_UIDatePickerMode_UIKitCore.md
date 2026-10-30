# `_UIDatePickerMode`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 27 instance variables, 28 properties, 110 instance methods, 6 class methods

## Instance variables

```
@"NSDateComponents" _selectedDateComponents;
@"NSDateComponents" _baseDateComponents;
^Q _elements;
q _yearsSinceBaseDate;
{_NSRange="location"Q"length"Q} _maxDayRange;
{_NSRange="location"Q"length"Q} _maxMonthRange;
@"NSString" _localizedFormatString;
@"NSArray" _dateFormatters;
@"UIColor" _todayTextColor;
@"UIFont" _amPmFont;
@"UIFont" _font;
@"UIFont" _defaultTimeFont;
@"NSDictionary" _dayPeriodsRanges;
@"NSArray" _dayPeriods;
@"NSDateComponents" _todayDateComponents;
@"NSNumberFormatter" _formatter;
@"_UIDatePickerView" _datePickerView;
B _isUsingJapaneseCalendar;
Q _numberOfComponents;
q _minuteInterval;
d _todaySinceReferenceDate;
@"NSDate" _minimumDate;
@"NSDateComponents" _minimumDateComponents;
@"NSDate" _maximumDate;
@"NSDateComponents" _maximumDateComponents;
@"NSDate" _baseDate;
@"NSDate" _originatingDate;
```

## Properties

```
@property (T@"_UIDatePickerView",W,N,V_datePickerView) datePickerView;
@property (T@"UIFont",R,N) amPmFont;
@property (T@"UIFont",R,N) font;
@property (T@"UIFont",R,N) defaultTimeFont;
@property (T@"UIFont",R,N) sizedFont;
@property (TQ,N,V_numberOfComponents) numberOfComponents;
@property (T^Q,N) elements;
@property (T@"NSString",&,N,V_localizedFormatString) localizedFormatString;
@property (T@"NSDate",&,N,V_baseDate) baseDate;
@property (T@"NSDateComponents",&,N) baseDateComponents;
@property (Tq,N,V_yearsSinceBaseDate) yearsSinceBaseDate;
@property (T@"NSDate",&,N,V_originatingDate) originatingDate;
@property (T@"NSDateComponents",&,N,V_selectedDateComponents) selectedDateComponents;
@property (Tq,R,N) datePickerMode;
@property (Td,R,N) rowHeight;
@property (Tq,R,N) displayedCalendarUnits;
@property (T@"UIColor",R,N) todayTextColor;
@property (Tq,N,V_minuteInterval) minuteInterval;
@property (T@"NSDateComponents",&,N) todayDateComponents;
@property (Td,N,V_todaySinceReferenceDate) todaySinceReferenceDate;
@property (T@"NSDate",R,N,V_minimumDate) minimumDate;
@property (T@"NSDateComponents",R,N,V_minimumDateComponents) minimumDateComponents;
@property (T@"NSDate",R,N,V_maximumDate) maximumDate;
@property (T@"NSDateComponents",R,N,V_maximumDateComponents) maximumDateComponents;
@property (TB,R,N) hasSelectedDateComponents;
@property (Td,R,D,N) totalComponentWidth;
@property (TB,R,D,N,Gis24Hour) is24Hour;
@property (TB,R,D,N,GisTimeIntervalMode) isTimeIntervalMode;
```

## Class methods

```
+[_UIDatePickerMode initialize];
+[_UIDatePickerMode datePickerMode];
+[_UIDatePickerMode _datePickerModeWithFormatString:datePickerView:];
+[_UIDatePickerMode _datePickerModeWithMode:datePickerView:];
+[_UIDatePickerMode extractableCalendarUnits];
+[_UIDatePickerMode newDateFromGregorianYear:month:day:timeZone:];
```

## Instance methods

```
-[_UIDatePickerMode setElements:];
-[_UIDatePickerMode nextUnitLargerThanUnit:];
-[_UIDatePickerMode setMinuteInterval:];
-[_UIDatePickerMode elements];
-[_UIDatePickerMode viewForRow:inComponent:reusingView:];
-[_UIDatePickerMode dateFormatForCalendarUnit:];
-[_UIDatePickerMode init];
-[_UIDatePickerMode dealloc];
-[_UIDatePickerMode widthForCalendarUnit:font:maxWidth:];
-[_UIDatePickerMode calendar];
-[_UIDatePickerMode rowForDate:dateComponents:component:currentRow:];
-[_UIDatePickerMode timeZone];
-[_UIDatePickerMode loadDate:animated:];
-[_UIDatePickerMode _shouldReset:];
-[_UIDatePickerMode nextUnitSmallerThanUnit:];
-[_UIDatePickerMode locale];
-[_UIDatePickerMode minimumDate];
-[_UIDatePickerMode minuteInterval];
-[_UIDatePickerMode baseDateComponents];
-[_UIDatePickerMode followsSystemHourCycle];
-[_UIDatePickerMode localizedFormatString];
-[_UIDatePickerMode rowHeight];
-[_UIDatePickerMode _shouldEnableValueForRow:inComponent:calendarUnit:];
-[_UIDatePickerMode _style];
-[_UIDatePickerMode numberOfRowsForCalendarUnit:];
-[_UIDatePickerMode titleForRow:inComponent:];
-[_UIDatePickerMode noteCalendarChanged];
-[_UIDatePickerMode dateForRow:inCalendarUnit:];
-[_UIDatePickerMode font];
-[_UIDatePickerMode updateEnabledStateOfViewForRow:inComponent:];
-[_UIDatePickerMode datePickerMode];
-[_UIDatePickerMode maximumDate];
-[_UIDatePickerMode numberOfComponents];
-[_UIDatePickerMode resetComponentWidths];
-[_UIDatePickerMode displayedCalendarUnits];
-[_UIDatePickerMode defaultTimeFont];
-[_UIDatePickerMode originatingDate];
-[_UIDatePickerMode _createDayPeriodsIfNeeded];
-[_UIDatePickerMode _dateByEnsuringValue:forCalendarUnit:];
-[_UIDatePickerMode _dateForYearRow:];
-[_UIDatePickerMode _incrementForStaggeredTimeIntervals];
-[_UIDatePickerMode _isComponentScrolling:];
-[_UIDatePickerMode _monthExists:inYear:];
-[_UIDatePickerMode _numberOfDaysInDateComponents:];
-[_UIDatePickerMode _scrollingAnyColumnExcept:];
-[_UIDatePickerMode _shouldEnableValueForRow:column:];
-[_UIDatePickerMode _updateSelectedDateComponentsWithNewValueInComponent:usingSelectionBarValue:];
-[_UIDatePickerMode _yearlessYearForMonth:];
-[_UIDatePickerMode amPmFont];
-[_UIDatePickerMode amPmValueForDayPeriodValue:hour:];
-[_UIDatePickerMode areValidDateComponents:comparingUnits:];
-[_UIDatePickerMode baseDate];
-[_UIDatePickerMode calendarForFormatters];
-[_UIDatePickerMode calendarUnitForComponent:];
-[_UIDatePickerMode clearBaseDate];
-[_UIDatePickerMode componentForCalendarUnit:];
-[_UIDatePickerMode componentWidthForTwoDigitCalendarUnit:font:maxWidth:];
-[_UIDatePickerMode dateComponentsByRestrictingSelectedComponents:withLastManipulatedColumn:];
-[_UIDatePickerMode dateFormatterForCalendarUnit:];
-[_UIDatePickerMode datePickerView];
-[_UIDatePickerMode dayForRow:];
-[_UIDatePickerMode dayPeriodForHour:];
-[_UIDatePickerMode dayPeriods];
-[_UIDatePickerMode dayPeriodsRanges];
-[_UIDatePickerMode eraForYearRow:];
-[_UIDatePickerMode fixUpElementsForRTL];
-[_UIDatePickerMode fontForCalendarUnit:];
-[_UIDatePickerMode hasSelectedDateComponents];
-[_UIDatePickerMode hourForRow:];
-[_UIDatePickerMode invalidateTodayTextColor];
-[_UIDatePickerMode is24Hour];
-[_UIDatePickerMode isTimeIntervalMode];
-[_UIDatePickerMode maximumDateComponents];
-[_UIDatePickerMode maximumDayPeriodWidth];
-[_UIDatePickerMode minimumDateComponents];
-[_UIDatePickerMode minuteForRow:];
-[_UIDatePickerMode monthForRow:];
-[_UIDatePickerMode numberOfRowsInComponent:];
-[_UIDatePickerMode rangeForCalendarUnit:];
-[_UIDatePickerMode resetSelectedDateComponentsWithValuesUnderSelectionBars];
-[_UIDatePickerMode rowForValue:forCalendarUnit:currentRow:];
-[_UIDatePickerMode secondForRow:];
-[_UIDatePickerMode selectedDateComponents];
-[_UIDatePickerMode setBaseDate:];
-[_UIDatePickerMode setBaseDateComponents:];
-[_UIDatePickerMode setDatePickerView:];
-[_UIDatePickerMode setLocalizedFormatString:];
-[_UIDatePickerMode setNumberOfComponents:];
-[_UIDatePickerMode setOriginatingDate:];
-[_UIDatePickerMode setSelectedDateComponents:];
-[_UIDatePickerMode setTodayDateComponents:];
-[_UIDatePickerMode setTodaySinceReferenceDate:];
-[_UIDatePickerMode setYearsSinceBaseDate:];
-[_UIDatePickerMode sizedFont];
-[_UIDatePickerMode titleAlignmentForCalendarUnit:];
-[_UIDatePickerMode todayDateComponents];
-[_UIDatePickerMode todaySinceReferenceDate];
-[_UIDatePickerMode todayTextColor];
-[_UIDatePickerMode totalComponentWidth];
-[_UIDatePickerMode totalComponentWidthWithFont:];
-[_UIDatePickerMode updateDateForNewDateRange];
-[_UIDatePickerMode updateSelectedDateComponentsWithNewValueInComponent:];
-[_UIDatePickerMode updatedDayPeriodIndexForHour:oldHour:selectedDayPeriodValue:];
-[_UIDatePickerMode updatedHourRowForDayPeriodValue:oldDayPeriodValue:selectedHourRow:];
-[_UIDatePickerMode validateValue:forCalendarUnit:];
-[_UIDatePickerMode valueForDate:dateComponents:calendarUnit:];
-[_UIDatePickerMode valueForRow:inCalendarUnit:];
-[_UIDatePickerMode widthForComponent:maxWidth:];
-[_UIDatePickerMode yearForRow:];
-[_UIDatePickerMode yearsSinceBaseDate];
```
