# `PKSelectionStatisticsManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"PKSelectionStatisticsSession" _selectionSession;
{CGPoint="x"d"y"d} _lastContentOffset;
```

## Class methods

```
+[PKSelectionStatisticsManager sharedStatisticsManager];
```

## Instance methods

```
-[PKSelectionStatisticsManager recordDidMakeSelectionWithType:];
-[PKSelectionStatisticsManager _endSelectionSession];
-[PKSelectionStatisticsManager _recordSelectionSession:];
-[PKSelectionStatisticsManager logEndSelectionSessionIfNecessary];
-[PKSelectionStatisticsManager logScrollEventWithContentOffset:];
-[PKSelectionStatisticsManager logSelectionAction:];
-[PKSelectionStatisticsManager recordLassoSelectionEventWithContentType:];
-[PKSelectionStatisticsManager recordSmartSelectionEventWithType:contentType:gestureInvoked:];
```
