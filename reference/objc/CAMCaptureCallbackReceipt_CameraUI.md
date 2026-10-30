# `CAMCaptureCallbackReceipt`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 0 class methods

## Instance variables

```
q _callback;
d _secondsSinceBegin;
@"NSError" _error;
```

## Properties

```
@property (Tq,R,N,V_callback) callback;
@property (Td,R,N,V_secondsSinceBegin) secondsSinceBegin;
@property (T@"NSError",R,N,V_error) error;
```

## Instance methods

```
-[CAMCaptureCallbackReceipt callback];
-[CAMCaptureCallbackReceipt error];
-[CAMCaptureCallbackReceipt initWithCallback:duration:error:];
-[CAMCaptureCallbackReceipt secondsSinceBegin];
```
