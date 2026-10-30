# `PKSelectionStatisticsSession`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _selectionGestures;
@"NSMutableArray" _selectionActions;
@"NSDate" _startTime;
d _timeSpentSelecting;
q _numberOfTimesSelectionWasClearedInASession;
q _selectionGestureCount;
@"NSString" _lastActionTaken;
@"NSString" _lastSignificantActionTaken;
q _lastSelectionType;
q _lastContentType;
```

## Properties

```
@property (T@"NSDictionary",R,N) selectionGestureDictionary;
@property (T@"NSDictionary",R,N) selectionActionDictionary;
@property (Td,N,V_timeSpentSelecting) timeSpentSelecting;
@property (Tq,N,V_numberOfTimesSelectionWasClearedInASession) numberOfTimesSelectionWasClearedInASession;
@property (Tq,N,V_selectionGestureCount) selectionGestureCount;
@property (T@"NSString",&,N,V_lastActionTaken) lastActionTaken;
@property (T@"NSString",&,N,V_lastSignificantActionTaken) lastSignificantActionTaken;
@property (Tq,N,V_lastSelectionType) lastSelectionType;
@property (Tq,N,V_lastContentType) lastContentType;
```

## Instance methods

```
-[PKSelectionStatisticsSession init];
-[PKSelectionStatisticsSession lastActionTaken];
-[PKSelectionStatisticsSession lastContentType];
-[PKSelectionStatisticsSession lastSelectionType];
-[PKSelectionStatisticsSession lastSignificantActionTaken];
-[PKSelectionStatisticsSession logGesture:selectionType:contentType:];
-[PKSelectionStatisticsSession logSelectionAction:];
-[PKSelectionStatisticsSession numberOfTimesSelectionWasClearedInASession];
-[PKSelectionStatisticsSession selectionActionDictionary];
-[PKSelectionStatisticsSession selectionGestureCount];
-[PKSelectionStatisticsSession selectionGestureDictionary];
-[PKSelectionStatisticsSession setLastActionTaken:];
-[PKSelectionStatisticsSession setLastContentType:];
-[PKSelectionStatisticsSession setLastSelectionType:];
-[PKSelectionStatisticsSession setLastSignificantActionTaken:];
-[PKSelectionStatisticsSession setNumberOfTimesSelectionWasClearedInASession:];
-[PKSelectionStatisticsSession setSelectionGestureCount:];
-[PKSelectionStatisticsSession setTimeSpentSelecting:];
-[PKSelectionStatisticsSession timeSpentSelecting];
```
