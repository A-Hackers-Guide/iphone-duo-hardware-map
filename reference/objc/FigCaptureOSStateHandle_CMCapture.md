# `FigCaptureOSStateHandle`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _title;
@"NSObject<OS_dispatch_queue>" _queue;
@"FigWeakReference" _dataProviderWeakReference;
@? _dataProviderBlock;
Q _osStateHandle;
```

## Class methods

```
+[FigCaptureOSStateHandle initialize];
```

## Instance methods

```
-[FigCaptureOSStateHandle debugDescription];
-[FigCaptureOSStateHandle dealloc];
-[FigCaptureOSStateHandle description];
-[FigCaptureOSStateHandle _initWithTitle:queue:dataProvider:dataProviderBlock:];
-[FigCaptureOSStateHandle _osStateData:];
-[FigCaptureOSStateHandle initWithTitle:queue:dataProvider:];
-[FigCaptureOSStateHandle initWithTitle:queue:dataProviderBlock:];
```
