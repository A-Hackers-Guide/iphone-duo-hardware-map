# `_UITableViewDropCoordinatorImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITableViewDropCoordinator`
- 6 instance variables, 14 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"<_UITableViewDropCoordinatorDelegate>" _delegate;
@"NSArray" _items;
@"NSIndexPath" _destinationIndexPath;
@"NSIndexPath" _translatedDestinationIndexPath;
@"UITableViewDropProposal" _proposal;
@"<UIDropSession>" _session;
```

## Properties

```
@property (T@"<_UITableViewDropCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",&,N,V_items) items;
@property (T@"NSIndexPath",&,N,V_destinationIndexPath) destinationIndexPath;
@property (T@"NSIndexPath",&,N,G_translatedDestinationIndexPath,S_setTranslatedDestinationIndexPath:,V_translatedDestinationIndexPath) translatedDestinationIndexPath;
@property (T@"UITableViewDropProposal",&,N,V_proposal) proposal;
@property (T@"<UIDropSession>",&,N,V_session) session;
@property (T@"NSArray",R,N) _items;
@property (T@"NSIndexPath",R,N) _destinationIndexPath;
@property (T@"UITableViewDropProposal",R,N) _dropProposal;
@property (T@"<UIDropSession>",R,N) _dropSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITableViewDropCoordinatorImpl dropItem:toPlaceholder:];
-[_UITableViewDropCoordinatorImpl setItems:];
-[_UITableViewDropCoordinatorImpl items];
-[_UITableViewDropCoordinatorImpl setSession:];
-[_UITableViewDropCoordinatorImpl setDelegate:];
-[_UITableViewDropCoordinatorImpl proposal];
-[_UITableViewDropCoordinatorImpl _items];
-[_UITableViewDropCoordinatorImpl delegate];
-[_UITableViewDropCoordinatorImpl dropItem:toTarget:];
-[_UITableViewDropCoordinatorImpl destinationIndexPath];
-[_UITableViewDropCoordinatorImpl session];
-[_UITableViewDropCoordinatorImpl _translateDestinationIndexPath:];
-[_UITableViewDropCoordinatorImpl _translatedDestinationIndexPath];
-[_UITableViewDropCoordinatorImpl _destinationIndexPath];
-[_UITableViewDropCoordinatorImpl _dropItem:toCell:withPreviewParameters:];
-[_UITableViewDropCoordinatorImpl _dropItem:toPlaceholderInsertedAtIndexPath:withReuseIdentifier:rowHeight:cellUpdateHandler:];
-[_UITableViewDropCoordinatorImpl _dropItem:toRowAtIndexPath:];
-[_UITableViewDropCoordinatorImpl _dropItem:toTarget:];
-[_UITableViewDropCoordinatorImpl _dropProposal];
-[_UITableViewDropCoordinatorImpl _dropSession];
-[_UITableViewDropCoordinatorImpl _setTranslatedDestinationIndexPath:];
-[_UITableViewDropCoordinatorImpl _sourceIndexPaths];
-[_UITableViewDropCoordinatorImpl _translateSourceIndexPathsOfDropItems:];
-[_UITableViewDropCoordinatorImpl dropItem:intoRowAtIndexPath:rect:];
-[_UITableViewDropCoordinatorImpl dropItem:toPlaceholderInsertedAtIndexPath:withReuseIdentifier:rowHeight:cellUpdateHandler:];
-[_UITableViewDropCoordinatorImpl dropItem:toRowAtIndexPath:];
-[_UITableViewDropCoordinatorImpl initWithDelegate:destinationIndexPath:dropProposal:session:];
-[_UITableViewDropCoordinatorImpl setDestinationIndexPath:];
-[_UITableViewDropCoordinatorImpl setProposal:];
```
