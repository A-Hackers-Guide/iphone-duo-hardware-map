# `SBHRootFolderCustomViewPresenting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `SBHLegibility`, `SBHVisibleContentPresenter`
- 0 instance variables, 14 properties, 22 instance methods, 0 class methods

## Properties

```
@property (TB,?,R,N) shouldBeIndicatedInPageControl;
@property (T@"<SBIconViewQuerying>",?,R) iconViewQueryable;
@property (T@"<SBIconLocationPresenting>",?,R) iconLocationPresenter;
@property (T@"<SBIconListViewQuerying>",?,R) iconListViewQueryable;
@property (TB,?,R,N) shouldShowDoneButtonWhenEditing;
@property (TB,?,R,N) shouldShowEditMenuButtonWhenEditing;
@property (Td,?,R,N) scrollPageOffsetForButtonsInEditingMode;
@property (TB,?,N) suppressesEditingStateForListViews;
@property (TB,?,R,N) shouldObscureBackgroundWhileVisible;
@property (T@"SBIconListView",?,R,N) rootIconListView;
@property (T@"SBIconListView",?,R,N) currentIconListView;
@property (T@"NSArray",?,R,C,N) rootIconListViews;
@property (T@"UIView",?,R,N) iconZoomView;
@property (TB,?,N,GisShownInScrollView) shownInScrollView;
```

## Instance methods

```
-[SBHRootFolderCustomViewPresenting setOrientation:];
-[SBHRootFolderCustomViewPresenting setSuppressesEditingStateForListViews:];
-[SBHRootFolderCustomViewPresenting iconViewQueryable];
-[SBHRootFolderCustomViewPresenting setIconZoomInProgress:];
-[SBHRootFolderCustomViewPresenting currentIconListView];
-[SBHRootFolderCustomViewPresenting setPrefersCenteredAlignment:];
-[SBHRootFolderCustomViewPresenting shouldShowDoneButtonWhenEditing];
-[SBHRootFolderCustomViewPresenting customViewPresenterDidReceiveBackgroundTap];
-[SBHRootFolderCustomViewPresenting iconListViewQueryable];
-[SBHRootFolderCustomViewPresenting iconLocationPresenter];
-[SBHRootFolderCustomViewPresenting iconZoomView];
-[SBHRootFolderCustomViewPresenting isShownInScrollView];
-[SBHRootFolderCustomViewPresenting rootIconListView];
-[SBHRootFolderCustomViewPresenting rootIconListViews];
-[SBHRootFolderCustomViewPresenting scrollPageOffsetForButtonsInEditingMode];
-[SBHRootFolderCustomViewPresenting setHomeScreenLayoutCompact:];
-[SBHRootFolderCustomViewPresenting setShouldPrewarmContent:];
-[SBHRootFolderCustomViewPresenting setShownInScrollView:];
-[SBHRootFolderCustomViewPresenting shouldBeIndicatedInPageControl];
-[SBHRootFolderCustomViewPresenting shouldObscureBackgroundWhileVisible];
-[SBHRootFolderCustomViewPresenting shouldShowEditMenuButtonWhenEditing];
-[SBHRootFolderCustomViewPresenting suppressesEditingStateForListViews];
```
