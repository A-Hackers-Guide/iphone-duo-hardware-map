# `_UIArchiveExtractionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _extractedContentAbsolutePaths;
@"NSString" _sourceArchivePath;
@"NSString" _destinationExtractionRootPath;
@"NSString" _destinationContentProtectionType;
@"NSString" _sourceArchiveExtractionRootPath;
```

## Properties

```
@property (T@"NSString",R,N,V_sourceArchivePath) sourceArchivePath;
@property (T@"NSString",&,N,V_destinationExtractionRootPath) destinationExtractionRootPath;
@property (T@"NSString",&,N,V_destinationContentProtectionType) destinationContentProtectionType;
@property (T@"NSString",&,N,V_sourceArchiveExtractionRootPath) sourceArchiveExtractionRootPath;
```

## Instance methods

```
-[_UIArchiveExtractionController sourceArchiveExtractionRootPath];
-[_UIArchiveExtractionController _createDestinationRoot:];
-[_UIArchiveExtractionController destinationContentProtectionType];
-[_UIArchiveExtractionController destinationExtractionRootPath];
-[_UIArchiveExtractionController extractArchiveContent:];
-[_UIArchiveExtractionController extractedContentAbsolutePathsMatchingPredicate:];
-[_UIArchiveExtractionController initWithSourceArchivePath:destinationExtractionRootPath:];
-[_UIArchiveExtractionController setDestinationContentProtectionType:];
-[_UIArchiveExtractionController setDestinationExtractionRootPath:];
-[_UIArchiveExtractionController setSourceArchiveExtractionRootPath:];
-[_UIArchiveExtractionController sourceArchivePath];
```
