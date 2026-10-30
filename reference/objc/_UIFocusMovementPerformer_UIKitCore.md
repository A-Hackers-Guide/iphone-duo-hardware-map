# `_UIFocusMovementPerformer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<_UIFocusMovementPerformerDelegate>" _delegate;
```

## Properties

```
@property (T@"<_UIFocusMovementPerformerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[_UIFocusMovementPerformer setDelegate:];
-[_UIFocusMovementPerformer delegate];
-[_UIFocusMovementPerformer __findFocusCandidateInEnvironment:container:forRequest:minimumSearchArea:isLoadingScrollableContainer:];
-[_UIFocusMovementPerformer _bestCandidateForLinearFocusMovement:];
-[_UIFocusMovementPerformer _bestCandidateForNonLinearFocusMovement:];
-[_UIFocusMovementPerformer _dummyFocusItemForFocusMovement:searchArea:parent:];
-[_UIFocusMovementPerformer _environmentContainersToCheckForRequest:];
-[_UIFocusMovementPerformer _findFocusCandidateByExhaustivelySearchingEnvironment:scrollableContainer:forRequest:];
-[_UIFocusMovementPerformer _findFocusCandidateBySearchingLinearFocusMovementSequencesForRequest:];
-[_UIFocusMovementPerformer _findFocusCandidateWithoutLoadingScrollableContentInEnvironment:container:forRequest:minimumSearchArea:];
-[_UIFocusMovementPerformer _isMovementValidForFocusSequences:];
-[_UIFocusMovementPerformer _minimumSearchAreaForContainer:inCoordinateSpace:];
-[_UIFocusMovementPerformer _minimumSearchAreaForContainer:inCoordinateSpace:shouldLoadScrollableContainer:];
-[_UIFocusMovementPerformer _nextLinearCandidateLoadingScrollableContentForRequest:];
-[_UIFocusMovementPerformer contextForFocusMovement:];
-[_UIFocusMovementPerformer performFocusMovement:];
```
