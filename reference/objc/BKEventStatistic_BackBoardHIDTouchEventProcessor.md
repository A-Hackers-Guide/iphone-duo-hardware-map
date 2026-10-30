# `BKEventStatistic`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionStreamable`
- 4 instance variables, 8 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _automaticResetDisabled;
B _needsLogging;
@"NSString" _label;
@"NSArray" _associatedStatistics;
```

## Properties

```
@property (T@"NSString",C,N,V_label) label;
@property (T@"NSArray",C,N,V_associatedStatistics) associatedStatistics;
@property (TB,N,V_automaticResetDisabled) automaticResetDisabled;
@property (TB,N,V_needsLogging) needsLogging;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKEventStatistic statisticWithLabel:];
```

## Instance methods

```
-[BKEventStatistic label];
-[BKEventStatistic setLabel:];
-[BKEventStatistic appendDescriptionToFormatter:];
-[BKEventStatistic reset];
-[BKEventStatistic copyWithZone:];
-[BKEventStatistic associatedStatistics];
-[BKEventStatistic automaticResetDisabled];
-[BKEventStatistic needsLogging];
-[BKEventStatistic setAssociatedStatistics:];
-[BKEventStatistic setAutomaticResetDisabled:];
-[BKEventStatistic setNeedsLogging:];
```
