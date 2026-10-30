# `_UIFocusMoveTest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFocusTest`
- 11 instance variables, 8 properties, 32 instance methods, 0 class methods

## Instance variables

```
Q _activeNumberOfIterations;
Q _currentIteration;
Q _currentMove;
{?="isPerformingFocusMovement"b1"delegateRespondsToWillStartIteration"b1"delegateRespondsToDidFinishIteration"b1"delegateRespondsToWillMoveFocusAlongHeadingForMoveDuringIteration"b1"delegateRespondsToDidMoveFocusAlongHeadingForMoveDuringIteration"b1"dataSourceRespondsToNumberOfIterations"b1"dataSourceRespondsToMaximumNumberOfMovesDuringIteration"b1"dataSourceRespondsToDelayBeforeMoveDuringIteration"b1"dataSourceRespondsToHeadingForMoveDuringIteration"b1"dataSourceRespondsToShouldResetFocusBeforeIteration"b1} _flags;
B _resetsFocusBeforeIterations;
@"<UIFocusEnvironment>" _containerFocusEnvironment;
Q _numberOfIterations;
Q _maximumMovesPerIteration;
d _movementDelay;
Q _movementHeading;
@"<_UIFocusMoveTestDataSource>" _dataSource;
```

## Properties

```
@property (T@"<UIFocusEnvironment>",W,N,V_containerFocusEnvironment) containerFocusEnvironment;
@property (TQ,N,V_numberOfIterations) numberOfIterations;
@property (TQ,N,V_maximumMovesPerIteration) maximumMovesPerIteration;
@property (Td,N,V_movementDelay) movementDelay;
@property (TQ,N,V_movementHeading) movementHeading;
@property (TB,N,V_resetsFocusBeforeIterations) resetsFocusBeforeIterations;
@property (T@"<_UIFocusMoveTestDelegate>",W,N) delegate;
@property (T@"<_UIFocusMoveTestDataSource>",W,N,V_dataSource) dataSource;
```

## Instance methods

```
-[_UIFocusMoveTest main];
-[_UIFocusMoveTest reset];
-[_UIFocusMoveTest setDataSource:];
-[_UIFocusMoveTest setDelegate:];
-[_UIFocusMoveTest dataSource];
-[_UIFocusMoveTest delegate];
-[_UIFocusMoveTest prepareWithCompletionHandler:];
-[_UIFocusMoveTest initWithIdentifier:];
-[_UIFocusMoveTest movementHeading];
-[_UIFocusMoveTest setResetsFocusBeforeIterations:];
-[_UIFocusMoveTest _dataSourceDelayBeforeMove:duringIteration:];
-[_UIFocusMoveTest _dataSourceHeadingForMove:duringIteration:];
-[_UIFocusMoveTest _dataSourceMaximumNumberOfMovesDuringIteration:];
-[_UIFocusMoveTest _dataSourceNumberOfIterations];
-[_UIFocusMoveTest _dataSourceShouldResetFocusBeforeIteration:];
-[_UIFocusMoveTest _notifyDelegateDidFinishIteration:];
-[_UIFocusMoveTest _notifyDelegateDidMoveFocusAlongHeading:forMove:duringIteration:];
-[_UIFocusMoveTest _notifyDelegateWillMoveFocusAlongHeading:forMove:duringIteration:];
-[_UIFocusMoveTest _notifyDelegateWillStartIteration:];
-[_UIFocusMoveTest _performFocusMovement];
-[_UIFocusMoveTest _performFocusMovementAfterDelayForMove:iteration:];
-[_UIFocusMoveTest _resetFocusIfNecessaryBeforeIteration:];
-[_UIFocusMoveTest containerFocusEnvironment];
-[_UIFocusMoveTest maximumMovesPerIteration];
-[_UIFocusMoveTest movementDelay];
-[_UIFocusMoveTest numberOfIterations];
-[_UIFocusMoveTest resetsFocusBeforeIterations];
-[_UIFocusMoveTest setContainerFocusEnvironment:];
-[_UIFocusMoveTest setMaximumMovesPerIteration:];
-[_UIFocusMoveTest setMovementDelay:];
-[_UIFocusMoveTest setMovementHeading:];
-[_UIFocusMoveTest setNumberOfIterations:];
```
