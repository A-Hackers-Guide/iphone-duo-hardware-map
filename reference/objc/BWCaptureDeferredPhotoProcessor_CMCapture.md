# `BWCaptureDeferredPhotoProcessor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureDeferredProcessingJobDelegate`
- 1 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"FigWeakReference" _weakDeferredPhotoProcessorReference;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWCaptureDeferredPhotoProcessor dealloc];
-[BWCaptureDeferredPhotoProcessor request:failedWithError:];
-[BWCaptureDeferredPhotoProcessor _prepareToTerminateImmediatelyDueToError:];
-[BWCaptureDeferredPhotoProcessor initWithFigCaptureDeferredPhotoProcessor:];
-[BWCaptureDeferredPhotoProcessor job:failedWithError:];
-[BWCaptureDeferredPhotoProcessor job:finalizedPhotoWithSampleBuffer:];
-[BWCaptureDeferredPhotoProcessor jobFinished:];
```
