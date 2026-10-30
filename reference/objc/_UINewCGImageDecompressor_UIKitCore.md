# `_UINewCGImageDecompressor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UICGImageDecompressor`
- 6 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
^{CMPhotoDecompressionContainer=} _container;
@ _imageOrError;
@"NSObject<OS_dispatch_queue>" _replyQueue;
@"NSObject<OS_dispatch_semaphore>" _sema;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
{?="started"b1"finished"b1"error"b1} _flags;
```

## Class methods

```
+[_UINewCGImageDecompressor _sharedDecompressionSession];
```

## Instance methods

```
-[_UINewCGImageDecompressor init];
-[_UINewCGImageDecompressor dealloc];
-[_UINewCGImageDecompressor waitForImageRef];
-[_UINewCGImageDecompressor _finishDecompressingWithImage:error:];
```
