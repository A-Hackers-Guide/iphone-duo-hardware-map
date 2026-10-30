# `BWStillImageProcessingPlan`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"BWStillImageSettings" _settings;
@"NSMutableDictionary" _inputsByBufferTypeByPortTypeBySequenceNumber;
```

## Instance methods

```
-[BWStillImageProcessingPlan dealloc];
-[BWStillImageProcessingPlan description];
-[BWStillImageProcessingPlan initWithSettings:];
-[BWStillImageProcessingPlan addInput:sequenceNumber:portType:bufferType:];
-[BWStillImageProcessingPlan addInput:sequenceNumber:portType:bufferTypes:];
-[BWStillImageProcessingPlan lastAddedInputForSequenceNumber:portType:bufferType:];
```
