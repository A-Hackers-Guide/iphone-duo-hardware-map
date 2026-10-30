# `UIManagedDocument`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDocument`
- 7 instance variables, 4 properties, 22 instance methods, 4 class methods

## Instance variables

```
@"NSManagedObjectContext" _managedObjectContext;
@"NSPersistentStoreCoordinator" _persistentStoreCoordinator;
@"NSManagedObjectModel" _managedObjectModel;
@"NSDictionary" _documentMetadata;
{__mdocFlags="shouldWriteAdditionalContent"b1"_reserved"b31} _mdocFlags;
@"NSDictionary" persistentStoreOptions;
@"NSString" modelConfiguration;
```

## Properties

```
@property (T@"NSManagedObjectContext",R,N) managedObjectContext;
@property (T@"NSManagedObjectModel",R,N) managedObjectModel;
@property (T@"NSDictionary",C,N,VpersistentStoreOptions) persistentStoreOptions;
@property (T@"NSString",C,N,VmodelConfiguration) modelConfiguration;
```

## Class methods

```
+[UIManagedDocument initialize];
+[UIManagedDocument additionalContentPathComponent];
+[UIManagedDocument isPersistentStoreSynchronizedViaUbiquitousContentWithOptions:];
+[UIManagedDocument persistentStoreName];
```

## Instance methods

```
-[UIManagedDocument managedObjectContext];
-[UIManagedDocument setModelConfiguration:];
-[UIManagedDocument initWithFileURL:];
-[UIManagedDocument dealloc];
-[UIManagedDocument modelConfiguration];
-[UIManagedDocument managedObjectModel];
-[UIManagedDocument writeContents:andAttributes:safelyToURL:forSaveOperation:error:];
-[UIManagedDocument persistentStoreTypeForFileType:];
-[UIManagedDocument writeContents:toURL:forSaveOperation:originalContentsURL:error:];
-[UIManagedDocument _handleRelocatingStoreContentDirectoryFromNonSyncedURL:toSyncedURL:];
-[UIManagedDocument _handleRelocatingStoreContentDirectoryFromSyncedURL:toNonSyncedURL:];
-[UIManagedDocument _readMetadataFromDocumentURL:];
-[UIManagedDocument _writeMetadataToDocumentURL:];
-[UIManagedDocument additionalContentForURL:error:];
-[UIManagedDocument configurePersistentStoreCoordinatorForURL:ofType:modelConfiguration:storeOptions:error:];
-[UIManagedDocument contentsForType:error:];
-[UIManagedDocument persistentStoreOptions];
-[UIManagedDocument readAdditionalContentFromURL:error:];
-[UIManagedDocument readFromURL:error:];
-[UIManagedDocument revertToContentsOfURL:completionHandler:];
-[UIManagedDocument setPersistentStoreOptions:];
-[UIManagedDocument writeAdditionalContent:toURL:originalContentsURL:error:];
```
