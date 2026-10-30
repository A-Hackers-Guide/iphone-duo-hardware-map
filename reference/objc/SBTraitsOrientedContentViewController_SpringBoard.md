# `SBTraitsOrientedContentViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughViewController`
- 3 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"TRAParticipant" _contentParticipant;
@"TRAParticipant" _containerParticipant;
@? _actuateAlongsideBlock;
```

## Properties

```
@property (T@"SBTraitsOrientedContentViewControllerView",&,D,N) view;
@property (T@"TRAParticipant",W,N,V_contentParticipant) contentParticipant;
@property (T@"TRAParticipant",W,N,V_containerParticipant) containerParticipant;
@property (T@?,C,N,V_actuateAlongsideBlock) actuateAlongsideBlock;
```

## Instance methods

```
-[SBTraitsOrientedContentViewController setContainerParticipant:];
-[SBTraitsOrientedContentViewController updateOrientationIfNeeded];
-[SBTraitsOrientedContentViewController contentParticipant];
-[SBTraitsOrientedContentViewController view];
-[SBTraitsOrientedContentViewController _canShowWhileLocked];
-[SBTraitsOrientedContentViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBTraitsOrientedContentViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBTraitsOrientedContentViewController loadView];
-[SBTraitsOrientedContentViewController setContentParticipant:];
-[SBTraitsOrientedContentViewController setActuateAlongsideBlock:];
-[SBTraitsOrientedContentViewController actuateAlongsideBlock];
-[SBTraitsOrientedContentViewController containerParticipant];
```
