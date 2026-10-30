# `JTFrameRateCalculator`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _name;
Q _receivedRenderCount;
Q _droppedRenderCount;
Q _receivedDisplayFrameCount;
Q _droppedDisplayFrameCount;
d _windowSize;
@"NSDate" _stateDate;
```

## Properties

```
@property (TQ,N,V_receivedRenderCount) receivedRenderCount;
@property (TQ,N,V_droppedRenderCount) droppedRenderCount;
@property (TQ,N,V_receivedDisplayFrameCount) receivedDisplayFrameCount;
@property (TQ,N,V_droppedDisplayFrameCount) droppedDisplayFrameCount;
@property (Td,N,V_windowSize) windowSize;
@property (T@"NSDate",&,N,V_stateDate) stateDate;
@property (T@"NSString",C,N,V_name) name;
```

## Instance methods

```
-[JTFrameRateCalculator windowSize];
-[JTFrameRateCalculator setWindowSize:];
-[JTFrameRateCalculator setName:];
-[JTFrameRateCalculator log:];
-[JTFrameRateCalculator name];
-[JTFrameRateCalculator initWithWindowSize:];
-[JTFrameRateCalculator setStateDate:];
-[JTFrameRateCalculator stateDate];
-[JTFrameRateCalculator JT_restart];
-[JTFrameRateCalculator droppedDisplayFrameCount];
-[JTFrameRateCalculator droppedRenderCount];
-[JTFrameRateCalculator receivedDisplayFrameCount];
-[JTFrameRateCalculator receivedRenderCount];
-[JTFrameRateCalculator setDroppedDisplayFrameCount:];
-[JTFrameRateCalculator setDroppedRenderCount:];
-[JTFrameRateCalculator setReceivedDisplayFrameCount:];
-[JTFrameRateCalculator setReceivedRenderCount:];
-[JTFrameRateCalculator tickDropped];
-[JTFrameRateCalculator tickDroppedDisplay];
-[JTFrameRateCalculator tickFrameReceived];
-[JTFrameRateCalculator tickReceived];
```
