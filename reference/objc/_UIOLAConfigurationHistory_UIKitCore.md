# `_UIOLAConfigurationHistory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UILAConfigurationHistory`
- Protocols: `_UIOLAPropertySource`
- 9 instance variables, 19 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _baselineRelativeArrangement;
B _itemOrderingChanged;
B _itemFittingSizeChanged;
B _hasEstablishedOrderingValues;
B _inOrderedArrangementUpdateSection;
d _spacing;
q _distribution;
@"NSMapTable" _customSpacings;
d _proportionalFillDenominator;
```

## Properties

```
@property (TB,N,V_hasEstablishedOrderingValues) hasEstablishedOrderingValues;
@property (TB,N,GisInOrderedArrangementUpdateSection,V_inOrderedArrangementUpdateSection) inOrderedArrangementUpdateSection;
@property (Td,N,V_proportionalFillDenominator) proportionalFillDenominator;
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

## Instance methods

```
-[_UIOLAConfigurationHistory spacing];
-[_UIOLAConfigurationHistory _itemOrderingChanged];
-[_UIOLAConfigurationHistory setHasEstablishedOrderingValues:];
-[_UIOLAConfigurationHistory isBaselineRelativeArrangement];
-[_UIOLAConfigurationHistory _setItemFittingSizeChanged:];
-[_UIOLAConfigurationHistory setSpacing:];
-[_UIOLAConfigurationHistory isInOrderedArrangementUpdateSection];
-[_UIOLAConfigurationHistory _setItemOrderingChanged:];
-[_UIOLAConfigurationHistory customSpacingAfterItem:];
-[_UIOLAConfigurationHistory customSpacings];
-[_UIOLAConfigurationHistory setInOrderedArrangementUpdateSection:];
-[_UIOLAConfigurationHistory hasEstablishedOrderingValues];
-[_UIOLAConfigurationHistory setProportionalFillDenominator:];
-[_UIOLAConfigurationHistory distribution];
-[_UIOLAConfigurationHistory _itemFittingSizeChanged];
-[_UIOLAConfigurationHistory setCustomSpacing:afterItem:];
-[_UIOLAConfigurationHistory copyWithZone:];
-[_UIOLAConfigurationHistory setBaselineRelativeArrangement:];
-[_UIOLAConfigurationHistory setDistribution:];
-[_UIOLAConfigurationHistory proportionalFillDenominator];
```
