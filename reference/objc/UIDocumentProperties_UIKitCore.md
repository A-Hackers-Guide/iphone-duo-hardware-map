# `UIDocumentProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 14 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _wantsIconRepresentation;
@"UINavigationItem" _associatedNavigationItem;
@"LPLinkMetadata" _metadata;
@? _dragItemsProvider;
@? _activityViewControllerProvider;
@"_UIDocumentPropertiesHeaderView" _headerView;
@"_UIDocumentPropertiesIconView" _iconView;
@"NSURL" _url;
@"_UIDocumentURLChangeObserver" _urlChangeObserver;
@"LPMetadataProvider" __metadataProvider;
@? __wantsIconRepresentationChangedHandler;
@"UIAction" _iconRepresentationAction;
```

## Properties

```
@property (T@"_UIDocumentPropertiesHeaderView",W,N,V_headerView) headerView;
@property (T@"_UIDocumentPropertiesIconView",W,N,V_iconView) iconView;
@property (T@"NSURL",&,N,V_url) url;
@property (T@"_UIDocumentURLChangeObserver",&,N,V_urlChangeObserver) urlChangeObserver;
@property (T@"LPLinkMetadata",&,N,S_setMetadata:,V_metadata) _metadata;
@property (T@"LPMetadataProvider",&,N,S_setMetadataProvider:,V__metadataProvider) _metadataProvider;
@property (T@"NSURL",R,N) _representedURL;
@property (T@?,C,N,S_setWantsIconRepresentationChangedHandler:,V__wantsIconRepresentationChangedHandler) _wantsIconRepresentationChangedHandler;
@property (T@"UINavigationItem",W,N,S_setAssociatedNavigationItem:,V_associatedNavigationItem) _associatedNavigationItem;
@property (T@"UIAction",&,N,V_iconRepresentationAction) iconRepresentationAction;
@property (T@"LPLinkMetadata",C,N) metadata;
@property (T@?,C,N,V_dragItemsProvider) dragItemsProvider;
@property (T@?,C,N,V_activityViewControllerProvider) activityViewControllerProvider;
@property (TB,N,V_wantsIconRepresentation) wantsIconRepresentation;
```

## Instance methods

```
-[UIDocumentProperties headerView];
-[UIDocumentProperties iconView];
-[UIDocumentProperties dealloc];
-[UIDocumentProperties setIconView:];
-[UIDocumentProperties metadata];
-[UIDocumentProperties _metadata];
-[UIDocumentProperties setMetadata:];
-[UIDocumentProperties _setMetadata:];
-[UIDocumentProperties setUrl:];
-[UIDocumentProperties initWithURL:];
-[UIDocumentProperties url];
-[UIDocumentProperties setHeaderView:];
-[UIDocumentProperties _representedURL];
-[UIDocumentProperties _associatedNavigationItem];
-[UIDocumentProperties _didLoadMetadata:];
-[UIDocumentProperties _fetchMetadataIfNecessary:];
-[UIDocumentProperties _headerViewForMenuInteraction:sourceViewProvider:];
-[UIDocumentProperties _iconView];
-[UIDocumentProperties _metadataProvider];
-[UIDocumentProperties _metadataWrapper];
-[UIDocumentProperties _performBlockAndCallIconRepresentationChangedHandlerIfNecessary:];
-[UIDocumentProperties _placeholderMetadata];
-[UIDocumentProperties _setAssociatedNavigationItem:];
-[UIDocumentProperties _setMetadataProvider:];
-[UIDocumentProperties _setWantsIconRepresentationChangedHandler:];
-[UIDocumentProperties _updateMetadataInUse];
-[UIDocumentProperties _wantsIconRepresentationChangedHandler];
-[UIDocumentProperties activityViewControllerProvider];
-[UIDocumentProperties dragItemsProvider];
-[UIDocumentProperties iconRepresentationAction];
-[UIDocumentProperties initWithMetadata:];
-[UIDocumentProperties setActivityViewControllerProvider:];
-[UIDocumentProperties setDragItemsProvider:];
-[UIDocumentProperties setIconRepresentationAction:];
-[UIDocumentProperties setUrlChangeObserver:];
-[UIDocumentProperties setWantsIconRepresentation:];
-[UIDocumentProperties urlChangeObserver];
-[UIDocumentProperties wantsIconRepresentation];
```
