# `FigCaptureTempFileRemover`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
d _staleTimeSeconds;
d _checkTimeSeconds;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSArray" _folderList;
@? _fileRemoverBlock;
```

## Instance methods

```
-[FigCaptureTempFileRemover init];
-[FigCaptureTempFileRemover dealloc];
-[FigCaptureTempFileRemover _removeStaleTempFilesInFolderURL:];
-[FigCaptureTempFileRemover _scheduleNextFileRemove];
```
