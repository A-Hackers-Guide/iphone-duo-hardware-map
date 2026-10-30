# `MLE5InputPortBinder`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLE5PortBinder`
- 6 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
^{__CVBuffer=} _temporarilyBoundPixelBuffer;
C _bindingMode;
@"MLPixelBufferPool" _pixelBufferPool;
^{e5rt_io_port=} _portHandle;
@"MLFeatureDescription" _featureDescription;
@"MLFeatureValue" _directlyBoundFeatureValue;
```

## Properties

```
@property (T^{e5rt_io_port=},R,V_portHandle) portHandle;
@property (T@"MLFeatureDescription",R,V_featureDescription) featureDescription;
@property (T@"MLFeatureValue",&,N,V_directlyBoundFeatureValue) directlyBoundFeatureValue;
@property (TC,N,V_bindingMode) bindingMode;
@property (T@"MLPixelBufferPool",&,N,V_pixelBufferPool) pixelBufferPool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLE5InputPortBinder setPixelBufferPool:];
-[MLE5InputPortBinder portHandle];
-[MLE5InputPortBinder pixelBufferPool];
-[MLE5InputPortBinder featureDescription];
-[MLE5InputPortBinder dealloc];
-[MLE5InputPortBinder reset];
-[MLE5InputPortBinder bindingMode];
-[MLE5InputPortBinder copyFeatureValue:error:];
-[MLE5InputPortBinder reusableForFeatureValue:willBindDirectly:];
-[MLE5InputPortBinder initWithPort:featureDescription:];
-[MLE5InputPortBinder setDirectlyBoundFeatureValue:];
-[MLE5InputPortBinder bindMemoryObjectForFeatureValue:error:];
-[MLE5InputPortBinder _reusableForFeatureValue:directMode:];
-[MLE5InputPortBinder directlyBoundFeatureValue];
-[MLE5InputPortBinder setBindingMode:];
```
