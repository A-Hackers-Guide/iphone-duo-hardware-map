# `AVCaptureAncillaryDataEncoder`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _setUUID;
@"NSMutableDictionary" _currentUserDefinedAncillaryData;
@"AVCaptureBroadcastVideoOutput" _output;
B _enabled;
```

## Properties

```
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"NSDictionary",R,N) currentUserDefinedAncillaryData;
@property (Ts,R,N) userDefinedAncillaryDataSizeRemaining;
```

## Instance methods

```
-[AVCaptureAncillaryDataEncoder isEnabled];
-[AVCaptureAncillaryDataEncoder setEnabled:];
-[AVCaptureAncillaryDataEncoder currentUserDefinedAncillaryData];
-[AVCaptureAncillaryDataEncoder removeRDD18AncillaryDataForTag:];
-[AVCaptureAncillaryDataEncoder canSetDataForTag:];
-[AVCaptureAncillaryDataEncoder canSetStringForTag:];
-[AVCaptureAncillaryDataEncoder initWithCaptureOutput:];
-[AVCaptureAncillaryDataEncoder sendUserDataEntryToCCD:value:];
-[AVCaptureAncillaryDataEncoder setRDD18AncillaryData:forTag:error:];
-[AVCaptureAncillaryDataEncoder setRDD18AncillaryDataString:forTag:error:];
-[AVCaptureAncillaryDataEncoder setUserInstanceUID:forUserUDAMVersion:];
-[AVCaptureAncillaryDataEncoder sizeForTag:];
-[AVCaptureAncillaryDataEncoder userDefinedAncillaryDataSizeRemaining];
```
