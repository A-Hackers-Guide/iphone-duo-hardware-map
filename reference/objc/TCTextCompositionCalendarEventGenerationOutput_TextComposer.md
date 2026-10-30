# `TCTextCompositionCalendarEventGenerationOutput`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 24 instance variables, 24 properties, 35 instance methods, 1 class methods

## Instance variables

```
B _allDay;
f _duration;
f _fuzzyDuration;
@"NSString" _eventTitle;
@"NSString" _location;
@"NSDictionary" _options;
@"NSDate" _startDate;
@"NSDate" _endDate;
@"NSString" _notes;
@"NSArray" _notesBullets;
@"NSArray" _participants;
@"NSString" _recurrenceRule;
@"NSString" _startDateString;
@"NSString" _startTimeString;
@"NSString" _endDateString;
@"NSString" _endTimeString;
@"NSString" _startDateTZ;
@"NSString" _endDateTZ;
@"NSString" _fuzzyStartDateString;
@"NSString" _fuzzyStartTimeString;
@"NSString" _fuzzyEndDateString;
@"NSString" _fuzzyEndTimeString;
@"NSString" _fuzzyStartDateBound;
@"NSString" _fuzzyEndDateBound;
```

## Properties

```
@property (T@"NSString",R,C,N,V_eventTitle) eventTitle;
@property (T@"NSString",R,C,N,V_location) location;
@property (TB,R,N,V_allDay) allDay;
@property (T@"NSDictionary",R,C,V_options) options;
@property (T@"NSDate",R,C,N,V_startDate) startDate;
@property (T@"NSDate",R,C,N,V_endDate) endDate;
@property (T@"NSString",R,C,N,V_notes) notes;
@property (T@"NSArray",R,C,N,V_notesBullets) notesBullets;
@property (T@"NSArray",R,C,N,V_participants) participants;
@property (T@"NSString",R,C,N,V_recurrenceRule) recurrenceRule;
@property (Tf,R,N,V_duration) duration;
@property (T@"NSString",R,C,N,V_startDateString) startDateString;
@property (T@"NSString",R,C,N,V_startTimeString) startTimeString;
@property (T@"NSString",R,C,N,V_endDateString) endDateString;
@property (T@"NSString",R,C,N,V_endTimeString) endTimeString;
@property (T@"NSString",R,C,N,V_startDateTZ) startDateTZ;
@property (T@"NSString",R,C,N,V_endDateTZ) endDateTZ;
@property (Tf,R,N,V_fuzzyDuration) fuzzyDuration;
@property (T@"NSString",R,C,N,V_fuzzyStartDateString) fuzzyStartDateString;
@property (T@"NSString",R,C,N,V_fuzzyStartTimeString) fuzzyStartTimeString;
@property (T@"NSString",R,C,N,V_fuzzyEndDateString) fuzzyEndDateString;
@property (T@"NSString",R,C,N,V_fuzzyEndTimeString) fuzzyEndTimeString;
@property (T@"NSString",R,C,N,V_fuzzyStartDateBound) fuzzyStartDateBound;
@property (T@"NSString",R,C,N,V_fuzzyEndDateBound) fuzzyEndDateBound;
```

## Class methods

```
+[TCTextCompositionCalendarEventGenerationOutput supportsSecureCoding];
```

## Instance methods

```
-[TCTextCompositionCalendarEventGenerationOutput allDay];
-[TCTextCompositionCalendarEventGenerationOutput startDate];
-[TCTextCompositionCalendarEventGenerationOutput location];
-[TCTextCompositionCalendarEventGenerationOutput endDate];
-[TCTextCompositionCalendarEventGenerationOutput notes];
-[TCTextCompositionCalendarEventGenerationOutput duration];
-[TCTextCompositionCalendarEventGenerationOutput encodeWithCoder:];
-[TCTextCompositionCalendarEventGenerationOutput description];
-[TCTextCompositionCalendarEventGenerationOutput initWithCoder:];
-[TCTextCompositionCalendarEventGenerationOutput options];
-[TCTextCompositionCalendarEventGenerationOutput copyWithZone:];
-[TCTextCompositionCalendarEventGenerationOutput participants];
-[TCTextCompositionCalendarEventGenerationOutput isEqual:];
-[TCTextCompositionCalendarEventGenerationOutput recurrenceRule];
-[TCTextCompositionCalendarEventGenerationOutput eventTitle];
-[TCTextCompositionCalendarEventGenerationOutput startDateString];
-[TCTextCompositionCalendarEventGenerationOutput startTimeString];
-[TCTextCompositionCalendarEventGenerationOutput endDateString];
-[TCTextCompositionCalendarEventGenerationOutput endDateTZ];
-[TCTextCompositionCalendarEventGenerationOutput endTimeString];
-[TCTextCompositionCalendarEventGenerationOutput fuzzyDuration];
-[TCTextCompositionCalendarEventGenerationOutput fuzzyEndDateBound];
-[TCTextCompositionCalendarEventGenerationOutput fuzzyEndDateString];
-[TCTextCompositionCalendarEventGenerationOutput fuzzyEndTimeString];
-[TCTextCompositionCalendarEventGenerationOutput fuzzyStartDateBound];
-[TCTextCompositionCalendarEventGenerationOutput fuzzyStartDateString];
-[TCTextCompositionCalendarEventGenerationOutput fuzzyStartTimeString];
-[TCTextCompositionCalendarEventGenerationOutput initWithEventTitle:location:allDay:participants:recurrenceRule:duration:startDateString:startTimeString:endDateString:endTimeString:startDateTZ:endDateTZ:fuzzyDuration:fuzzyStartDateString:fuzzyStartTimeString:fuzzyEndDateString:fuzzyEndTimeString:options:];
-[TCTextCompositionCalendarEventGenerationOutput initWithEventTitle:location:startDate:endDate:notes:notesBullets:allDay:options:];
-[TCTextCompositionCalendarEventGenerationOutput initWithEventTitle:location:startDate:endDate:notes:notesBullets:allDay:participants:recurrenceRule:duration:startDateString:startTimeString:endDateString:endTimeString:startDateTZ:endDateTZ:fuzzyDuration:fuzzyStartDateString:fuzzyStartTimeString:fuzzyEndDateString:fuzzyEndTimeString:fuzzyStartDateBound:fuzzyEndDateBound:options:];
-[TCTextCompositionCalendarEventGenerationOutput initWithEventTitle:location:startDate:endDate:notes:notesBullets:allDay:participants:recurrenceRule:fuzzyStartDateBound:fuzzyEndDateBound:fuzzyDuration:startDateTZ:endDateTZ:options:];
-[TCTextCompositionCalendarEventGenerationOutput initWithEventTitle:location:startDate:endDate:notes:notesBullets:options:];
-[TCTextCompositionCalendarEventGenerationOutput initWithEventTitle:location:startDate:endDate:notes:options:];
-[TCTextCompositionCalendarEventGenerationOutput notesBullets];
-[TCTextCompositionCalendarEventGenerationOutput startDateTZ];
```
