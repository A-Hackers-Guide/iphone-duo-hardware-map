# `TBCoreDataStoreDescriptor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 8 class methods

## Instance variables

```
Q _type;
@"NSURL" _storeURL;
@"NSURL" _modelURL;
@"NSDictionary" _storeOptions;
@"NSPersistentStoreDescription" _storeDescription;
```

## Properties

```
@property (TQ,N,V_type) type;
@property (T@"NSURL",&,N,V_storeURL) storeURL;
@property (T@"NSURL",&,N,V_modelURL) modelURL;
@property (T@"NSDictionary",&,N,V_storeOptions) storeOptions;
@property (T@"NSPersistentStoreDescription",R,N,V_storeDescription) storeDescription;
```

## Class methods

```
+[TBCoreDataStoreDescriptor defaultModelURL];
+[TBCoreDataStoreDescriptor clientStoreDescriptor];
+[TBCoreDataStoreDescriptor defaultPersistentStoreURLWithDirectory:];
+[TBCoreDataStoreDescriptor defaultStoresDirectoryURL];
+[TBCoreDataStoreDescriptor directStoreDescriptor];
+[TBCoreDataStoreDescriptor serverStoreDescriptor];
+[TBCoreDataStoreDescriptor tempStoreDescriptor];
+[TBCoreDataStoreDescriptor tempStoresDirectoryURL];
```

## Instance methods

```
-[TBCoreDataStoreDescriptor storeURL];
-[TBCoreDataStoreDescriptor setType:];
-[TBCoreDataStoreDescriptor type];
-[TBCoreDataStoreDescriptor setStoreOptions:];
-[TBCoreDataStoreDescriptor storeOptions];
-[TBCoreDataStoreDescriptor setStoreURL:];
-[TBCoreDataStoreDescriptor modelURL];
-[TBCoreDataStoreDescriptor setModelURL:];
-[TBCoreDataStoreDescriptor storeDescription];
-[TBCoreDataStoreDescriptor initWithType:storeURL:modelURL:];
```
