# `SBCoverSheetPositionView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughView`
- 7 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _delegateRespondsToUpdateContentPosition;
@"UIView" _contentView;
d _progress;
d _contentScale;
@"<SBCoverSheetPositionViewDelegate>" _delegate;
d _minimumDismissScale;
{CGPoint="x"d"y"d} _contentCenter;
```

## Properties

```
@property (Td,N,V_progress) progress;
@property (Td,N,V_contentScale) contentScale;
@property (T{CGPoint=dd},N,V_contentCenter) contentCenter;
@property (TB,N,V_delegateRespondsToUpdateContentPosition) delegateRespondsToUpdateContentPosition;
@property (T@"UIView",R,N,V_contentView) contentView;
@property (T@"<SBCoverSheetPositionViewDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_minimumDismissScale) minimumDismissScale;
```

## Instance methods

```
-[SBCoverSheetPositionView _simulatedTouchLocationForProgress];
-[SBCoverSheetPositionView setContentCenter:];
-[SBCoverSheetPositionView setProgress:];
-[SBCoverSheetPositionView _createContentView];
-[SBCoverSheetPositionView positionContentForTouchAtLocation:];
-[SBCoverSheetPositionView progress];
-[SBCoverSheetPositionView minimumDismissScale];
-[SBCoverSheetPositionView setDelegate:];
-[SBCoverSheetPositionView _progressFromContentViewFrame:];
-[SBCoverSheetPositionView scaleForDismissProgress:];
-[SBCoverSheetPositionView positionContentForTouchAtLocation:withVelocity:progress:transformMode:forPresentationValue:];
-[SBCoverSheetPositionView setContentScale:];
-[SBCoverSheetPositionView contentScale];
-[SBCoverSheetPositionView contentView];
-[SBCoverSheetPositionView delegate];
-[SBCoverSheetPositionView setFrame:];
-[SBCoverSheetPositionView contentCenter];
-[SBCoverSheetPositionView setMinimumDismissScale:];
-[SBCoverSheetPositionView delegateRespondsToUpdateContentPosition];
-[SBCoverSheetPositionView setDelegateRespondsToUpdateContentPosition:];
-[SBCoverSheetPositionView initWithFrame:];
```
