# `MTLCaptureManager`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _isCapturing;
@"<MTLCaptureScope>" _defaultCaptureScope;
```

## Properties

```
@property (T@"<MTLCaptureScope>",&,V_defaultCaptureScope) defaultCaptureScope;
@property (TB,R,V_isCapturing) isCapturing;
```

## Class methods

```
+[MTLCaptureManager sharedCaptureManager];
```

## Instance methods

```
-[MTLCaptureManager isCapturing];
-[MTLCaptureManager stopCapture];
-[MTLCaptureManager newCaptureScopeWithCommandQueue:];
-[MTLCaptureManager dealloc];
-[MTLCaptureManager newCaptureScopeWithDevice:];
-[MTLCaptureManager startCaptureWithDescriptor:error:];
-[MTLCaptureManager startCaptureWithScope:];
-[MTLCaptureManager startCaptureWithDevice:];
-[MTLCaptureManager defaultCaptureScope];
-[MTLCaptureManager startCaptureWithCommandQueue:];
-[MTLCaptureManager setDefaultCaptureScope:];
-[MTLCaptureManager newCaptureScopeWithMTL4CommandQueue:];
-[MTLCaptureManager supportsDestination:];
```
