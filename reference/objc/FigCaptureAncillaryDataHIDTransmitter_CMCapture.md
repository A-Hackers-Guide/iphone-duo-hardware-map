# `FigCaptureAncillaryDataHIDTransmitter`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 17 instance methods, 1 class methods

## Instance variables

```
I _targetUsagePage;
I _targetVendor;
I _targetProduct;
@"<FigCaptureAncillaryDataHIDTransmitterDelegate>" _delegate;
^{__IOHIDManager=} _hidManager;
^{__IOHIDDevice=} _hidDevice;
```

## Properties

```
@property (T^{__IOHIDManager=},N,V_hidManager) hidManager;
@property (T^{__IOHIDDevice=},N,V_hidDevice) hidDevice;
@property (TI,N,V_targetUsagePage) targetUsagePage;
@property (TI,N,V_targetVendor) targetVendor;
@property (TI,N,V_targetProduct) targetProduct;
@property (T@"<FigCaptureAncillaryDataHIDTransmitterDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[FigCaptureAncillaryDataHIDTransmitter initialize];
```

## Instance methods

```
-[FigCaptureAncillaryDataHIDTransmitter init];
-[FigCaptureAncillaryDataHIDTransmitter dealloc];
-[FigCaptureAncillaryDataHIDTransmitter setDelegate:];
-[FigCaptureAncillaryDataHIDTransmitter delegate];
-[FigCaptureAncillaryDataHIDTransmitter hidDevice];
-[FigCaptureAncillaryDataHIDTransmitter setHidDevice:];
-[FigCaptureAncillaryDataHIDTransmitter targetUsagePage];
-[FigCaptureAncillaryDataHIDTransmitter closeDevice];
-[FigCaptureAncillaryDataHIDTransmitter hidManager];
-[FigCaptureAncillaryDataHIDTransmitter openDeviceWithUsagePage:vendor:product:error:];
-[FigCaptureAncillaryDataHIDTransmitter sendReport:];
-[FigCaptureAncillaryDataHIDTransmitter setHidManager:];
-[FigCaptureAncillaryDataHIDTransmitter setTargetProduct:];
-[FigCaptureAncillaryDataHIDTransmitter setTargetUsagePage:];
-[FigCaptureAncillaryDataHIDTransmitter setTargetVendor:];
-[FigCaptureAncillaryDataHIDTransmitter targetProduct];
-[FigCaptureAncillaryDataHIDTransmitter targetVendor];
```
