# `_UILAConfigurationHistory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UILAPropertySource`, `NSCopying`
- 8 instance variables, 12 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _newlyHiddenItems;
@"NSMutableSet" _newlyUnhiddenItems;
@"NSMutableSet" _invalidBaselineConstraints;
B _layoutFillsCanvas;
B _layoutUsesCanvasMarginsWhenFilling;
B _hasEstablishedBaseValues;
B _inLayoutArrangementUpdateSection;
q _axis;
```

## Properties

```
@property (TB,N,V_hasEstablishedBaseValues) hasEstablishedBaseValues;
@property (TB,N,GisInLayoutArrangementUpdateSection,V_inLayoutArrangementUpdateSection) inLayoutArrangementUpdateSection;
@property (Tq,N,V_axis) axis;
@property (TB,N,V_layoutFillsCanvas) layoutFillsCanvas;
@property (TB,N,V_layoutUsesCanvasMarginsWhenFilling) layoutUsesCanvasMarginsWhenFilling;
@property (T@"NSSet",R,N,V_newlyHiddenItems) _newlyHiddenItems;
@property (T@"NSSet",R,N,V_newlyUnhiddenItems) _newlyUnhiddenItems;
@property (T@"NSSet",R,N,V_invalidBaselineConstraints) invalidBaselineConstraints;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UILAConfigurationHistory axis];
-[_UILAConfigurationHistory setAxis:];
-[_UILAConfigurationHistory init];
-[_UILAConfigurationHistory setLayoutFillsCanvas:];
-[_UILAConfigurationHistory _invalidateBaselineConstraint:];
-[_UILAConfigurationHistory layoutFillsCanvas];
-[_UILAConfigurationHistory _newlyUnhiddenItems];
-[_UILAConfigurationHistory invalidBaselineConstraints];
-[_UILAConfigurationHistory setLayoutUsesCanvasMarginsWhenFilling:];
-[_UILAConfigurationHistory layoutUsesCanvasMarginsWhenFilling];
-[_UILAConfigurationHistory copyWithZone:];
-[_UILAConfigurationHistory _newlyHiddenItems];
-[_UILAConfigurationHistory hasEstablishedBaseValues];
-[_UILAConfigurationHistory isInLayoutArrangementUpdateSection];
-[_UILAConfigurationHistory setHasEstablishedBaseValues:];
-[_UILAConfigurationHistory setInLayoutArrangementUpdateSection:];
```
