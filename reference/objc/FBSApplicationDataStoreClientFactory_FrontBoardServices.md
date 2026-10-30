# `FBSApplicationDataStoreClientFactory`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 5 instance methods, 2 class methods

## Instance variables

```
Q _count;
@"NSObject<OS_dispatch_queue>" _queue;
@"<FBSApplicationDataStoreRepositoryClient>" _sharedClient;
@"NSArray" _prefetchedKeys;
```

## Properties

```
@property (T@"NSArray",&,N,V_prefetchedKeys) prefetchedKeys;
```

## Class methods

```
+[FBSApplicationDataStoreClientFactory sharedInstance];
+[FBSApplicationDataStoreClientFactory isServerProcess];
```

## Instance methods

```
-[FBSApplicationDataStoreClientFactory checkin];
-[FBSApplicationDataStoreClientFactory init];
-[FBSApplicationDataStoreClientFactory checkout];
-[FBSApplicationDataStoreClientFactory prefetchedKeys];
-[FBSApplicationDataStoreClientFactory setPrefetchedKeys:];
```
