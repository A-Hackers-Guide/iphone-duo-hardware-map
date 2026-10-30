# `SBCoverSheetSpotlightViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSCoverSheetViewControllerBase`
- Protocols: `CSDismissableModalViewControllerDelegate`, `SBSearchPresentable`
- 8 instance variables, 10 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"CSProudLockComponent" _proudLockComponent;
@"CSDateViewComponent" _dateViewComponent;
@"CSContentComponent" _contentComponent;
@"CSWallpaperFloatingLayerComponent" _wallpaperFloatingLayerComponent;
@"<SBCoverSheetSpotlightViewControllerDelegate>" _delegate;
@"SBSpotlightPresentableViewController" _spotlightViewController;
d _topOffset;
d _maxPresentationOffset;
```

## Properties

```
@property (T@"<SBCoverSheetSpotlightViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"SBSpotlightPresentableViewController",&,N,V_spotlightViewController) spotlightViewController;
@property (Td,N,V_topOffset) topOffset;
@property (Td,N,V_maxPresentationOffset) maxPresentationOffset;
@property (T@"SBHHomePullToSearchSettings",&,N) searchTransitionSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"FBSDisplayConfiguration",?,&,N) targetDisplayConfiguration;
```

## Instance methods

```
-[SBCoverSheetSpotlightViewController addGrabberView:];
-[SBCoverSheetSpotlightViewController handleEvent:];
-[SBCoverSheetSpotlightViewController willBeginModifyingPresentationProgressForState:animated:needsInitialLayout:];
-[SBCoverSheetSpotlightViewController setSpotlightViewController:];
-[SBCoverSheetSpotlightViewController dismissForHomeButton];
-[SBCoverSheetSpotlightViewController setMaxPresentationOffset:];
-[SBCoverSheetSpotlightViewController topOffset];
-[SBCoverSheetSpotlightViewController handleBottomEdgeGestureEnded:];
-[SBCoverSheetSpotlightViewController aggregateBehavior:];
-[SBCoverSheetSpotlightViewController maxPresentationOffset];
-[SBCoverSheetSpotlightViewController viewDidLoad];
-[SBCoverSheetSpotlightViewController _newDisplayLayoutElement];
-[SBCoverSheetSpotlightViewController setTargetDisplayConfiguration:];
-[SBCoverSheetSpotlightViewController viewWillAppear:];
-[SBCoverSheetSpotlightViewController invalidate];
-[SBCoverSheetSpotlightViewController aggregateAppearance:];
-[SBCoverSheetSpotlightViewController setDelegate:];
-[SBCoverSheetSpotlightViewController presentationCancelsTouches];
-[SBCoverSheetSpotlightViewController updatePresentationProgress:withOffset:velocity:presentationState:];
-[SBCoverSheetSpotlightViewController setTopOffset:];
-[SBCoverSheetSpotlightViewController delegate];
-[SBCoverSheetSpotlightViewController viewDidDisappear:];
-[SBCoverSheetSpotlightViewController handleBottomEdgeGestureChanged:];
-[SBCoverSheetSpotlightViewController spotlightViewController];
-[SBCoverSheetSpotlightViewController _scaleGivenTranslation:];
-[SBCoverSheetSpotlightViewController _updatePresentationProgress:withOffset:velocity:presentationState:];
-[SBCoverSheetSpotlightViewController _updateSpotlightScale:interactive:];
-[SBCoverSheetSpotlightViewController initWithSpotlightViewController:];
-[SBCoverSheetSpotlightViewController searchTransitionSettings];
-[SBCoverSheetSpotlightViewController setSearchTransitionSettings:];
-[SBCoverSheetSpotlightViewController updateComponentTransitionWithOffset:presentationState:];
```
