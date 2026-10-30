# `_UICollectionViewFeedbackLoopDebugger`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
currentlyTrackedChangeRecords;
invalidationRecords;
updateVisibleCellsRecords;
```

## Instance methods

```
-[_UICollectionViewFeedbackLoopDebugger init];
-[_UICollectionViewFeedbackLoopDebugger recordGenericChangeWithMessage:];
-[_UICollectionViewFeedbackLoopDebugger printCollectedRecordsForCollectionView:raiseException:];
-[_UICollectionViewFeedbackLoopDebugger recordCollectionViewInsetsPropertyChange:fromInsets:toInsets:];
-[_UICollectionViewFeedbackLoopDebugger recordCollectionViewPointPropertyChange:fromPoint:toPoint:];
-[_UICollectionViewFeedbackLoopDebugger recordCollectionViewRectPropertyChange:fromRect:toRect:];
-[_UICollectionViewFeedbackLoopDebugger recordInvalidationWithContext:];
-[_UICollectionViewFeedbackLoopDebugger recordPreferredAttributesChangeForElementWithAttributes:reason:changedAttribute:fromValue:toValue:layoutGeneratedValue:];
-[_UICollectionViewFeedbackLoopDebugger recordUpdateVisibleCellsScheduledWithCallStack:];
```
