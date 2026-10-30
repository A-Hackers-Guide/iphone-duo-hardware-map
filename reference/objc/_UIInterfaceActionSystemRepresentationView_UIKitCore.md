# `_UIInterfaceActionSystemRepresentationView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInterfaceActionRepresentationView`
- Protocols: `UIInterfaceActionDisplayPropertyObserver`
- 7 instance variables, 11 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"_UIInterfaceActionImagePropertyView" _leadingImageView;
@"_UIInterfaceActionImagePropertyView" _trailingImageView;
@"_UIInterfaceActionLabelsPropertyView" _labelsView;
@"NSSet" _viewsToDisplayWhenContentsVisible;
@"NSSet" _displayedViews;
@"NSArray" _displayedViewsSpacingConstraints;
@"NSArray" _displayedViewsPositioningConstraints;
```

## Properties

```
@property (T@"_UIInterfaceActionImagePropertyView",R,N,V_leadingImageView) leadingImageView;
@property (T@"_UIInterfaceActionImagePropertyView",R,N,V_trailingImageView) trailingImageView;
@property (T@"_UIInterfaceActionLabelsPropertyView",R,N,V_labelsView) labelsView;
@property (T@"NSSet",&,N,V_viewsToDisplayWhenContentsVisible) viewsToDisplayWhenContentsVisible;
@property (T@"NSSet",&,N,V_displayedViews) displayedViews;
@property (T@"NSArray",R,N,V_displayedViewsSpacingConstraints) displayedViewsSpacingConstraints;
@property (T@"NSArray",R,N,V_displayedViewsPositioningConstraints) displayedViewsPositioningConstraints;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIInterfaceActionSystemRepresentationView updateContentsInsertedIntoHierarchy];
-[_UIInterfaceActionSystemRepresentationView initWithAction:];
-[_UIInterfaceActionSystemRepresentationView _applyVisualStyle];
-[_UIInterfaceActionSystemRepresentationView interfaceAction:reloadDisplayedContentVisualStyle:];
-[_UIInterfaceActionSystemRepresentationView updateConstraints];
-[_UIInterfaceActionSystemRepresentationView interfaceAction:reloadDisplayedContentActionProperties:];
-[_UIInterfaceActionSystemRepresentationView _activateDisplayedViewsConstraints];
-[_UIInterfaceActionSystemRepresentationView _applyVisualStyleToDisplayedViews];
-[_UIInterfaceActionSystemRepresentationView _arrangeDisplayedViews];
-[_UIInterfaceActionSystemRepresentationView _constraintForBaselineAligningOrVerticallyCenteringImageViewToLabelsView:];
-[_UIInterfaceActionSystemRepresentationView _constraintForVerticallyCenteringLabelsView];
-[_UIInterfaceActionSystemRepresentationView _constraintsForHorizontallyCenteringLabelsView];
-[_UIInterfaceActionSystemRepresentationView _constraintsForInsettingImageViewsLeadingAndTrailingEdge];
-[_UIInterfaceActionSystemRepresentationView _constraintsForInsettingLabelsViewLeadingAndTrailing];
-[_UIInterfaceActionSystemRepresentationView _constraintsForInsettingLabelsViewLeadingAndTrailingHorizontalEdgeReferenceExact:];
-[_UIInterfaceActionSystemRepresentationView _constraintsForInsettingLabelsViewLeadingAndTrailingToImageViewsExact:];
-[_UIInterfaceActionSystemRepresentationView _constraintsToEnsureContainerHeightTallEnoughForViews:];
-[_UIInterfaceActionSystemRepresentationView _displayedViewsConstraintsNeedsLoading];
-[_UIInterfaceActionSystemRepresentationView _hasLoadedContents];
-[_UIInterfaceActionSystemRepresentationView _horizontalEdgeReference];
-[_UIInterfaceActionSystemRepresentationView _invalidateDisplayedViewsConstraints];
-[_UIInterfaceActionSystemRepresentationView _isDisplayingLeadingImageView];
-[_UIInterfaceActionSystemRepresentationView _isDisplayingTrailingImageView];
-[_UIInterfaceActionSystemRepresentationView _loadConstraintsForDisplayedViews];
-[_UIInterfaceActionSystemRepresentationView _loadConstraintsForLabelsAndImagesDisplay];
-[_UIInterfaceActionSystemRepresentationView _loadConstraintsForLabelsOnlyDisplay];
-[_UIInterfaceActionSystemRepresentationView _reloadHierarchyWithViewsToDisplayWhenContentsVisible];
-[_UIInterfaceActionSystemRepresentationView _reloadViewsToDisplayWhenContentsVisible];
-[_UIInterfaceActionSystemRepresentationView _removeAllDisplayedViews];
-[_UIInterfaceActionSystemRepresentationView _updateDisplayedViewsConstraintsVisualStyleConstants];
-[_UIInterfaceActionSystemRepresentationView displayedViews];
-[_UIInterfaceActionSystemRepresentationView displayedViewsPositioningConstraints];
-[_UIInterfaceActionSystemRepresentationView displayedViewsSpacingConstraints];
-[_UIInterfaceActionSystemRepresentationView labelsView];
-[_UIInterfaceActionSystemRepresentationView leadingImageView];
-[_UIInterfaceActionSystemRepresentationView loadContents];
-[_UIInterfaceActionSystemRepresentationView setDisplayedViews:];
-[_UIInterfaceActionSystemRepresentationView setViewsToDisplayWhenContentsVisible:];
-[_UIInterfaceActionSystemRepresentationView trailingImageView];
-[_UIInterfaceActionSystemRepresentationView viewsToDisplayWhenContentsVisible];
```
