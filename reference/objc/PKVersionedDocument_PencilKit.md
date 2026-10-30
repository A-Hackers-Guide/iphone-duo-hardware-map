# `PKVersionedDocument`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 19 instance methods, 3 class methods

## Instance variables

```
^v _documentArchive;
```

## Properties

```
@property (T^v,N,V_documentArchive) documentArchive;
@property (TQ,R,N) futureVersionCount;
```

## Class methods

```
+[PKVersionedDocument minimumSupportedVersion];
+[PKVersionedDocument serializationVersion];
+[PKVersionedDocument versionedDocumentSerializationVersion];
```

## Instance methods

```
-[PKVersionedDocument init];
-[PKVersionedDocument dealloc];
-[PKVersionedDocument initWithArchive:];
-[PKVersionedDocument serialize];
-[PKVersionedDocument saveToArchive:];
-[PKVersionedDocument initWithData:];
-[PKVersionedDocument loadArchive:];
-[PKVersionedDocument documentArchive];
-[PKVersionedDocument futureVersionCount];
-[PKVersionedDocument loadData:];
-[PKVersionedDocument loadDocumentArchive:];
-[PKVersionedDocument maxDocumentVersion];
-[PKVersionedDocument mergeVersion:fromData:];
-[PKVersionedDocument mergeWithVersionedDocument:];
-[PKVersionedDocument saveCurrentVersion:];
-[PKVersionedDocument serializeCurrentVersion:];
-[PKVersionedDocument setDocumentArchive:];
-[PKVersionedDocument initWithUnzippedData:];
-[PKVersionedDocument loadUnzippedData:];
```
