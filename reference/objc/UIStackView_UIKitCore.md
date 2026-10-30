# `UIStackView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 7 properties, 43 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _mutableLayoutArrangements;
@"_UIOrderedLayoutArrangement" _distributionArrangement;
@"_UIAlignedLayoutArrangement" _alignmentArrangement;
B _didRequestTallestBaselineViewForFirst;
B _didRequestTallestBaselineViewForLast;
B _viewForFirstBaselineLayoutDidChange;
B _viewForLastBaselineLayoutDidChange;
B _layoutMarginsRelativeArrangement;
```

## Properties

```
@property (T@"NSArray",R,C,N) arrangedSubviews;
@property (Tq,N) axis;
@property (Tq,N) distribution;
@property (Tq,N) alignment;
@property (Td,N) spacing;
@property (TB,N,GisBaselineRelativeArrangement) baselineRelativeArrangement;
@property (TB,N,GisLayoutMarginsRelativeArrangement,V_layoutMarginsRelativeArrangement) layoutMarginsRelativeArrangement;
```

## Class methods

```
+[UIStackView layerClass];
```

## Instance methods

```
-[UIStackView spacing];
-[UIStackView axis];
-[UIStackView _intrinsicContentSizeInvalidatedForChildView:];
-[UIStackView setAxis:];
-[UIStackView _calculatedIntrinsicHeight];
-[UIStackView initWithArrangedSubviews:];
-[UIStackView setOpaque:];
-[UIStackView viewForLastBaselineLayout];
-[UIStackView setAlignment:];
-[UIStackView setTranslatesAutoresizingMaskIntoConstraints:];
-[UIStackView setArrangedSubviews:];
-[UIStackView setBackgroundColor:];
-[UIStackView alignment];
-[UIStackView isBaselineRelativeArrangement];
-[UIStackView setSpacing:];
-[UIStackView viewForFirstBaselineLayout];
-[UIStackView encodeWithCoder:];
-[UIStackView description];
-[UIStackView updateConstraints];
-[UIStackView initWithCoder:];
-[UIStackView distribution];
-[UIStackView arrangedSubviews];
-[UIStackView setBaselineRelativeArrangement:];
-[UIStackView initWithFrame:];
-[UIStackView setDistribution:];
-[UIStackView _ola_isCandidateForMultilineTextWidthDisambiguationWhenArranged];
-[UIStackView _baselineViewForFirst:];
-[UIStackView _commonStackViewInitializationWithArrangedSubviews:];
-[UIStackView _hasLayoutArrangements];
-[UIStackView _mutableLayoutArrangements];
-[UIStackView _proportionalFillLengthForOrderedArrangement:relevantParentAxis:];
-[UIStackView _recordBaselineLoweringInfo];
-[UIStackView _shouldRequestTallestBaselineViewForFirst:];
-[UIStackView _systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:hasIntentionallyCollapsedHeight:];
-[UIStackView _vendedBaselineViewDidMoveForFirst:];
-[UIStackView _vendedBaselineViewParametersDidChange];
-[UIStackView addArrangedSubview:];
-[UIStackView customSpacingAfterView:];
-[UIStackView insertArrangedSubview:atIndex:];
-[UIStackView isLayoutMarginsRelativeArrangement];
-[UIStackView removeArrangedSubview:];
-[UIStackView setCustomSpacing:afterView:];
-[UIStackView setLayoutMarginsRelativeArrangement:];
```
