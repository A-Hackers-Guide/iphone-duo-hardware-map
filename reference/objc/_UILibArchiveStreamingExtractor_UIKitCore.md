# `_UILibArchiveStreamingExtractor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"NSString" _archivePath;
@"NSArray" _extractedContentAbsolutePaths;
```

## Properties

```
@property (T@"NSString",R,N,V_archivePath) archivePath;
@property (T@"NSArray",R,N,V_extractedContentAbsolutePaths) extractedContentAbsolutePaths;
```

## Class methods

```
+[_UILibArchiveStreamingExtractor archiveSubpathByStandardizingArchiveSubpath:];
+[_UILibArchiveStreamingExtractor shouldExtractPathInArchive:forExtractionRootedAtStandardizedSubpathInArchive:];
```

## Instance methods

```
-[_UILibArchiveStreamingExtractor archivePath];
-[_UILibArchiveStreamingExtractor extractArchivePath:toDirectory:error:];
-[_UILibArchiveStreamingExtractor extractedContentAbsolutePaths];
-[_UILibArchiveStreamingExtractor initForExtractingArchivePath:];
```
