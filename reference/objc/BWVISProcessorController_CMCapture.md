# `BWVISProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VISProcessorDelegate`
- 8 instance variables, 9 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"<VISProcessor>" _visProcessor;
@"<VISConfiguration>" _visConfiguration;
B _buffersEnqueued;
B _longPressModeEnabled;
B _flipHorizontalOrientationEnabled;
B _smartStyleReversibilityProcessingEnabled;
@"BWVISProcessorControllerConfiguration" _configuration;
@"<BWVISProcessorDelegate>" _delegate;
```

## Properties

```
@property (TB,N,V_longPressModeEnabled) longPressModeEnabled;
@property (TB,N,V_flipHorizontalOrientationEnabled) flipHorizontalOrientationEnabled;
@property (TB,N,V_smartStyleReversibilityProcessingEnabled) smartStyleReversibilityProcessingEnabled;
@property (T@"BWVISProcessorControllerConfiguration",&,N,V_configuration) configuration;
@property (T@"<BWVISProcessorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWVISProcessorController initialize];
```

## Instance methods

```
-[BWVISProcessorController dealloc];
-[BWVISProcessorController setConfiguration:];
-[BWVISProcessorController willStartProcessingBuffer:withStatus:];
-[BWVISProcessorController setDelegate:];
-[BWVISProcessorController configuration];
-[BWVISProcessorController delegate];
-[BWVISProcessorController didCompleteProcessingOfBuffer:withStatus:];
-[BWVISProcessorController enqueueBufferForProcessing:];
-[BWVISProcessorController finishPendingProcessing];
-[BWVISProcessorController flipHorizontalOrientationEnabled];
-[BWVISProcessorController longPressModeEnabled];
-[BWVISProcessorController prepareToProcess];
-[BWVISProcessorController setFlipHorizontalOrientationEnabled:];
-[BWVISProcessorController setLongPressModeEnabled:];
-[BWVISProcessorController setSmartStyleReversibilityProcessingEnabled:];
-[BWVISProcessorController smartStyleReversibilityProcessingEnabled];
```
