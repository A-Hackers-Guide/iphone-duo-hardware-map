# `UICellConfigurationState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewConfigurationState`
- Protocols: `_UICellConfigurationStateReadonly`
- 2 instance variables, 21 properties, 28 instance methods, 1 class methods

## Instance variables

```
{?="isEditing"b1"isExpanded"b1"isSwiped"b1"isReordering"b1"cellDragState"b2"cellDropState"b2"usesAnyPlainListStyle"b1"inMultiSelectGroup"b1"typeSelectState"b2"edgesAbuttingAccessories"b4} _cellStateFlags;
q __typeSelectState;
```

## Properties

```
@property (TB,N,S_setUsesAnyPlainListStyle:) _usesAnyPlainListStyle;
@property (TB,N,S_setInMultiSelectGroup:) _inMultiSelectGroup;
@property (Tq,N,S_setTypeSelectState:,V__typeSelectState) _typeSelectState;
@property (TQ,N,S_setEdgesAbuttingAccessories:) _edgesAbuttingAccessories;
@property (TB,N,GisEditing) editing;
@property (TB,N,GisExpanded) expanded;
@property (TB,N,GisSwiped) swiped;
@property (TB,N,GisReordering) reordering;
@property (Tq,N) cellDragState;
@property (Tq,N) cellDropState;
@property (TB,R,N,GisDisabled) disabled;
@property (TB,R,N,GisHighlighted) highlighted;
@property (TB,R,N,GisSelected) selected;
@property (TB,R,N,GisFocused) focused;
@property (TB,R,N,GisPinned) pinned;
@property (Tq,R,N) _contextMenuGroupLocation;
@property (TQ,R,N) _viewConfigurationState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UICellConfigurationState supportsSecureCoding];
```

## Instance methods

```
-[UICellConfigurationState _setTypeSelectState:];
-[UICellConfigurationState setExpanded:];
-[UICellConfigurationState _initWithState:];
-[UICellConfigurationState isExpanded];
-[UICellConfigurationState _setEdgesAbuttingAccessories:];
-[UICellConfigurationState setCellDropState:];
-[UICellConfigurationState _setInMultiSelectGroup:];
-[UICellConfigurationState _inMultiSelectGroup];
-[UICellConfigurationState cellDropState];
-[UICellConfigurationState _configureWithViewConfigurationState:];
-[UICellConfigurationState setEditing:];
-[UICellConfigurationState setReordering:];
-[UICellConfigurationState setCellDragState:];
-[UICellConfigurationState encodeWithCoder:];
-[UICellConfigurationState _usesAnyPlainListStyle];
-[UICellConfigurationState _edgesAbuttingAccessories];
-[UICellConfigurationState hash];
-[UICellConfigurationState isReordering];
-[UICellConfigurationState cellDragState];
-[UICellConfigurationState _setUsesAnyPlainListStyle:];
-[UICellConfigurationState initWithCoder:];
-[UICellConfigurationState _typeSelectState];
-[UICellConfigurationState setSwiped:];
-[UICellConfigurationState _appendPropertiesForDescription:];
-[UICellConfigurationState isEditing];
-[UICellConfigurationState isEqual:];
-[UICellConfigurationState isSwiped];
-[UICellConfigurationState _viewConfigurationState];
```
