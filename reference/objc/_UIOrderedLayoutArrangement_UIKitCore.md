# `_UIOrderedLayoutArrangement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UILayoutArrangement`
- Protocols: `_UIOLAPropertySource`
- 13 instance variables, 16 properties, 72 instance methods, 1 class methods

## Instance variables

```
@"NSMapTable" _spacingOrCenteringGuides;
@"NSMapTable" _edgeToEdgeConstraintsForVisibleItems;
@"NSMapTable" _edgeToEdgeConstraintsForHiddenItems;
@"NSMapTable" _relatedDimensionConstraints;
@"NSMapTable" _hidingDimensionConstraints;
@"NSMapTable" _multilineTextWidthDisambiguationConstraints;
@"NSMapTable" _customSpacings;
d _proportionalFillDenominator;
B _itemOrderingChanged;
B _itemFittingSizeChanged;
B _baselineRelativeArrangement;
d _spacing;
q _distribution;
```

## Properties

```
@property (Td,N,V_spacing) spacing;
@property (TB,N,GisBaselineRelativeArrangement,V_baselineRelativeArrangement) baselineRelativeArrangement;
@property (Tq,N,V_distribution) distribution;
@property (TB,N,S_setItemOrderingChanged:,V_itemOrderingChanged) _itemOrderingChanged;
@property (TB,N,S_setItemFittingSizeChanged:,V_itemFittingSizeChanged) _itemFittingSizeChanged;
@property (T@"NSMapTable",R,N,V_customSpacings) customSpacings;
@property (Tq,N) axis;
@property (TB,N) layoutFillsCanvas;
@property (TB,N) layoutUsesCanvasMarginsWhenFilling;
@property (T@"NSSet",R,N) _newlyHiddenItems;
@property (T@"NSSet",R,N) _newlyUnhiddenItems;
@property (T@"NSSet",R,N) invalidBaselineConstraints;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIOrderedLayoutArrangement _configurationHistoryClass];
```

## Instance methods

```
-[_UIOrderedLayoutArrangement spacing];
-[_UIOrderedLayoutArrangement _orderedConfigurationHistory];
-[_UIOrderedLayoutArrangement _adjustConstraintConstantsIfPossible];
-[_UIOrderedLayoutArrangement _visibleItemAtEndWithEnumerationOptions:];
-[_UIOrderedLayoutArrangement _removeIndividualGuidesAndConstraintsAsNecessary];
-[_UIOrderedLayoutArrangement _tallestItem];
-[_UIOrderedLayoutArrangement _preparedImprovedMultilineTextWidthDisambiguationConstraintForItem:numberOfVisibleMultilineItems:];
-[_UIOrderedLayoutArrangement setAxis:];
-[_UIOrderedLayoutArrangement _intrinsicContentSizeInvalidatedForItem:];
-[_UIOrderedLayoutArrangement _itemOrderingChanged];
-[_UIOrderedLayoutArrangement _identifierForSpanningLayoutGuide];
-[_UIOrderedLayoutArrangement _baselineViewVendTallest:forFirstBaseline:];
-[_UIOrderedLayoutArrangement _calculatedIntrinsicHeight];
-[_UIOrderedLayoutArrangement _hasStaleConfiguration];
-[_UIOrderedLayoutArrangement _expectedEdgeToEdgeSpacingForPrecedingItem:followingItem:isPrecededByVisibleItem:isFollowedByVisibleItem:];
-[_UIOrderedLayoutArrangement _dimensionRefItemFromConstraint:];
-[_UIOrderedLayoutArrangement dealloc];
-[_UIOrderedLayoutArrangement _minAttributeForGapConstraint];
-[_UIOrderedLayoutArrangement _activateAndInsertEdgeToEdgeConstraintForGapBetweenSpanningLayoutGuide:hiddenItem:];
-[_UIOrderedLayoutArrangement _cleanUpGuides];
-[_UIOrderedLayoutArrangement _cleanUpEdgeToEdgeConstraintsForHiddenItemsForItem:atIndex:processAdjacentHiddenItems:];
-[_UIOrderedLayoutArrangement removeItem:];
-[_UIOrderedLayoutArrangement _itemCountChanged];
-[_UIOrderedLayoutArrangement _insertIndividualGuidesAndConstraintsAsNecessary];
-[_UIOrderedLayoutArrangement isBaselineRelativeArrangement];
-[_UIOrderedLayoutArrangement _maxAttributeForGapConstraintRespectingBaselineRelative:];
-[_UIOrderedLayoutArrangement _setItemFittingSizeChanged:];
-[_UIOrderedLayoutArrangement setSpacing:];
-[_UIOrderedLayoutArrangement _setUpHidingDimensionConstraintForItem:];
-[_UIOrderedLayoutArrangement _clearAllConstraintsArrays];
-[_UIOrderedLayoutArrangement _setItemOrderingChanged:];
-[_UIOrderedLayoutArrangement _systemLayoutFittingSizeDidChangeForItem:];
-[_UIOrderedLayoutArrangement _constantForMultilineTextWidthDisambiguationConstraintWithNumberOfRelevantItems:];
-[_UIOrderedLayoutArrangement _visibilityParameterChangedForItem:];
-[_UIOrderedLayoutArrangement customSpacingAfterItem:];
-[_UIOrderedLayoutArrangement _wantsProportionalDistribution];
-[_UIOrderedLayoutArrangement setLayoutFillsCanvas:];
-[_UIOrderedLayoutArrangement _monitorsSystemLayoutFittingSizeForItem:];
-[_UIOrderedLayoutArrangement _precedingLocationAttributeForGuideConstraint];
-[_UIOrderedLayoutArrangement _hasStaleSpacing];
-[_UIOrderedLayoutArrangement customSpacings];
-[_UIOrderedLayoutArrangement _updateArrangementConstraints];
-[_UIOrderedLayoutArrangement _activateAndInsertEdgeToEdgeConstraintForGapBetweenPrecedingItem:followingItem:isPrecededByVisibleItem:isFollowedByVisibleItem:isHidden:];
-[_UIOrderedLayoutArrangement _cleanUpEdgeToEdgeConstraintsForVisibleItemsForItem:atIndex:processPrecedingVisibleItem:];
-[_UIOrderedLayoutArrangement description];
-[_UIOrderedLayoutArrangement _setUpSpacingOrCenteringGuideForGapIndex:];
-[_UIOrderedLayoutArrangement _setUpMultilineTextWidthDisambiguationConstraintForItem:numberOfVisibleMultilineItems:];
-[_UIOrderedLayoutArrangement _firstVisibleItem];
-[_UIOrderedLayoutArrangement distribution];
-[_UIOrderedLayoutArrangement _itemFittingSizeChanged];
-[_UIOrderedLayoutArrangement _orderedPropertySource];
-[_UIOrderedLayoutArrangement _minAttributeForGapConstraintRespectingBaselineRelative:];
-[_UIOrderedLayoutArrangement _trackChangesAffectingExternalBaselineConstraints:];
-[_UIOrderedLayoutArrangement insertItem:atIndex:];
-[_UIOrderedLayoutArrangement _cleanUpWithoutResettingKeepAliveWorkaround];
-[_UIOrderedLayoutArrangement setLayoutUsesCanvasMarginsWhenFilling:];
-[_UIOrderedLayoutArrangement setCustomSpacing:afterItem:];
-[_UIOrderedLayoutArrangement _lastVisibleItem];
-[_UIOrderedLayoutArrangement _updateConfigurationHistory];
-[_UIOrderedLayoutArrangement _preparedFaultyCompatibleMultilineTextWidthDisambiguationConstraintForItem:];
-[_UIOrderedLayoutArrangement _indexOfItemForLocationAttribute:];
-[_UIOrderedLayoutArrangement setBaselineRelativeArrangement:];
-[_UIOrderedLayoutArrangement _configurationRequiresCanvasConnectionFittingConstraint];
-[_UIOrderedLayoutArrangement _setUpDimensionConstraintForItem:referenceItem:atIndex:];
-[_UIOrderedLayoutArrangement _removeGuideAndConstraintGroupsAsNecessary];
-[_UIOrderedLayoutArrangement _didEvaluateMultilineHeightForView:];
-[_UIOrderedLayoutArrangement _notifyCanvasesBaselineParametersDidChange];
-[_UIOrderedLayoutArrangement _edgeToEdgeConstraintForGapBetweenPrecedingItem:followingItem:isPrecededByVisibleItem:isFollowedByVisibleItem:];
-[_UIOrderedLayoutArrangement _canvasConnectionConstraintsNeedUpdatePass];
-[_UIOrderedLayoutArrangement setDistribution:];
-[_UIOrderedLayoutArrangement _customSpacingChanged];
-[_UIOrderedLayoutArrangement _cleanUpGuideAtGapFollowingItem:];
```
