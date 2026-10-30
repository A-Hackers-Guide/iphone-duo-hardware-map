# `SBFDefaultDateProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFDateProviding`
- 4 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _minuteHandlers;
Q _nextToken;
@"NSTimer" _minuteTimer;
@"NSCalendar" _calendar;
```

## Properties

```
@property (Td,?,N) additionalOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFDefaultDateProvider init];
-[SBFDefaultDateProvider date];
-[SBFDefaultDateProvider observeMinuteUpdatesWithHandler:];
-[SBFDefaultDateProvider removeMinuteUpdateHandler:];
-[SBFDefaultDateProvider _minuteTimerFired];
-[SBFDefaultDateProvider _scheduleNextMinuteTimer];
-[SBFDefaultDateProvider _updateMinuteTimer];
```
