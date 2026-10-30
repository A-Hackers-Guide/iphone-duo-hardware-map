# `_UICalendarViewDataSourceController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSCalendar" _calendar;
@"UICollectionViewDiffableDataSource" _dataSource;
@"_UIDatePickerCalendarMonthSet" _loadedMonthSet;
@"_UIDatePickerCalendarDaySet" _loadedDaySet;
```

## Instance methods

```
-[_UICalendarViewDataSourceController _loadedDays];
-[_UICalendarViewDataSourceController _loadedMonths];
-[_UICalendarViewDataSourceController _reloadDataSourceWithScrollPosition:];
-[_UICalendarViewDataSourceController cleanupDataSourceWithScrollPositionIfNecessary:];
-[_UICalendarViewDataSourceController initWithCalendar:dataSource:];
-[_UICalendarViewDataSourceController prepareDataSourceWithScrollPositionIfNecessary:];
-[_UICalendarViewDataSourceController reloadDataSourceAroundMonth:];
```
