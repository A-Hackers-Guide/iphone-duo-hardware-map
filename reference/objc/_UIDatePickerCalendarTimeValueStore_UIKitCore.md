# `_UIDatePickerCalendarTimeValueStore`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _timeOfDayChangesPerPeriod;
Q _dayPeriod;
q _minuteInterval;
q _decrementBehaviour;
^Q _inputBuffer;
@"_UIDatePickerCalendarTimeFormat" _timeFormat;
```

## Properties

```
@property (T^Q,R,N,V_inputBuffer) inputBuffer;
@property (T@"_UIDatePickerCalendarTimeFormat",R,N,V_timeFormat) timeFormat;
@property (TB,N,V_timeOfDayChangesPerPeriod) timeOfDayChangesPerPeriod;
@property (TQ,N) hourValue;
@property (TQ,N) minuteValue;
@property (TQ,N,V_dayPeriod) dayPeriod;
@property (Tq,N,V_minuteInterval) minuteInterval;
@property (Tq,N,V_decrementBehaviour) decrementBehaviour;
```

## Instance methods

```
-[_UIDatePickerCalendarTimeValueStore setDecrementBehaviour:];
-[_UIDatePickerCalendarTimeValueStore dayPeriod];
-[_UIDatePickerCalendarTimeValueStore __integerInBufferWithRange:];
-[_UIDatePickerCalendarTimeValueStore setMinuteInterval:];
-[_UIDatePickerCalendarTimeValueStore setMinuteValue:];
-[_UIDatePickerCalendarTimeValueStore setDayPeriod:];
-[_UIDatePickerCalendarTimeValueStore inputBuffer];
-[_UIDatePickerCalendarTimeValueStore digitsInScope:];
-[_UIDatePickerCalendarTimeValueStore setHourValue:];
-[_UIDatePickerCalendarTimeValueStore dealloc];
-[_UIDatePickerCalendarTimeValueStore hourValue];
-[_UIDatePickerCalendarTimeValueStore minuteValue];
-[_UIDatePickerCalendarTimeValueStore updateTimeOfDayPeriodIncrease:];
-[_UIDatePickerCalendarTimeValueStore __setIntegerInBuffer:range:];
-[_UIDatePickerCalendarTimeValueStore roundToMinuteInterval];
-[_UIDatePickerCalendarTimeValueStore _verifyInputWithScope:];
-[_UIDatePickerCalendarTimeValueStore initWithTimeFormat:minuteInterval:decrementBehaviour:];
-[_UIDatePickerCalendarTimeValueStore _removeLastDigitInRange:];
-[_UIDatePickerCalendarTimeValueStore setTimeOfDayChangesPerPeriod:];
-[_UIDatePickerCalendarTimeValueStore incrementDigitForScope:];
-[_UIDatePickerCalendarTimeValueStore timeFormat];
-[_UIDatePickerCalendarTimeValueStore minuteInterval];
-[_UIDatePickerCalendarTimeValueStore decrementBehaviour];
-[_UIDatePickerCalendarTimeValueStore decrementDigitForScope:];
-[_UIDatePickerCalendarTimeValueStore timeOfDayChangesPerPeriod];
-[_UIDatePickerCalendarTimeValueStore _setDigits:count:inRange:append:];
-[_UIDatePickerCalendarTimeValueStore setDigits:count:inScope:append:];
-[_UIDatePickerCalendarTimeValueStore removeLastDigitInScope:];
-[_UIDatePickerCalendarTimeValueStore toggleTimeOfDay];
-[_UIDatePickerCalendarTimeValueStore initWithTimeFormat:];
```
