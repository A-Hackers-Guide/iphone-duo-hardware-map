# `__NSCFLocalDownloadFile`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 1 properties, 3 instance methods, 0 class methods

## Instance variables

```
{stat="st_dev"i"st_mode"S"st_nlink"S"st_ino"Q"st_uid"I"st_gid"I"st_rdev"i"st_atimespec"{timespec="tv_sec"q"tv_nsec"q}"st_mtimespec"{timespec="tv_sec"q"tv_nsec"q}"st_ctimespec"{timespec="tv_sec"q"tv_nsec"q}"st_birthtimespec"{timespec="tv_sec"q"tv_nsec"q}"st_size"q"st_blocks"q"st_blksize"i"st_flags"I"st_gen"I"st_lspare"i"st_qspare"[2q]} _stat;
@"NSObject<OS_dispatch_io>" _writeIO;
@"NSObject<OS_dispatch_queue>" _workQueue;
B _finished;
@"NSString" _path;
B _createdPlaceholder;
B _skipUnlink;
B _truncateFile;
i _error;
@"<__NSCFLocalDownloadFileOpener>" _fileProvider;
@? _finishCompletion;
@"NSString" _protectionType;
```

## Properties

```
@property (T@"NSString",&,V_path) path;
```

## Instance methods

```
-[__NSCFLocalDownloadFile dealloc];
-[__NSCFLocalDownloadFile setPath:];
-[__NSCFLocalDownloadFile path];
```
