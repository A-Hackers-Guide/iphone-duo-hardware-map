# `FigCaptureLogSmartCameraGating`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
i _gateIdentifier;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSDate" _openingTimestamp;
@"NSSet" _currentPresentations;
i _numFrames;
i _numTrackedRegions;
i _numBoxesPresented;
i _numEmptyFrames;
i _numClosingFrames;
```

## Class methods

```
+[FigCaptureLogSmartCameraGating initialize];
```

## Instance methods

```
-[FigCaptureLogSmartCameraGating dealloc];
-[FigCaptureLogSmartCameraGating initWithGateIdentifier:];
-[FigCaptureLogSmartCameraGating logGateClosed];
-[FigCaptureLogSmartCameraGating logGateOpened];
-[FigCaptureLogSmartCameraGating logSmartCamIsConfident:presentedIdentifiers:presentedCount:];
-[FigCaptureLogSmartCameraGating logTracksCreated:];
```
