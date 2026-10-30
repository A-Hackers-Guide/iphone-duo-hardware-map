# `VTFrameProcessorOpticalFlow`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"VEFrameOpticalFlow" _veFrameOpticalFlow;
^{__CVBuffer=} _forwardFlow;
^{__CVBuffer=} _backwardFlow;
```

## Properties

```
@property (T^{__CVBuffer=},R,N,V_forwardFlow) forwardFlow;
@property (T^{__CVBuffer=},R,N,V_backwardFlow) backwardFlow;
```

## Instance methods

```
-[VTFrameProcessorOpticalFlow dealloc];
-[VTFrameProcessorOpticalFlow backwardFlow];
-[VTFrameProcessorOpticalFlow forwardFlow];
-[VTFrameProcessorOpticalFlow initWithForwardFlow:backwardFlow:];
-[VTFrameProcessorOpticalFlow veFrameOpticalFlow];
```
