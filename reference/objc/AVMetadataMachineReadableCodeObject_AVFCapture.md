# `AVMetadataMachineReadableCodeObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- 1 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"AVMetadataMachineReadableCodeObjectInternal" _internal;
```

## Properties

```
@property (T@"CIBarcodeDescriptor",R) descriptor;
@property (T@"NSArray",R) corners;
@property (T@"NSString",R) stringValue;
```

## Class methods

```
+[AVMetadataMachineReadableCodeObject machineReadableCodeObjectWithAppClipCodeDictionary:input:];
+[AVMetadataMachineReadableCodeObject machineReadableCodeObjectWithFigEmbeddedCaptureDeviceMachineReadableCodeDictionary:input:];
```

## Instance methods

```
-[AVMetadataMachineReadableCodeObject stringValue];
-[AVMetadataMachineReadableCodeObject descriptor];
-[AVMetadataMachineReadableCodeObject dealloc];
-[AVMetadataMachineReadableCodeObject description];
-[AVMetadataMachineReadableCodeObject corners];
-[AVMetadataMachineReadableCodeObject basicDescriptor];
-[AVMetadataMachineReadableCodeObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataMachineReadableCodeObject initWithAppClipCodeDictionary:input:];
-[AVMetadataMachineReadableCodeObject initWithFigEmbeddedCaptureDeviceMachineReadableCodeDictionary:input:];
```
