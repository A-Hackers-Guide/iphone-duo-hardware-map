# `_UIDocumentPropertiesHeaderView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIDragInteractionDelegate`, `UIGestureRecognizerDelegate`, `LPLinkViewDelegate`, `UIPointerInteractionDelegate`
- 6 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIDocumentProperties" _properties;
@"UIContextMenuInteraction" _menuInteraction;
@? _sourceViewProvider;
@"LPLinkView" _linkView;
@"UIButton" _shareButton;
{?="didSetupDragInteraction"b1} _flags;
```

## Properties

```
@property (T@"LPLinkView",R,N,V_linkView) linkView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDocumentPropertiesHeaderView dragInteraction:previewForLiftingItem:session:];
-[_UIDocumentPropertiesHeaderView _share:];
-[_UIDocumentPropertiesHeaderView dragInteraction:itemsForBeginningSession:];
-[_UIDocumentPropertiesHeaderView dragInteraction:previewForCancellingItem:withDefault:];
-[_UIDocumentPropertiesHeaderView dragInteraction:sessionWillBegin:];
-[_UIDocumentPropertiesHeaderView linkView];
-[_UIDocumentPropertiesHeaderView pointerInteraction:styleForRegion:];
-[_UIDocumentPropertiesHeaderView update];
-[_UIDocumentPropertiesHeaderView pointerInteraction:regionForRequest:defaultRegion:];
-[_UIDocumentPropertiesHeaderView initWithProperties:metadata:menuInteraction:sourceViewProvider:];
-[_UIDocumentPropertiesHeaderView _defaultDragPreview];
-[_UIDocumentPropertiesHeaderView _defaultSharePreview];
-[_UIDocumentPropertiesHeaderView _rectForDragInteraction];
-[_UIDocumentPropertiesHeaderView _rectForShareButton];
-[_UIDocumentPropertiesHeaderView linkViewNeedsResize:];
```
