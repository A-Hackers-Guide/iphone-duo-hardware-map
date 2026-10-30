# `_DUIDragContinuation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<_DUIDragContinuation>" _continuation;
@"NSXPCConnection" _connection;
@"NSArray" _itemProviders;
@"PBItemCollection" _collection;
q _options;
```

## Instance methods

```
-[_DUIDragContinuation initWithListenerEndpoint:];
-[_DUIDragContinuation dealloc];
-[_DUIDragContinuation itemProviders];
-[_DUIDragContinuation _fetchItemCollectionFromDragContinuationIfNeeded];
-[_DUIDragContinuation _itemProvidersFromPBItemCollectionWithUserInfo:];
-[_DUIDragContinuation initWithListenerEndpoint:options:];
-[_DUIDragContinuation itemCollectionIdentifier];
-[_DUIDragContinuation itemProvidersWithUserInfo:];
-[_DUIDragContinuation originatorDataOwner];
-[_DUIDragContinuation sendDidFinishRequestingDataFromItemProvidersWithCompletion:];
```
