# `UIDragItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 20 properties, 54 instance methods, 0 class methods

## Instance variables

```
B _previewProviderIsSystemSet;
B _dirty;
B _deferPreviewUpdates;
@? _previewProvider;
@"NSItemProvider" _itemProvider;
@ _localObject;
@"_UIDragPreviewBlockProvider" _dragPreviewBlockProvider;
Q _preferredPreviewType;
Q _updatedPreviewType;
@"<_UIDragDropSessionInternal>" _dragDropSession;
@"<_UIDragSetDownAnimationTarget>" _sourceVisualTarget;
@"<_UIDragSetDownAnimationTarget>" _destinationVisualTarget;
@"_UIDragSetDownAnimation" __currentSetDownAnimation;
@"UITargetedDragPreview" _targetedLiftPreview;
Q _associatedObjectManipulationSessionIdentifier;
@ _privateLocalContext;
Q __managementState;
{CGSize="width"d"height"d} _visibleDropItemSize;
{CGPoint="x"d"y"d} _visibleDropItemCenter;
{?="width"d"height"d"depth"d} _associatedObjectManipulationDragItemSize;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} __suggestedTransform;
```

## Properties

```
@property (T@"UITextRange",&,N,S_setDraggedTextRange:) _draggedTextRange;
@property (T@"NSItemProvider",&,N,V_itemProvider) itemProvider;
@property (T@"_UIDragPreviewBlockProvider",&,N,V_dragPreviewBlockProvider) dragPreviewBlockProvider;
@property (TQ,N,V_preferredPreviewType) preferredPreviewType;
@property (TQ,N,V_updatedPreviewType) updatedPreviewType;
@property (T@"<_UIDragDropSessionInternal>",W,N,G_dragDropSession,S_setDragDropSession:,V_dragDropSession) dragDropSession;
@property (T{CGSize=dd},N,G_visibleDropItemSize,S_setVisibleDropItemSize:,V_visibleDropItemSize) visibleDropItemSize;
@property (T{CGPoint=dd},N,G_visibleDropItemCenter,S_setVisibleDropItemCenter:,V_visibleDropItemCenter) visibleDropItemCenter;
@property (T@"<_UIDragSetDownAnimationTarget>",W,N,G_sourceVisualTarget,S_setSourceVisualTarget:,V_sourceVisualTarget) sourceVisualTarget;
@property (T@"<_UIDragSetDownAnimationTarget>",W,N,G_destinationVisualTarget,S_setDestinationVisualTarget:,V_destinationVisualTarget) destinationVisualTarget;
@property (TB,N,G_isDirty,S_setDirty:,V_dirty) dirty;
@property (TB,N,G_deferPreviewUpdates,S_setDeferPreviewUpdates:,V_deferPreviewUpdates) deferPreviewUpdates;
@property (T@"UITargetedDragPreview",&,N,G_targetedLiftPreview,V_targetedLiftPreview) targetedLiftPreview;
@property (TQ,N,G_associatedObjectManipulationSessionIdentifier,S_setAssociatedObjectManipulationSessionIdentifier:,V_associatedObjectManipulationSessionIdentifier) associatedObjectManipulationSessionIdentifier;
@property (T{?=ddd},N,G_associatedObjectManipulationDragItemSize,S_setAssociatedObjectManipulationDragItemSize:,V_associatedObjectManipulationDragItemSize) associatedObjectManipulationDragItemSize;
@property (T@,&,N,G_privateLocalContext,S_setPrivateLocalContext:,V_privateLocalContext) privateLocalContext;
@property (TQ,N,V__managementState) _managementState;
@property (T{CGAffineTransform=dddddd},N,V__suggestedTransform) _suggestedTransform;
@property (T@,&,N,V_localObject) localObject;
@property (T@?,C,N,V_previewProvider) previewProvider;
```

## Instance methods

```
-[UIDragItem setLocalObject:];
-[UIDragItem localObject];
-[UIDragItem setPreviewProvider:];
-[UIDragItem itemProvider];
-[UIDragItem previewProvider];
-[UIDragItem _associatedObjectManipulationDragItemSize];
-[UIDragItem _associatedObjectManipulationSessionIdentifier];
-[UIDragItem _chiclet];
-[UIDragItem _currentPreviewProvider];
-[UIDragItem _currentPreviewProviderView];
-[UIDragItem _deferPreviewUpdates];
-[UIDragItem _destinationVisualTarget];
-[UIDragItem _dragDropSession];
-[UIDragItem _draggedTextRange];
-[UIDragItem _isDirty];
-[UIDragItem _loadOriginalImageComponentProvider];
-[UIDragItem _managementState];
-[UIDragItem _previewNeedsUpdateForType:];
-[UIDragItem _previewProviderForType:];
-[UIDragItem _privateLocalContext];
-[UIDragItem _setAssociatedObjectManipulationDragItemSize:];
-[UIDragItem _setAssociatedObjectManipulationSessionIdentifier:];
-[UIDragItem _setDeferPreviewUpdates:];
-[UIDragItem _setDestinationVisualTarget:];
-[UIDragItem _setDirty:];
-[UIDragItem _setDragDropSession:];
-[UIDragItem _setDraggedTextRange:];
-[UIDragItem _setNeedsDropPreviewUpdate];
-[UIDragItem _setPreviewProvider:systemSet:];
-[UIDragItem _setPrivateLocalContext:];
-[UIDragItem _setSourceVisualTarget:];
-[UIDragItem _setSystemPreviewProvider:];
-[UIDragItem _setVisibleDropItemCenter:];
-[UIDragItem _setVisibleDropItemSize:];
-[UIDragItem _sourceVisualTarget];
-[UIDragItem _suggestedTransform];
-[UIDragItem _targetedLiftPreview];
-[UIDragItem _uicmi_getAssociatedMenuIdentifier];
-[UIDragItem _uicmi_setAssociatedMenuIdentifier:];
-[UIDragItem _updatePreferredPreview];
-[UIDragItem _visibleDropItemCenter];
-[UIDragItem _visibleDropItemSize];
-[UIDragItem dragPreviewBlockProvider];
-[UIDragItem initWithItemProvider:];
-[UIDragItem preferredPreviewType];
-[UIDragItem setDragPreviewBlockProvider:];
-[UIDragItem setItemProvider:];
-[UIDragItem setNeedsDropPreviewUpdate];
-[UIDragItem setPreferredPreviewType:];
-[UIDragItem setTargetedLiftPreview:];
-[UIDragItem setUpdatedPreviewType:];
-[UIDragItem set_managementState:];
-[UIDragItem set_suggestedTransform:];
-[UIDragItem updatedPreviewType];
```
