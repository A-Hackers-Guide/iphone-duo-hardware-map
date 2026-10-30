# `SBFOverridableDateProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFDateTimeOverrideObserver`, `SBFDateProviding`
- 7 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SBFDateTimeController" _dateTimeController;
@"<SBFDateProviding>" _underlyingProvider;
@"NSMutableDictionary" _minuteHandlers;
Q _nextToken;
@ _underlyingToken;
@"NSDate" _overrideDate;
d _overrideDateOffset;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,?,N) additionalOffset;
```

## Instance methods

```
-[SBFOverridableDateProvider init];
-[SBFOverridableDateProvider date];
-[SBFOverridableDateProvider controller:didChangeOverrideDateFromDate:];
-[SBFOverridableDateProvider initWithDateProvider:];
-[SBFOverridableDateProvider additionalOffset];
-[SBFOverridableDateProvider observeMinuteUpdatesWithHandler:];
-[SBFOverridableDateProvider removeMinuteUpdateHandler:];
-[SBFOverridableDateProvider setAdditionalOffset:];
-[SBFOverridableDateProvider _fireHandlersForDate:];
-[SBFOverridableDateProvider _updateForOverrides];
-[SBFOverridableDateProvider _updateUnderlyingProvider];
```
