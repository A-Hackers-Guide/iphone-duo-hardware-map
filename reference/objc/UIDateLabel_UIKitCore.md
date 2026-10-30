# `UIDateLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILabel`
- 11 instance variables, 12 properties, 37 instance methods, 6 class methods

## Instance variables

```
B _forceTimeOnly;
@"NSDate" _date;
B _boldForAllLocales;
@"NSDate" _yesterday;
@"NSDate" _today;
@"NSDate" _noon;
@"NSDate" _tomorrow;
@"NSDate" _weekdayFormatCutoff;
@"NSCalendar" _calendar;
B _shouldRecomputeText;
d _paddingFromTimeToDesignator;
```

## Properties

```
@property (TB,R,N) use24HourTime;
@property (TB,R,N) timeDesignatorAppearsBeforeTime;
@property (T{CGSize=dd},R,N) timeDesignatorSize;
@property (T@"NSString",R,N,G_dateString) dateString;
@property (TB,N,V_shouldRecomputeText) shouldRecomputeText;
@property (T@"NSDate",&,N) date;
@property (Td,N) timeInterval;
@property (T@"UIFont",R,N) timeDesignatorFont;
@property (T@"NSString",R,N) timeDesignator;
@property (TB,N,V_forceTimeOnly) forceTimeOnly;
@property (TB,N,V_boldForAllLocales) boldForAllLocales;
@property (Td,N,V_paddingFromTimeToDesignator) paddingFromTimeToDesignator;
```

## Class methods

```
+[UIDateLabel _relativeDateFormatter];
+[UIDateLabel _dateFormatter];
+[UIDateLabel defaultFont];
+[UIDateLabel _designatorFormatter];
+[UIDateLabel _timeOnlyDateFormatter];
+[UIDateLabel _weekdayDateFormatter];
```

## Instance methods

```
-[UIDateLabel timeInterval];
-[UIDateLabel _tomorrow];
-[UIDateLabel text];
-[UIDateLabel setDate:];
-[UIDateLabel _intrinsicSizeWithinSize:];
-[UIDateLabel _dateString];
-[UIDateLabel dealloc];
-[UIDateLabel drawRect:];
-[UIDateLabel date];
-[UIDateLabel invalidate];
-[UIDateLabel setTimeInterval:];
-[UIDateLabel font];
-[UIDateLabel drawTextInRect:];
-[UIDateLabel initWithFrame:];
-[UIDateLabel setPaddingFromTimeToDesignator:];
-[UIDateLabel timeDesignatorAppearsBeforeTime];
-[UIDateLabel _calendar];
-[UIDateLabel _dateWithDayDiffFromToday:];
-[UIDateLabel _didUpdateDate];
-[UIDateLabel _noon];
-[UIDateLabel _recomputeTextIfNecessary];
-[UIDateLabel _stringDrawingContext];
-[UIDateLabel _today];
-[UIDateLabel _todayDate];
-[UIDateLabel _weekdayFormatCutoff];
-[UIDateLabel _yesterday];
-[UIDateLabel boldForAllLocales];
-[UIDateLabel forceTimeOnly];
-[UIDateLabel paddingFromTimeToDesignator];
-[UIDateLabel setBoldForAllLocales:];
-[UIDateLabel setForceTimeOnly:];
-[UIDateLabel setShouldRecomputeText:];
-[UIDateLabel shouldRecomputeText];
-[UIDateLabel timeDesignator];
-[UIDateLabel timeDesignatorFont];
-[UIDateLabel timeDesignatorSize];
-[UIDateLabel use24HourTime];
```
