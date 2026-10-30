# `DCArchiveReader`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
^{archive=} _archive;
B _overwrite;
B _writesTemporaryFilesInsideDestination;
B _skipsInvisibleHeaders;
@"NSString" _sourcePath;
@"NSString" _destinationPath;
```

## Properties

```
@property (T@"NSString",C,N,V_sourcePath) sourcePath;
@property (T@"NSString",C,N,V_destinationPath) destinationPath;
@property (TB,N,V_overwrite) overwrite;
@property (TB,N,V_writesTemporaryFilesInsideDestination) writesTemporaryFilesInsideDestination;
@property (TB,N,V_skipsInvisibleHeaders) skipsInvisibleHeaders;
```

## Instance methods

```
-[DCArchiveReader temporaryDirectory];
-[DCArchiveReader sourcePath];
-[DCArchiveReader overwrite];
-[DCArchiveReader setOverwrite:];
-[DCArchiveReader destinationPath];
-[DCArchiveReader setDestinationPath:];
-[DCArchiveReader incrementalPathInDirectory:withFilename:andExtension:];
-[DCArchiveReader initWithSourceURL:destinationURL:];
-[DCArchiveReader moveContentsOfDirectory:toDirectory:resultURLs:error:];
-[DCArchiveReader setSkipsInvisibleHeaders:];
-[DCArchiveReader setSourcePath:];
-[DCArchiveReader setWritesTemporaryFilesInsideDestination:];
-[DCArchiveReader skipsInvisibleHeaders];
-[DCArchiveReader unarchiveResultURLs:error:];
-[DCArchiveReader unarchiveSourcePath:toDestinationPath:error:];
-[DCArchiveReader writesTemporaryFilesInsideDestination];
```
