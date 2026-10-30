# `SBHomeScreenOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBHLibraryViewControllerPresenter`, `SBHWidgetSheetViewControllerPresenter`, `SBHVisibleContentPresenter`
- 27 instance variables, 33 properties, 85 instance methods, 0 class methods

## Instance variables

```
@"NSCountedSet" _reasonsToSnapshotBackgroundView;
Q _defaultAnimationCount;
Q _fadingAnimationCount;
{CGSize="width"d"height"d} _boundsSizeForConstraints;
B _fromLeading;
B _shouldUseReducedMotionAnimation;
B _suppressesExtraEditingButtons;
B _showsDoneButton;
B _showsAddWidgetButton;
B _transitioningPresentationProgress;
Q _contentVisibility;
d _titledButtonsAlpha;
@"<SBHomeScreenOverlayViewControllerDelegate>" _delegate;
d _presentationProgress;
@"SBHRootSidebarController" _contentViewController;
@"UIViewController<SBHVisibleContentPresenter>" _leadingSidebarViewController;
@"UIViewController<SBHVisibleContentPresenter>" _trailingSidebarViewController;
@"<SBIconListLayoutProvider>" _listLayoutProvider;
@"MTMaterialView" _backgroundView;
@"SBHRootFolderVisualConfiguration" _rootFolderVisualConfiguration;
@"NSLayoutConstraint" _contentLeadingConstraint;
@"NSLayoutConstraint" _contentWidthConstraint;
@"SBTitledHomeScreenButton" _doneButton;
@"SBTitledHomeScreenButton" _widgetButton;
@"SBFTodayGestureSettings" _gestureSettings;
@"UIViewFloatAnimatableProperty" _overlayPresentationFloatAnimatableProperty;
@"UIView" _buttonBackgroundView;
```

## Properties

```
@property (T@"<SBIconListLayoutProvider>",R,N,V_listLayoutProvider) listLayoutProvider;
@property (T@"MTMaterialView",R,N,V_backgroundView) backgroundView;
@property (T@"SBHRootFolderVisualConfiguration",R,N,V_rootFolderVisualConfiguration) rootFolderVisualConfiguration;
@property (T@"NSLayoutConstraint",&,N,V_contentLeadingConstraint) contentLeadingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_contentWidthConstraint) contentWidthConstraint;
@property (T@"SBTitledHomeScreenButton",&,N,V_doneButton) doneButton;
@property (T@"SBTitledHomeScreenButton",&,N,V_widgetButton) widgetButton;
@property (TB,N,V_showsDoneButton) showsDoneButton;
@property (TB,N,V_showsAddWidgetButton) showsAddWidgetButton;
@property (T@"SBFTodayGestureSettings",&,N,V_gestureSettings) gestureSettings;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_overlayPresentationFloatAnimatableProperty) overlayPresentationFloatAnimatableProperty;
@property (TB,N,GisTransitioningPresentationProgress,V_transitioningPresentationProgress) transitioningPresentationProgress;
@property (T@"UIView",R,N,V_buttonBackgroundView) buttonBackgroundView;
@property (T@"<SBHomeScreenOverlayViewControllerDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_presentationProgress) presentationProgress;
@property (Td,R,N) layerPresentationProgress;
@property (TB,N,GisFromLeading,V_fromLeading) fromLeading;
@property (Td,R,N) contentWidth;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) contentRect;
@property (TB,N,V_shouldUseReducedMotionAnimation) shouldUseReducedMotionAnimation;
@property (TB,R,N,GisHeaderVisible) headerVisible;
@property (T@"SBHRootSidebarController",R,N,V_contentViewController) contentViewController;
@property (T@"UIViewController<SBHVisibleContentPresenter>",&,N,V_leadingSidebarViewController) leadingSidebarViewController;
@property (T@"UIViewController<SBHVisibleContentPresenter>",&,N,V_trailingSidebarViewController) trailingSidebarViewController;
@property (TB,N,V_suppressesExtraEditingButtons) suppressesExtraEditingButtons;
@property (TB,R,N,GisLibraryPresentationModal) libraryPresentationModal;
@property (TB,R,N) hasBackgroundBlur;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_titledButtonsAlpha) titledButtonsAlpha;
@property (TQ,N,V_contentVisibility) contentVisibility;
```

## Instance methods

```
-[SBHomeScreenOverlayViewController showsDoneButton];
-[SBHomeScreenOverlayViewController isPresentingLibraryInMostForegroundState:];
-[SBHomeScreenOverlayViewController rootFolderVisualConfiguration];
-[SBHomeScreenOverlayViewController setShowsDoneButton:animated:];
-[SBHomeScreenOverlayViewController widgetButton];
-[SBHomeScreenOverlayViewController makeTitledButtonOfClass:];
-[SBHomeScreenOverlayViewController setTitledButtonsAlpha:];
-[SBHomeScreenOverlayViewController setShowsDoneButton:];
-[SBHomeScreenOverlayViewController newHomeScreenButtonBackgroundView];
-[SBHomeScreenOverlayViewController titledButtonsAlpha];
-[SBHomeScreenOverlayViewController setDoneButton:];
-[SBHomeScreenOverlayViewController doneButtonTriggered:];
-[SBHomeScreenOverlayViewController doneButton];
-[SBHomeScreenOverlayViewController viewWillDisappear:];
-[SBHomeScreenOverlayViewController contentRect];
-[SBHomeScreenOverlayViewController contentViewController];
-[SBHomeScreenOverlayViewController _updateBackgroundView];
-[SBHomeScreenOverlayViewController isDisplayingEditingButtons];
-[SBHomeScreenOverlayViewController viewWillAppear:];
-[SBHomeScreenOverlayViewController _canShowWhileLocked];
-[SBHomeScreenOverlayViewController setDelegate:];
-[SBHomeScreenOverlayViewController setPresentationProgress:];
-[SBHomeScreenOverlayViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBHomeScreenOverlayViewController viewDidAppear:];
-[SBHomeScreenOverlayViewController acquireUseSnapshotAsBackgroundViewAssertionForReason:];
-[SBHomeScreenOverlayViewController contentVisibility];
-[SBHomeScreenOverlayViewController suppressesExtraEditingButtons];
-[SBHomeScreenOverlayViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBHomeScreenOverlayViewController loadView];
-[SBHomeScreenOverlayViewController setSuppressesEditingStateForListView:];
-[SBHomeScreenOverlayViewController setContentVisibility:];
-[SBHomeScreenOverlayViewController delegate];
-[SBHomeScreenOverlayViewController presenterType];
-[SBHomeScreenOverlayViewController backgroundView];
-[SBHomeScreenOverlayViewController viewWillLayoutSubviews];
-[SBHomeScreenOverlayViewController contentWidth];
-[SBHomeScreenOverlayViewController viewDidDisappear:];
-[SBHomeScreenOverlayViewController isLibraryPresentationModal];
-[SBHomeScreenOverlayViewController setSuppressesExtraEditingButtons:];
-[SBHomeScreenOverlayViewController listLayoutProvider];
-[SBHomeScreenOverlayViewController hasBackgroundBlur];
-[SBHomeScreenOverlayViewController updateExtraButtonVisibilityAnimated:];
-[SBHomeScreenOverlayViewController contentWidthConstraint];
-[SBHomeScreenOverlayViewController bs_endAppearanceTransition:];
-[SBHomeScreenOverlayViewController contentLeadingConstraint];
-[SBHomeScreenOverlayViewController setContentLeadingConstraint:];
-[SBHomeScreenOverlayViewController bs_beginAppearanceTransition:animated:];
-[SBHomeScreenOverlayViewController bs_endAppearanceTransition];
-[SBHomeScreenOverlayViewController initWithListLayoutProvider:];
-[SBHomeScreenOverlayViewController setContentWidthConstraint:];
-[SBHomeScreenOverlayViewController presentationProgress];
-[SBHomeScreenOverlayViewController setPresentationProgress:interactive:animated:completionHandler:];
-[SBHomeScreenOverlayViewController layerPresentationProgress];
-[SBHomeScreenOverlayViewController gestureSettings];
-[SBHomeScreenOverlayViewController setFromLeading:];
-[SBHomeScreenOverlayViewController contentWidthWithContainerWidth:];
-[SBHomeScreenOverlayViewController isHeaderVisible];
-[SBHomeScreenOverlayViewController shouldUseReducedMotionAnimation];
-[SBHomeScreenOverlayViewController _button:appearAnimated:];
-[SBHomeScreenOverlayViewController _button:disappearAnimated:completion:];
-[SBHomeScreenOverlayViewController _configureMatchMoveAnimationForBackgroundView:withSourceView:];
-[SBHomeScreenOverlayViewController _updateConstraintsForPresentationProgress:];
-[SBHomeScreenOverlayViewController _updateConstraintsForPresentationProgress:layoutIfNeeded:];
-[SBHomeScreenOverlayViewController _updateLayoutForEditButtonsWithSize:];
-[SBHomeScreenOverlayViewController animatePresentationProgress:withGestureLiftOffVelocity:completionHandler:];
-[SBHomeScreenOverlayViewController buttonBackgroundView];
-[SBHomeScreenOverlayViewController childContentVisibility];
-[SBHomeScreenOverlayViewController currentSidebarViewController];
-[SBHomeScreenOverlayViewController isFromLeading];
-[SBHomeScreenOverlayViewController isTransitioningPresentationProgress];
-[SBHomeScreenOverlayViewController leadingSidebarViewController];
-[SBHomeScreenOverlayViewController overlayPresentationFloatAnimatableProperty];
-[SBHomeScreenOverlayViewController setGestureSettings:];
-[SBHomeScreenOverlayViewController setLeadingSidebarViewController:];
-[SBHomeScreenOverlayViewController setOverlayPresentationFloatAnimatableProperty:];
-[SBHomeScreenOverlayViewController setPresentationProgress:withAnimationUpdateMode:overrideAnimationSettings:completionHandler:];
-[SBHomeScreenOverlayViewController setShouldUseReducedMotionAnimation:];
-[SBHomeScreenOverlayViewController setShowsAddWidgetButton:];
-[SBHomeScreenOverlayViewController setShowsAddWidgetButton:animated:];
-[SBHomeScreenOverlayViewController setTrailingSidebarViewController:];
-[SBHomeScreenOverlayViewController setTransitioningPresentationProgress:];
-[SBHomeScreenOverlayViewController setWidgetButton:];
-[SBHomeScreenOverlayViewController showsAddWidgetButton];
-[SBHomeScreenOverlayViewController trailingSidebarViewController];
-[SBHomeScreenOverlayViewController widgetButtonTriggered:];
```
