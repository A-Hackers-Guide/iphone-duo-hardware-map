# `SRResearchDaysViewController`

- Image: [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](../userland/System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewController`
- 4 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
d _end;
q _numberOfDays;
@"NSArray" _tombstones;
@"NSMutableSet" _deletedDays;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_deletedDays) deletedDays;
@property (Td,N,V_end) end;
@property (Tq,N,V_numberOfDays) numberOfDays;
@property (T@"NSArray",&,N,V_tombstones) tombstones;
```

## Instance methods

```
-[SRResearchDaysViewController tableView:numberOfRowsInSection:];
-[SRResearchDaysViewController tableView:cellForRowAtIndexPath:];
-[SRResearchDaysViewController init];
-[SRResearchDaysViewController dealloc];
-[SRResearchDaysViewController viewDidLoad];
-[SRResearchDaysViewController end];
-[SRResearchDaysViewController setEnd:];
-[SRResearchDaysViewController tombstones];
-[SRResearchDaysViewController setTombstones:];
-[SRResearchDaysViewController numberOfDays];
-[SRResearchDaysViewController setDeletedDays:];
-[SRResearchDaysViewController dateForRow:];
-[SRResearchDaysViewController datesFrom:to:];
-[SRResearchDaysViewController deletedDays];
-[SRResearchDaysViewController setNumberOfDays:];
```
