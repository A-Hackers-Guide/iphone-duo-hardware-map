# `UIMultiSelectInteractionState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 26 instance methods, 0 class methods

## Instance variables

```
Q _ignoringSelectionChangedNotificationsCounter;
Q _multiselectInteractionCounter;
@"NSMutableSet" _indexPathsWithProgrammaticSelectionChanges;
B _selecting;
@"NSIndexPath" _startIndexPath;
@"NSIndexPath" _endIndexPath;
@"NSArray" _originallySelectedIndexPaths;
@"NSArray" _allSelectedIndexPaths;
{CGPoint="x"d"y"d} _startPoint;
```

## Properties

```
@property (T{CGPoint=dd},N,V_startPoint) startPoint;
@property (T@"NSIndexPath",&,N,V_startIndexPath) startIndexPath;
@property (T@"NSIndexPath",&,N,V_endIndexPath) endIndexPath;
@property (TB,N,GisSelecting,V_selecting) selecting;
@property (T@"NSArray",C,N,V_originallySelectedIndexPaths) originallySelectedIndexPaths;
@property (T@"NSArray",C,N,V_allSelectedIndexPaths) allSelectedIndexPaths;
@property (TB,R,N) ignoringSelectionChangedNotifications;
@property (T@"NSSet",R,N) indexPathsWithProgrammaticSelectionChanges;
@property (TB,R,N,GisInMultiselectInteraction) inMultiselectInteraction;
```

## Instance methods

```
-[UIMultiSelectInteractionState isSelecting];
-[UIMultiSelectInteractionState noteProgrammaticSelectionChangeForIndexPath:];
-[UIMultiSelectInteractionState updateStateWithStartingIndexPath:otherSelectedIndexPaths:];
-[UIMultiSelectInteractionState ignoringSelectionChangedNotifications];
-[UIMultiSelectInteractionState setSelecting:];
-[UIMultiSelectInteractionState setStartPoint:];
-[UIMultiSelectInteractionState pathsToSelectForInterpolatedIndexPaths:];
-[UIMultiSelectInteractionState initWithCurrentSelection:];
-[UIMultiSelectInteractionState startPoint];
-[UIMultiSelectInteractionState isInMultiselectInteraction];
-[UIMultiSelectInteractionState startIndexPath];
-[UIMultiSelectInteractionState stillValidForSelectedIndexPaths:];
-[UIMultiSelectInteractionState beginSelectingWithStartingIndexPath:otherSelectedIndexPaths:keepCurrentSelection:];
-[UIMultiSelectInteractionState pathsToDeselectForInterpolatedIndexPaths:currentlySelectedIndexPaths:];
-[UIMultiSelectInteractionState setEndIndexPath:];
-[UIMultiSelectInteractionState endIndexPath];
-[UIMultiSelectInteractionState ignoreSelectionChangedNotificationsWithBlock:];
-[UIMultiSelectInteractionState indexPathsWithProgrammaticSelectionChanges];
-[UIMultiSelectInteractionState setAllSelectedIndexPaths:];
-[UIMultiSelectInteractionState allSelectedIndexPaths];
-[UIMultiSelectInteractionState setOriginallySelectedIndexPaths:];
-[UIMultiSelectInteractionState setStartIndexPath:];
-[UIMultiSelectInteractionState updateStateWithDifferenceFromCurrentSelection:];
-[UIMultiSelectInteractionState endMultiselectInteraction];
-[UIMultiSelectInteractionState beginMultiselectInteraction];
-[UIMultiSelectInteractionState originallySelectedIndexPaths];
```
