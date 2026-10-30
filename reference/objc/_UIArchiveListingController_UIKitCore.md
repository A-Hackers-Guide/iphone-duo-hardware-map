# `_UIArchiveListingController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"_UILibArchiveStreamingReader" _archiveReader;
B _isValidArchive;
B _excludeDotFilesFromResults;
@"NSString" _archivePath;
q _appleDoubleIdentificationType;
```

## Properties

```
@property (T@"NSString",R,N,V_archivePath) archivePath;
@property (Tq,N,V_appleDoubleIdentificationType) appleDoubleIdentificationType;
@property (TB,N,V_excludeDotFilesFromResults) excludeDotFilesFromResults;
```

## Instance methods

```
-[_UIArchiveListingController dealloc];
-[_UIArchiveListingController _shouldVisitItem:];
-[_UIArchiveListingController appleDoubleIdentificationType];
-[_UIArchiveListingController archivePath];
-[_UIArchiveListingController determineIsReadableArchive];
-[_UIArchiveListingController enumerateLogicalItemsWithBlock:error:];
-[_UIArchiveListingController excludeDotFilesFromResults];
-[_UIArchiveListingController initWithArchivePath:];
-[_UIArchiveListingController setAppleDoubleIdentificationType:];
-[_UIArchiveListingController setExcludeDotFilesFromResults:];
```
