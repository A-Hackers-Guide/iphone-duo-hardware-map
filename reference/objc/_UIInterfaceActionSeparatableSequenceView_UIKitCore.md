# `_UIInterfaceActionSeparatableSequenceView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 11 instance variables, 9 properties, 46 instance methods, 0 class methods

## Instance variables

```
@"UILayoutGuide" _actionSequenceViewLayoutGuide;
@"NSArray" _layoutGuideConstraints;
B _visualCornerForcedOverride;
@"UIInterfaceActionVisualStyle" _visualStyle;
q _axis;
q _distribution;
@"NSArray" _arrangedContentViews;
Q _visualCornerPosition;
@"UIStackView" _stackView;
@"NSArray" _arrangedContentSeparatorViews;
@"NSArray" _arrangedContentViewsDistributionConstraints;
```

## Properties

```
@property (T@"UIStackView",R,N,V_stackView) stackView;
@property (T@"NSArray",R,N,V_arrangedContentSeparatorViews) arrangedContentSeparatorViews;
@property (T@"NSArray",R,N,V_arrangedContentViewsDistributionConstraints) arrangedContentViewsDistributionConstraints;
@property (T@"UIInterfaceActionVisualStyle",&,N,V_visualStyle) visualStyle;
@property (Tq,N,V_axis) axis;
@property (Tq,N,V_distribution) distribution;
@property (T@"NSArray",&,N,V_arrangedContentViews) arrangedContentViews;
@property (TQ,N,V_visualCornerPosition) visualCornerPosition;
@property (TB,N,V_visualCornerForcedOverride) visualCornerForcedOverride;
```

## Instance methods

```
-[_UIInterfaceActionSeparatableSequenceView layoutSublayersOfLayer:];
-[_UIInterfaceActionSeparatableSequenceView axis];
-[_UIInterfaceActionSeparatableSequenceView systemLayoutSizeFittingSize:];
-[_UIInterfaceActionSeparatableSequenceView setVisualStyle:];
-[_UIInterfaceActionSeparatableSequenceView intrinsicContentSize];
-[_UIInterfaceActionSeparatableSequenceView setAxis:];
-[_UIInterfaceActionSeparatableSequenceView _addSeparatorToStackAndMutableArray:preferSectionStyle:];
-[_UIInterfaceActionSeparatableSequenceView visualCornerPosition];
-[_UIInterfaceActionSeparatableSequenceView visualStyle];
-[_UIInterfaceActionSeparatableSequenceView setVisualCornerPosition:];
-[_UIInterfaceActionSeparatableSequenceView fittingWidthForLayoutAxis:];
-[_UIInterfaceActionSeparatableSequenceView _dimensionAttributeToConstrainEqual];
-[_UIInterfaceActionSeparatableSequenceView _markRoundedCornerPositionOnNoCornersOfView:];
-[_UIInterfaceActionSeparatableSequenceView initWithVisualStyle:];
-[_UIInterfaceActionSeparatableSequenceView _viewBoundsForStackViewFrame:];
-[_UIInterfaceActionSeparatableSequenceView _updateSeparatorConstantSizedAxis];
-[_UIInterfaceActionSeparatableSequenceView _withUnsatisfiableConstraintsLoggingSuspendedIfEngineDelegateExists:];
-[_UIInterfaceActionSeparatableSequenceView sizeThatFits:];
-[_UIInterfaceActionSeparatableSequenceView arrangedContentViews];
-[_UIInterfaceActionSeparatableSequenceView actionSequenceViewLayoutGuide];
-[_UIInterfaceActionSeparatableSequenceView arrangedContentViewsDistributionConstraints];
-[_UIInterfaceActionSeparatableSequenceView _systemLayoutSizeFittingStackView:];
-[_UIInterfaceActionSeparatableSequenceView setVisualCornerForcedOverride:];
-[_UIInterfaceActionSeparatableSequenceView _markRoundedCornerPositionOnAllCornersOfView:];
-[_UIInterfaceActionSeparatableSequenceView _reloadStackViewArrangement];
-[_UIInterfaceActionSeparatableSequenceView _separatorConstantSizedAxis];
-[_UIInterfaceActionSeparatableSequenceView _updateLayoutWithStackFrameForActionSequenceEdgeInsets];
-[_UIInterfaceActionSeparatableSequenceView _reloadContentDistributionConstraintsForArrangedContentViews];
-[_UIInterfaceActionSeparatableSequenceView _stackViewFrameForViewBounds:];
-[_UIInterfaceActionSeparatableSequenceView arrangedContentSeparatorViews];
-[_UIInterfaceActionSeparatableSequenceView stackView];
-[_UIInterfaceActionSeparatableSequenceView updateConstraints];
-[_UIInterfaceActionSeparatableSequenceView distribution];
-[_UIInterfaceActionSeparatableSequenceView _updateRoundedCornerPositionForActionRepViews];
-[_UIInterfaceActionSeparatableSequenceView _updateActionSpacing];
-[_UIInterfaceActionSeparatableSequenceView visualCornerForcedOverride];
-[_UIInterfaceActionSeparatableSequenceView reloadDisplayedContentVisualStyle];
-[_UIInterfaceActionSeparatableSequenceView setArrangedContentViews:];
-[_UIInterfaceActionSeparatableSequenceView updateContentLayoutGuideConstraints];
-[_UIInterfaceActionSeparatableSequenceView _isVerticalLayout];
-[_UIInterfaceActionSeparatableSequenceView _setRoundedCornersOfView:toCornerPosition:];
-[_UIInterfaceActionSeparatableSequenceView setDistribution:];
-[_UIInterfaceActionSeparatableSequenceView _setLayoutDebuggingIdentifier:];
-[_UIInterfaceActionSeparatableSequenceView _markRoundedCornerPositionOnTrailingEdgeOfView:];
-[_UIInterfaceActionSeparatableSequenceView _updateActionRepresentationViewsCanRemoveContentFromHierarchyWhenNotVisibleSetting];
-[_UIInterfaceActionSeparatableSequenceView _markRoundedCornerPositionOnLeadingEdgeOfView:];
```
