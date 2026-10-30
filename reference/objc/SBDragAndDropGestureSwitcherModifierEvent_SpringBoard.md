# `SBDragAndDropGestureSwitcherModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifierEvent`
- 10 instance variables, 10 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _performedDrop;
B _previewHasLifted;
B _platterized;
B _windowDrag;
B _switcherDrag;
q _dropAction;
@"NSString" _draggedSceneIdentifier;
q _draggedSceneLayoutRole;
d _platterScale;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _platterViewFrame;
```

## Properties

```
@property (Tq,N,V_dropAction) dropAction;
@property (T@"NSString",&,N,V_draggedSceneIdentifier) draggedSceneIdentifier;
@property (Tq,N,V_draggedSceneLayoutRole) draggedSceneLayoutRole;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_platterViewFrame) platterViewFrame;
@property (Td,N,V_platterScale) platterScale;
@property (TB,N,GhasPerformedDrop,V_performedDrop) performedDrop;
@property (TB,N,GhasPreviewLifted,V_previewHasLifted) previewHasLifted;
@property (TB,N,GhasPlatterized,V_platterized) platterized;
@property (TB,N,GisWindowDrag,V_windowDrag) windowDrag;
@property (TB,N,GisSwitcherDrag,V_switcherDrag) switcherDrag;
```

## Instance methods

```
-[SBDragAndDropGestureSwitcherModifierEvent type];
-[SBDragAndDropGestureSwitcherModifierEvent copyWithZone:];
-[SBDragAndDropGestureSwitcherModifierEvent dropAction];
-[SBDragAndDropGestureSwitcherModifierEvent platterViewFrame];
-[SBDragAndDropGestureSwitcherModifierEvent setDropAction:];
-[SBDragAndDropGestureSwitcherModifierEvent setPlatterViewFrame:];
-[SBDragAndDropGestureSwitcherModifierEvent draggedSceneIdentifier];
-[SBDragAndDropGestureSwitcherModifierEvent setDraggedSceneIdentifier:];
-[SBDragAndDropGestureSwitcherModifierEvent setPerformedDrop:];
-[SBDragAndDropGestureSwitcherModifierEvent setPlatterized:];
-[SBDragAndDropGestureSwitcherModifierEvent draggedSceneLayoutRole];
-[SBDragAndDropGestureSwitcherModifierEvent hasPerformedDrop];
-[SBDragAndDropGestureSwitcherModifierEvent hasPlatterized];
-[SBDragAndDropGestureSwitcherModifierEvent hasPreviewLifted];
-[SBDragAndDropGestureSwitcherModifierEvent isSwitcherDrag];
-[SBDragAndDropGestureSwitcherModifierEvent isWindowDrag];
-[SBDragAndDropGestureSwitcherModifierEvent platterScale];
-[SBDragAndDropGestureSwitcherModifierEvent setDraggedSceneLayoutRole:];
-[SBDragAndDropGestureSwitcherModifierEvent setPlatterScale:];
-[SBDragAndDropGestureSwitcherModifierEvent setPreviewHasLifted:];
-[SBDragAndDropGestureSwitcherModifierEvent setSwitcherDrag:];
-[SBDragAndDropGestureSwitcherModifierEvent setWindowDrag:];
```
