# `_UIAlignedLayoutArrangement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UILayoutArrangement`
- Protocols: `_UIALAPropertySource`
- 2 instance variables, 11 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _alignmentConstraints;
Q _alignment;
```

## Properties

```
@property (TQ,N,V_alignment) alignment;
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
+[_UIAlignedLayoutArrangement _configurationHistoryClass];
```

## Instance methods

```
-[_UIAlignedLayoutArrangement _wantsConstraintsUsingAttributesForAxis:];
-[_UIAlignedLayoutArrangement setAxis:];
-[_UIAlignedLayoutArrangement _removeIndividualConstraintsAsNecessary];
-[_UIAlignedLayoutArrangement _alignmentConfigurationHistory];
-[_UIAlignedLayoutArrangement _axisForSpanningLayoutGuide];
-[_UIAlignedLayoutArrangement _identifierForSpanningLayoutGuide];
-[_UIAlignedLayoutArrangement _requiresNotificationForHasBaselinePropertyChanges];
-[_UIAlignedLayoutArrangement _hasStaleConfiguration];
-[_UIAlignedLayoutArrangement _addIndividualConstraintsIfPossible];
-[_UIAlignedLayoutArrangement dealloc];
-[_UIAlignedLayoutArrangement _baselineDependentConstraints];
-[_UIAlignedLayoutArrangement _usesCenteringConnectionConstraint];
-[_UIAlignedLayoutArrangement setAlignment:];
-[_UIAlignedLayoutArrangement _alignmentPropertySource];
-[_UIAlignedLayoutArrangement alignment];
-[_UIAlignedLayoutArrangement _removeConstraintGroupsAsNecessary];
-[_UIAlignedLayoutArrangement _clearAllConstraintsArrays];
-[_UIAlignedLayoutArrangement _layoutRelationForCanvasConnectionForAttribute:];
-[_UIAlignedLayoutArrangement setLayoutFillsCanvas:];
-[_UIAlignedLayoutArrangement _wantsConstraintsForAttribute:];
-[_UIAlignedLayoutArrangement _usesInequalitySpanningConstraintForAttribute:];
-[_UIAlignedLayoutArrangement _updateArrangementConstraints];
-[_UIAlignedLayoutArrangement _attributeForConstraintGroupName:];
-[_UIAlignedLayoutArrangement _wantsAmbiguitySuppressionConstraints];
-[_UIAlignedLayoutArrangement description];
-[_UIAlignedLayoutArrangement _addConstraintGroupsAsNecessary];
-[_UIAlignedLayoutArrangement setLayoutUsesCanvasMarginsWhenFilling:];
-[_UIAlignedLayoutArrangement _updateConfigurationHistory];
-[_UIAlignedLayoutArrangement _setUpConstraintForItem:referenceItem:attribute:inConstraintsTable:];
-[_UIAlignedLayoutArrangement _indexOfItemForLocationAttribute:];
-[_UIAlignedLayoutArrangement _canvasConnectionConstraintsNeedUpdatePass];
-[_UIAlignedLayoutArrangement _spanningGuideConstraintsNeedUpdate];
-[_UIAlignedLayoutArrangement initWithItems:];
```
