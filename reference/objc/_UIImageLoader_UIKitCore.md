# `_UIImageLoader`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 9 instance methods, 3 class methods

## Instance variables

```
{atomic_flag="_Value"AB} _started;
AB _finished;
AB _cancelled;
@"UIImage" _image;
@"NSError" _error;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _trampolineLock;
@"NSMutableArray" _completionTrampolines;
```

## Properties

```
@property (TB,R) _isFinished;
@property (TB,R) _isCancelled;
@property (T@"UIImage",R) _image;
@property (T@"NSError",R) _error;
```

## Class methods

```
+[_UIImageLoader _imageLoaderWithDataFromItemProvider:typeIdentifier:];
+[_UIImageLoader _imageLoaderWithLoadingQueue:handler:];
+[_UIImageLoader _imageLoaderWithURLRequest:session:];
```

## Instance methods

```
-[_UIImageLoader _isCancelled];
-[_UIImageLoader init];
-[_UIImageLoader _error];
-[_UIImageLoader _cancel];
-[_UIImageLoader _image];
-[_UIImageLoader _isFinished];
-[_UIImageLoader _loadImageWithCompletionQueue:handler:];
-[_UIImageLoader _really_cancel];
-[_UIImageLoader _really_loadImage:];
```
