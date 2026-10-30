# `_UICustomScheduleController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 4 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _observers;
B _inScheduleTime;
@"NSTimer" _nextEventTimer;
{?="beginTime"{?="hour"q"minute"q}"endTime"{?="hour"q"minute"q}} _schedule;
```

## Properties

```
@property (T{?={?=qq}{?=qq}},N,V_schedule) schedule;
@property (TB,R,N,GisInScheduleTime) inScheduleTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICustomScheduleController debugDescription];
-[_UICustomScheduleController _significantTimeChange];
-[_UICustomScheduleController succinctDescriptionBuilder];
-[_UICustomScheduleController removeObserver:];
-[_UICustomScheduleController init];
-[_UICustomScheduleController dealloc];
-[_UICustomScheduleController forceUpdate];
-[_UICustomScheduleController descriptionWithMultilinePrefix:];
-[_UICustomScheduleController succinctDescription];
-[_UICustomScheduleController description];
-[_UICustomScheduleController setSchedule:];
-[_UICustomScheduleController descriptionBuilderWithMultilinePrefix:];
-[_UICustomScheduleController schedule];
-[_UICustomScheduleController nextTransition:];
-[_UICustomScheduleController _notifyChange];
-[_UICustomScheduleController _updateStatus:];
-[_UICustomScheduleController _updateTimeMonitoring];
-[_UICustomScheduleController _updateTimeMonitoring:];
-[_UICustomScheduleController _updateWithDate:];
-[_UICustomScheduleController addObserver:changeHandler:];
-[_UICustomScheduleController isInScheduleTime];
```
