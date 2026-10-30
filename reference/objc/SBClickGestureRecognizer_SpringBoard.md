# `SBClickGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBPressGestureRecognizer`
- 11 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
Q _numberOfClicksRequired;
B _allPressesUpRequired;
d _maximumClickFormationDuration;
d _maximumClickDownDuration;
d _maximumBetweenClicksDelay;
Q _recognizedClicksCount;
B _gestureWasRecognized;
B _allPressBeganReceived;
@"NSMutableArray" _shortcutPressTypesSubsets;
@"NSMutableSet" _receivedPressBeganTypes;
@"NSMutableSet" _receivedPressEndedTypes;
```

## Properties

```
@property (TQ,N,V_numberOfClicksRequired) numberOfClicksRequired;
@property (TB,N,V_allPressesUpRequired) allPressesUpRequired;
@property (Td,N,V_maximumClickFormationDuration) maximumClickFormationDuration;
@property (Td,N,V_maximumClickDownDuration) maximumClickDownDuration;
@property (Td,N,V_maximumBetweenClicksDelay) maximumBetweenClicksDelay;
```

## Instance methods

```
-[SBClickGestureRecognizer setAllPressesUpRequired:];
-[SBClickGestureRecognizer numberOfClicksRequired];
-[SBClickGestureRecognizer setMaximumBetweenClicksDelay:];
-[SBClickGestureRecognizer resetShortcutsTracking];
-[SBClickGestureRecognizer maximumClickFormationDuration];
-[SBClickGestureRecognizer didReceiveRequiredPressEndedCount];
-[SBClickGestureRecognizer didReceiveRequiredPressBeganCount];
-[SBClickGestureRecognizer setMaximumClickFormationDuration:];
-[SBClickGestureRecognizer setNumberOfClicksRequired:];
-[SBClickGestureRecognizer addShortcutWithPressTypes:];
-[SBClickGestureRecognizer setMaximumClickDownDuration:];
-[SBClickGestureRecognizer reset];
-[SBClickGestureRecognizer maximumBetweenClicksDelay];
-[SBClickGestureRecognizer initWithTarget:action:];
-[SBClickGestureRecognizer _areRequiredPressTypesContainedInSet:];
-[SBClickGestureRecognizer gestureStateInfoForUnbalancedPressBeganCount:previousCount:];
-[SBClickGestureRecognizer _notePressReceivedWithType:phase:];
-[SBClickGestureRecognizer maximumClickDownDuration];
-[SBClickGestureRecognizer allPressesUpRequired];
```
