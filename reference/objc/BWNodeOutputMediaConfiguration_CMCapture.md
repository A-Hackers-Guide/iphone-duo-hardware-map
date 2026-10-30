# `BWNodeOutputMediaConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 12 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSString" _associatedAttachedMediaKey;
@"BWFormatRequirements" _formatRequirements;
@"NSArray" _indexesOfInputsWhichDrivesThisOutput;
@"NSString" _attachedMediaKeyOfInputWhichDrivesThisOutput;
i _passthroughMode;
i _indexOfInputWhichDrivesThisOutput;
i _owningNodeRetainedBufferCount;
B _providesPixelBufferPool;
B _providesDataBufferPool;
B _pixelBufferPoolProvidesBackPressure;
B _pixelBufferPoolReportSlowBackPressureAllocations;
B _performsAttachedMediaRemapping;
i _owningNodeIndefinitelyHeldBufferCount;
```

## Properties

```
@property (T@"BWFormatRequirements",&,N,V_formatRequirements) formatRequirements;
@property (TB,N,V_providesPixelBufferPool) providesPixelBufferPool;
@property (TB,N,V_providesDataBufferPool) providesDataBufferPool;
@property (TB,N,V_pixelBufferPoolProvidesBackPressure) pixelBufferPoolProvidesBackPressure;
@property (TB,N,V_pixelBufferPoolReportSlowBackPressureAllocations) pixelBufferPoolReportSlowBackPressureAllocations;
@property (Ti,N,V_passthroughMode) passthroughMode;
@property (Ti,N) indexOfInputWhichDrivesThisOutput;
@property (T@"NSArray",C,N) indexesOfInputsWhichDrivesThisOutput;
@property (TB,R,N) performsAttachedMediaRemapping;
@property (T@"NSString",C,N) attachedMediaKeyOfInputWhichDrivesThisOutput;
@property (Ti,N,V_owningNodeRetainedBufferCount) owningNodeRetainedBufferCount;
@property (Ti,N,V_owningNodeIndefinitelyHeldBufferCount) owningNodeIndefinitelyHeldBufferCount;
```

## Instance methods

```
-[BWNodeOutputMediaConfiguration pixelBufferPoolProvidesBackPressure];
-[BWNodeOutputMediaConfiguration pixelBufferPoolReportSlowBackPressureAllocations];
-[BWNodeOutputMediaConfiguration indexOfInputWhichDrivesThisOutput];
-[BWNodeOutputMediaConfiguration providesPixelBufferPool];
-[BWNodeOutputMediaConfiguration setProvidesPixelBufferPool:];
-[BWNodeOutputMediaConfiguration setFormatRequirements:];
-[BWNodeOutputMediaConfiguration setOwningNodeRetainedBufferCount:];
-[BWNodeOutputMediaConfiguration setProvidesDataBufferPool:];
-[BWNodeOutputMediaConfiguration setIndexOfInputWhichDrivesThisOutput:];
-[BWNodeOutputMediaConfiguration setPixelBufferPoolReportSlowBackPressureAllocations:];
-[BWNodeOutputMediaConfiguration setPixelBufferPoolProvidesBackPressure:];
-[BWNodeOutputMediaConfiguration formatRequirements];
-[BWNodeOutputMediaConfiguration owningNodeRetainedBufferCount];
-[BWNodeOutputMediaConfiguration setPassthroughMode:];
-[BWNodeOutputMediaConfiguration indexesOfInputsWhichDrivesThisOutput];
-[BWNodeOutputMediaConfiguration passthroughMode];
-[BWNodeOutputMediaConfiguration init];
-[BWNodeOutputMediaConfiguration owningNodeIndefinitelyHeldBufferCount];
-[BWNodeOutputMediaConfiguration setIndexesOfInputsWhichDrivesThisOutput:];
-[BWNodeOutputMediaConfiguration dealloc];
-[BWNodeOutputMediaConfiguration setAttachedMediaKeyOfInputWhichDrivesThisOutput:];
-[BWNodeOutputMediaConfiguration isDrivenByInputWithIndex:];
-[BWNodeOutputMediaConfiguration attachedMediaKeyOfInputWhichDrivesThisOutput];
-[BWNodeOutputMediaConfiguration _setAssociatedAttachedMediaKey:];
-[BWNodeOutputMediaConfiguration providesDataBufferPool];
-[BWNodeOutputMediaConfiguration performsAttachedMediaRemapping];
-[BWNodeOutputMediaConfiguration setOwningNodeIndefinitelyHeldBufferCount:];
```
