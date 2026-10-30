# `_UIFulfilledContextMenuConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 17 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _allowsTypeSelect;
B _shouldMenuOverlapSourceMenu;
@"<NSCopying>" _identifier;
@"NSSet" _internalIdentifiers;
@"UITargetedPreview" _sourcePreview;
@"NSArray" _secondarySourcePreviews;
@"UITargetedPreview" _alignmentSourcePreview;
@"UIViewController" _previewViewController;
@"NSArray" _accessoryViews;
@"UIMenu" _menu;
@"UIAction" _previewAction;
@"_UIMenuPresentationSource" __presentationSource;
Q _representedItemCount;
Q _badgeCount;
@"UIResponder" _firstResponderTarget;
@"UITargetedPreview" _resolvedPreview;
```

## Properties

```
@property (T@"UITargetedPreview",&,N,V_resolvedPreview) resolvedPreview;
@property (T@"<NSCopying>",C,N,V_identifier) identifier;
@property (T@"NSSet",R,N,V_internalIdentifiers) internalIdentifiers;
@property (T@"UITargetedPreview",&,N,V_sourcePreview) sourcePreview;
@property (T@"NSArray",&,N,V_secondarySourcePreviews) secondarySourcePreviews;
@property (T@"UITargetedPreview",&,N,V_alignmentSourcePreview) alignmentSourcePreview;
@property (T@"UIViewController",&,N,V_previewViewController) previewViewController;
@property (T@"NSArray",&,N,V_accessoryViews) accessoryViews;
@property (T@"UIMenu",C,N,V_menu) menu;
@property (T@"UIAction",C,N,V_previewAction) previewAction;
@property (TB,R,N) isMultiItemMenu;
@property (TB,N,V_allowsTypeSelect) allowsTypeSelect;
@property (TB,N,V_shouldMenuOverlapSourceMenu) shouldMenuOverlapSourceMenu;
@property (T@"_UIMenuPresentationSource",&,N,V__presentationSource) _presentationSource;
@property (TQ,N,V_representedItemCount) representedItemCount;
@property (TQ,N,V_badgeCount) badgeCount;
@property (T@"UIResponder",W,N,V_firstResponderTarget) firstResponderTarget;
```

## Instance methods

```
-[_UIFulfilledContextMenuConfiguration menu];
-[_UIFulfilledContextMenuConfiguration isPresentable];
-[_UIFulfilledContextMenuConfiguration firstResponderTarget];
-[_UIFulfilledContextMenuConfiguration identifier];
-[_UIFulfilledContextMenuConfiguration internalIdentifiers];
-[_UIFulfilledContextMenuConfiguration sourcePreview];
-[_UIFulfilledContextMenuConfiguration allowsTypeSelect];
-[_UIFulfilledContextMenuConfiguration badgeCount];
-[_UIFulfilledContextMenuConfiguration setPrimaryInternalIdentifier:secondaryIdentifiers:];
-[_UIFulfilledContextMenuConfiguration setAccessoryViews:];
-[_UIFulfilledContextMenuConfiguration isMultiItemMenu];
-[_UIFulfilledContextMenuConfiguration setPreviewViewController:];
-[_UIFulfilledContextMenuConfiguration setIdentifier:];
-[_UIFulfilledContextMenuConfiguration previewViewController];
-[_UIFulfilledContextMenuConfiguration secondarySourcePreviews];
-[_UIFulfilledContextMenuConfiguration accessoryViews];
-[_UIFulfilledContextMenuConfiguration setSecondarySourcePreviews:];
-[_UIFulfilledContextMenuConfiguration setResolvedPreview:];
-[_UIFulfilledContextMenuConfiguration shouldMenuOverlapSourceMenu];
-[_UIFulfilledContextMenuConfiguration setAlignmentSourcePreview:];
-[_UIFulfilledContextMenuConfiguration resolvedPreview];
-[_UIFulfilledContextMenuConfiguration resolvedSourcePreview];
-[_UIFulfilledContextMenuConfiguration setSourcePreview:];
-[_UIFulfilledContextMenuConfiguration setAllowsTypeSelect:];
-[_UIFulfilledContextMenuConfiguration previewAction];
-[_UIFulfilledContextMenuConfiguration setPreviewAction:];
-[_UIFulfilledContextMenuConfiguration alignmentSourcePreview];
-[_UIFulfilledContextMenuConfiguration setBadgeCount:];
-[_UIFulfilledContextMenuConfiguration setShouldMenuOverlapSourceMenu:];
-[_UIFulfilledContextMenuConfiguration set_presentationSource:];
-[_UIFulfilledContextMenuConfiguration _presentationSource];
-[_UIFulfilledContextMenuConfiguration representedItemCount];
-[_UIFulfilledContextMenuConfiguration setRepresentedItemCount:];
-[_UIFulfilledContextMenuConfiguration setFirstResponderTarget:];
-[_UIFulfilledContextMenuConfiguration setMenu:];
```
