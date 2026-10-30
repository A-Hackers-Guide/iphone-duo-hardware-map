# `TBPersistenceManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSManagedObjectContext" _persistenceContext;
@"NSPersistentStoreCoordinator" _persistenceCoordinator;
@"NSManagedObjectModel" _managedObjectModel;
@"TBPersistenceRemoteStoreServer" _remoteStoreServer;
```

## Properties

```
@property (T@"NSManagedObjectModel",&,N,V_managedObjectModel) managedObjectModel;
@property (T@"NSManagedObjectContext",&,N,V_persistenceContext) persistenceContext;
@property (T@"TBPersistenceRemoteStoreServer",&,N,V_remoteStoreServer) remoteStoreServer;
@property (T@"NSPersistentStoreCoordinator",&,N,V_persistenceCoordinator) persistenceCoordinator;
```

## Class methods

```
+[TBPersistenceManager isStoreCompatibleAtURL:withModel:];
```

## Instance methods

```
-[TBPersistenceManager setManagedObjectModel:];
-[TBPersistenceManager managedObjectModel];
-[TBPersistenceManager persistenceContext];
-[TBPersistenceManager addPersistentStorage:completionHandler:];
-[TBPersistenceManager initWithManagedObjectModel:storeDescriptor:];
-[TBPersistenceManager persistenceCoordinator];
-[TBPersistenceManager remoteStoreServer];
-[TBPersistenceManager setPersistenceContext:];
-[TBPersistenceManager setPersistenceCoordinator:];
-[TBPersistenceManager setRemoteStoreServer:];
```
