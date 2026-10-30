# `_UIInterfaceActionRepresentationsSequenceView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIScrollView`
- 9 instance variables, 8 properties, 39 instance methods, 0 class methods

## Instance variables

```
q _sizingSeparatedContentSequenceViewToFitDisabledCount;
B _visualCornerForcedOverride;
@"UIInterfaceActionVisualStyle" _visualStyle;
@"NSArray" _arrangedActionRepresentationViews;
q _actionLayoutAxis;
Q _visualCornerPosition;
@"NSLayoutConstraint" _minimumHeightConstraint;
@"_UIInterfaceActionSeparatableSequenceView" _separatedContentSequenceView;
@"UIView" _backgroundView;
```

## Properties

```
@property (T@"NSLayoutConstraint",R,N,V_minimumHeightConstraint) minimumHeightConstraint;
@property (T@"_UIInterfaceActionSeparatableSequenceView",R,N,V_separatedContentSequenceView) separatedContentSequenceView;
@property (T@"UIView",&,N,V_backgroundView) backgroundView;
@property (T@"UIInterfaceActionVisualStyle",&,N,V_visualStyle) visualStyle;
@property (T@"NSArray",&,N,V_arrangedActionRepresentationViews) arrangedActionRepresentationViews;
@property (Tq,N,V_actionLayoutAxis) actionLayoutAxis;
@property (TQ,N,V_visualCornerPosition) visualCornerPosition;
@property (TB,N,V_visualCornerForcedOverride) visualCornerForcedOverride;
```

## Instance methods

```
-[_UIInterfaceActionRepresentationsSequenceView systemLayoutSizeFittingSize:];
-[_UIInterfaceActionRepresentationsSequenceView setVisualStyle:];
-[_UIInterfaceActionRepresentationsSequenceView _systemDefaultFocusGroupIdentifier];
-[_UIInterfaceActionRepresentationsSequenceView intrinsicContentSize];
-[_UIInterfaceActionRepresentationsSequenceView visualCornerPosition];
-[_UIInterfaceActionRepresentationsSequenceView visualStyle];
-[_UIInterfaceActionRepresentationsSequenceView setVisualCornerPosition:];
-[_UIInterfaceActionRepresentationsSequenceView didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIInterfaceActionRepresentationsSequenceView _notifyDidScroll];
-[_UIInterfaceActionRepresentationsSequenceView _applyVisualStyleToSeparatedContentSequenceView];
-[_UIInterfaceActionRepresentationsSequenceView arrangedActionRepresentationViews];
-[_UIInterfaceActionRepresentationsSequenceView fittingWidthForLayoutAxis:];
-[_UIInterfaceActionRepresentationsSequenceView _updateBackgroundView];
-[_UIInterfaceActionRepresentationsSequenceView _disableSeparatedContentSequenceViewToFit];
-[_UIInterfaceActionRepresentationsSequenceView layoutSubviews];
-[_UIInterfaceActionRepresentationsSequenceView _loadDefaultSizingConstraints];
-[_UIInterfaceActionRepresentationsSequenceView _temporarilySkipSizingSeparatedContentSequenceViewToFit];
-[_UIInterfaceActionRepresentationsSequenceView initWithVisualStyle:];
-[_UIInterfaceActionRepresentationsSequenceView _contentFitCanScrollThreshold];
-[_UIInterfaceActionRepresentationsSequenceView setArrangedActionRepresentationViews:];
-[_UIInterfaceActionRepresentationsSequenceView separatedContentSequenceView];
-[_UIInterfaceActionRepresentationsSequenceView _enableSeparatedContentSequenceViewToFit];
-[_UIInterfaceActionRepresentationsSequenceView setActionLayoutAxis:];
-[_UIInterfaceActionRepresentationsSequenceView actionSequenceViewLayoutGuide];
-[_UIInterfaceActionRepresentationsSequenceView setVisualCornerForcedOverride:];
-[_UIInterfaceActionRepresentationsSequenceView _applyVisualStyle];
-[_UIInterfaceActionRepresentationsSequenceView backgroundView];
-[_UIInterfaceActionRepresentationsSequenceView _updateMinimumHeightConstraint];
-[_UIInterfaceActionRepresentationsSequenceView _isHorizontalLayout];
-[_UIInterfaceActionRepresentationsSequenceView updateConstraints];
-[_UIInterfaceActionRepresentationsSequenceView _sizeByApplyingLayoutMarginsAsOutsetToSize:];
-[_UIInterfaceActionRepresentationsSequenceView visualCornerForcedOverride];
-[_UIInterfaceActionRepresentationsSequenceView reloadDisplayedContentVisualStyle];
-[_UIInterfaceActionRepresentationsSequenceView setBackgroundView:];
-[_UIInterfaceActionRepresentationsSequenceView minimumHeightConstraint];
-[_UIInterfaceActionRepresentationsSequenceView _updateSeparatedContentSequenceViewToFitSizeIfPossible];
-[_UIInterfaceActionRepresentationsSequenceView _willUpdateFocusInContext:];
-[_UIInterfaceActionRepresentationsSequenceView _minimumNumberOfRowsRequiredVisible];
-[_UIInterfaceActionRepresentationsSequenceView actionLayoutAxis];
```
