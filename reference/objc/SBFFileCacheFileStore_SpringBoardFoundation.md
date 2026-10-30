# `SBFFileCacheFileStore`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFFileCacheStore`
- 1 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _directoryURL;
```

## Properties

```
@property (T@"NSURL",R,C,N,V_directoryURL) directoryURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFFileCacheFileStore init];
-[SBFFileCacheFileStore description];
-[SBFFileCacheFileStore directoryURL];
-[SBFFileCacheFileStore initWithDirectoryURL:];
-[SBFFileCacheFileStore fileCache:loadFileWrapperNamed:];
-[SBFFileCacheFileStore fileCache:removeFileWrapperNamed:];
-[SBFFileCacheFileStore fileCache:storeFileWrapper:];
-[SBFFileCacheFileStore fileURLForFileNamed:];
-[SBFFileCacheFileStore removeAllFileWrappersForFileCache:];
```
