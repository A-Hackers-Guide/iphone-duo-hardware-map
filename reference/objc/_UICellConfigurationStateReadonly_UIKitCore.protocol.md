# `_UICellConfigurationStateReadonly` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `_UIViewConfigurationStateReadonly`
- 0 instance variables, 10 properties, 10 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisEditing) editing;
@property (TB,R,N,GisExpanded) expanded;
@property (TB,R,N,GisSwiped) swiped;
@property (TB,R,N,GisReordering) reordering;
@property (Tq,R,N,G_typeSelectState) _typeSelectState;
@property (Tq,R,N) cellDragState;
@property (Tq,R,N) cellDropState;
@property (TB,R,N) _usesAnyPlainListStyle;
@property (TB,R,N) _inMultiSelectGroup;
@property (TQ,R,N) _edgesAbuttingAccessories;
```

## Instance methods

```
-[_UICellConfigurationStateReadonly isExpanded];
-[_UICellConfigurationStateReadonly _inMultiSelectGroup];
-[_UICellConfigurationStateReadonly cellDropState];
-[_UICellConfigurationStateReadonly _usesAnyPlainListStyle];
-[_UICellConfigurationStateReadonly _edgesAbuttingAccessories];
-[_UICellConfigurationStateReadonly isReordering];
-[_UICellConfigurationStateReadonly cellDragState];
-[_UICellConfigurationStateReadonly _typeSelectState];
-[_UICellConfigurationStateReadonly isEditing];
-[_UICellConfigurationStateReadonly isSwiped];
```
