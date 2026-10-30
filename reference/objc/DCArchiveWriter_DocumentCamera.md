# `DCArchiveWriter`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
^{archive=} _archive;
B _usesCompression;
B _flatten;
@"NSString" _flattenFolderName;
@"NSURL" _destinationURL;
@"NSString" _basePath;
```

## Properties

```
@property (T@"NSURL",&,N,V_destinationURL) destinationURL;
@property (T@"NSString",&,N,V_basePath) basePath;
@property (TB,N,V_usesCompression) usesCompression;
@property (TB,N,V_flatten) flatten;
@property (T@"NSString",C,N,V_flattenFolderName) flattenFolderName;
```

## Instance methods

```
-[DCArchiveWriter open:];
-[DCArchiveWriter basePath];
-[DCArchiveWriter dealloc];
-[DCArchiveWriter finish:];
-[DCArchiveWriter destinationURL];
-[DCArchiveWriter setDestinationURL:];
-[DCArchiveWriter initWithDestinationURL:baseURL:];
-[DCArchiveWriter flatten];
-[DCArchiveWriter usesCompression];
-[DCArchiveWriter flattenFolderName];
-[DCArchiveWriter setBasePath:];
-[DCArchiveWriter setFlatten:];
-[DCArchiveWriter setFlattenFolderName:];
-[DCArchiveWriter setUsesCompression:];
-[DCArchiveWriter writeURL:isDirectory:error:];
-[DCArchiveWriter writeURLs:error:];
```
