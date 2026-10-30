# `ANGetUserstatsTask`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ANTask`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _lastFragmentReceived;
B _shouldSubmitMetrics;
@"NSMutableData" _userStatsData;
```

## Properties

```
@property (T@"NSMutableData",&,V_userStatsData) userStatsData;
@property (TB,V_lastFragmentReceived) lastFragmentReceived;
@property (TB,V_shouldSubmitMetrics) shouldSubmitMetrics;
```

## Instance methods

```
-[ANGetUserstatsTask isComplete];
-[ANGetUserstatsTask dealloc];
-[ANGetUserstatsTask appendUserStatsData:opcode:];
-[ANGetUserstatsTask initWithOpcode:persistence:context:];
-[ANGetUserstatsTask initWithOpcode:persistenceConfig:context:];
-[ANGetUserstatsTask lastFragmentReceived];
-[ANGetUserstatsTask setLastFragmentReceived:];
-[ANGetUserstatsTask setShouldSubmitMetrics:];
-[ANGetUserstatsTask setUserStatsData:];
-[ANGetUserstatsTask shouldSubmitMetrics];
-[ANGetUserstatsTask userStatsData];
```
