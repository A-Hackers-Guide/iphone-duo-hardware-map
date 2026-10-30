# `CAMTransientImageManagerRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _isCanceled;
B _isFinished;
@"NSString" _uuid;
@? _resultHandler;
```

## Properties

```
@property (T@"NSString",C,N,V_uuid) uuid;
@property (T@?,C,N,V_resultHandler) resultHandler;
@property (TB,N,V_isCanceled) isCanceled;
@property (TB,N,V_isFinished) isFinished;
```

## Instance methods

```
-[CAMTransientImageManagerRequest isFinished];
-[CAMTransientImageManagerRequest isCanceled];
-[CAMTransientImageManagerRequest uuid];
-[CAMTransientImageManagerRequest setIsCanceled:];
-[CAMTransientImageManagerRequest setUuid:];
-[CAMTransientImageManagerRequest resultHandler];
-[CAMTransientImageManagerRequest setIsFinished:];
-[CAMTransientImageManagerRequest setResultHandler:];
```
