# `_UIContextMenuSection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _identifier;
B _overridesCellSizeForLargeText;
B _isRoot;
B _wantsSectionSeparator;
B _isMultiColorPalette;
B _containsLargeCellWithVisibleImage;
B _wantsContentMarginsForSelection;
@"NSString" _title;
@"UIAction" _accessoryAction;
q _preferredCellSize;
q _layout;
Q _actionLineLimit;
```

## Properties

```
@property (TB,N,V_isRoot) isRoot;
@property (TB,N,V_wantsSectionSeparator) wantsSectionSeparator;
@property (T@"NSString",R,N,V_title) title;
@property (T@"UIAction",R,N,V_accessoryAction) accessoryAction;
@property (Tq,R,N,V_preferredCellSize) preferredCellSize;
@property (Tq,R,N,V_layout) layout;
@property (TQ,R,N,V_actionLineLimit) actionLineLimit;
@property (TB,R,N,V_isMultiColorPalette) isMultiColorPalette;
@property (TB,R,N,V_containsLargeCellWithVisibleImage) containsLargeCellWithVisibleImage;
@property (TB,R,N,V_wantsContentMarginsForSelection) wantsContentMarginsForSelection;
```

## Class methods

```
+[_UIContextMenuSection sectionWithMenu:prefersVisibleImages:];
```

## Instance methods

```
-[_UIContextMenuSection isRoot];
-[_UIContextMenuSection isMultiColorPalette];
-[_UIContextMenuSection wantsSectionSeparator];
-[_UIContextMenuSection setIsRoot:];
-[_UIContextMenuSection cellSizeGivenTraits:];
-[_UIContextMenuSection title];
-[_UIContextMenuSection setWantsSectionSeparator:];
-[_UIContextMenuSection accessoryAction];
-[_UIContextMenuSection hash];
-[_UIContextMenuSection containsLargeCellWithVisibleImage];
-[_UIContextMenuSection actionLineLimit];
-[_UIContextMenuSection layout];
-[_UIContextMenuSection wantsContentMarginsForSelection];
-[_UIContextMenuSection isEqual:];
-[_UIContextMenuSection preferredCellSize];
```
