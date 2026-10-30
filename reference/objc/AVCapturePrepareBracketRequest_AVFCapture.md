# `AVCapturePrepareBracketRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 1 class methods

## Instance variables

```
@? _completionBlock;
@"FigCaptureStillImageSettings" _settings;
```

## Properties

```
@property (T@"FigCaptureStillImageSettings",R,V_settings) settings;
@property (T@?,R,V_completionBlock) completionBlock;
```

## Class methods

```
+[AVCapturePrepareBracketRequest prepareBracketRequestWithCompletionBlock:settings:];
```

## Instance methods

```
-[AVCapturePrepareBracketRequest completionBlock];
-[AVCapturePrepareBracketRequest settings];
-[AVCapturePrepareBracketRequest dealloc];
-[AVCapturePrepareBracketRequest _initWithCompletionBlock:settings:];
```
