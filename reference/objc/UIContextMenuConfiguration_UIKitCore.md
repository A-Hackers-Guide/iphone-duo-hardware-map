# `UIContextMenuConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 20 properties, 39 instance methods, 1 class methods

## Instance variables

```
B _allowsTypeSelect;
B _prefersHorizontalAttachment;
@"<NSCopying>" _identifier;
@"NSSet" _secondaryItemIdentifiers;
q _badgeCount;
q _preferredMenuElementOrder;
@? _previewProvider;
@? _actionProvider;
@"UIResponder" _firstResponderTarget;
@"UITargetedPreview" __primarySourcePreview;
@"NSArray" __secondarySourcePreviews;
@"UITargetedPreview" __alignmentSourcePreview;
@"_UIMenuPresentationSource" __presentationSource;
@ __internalIdentifier;
@"NSSet" __internalSecondaryItemIdentifiers;
q _preferredMenuAlignment;
```

## Properties

```
@property (T@"UITab",&,N,S_setTab:) _tab;
@property (T@"<NSCopying>",C,N,V_identifier) identifier;
@property (T@?,C,N,V_previewProvider) previewProvider;
@property (T@?,C,N,V_actionProvider) actionProvider;
@property (T@"UIResponder",W,N,V_firstResponderTarget) firstResponderTarget;
@property (T@"UITargetedPreview",&,N,V__primarySourcePreview) _primarySourcePreview;
@property (T@"NSArray",&,N,V__secondarySourcePreviews) _secondarySourcePreviews;
@property (T@"_UIMenuPresentationSource",&,N,V__presentationSource) _presentationSource;
@property (T@,&,N,V__internalIdentifier) _internalIdentifier;
@property (T@"NSSet",&,N,V__internalSecondaryItemIdentifiers) _internalSecondaryItemIdentifiers;
@property (T@,R,N) _effectiveInternalIdentifier;
@property (T@"NSSet",R,N) _effectiveSecondaryItemIdentifiers;
@property (TB,R,N) _clientDidSetBadgeCount;
@property (TB,R,N) _isMultiItemMenu;
@property (TB,N,V_prefersHorizontalAttachment) prefersHorizontalAttachment;
@property (Tq,N,V_preferredMenuAlignment) preferredMenuAlignment;
@property (T@"NSSet",C,N,V_secondaryItemIdentifiers) secondaryItemIdentifiers;
@property (Tq,N,V_badgeCount) badgeCount;
@property (Tq,N,V_preferredMenuElementOrder) preferredMenuElementOrder;
@property (TB,N,V_allowsTypeSelect) allowsTypeSelect;
```

## Class methods

```
+[UIContextMenuConfiguration configurationWithIdentifier:previewProvider:actionProvider:];
```

## Instance methods

```
-[UIContextMenuConfiguration setPreferredMenuElementOrder:];
-[UIContextMenuConfiguration setActionProvider:];
-[UIContextMenuConfiguration actionProvider];
-[UIContextMenuConfiguration firstResponderTarget];
-[UIContextMenuConfiguration identifier];
-[UIContextMenuConfiguration setSecondaryItemIdentifiers:];
-[UIContextMenuConfiguration init];
-[UIContextMenuConfiguration _secondarySourcePreviews];
-[UIContextMenuConfiguration _effectiveSecondaryItemIdentifiers];
-[UIContextMenuConfiguration set_primarySourcePreview:];
-[UIContextMenuConfiguration allowsTypeSelect];
-[UIContextMenuConfiguration setPreviewProvider:];
-[UIContextMenuConfiguration badgeCount];
-[UIContextMenuConfiguration _prepareWithCompletion:];
-[UIContextMenuConfiguration _tab];
-[UIContextMenuConfiguration set_internalIdentifier:];
-[UIContextMenuConfiguration setPreferredMenuAlignment:];
-[UIContextMenuConfiguration _clientDidSetBadgeCount];
-[UIContextMenuConfiguration _primarySourcePreview];
-[UIContextMenuConfiguration setIdentifier:];
-[UIContextMenuConfiguration _internalIdentifier];
-[UIContextMenuConfiguration secondaryItemIdentifiers];
-[UIContextMenuConfiguration set_internalSecondaryItemIdentifiers:];
-[UIContextMenuConfiguration _isMultiItemMenu];
-[UIContextMenuConfiguration preferredMenuAlignment];
-[UIContextMenuConfiguration _setTab:];
-[UIContextMenuConfiguration preferredMenuElementOrder];
-[UIContextMenuConfiguration setAllowsTypeSelect:];
-[UIContextMenuConfiguration _effectiveInternalIdentifier];
-[UIContextMenuConfiguration setBadgeCount:];
-[UIContextMenuConfiguration setPrefersHorizontalAttachment:];
-[UIContextMenuConfiguration set_presentationSource:];
-[UIContextMenuConfiguration set_secondarySourcePreviews:];
-[UIContextMenuConfiguration _presentationSource];
-[UIContextMenuConfiguration _internalSecondaryItemIdentifiers];
-[UIContextMenuConfiguration prefersHorizontalAttachment];
-[UIContextMenuConfiguration previewProvider];
-[UIContextMenuConfiguration _isCollectionViewBackgroundMenu];
-[UIContextMenuConfiguration setFirstResponderTarget:];
```
