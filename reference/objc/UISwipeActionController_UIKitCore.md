# `UISwipeActionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIScrollViewScrollObserver`
- 9 instance variables, 17 properties, 53 instance methods, 0 class methods

## Instance variables

```
@"UISwipeOccurrence" _preparingSwipeOccurrence;
{?="didResetWhilePreparingSwipeOccurrence"b1} _flags;
@"<UISwipeActionHost>" _swipeActionHost;
Q _style;
@"UISwipeActionsConfiguration" _incomingSwipeActionsConfiguration;
@"UIScrollView" _containerView;
@"_UISwipeHandler" _swipeHandler;
@"NSMutableSet" _swipeOccurrences;
@"UISwipeOccurrence" _currentSwipeOccurrence;
```

## Properties

```
@property (T@"UISwipeActionsConfiguration",&,N,V_incomingSwipeActionsConfiguration) incomingSwipeActionsConfiguration;
@property (T@"<UISwipeActionHost>",W,N,V_swipeActionHost) swipeActionHost;
@property (T@"UIScrollView",W,N,V_containerView) containerView;
@property (T@"_UISwipeHandler",&,N,V_swipeHandler) swipeHandler;
@property (T@"<UISwipeActionHost_Internal>",R,N,G_internalSwipeActionHost) internalSwipeActionHost;
@property (TB,R,N,G_prefersRTL) prefersRTL;
@property (T@"NSMutableSet",&,N,V_swipeOccurrences) swipeOccurrences;
@property (T@"UISwipeOccurrence",W,N,V_currentSwipeOccurrence) currentSwipeOccurrence;
@property (T@"NSSet",R,N) swipedIndexPaths;
@property (T@"NSIndexPath",R,N) swipedIndexPath;
@property (T@"UIView",R,N) swipedItemView;
@property (TQ,N,V_style) style;
@property (TB,N) swipeEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISwipeActionController moveSectionAtIndex:toIndex:];
-[UISwipeActionController _observeScrollViewDidScroll:];
-[UISwipeActionController setContainerView:];
-[UISwipeActionController updateLayout];
-[UISwipeActionController swipeHandler:didConfirmSwipeWithInfo:];
-[UISwipeActionController deleteRowAtIndexPath:];
-[UISwipeActionController rebaseUnambiguousSwipeOccurrencesWithBlock:];
-[UISwipeActionController swipeHandler:didGenerateSwipeWithInfo:isTracking:];
-[UISwipeActionController _internalSwipeActionHost];
-[UISwipeActionController swipeEnabled];
-[UISwipeActionController swipeOccurrence:didChangeStateFrom:];
-[UISwipeActionController setIncomingSwipeActionsConfiguration:];
-[UISwipeActionController initWithSwipeActionHost:style:];
-[UISwipeActionController reconfigureActiveSwipeOccurrences];
-[UISwipeActionController _existingSwipeOccurrenceForIndexPath:];
-[UISwipeActionController _swipedViewForItemAtIndexPath:];
-[UISwipeActionController dealloc];
-[UISwipeActionController swipeHandlerRestingFrame:];
-[UISwipeActionController style];
-[UISwipeActionController setStyle:];
-[UISwipeActionController setSwipeOccurrences:];
-[UISwipeActionController touchAtLocationShouldDismissSwipedItem:isTouchUp:];
-[UISwipeActionController reloadData];
-[UISwipeActionController containerView];
-[UISwipeActionController resetSwipedItemAnimated:completion:];
-[UISwipeActionController swipedItemView];
-[UISwipeActionController setSwipeEnabled:];
-[UISwipeActionController setCurrentSwipeOccurrence:];
-[UISwipeActionController _prefersRTL];
-[UISwipeActionController swipeHandler];
-[UISwipeActionController swipeHandler:mayBeginSwipeAtLocation:withProposedDirection:];
-[UISwipeActionController swipeOccurrences];
-[UISwipeActionController currentSwipeOccurrence];
-[UISwipeActionController _isSwipeForIndexPathFirstOccurrenceBeginningOrLastOccurrenceEnding:];
-[UISwipeActionController incomingSwipeActionsConfiguration];
-[UISwipeActionController swipedIndexPaths];
-[UISwipeActionController _handleDeleteOfSwipeOccurrence:];
-[UISwipeActionController insertRowAtIndexPath:];
-[UISwipeActionController _swipeActionsConfigurationForSwipeDirection:indexPath:];
-[UISwipeActionController setSwipeHandler:];
-[UISwipeActionController setSwipeActionHost:];
-[UISwipeActionController insertSectionAtIndex:];
-[UISwipeActionController swipeActionHost];
-[UISwipeActionController swipeOccurrence:willFinishWithDeletion:];
-[UISwipeActionController moveRowAtIndexPath:toIndexPath:];
-[UISwipeActionController prepareForSwipeDirection:startingAtTouchLocation:];
-[UISwipeActionController swipeItemAtIndexPath:configuration:direction:animated:completion:];
-[UISwipeActionController deleteSectionAtIndex:];
-[UISwipeActionController _swipeDirectionForLeadingEdge:];
-[UISwipeActionController swipedIndexPath];
-[UISwipeActionController configureForSwipeDirection:configuration:startingAtTouchLocation:];
-[UISwipeActionController swipeOccurrenceDidFinish:];
-[UISwipeActionController swipeHandlerDidBeginSwipe:];
```
