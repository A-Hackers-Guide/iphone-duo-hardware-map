# `_UILayoutArrangement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UILAPropertySource`
- 16 instance variables, 21 properties, 74 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _incomingItems;
@"NSMutableSet" _outgoingItems;
@"NSMutableSet" _hiddenItems;
@"NSMutableSet" _newlyHiddenItems;
@"NSMutableSet" _newlyUnhiddenItems;
@"NSMutableSet" _invalidBaselineConstraints;
@"NSMutableArray" _canvasConnectionConstraints;
B _awaitingAnimationLayoutPass;
B _layoutFillsCanvas;
B _layoutUsesCanvasMarginsWhenFilling;
@"_UILAConfigurationHistory" _unanimatedConfigurationTarget;
@"NSMutableArray" _mutableItems;
@"_UILayoutSpacer" _spanningLayoutGuide;
@"_UILAConfigurationHistory" _configurationHistory;
@"UIView" _canvas;
q _axis;
```

## Properties

```
@property (T@"NSMutableArray",&,N,S_setMutableItems:,V_mutableItems) _mutableItems;
@property (T@"NSSet",R,N) _hiddenItems;
@property (T@"NSSet",R,N) _incomingItems;
@property (T@"NSSet",R,N) _outgoingItems;
@property (T@"_UILAConfigurationHistory",&,N,S_setUnanimatedConfigurationTarget:,V_unanimatedConfigurationTarget) _unanimatedConfigurationTarget;
@property (TB,R,N,V_awaitingAnimationLayoutPass) _awaitingAnimationLayoutPass;
@property (T@"<_UILAPropertySource>",R,N) _propertySource;
@property (T@"_UILayoutSpacer",R,&,N,V_spanningLayoutGuide) _spanningLayoutGuide;
@property (T@"_UILAConfigurationHistory",R,&,N,V_configurationHistory) _configurationHistory;
@property (TB,N,V_layoutFillsCanvas) layoutFillsCanvas;
@property (TB,N,V_layoutUsesCanvasMarginsWhenFilling) layoutUsesCanvasMarginsWhenFilling;
@property (T@"UIView",W,N,V_canvas) canvas;
@property (Tq,N,V_axis) axis;
@property (T@"NSArray",R,C,N) items;
@property (T@"NSSet",R,N) _newlyHiddenItems;
@property (T@"NSSet",R,N) _newlyUnhiddenItems;
@property (T@"NSSet",R,N,V_invalidBaselineConstraints) invalidBaselineConstraints;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UILayoutArrangement _configurationHistoryClass];
```

## Instance methods

```
-[_UILayoutArrangement _hiddenItems];
-[_UILayoutArrangement axis];
-[_UILayoutArrangement _awaitingAnimationLayoutPass];
-[_UILayoutArrangement _removeSpanningLayoutGuide];
-[_UILayoutArrangement _viewOrGuideForLocationAttribute:];
-[_UILayoutArrangement setAxis:];
-[_UILayoutArrangement _intrinsicContentSizeInvalidatedForItem:];
-[_UILayoutArrangement _setLayoutUsesCanvasMarginsWhenFilling:notify:];
-[_UILayoutArrangement _allItemsHidden];
-[_UILayoutArrangement _axisForSpanningLayoutGuide];
-[_UILayoutArrangement init];
-[_UILayoutArrangement _identifierForSpanningLayoutGuide];
-[_UILayoutArrangement _requiresNotificationForHasBaselinePropertyChanges];
-[_UILayoutArrangement _hasStaleConfiguration];
-[_UILayoutArrangement _minAttributeForCanvasConnections];
-[_UILayoutArrangement _trackChangesWithConfigBlock:];
-[_UILayoutArrangement _baselineDependentConstraints];
-[_UILayoutArrangement _propertySource];
-[_UILayoutArrangement _spanningLayoutGuideFittingPriority];
-[_UILayoutArrangement _updateCanvasConnectionConstraintsIfNecessary];
-[_UILayoutArrangement _usesCenteringConnectionConstraint];
-[_UILayoutArrangement initWithItems:onAxis:];
-[_UILayoutArrangement _registerAnimationRequest];
-[_UILayoutArrangement items];
-[_UILayoutArrangement _setMutableItems:];
-[_UILayoutArrangement removeItem:];
-[_UILayoutArrangement _unanimatedConfigurationTarget];
-[_UILayoutArrangement _spanningLayoutGuideCreateIfNecessary];
-[_UILayoutArrangement _configurationHistory];
-[_UILayoutArrangement _clearAllConstraintsArrays];
-[_UILayoutArrangement _systemLayoutFittingSizeDidChangeForItem:];
-[_UILayoutArrangement _setLayoutFillsCanvas:notify:];
-[_UILayoutArrangement _visibilityParameterChangedForItem:];
-[_UILayoutArrangement _layoutRelationForCanvasConnectionForAttribute:];
-[_UILayoutArrangement setLayoutFillsCanvas:];
-[_UILayoutArrangement _hasBaselineChangedNotificationRequirementDidChange];
-[_UILayoutArrangement _monitorsSystemLayoutFittingSizeForItem:];
-[_UILayoutArrangement _usesInequalitySpanningConstraintForAttribute:];
-[_UILayoutArrangement addItem:];
-[_UILayoutArrangement _dimensionAttributeForCurrentAxis];
-[_UILayoutArrangement _invalidateBaselineConstraint:];
-[_UILayoutArrangement _spanningLayoutGuide];
-[_UILayoutArrangement _incomingItems];
-[_UILayoutArrangement _updateArrangementConstraints];
-[_UILayoutArrangement layoutFillsCanvas];
-[_UILayoutArrangement _newlyUnhiddenItems];
-[_UILayoutArrangement _centerAttributeForCanvasConnections];
-[_UILayoutArrangement _spanningLayoutGuideAlwaysUsesFittingConstraint];
-[_UILayoutArrangement description];
-[_UILayoutArrangement _updateSpanningLayoutGuideConstraintsIfNecessary];
-[_UILayoutArrangement invalidBaselineConstraints];
-[_UILayoutArrangement _setAxis:notify:];
-[_UILayoutArrangement _hasBaselineChangedNotification:];
-[_UILayoutArrangement _createUnanimatedConfigurationTargetIfNecessary];
-[_UILayoutArrangement canvas];
-[_UILayoutArrangement insertItem:atIndex:];
-[_UILayoutArrangement setLayoutUsesCanvasMarginsWhenFilling:];
-[_UILayoutArrangement layoutUsesCanvasMarginsWhenFilling];
-[_UILayoutArrangement _updateConfigurationHistory];
-[_UILayoutArrangement _indexOfItemForLocationAttribute:];
-[_UILayoutArrangement _setUnanimatedConfigurationTarget:];
-[_UILayoutArrangement _itemWantsLayoutAsIfVisible:];
-[_UILayoutArrangement _newlyHiddenItems];
-[_UILayoutArrangement _configurationRequiresCanvasConnectionFittingConstraint];
-[_UILayoutArrangement _didEvaluateMultilineHeightForView:];
-[_UILayoutArrangement _createSpanningLayoutGuide];
-[_UILayoutArrangement _mutableItems];
-[_UILayoutArrangement _respondToChangesWithIncomingItem:outgoingItem:newlyHiddenItem:newlyUnhiddenItem:];
-[_UILayoutArrangement setCanvas:];
-[_UILayoutArrangement _clearCanvasConnectionConstraints];
-[_UILayoutArrangement _canvasConnectionConstraintsNeedUpdatePass];
-[_UILayoutArrangement _spanningGuideConstraintsNeedUpdate];
-[_UILayoutArrangement initWithItems:];
-[_UILayoutArrangement _outgoingItems];
```
