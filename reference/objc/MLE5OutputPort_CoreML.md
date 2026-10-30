# `MLE5OutputPort`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLE5IOPort`
- 4 instance variables, 12 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
^{e5rt_io_port=} _portHandle;
@"MLFeatureDescription" _featureDescription;
@"MLE5OutputPortBinder" _binder;
```

## Properties

```
@property (T^{e5rt_io_port=},R,V_portHandle) portHandle;
@property (T@"MLFeatureDescription",R,V_featureDescription) featureDescription;
@property (T@"MLE5OutputPortBinder",&,V_binder) binder;
@property (TB,R,N) outputBackingWasDirectlyBound;
@property (TB,R,N) boundFeatureDirectly;
@property (T@"MLFeatureValue",R) featureValue;
@property (T@"NSString",R,V_name) name;
@property (T@"MLPixelBufferPool",&,N) pixelBufferPool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLE5OutputPort setPixelBufferPool:];
-[MLE5OutputPort portHandle];
-[MLE5OutputPort outputBackingWasDirectlyBound];
-[MLE5OutputPort pixelBufferPool];
-[MLE5OutputPort featureDescription];
-[MLE5OutputPort prepareWithOptions:error:];
-[MLE5OutputPort dealloc];
-[MLE5OutputPort featureValue];
-[MLE5OutputPort reset];
-[MLE5OutputPort binder];
-[MLE5OutputPort description];
-[MLE5OutputPort reusableForOutputBacking:willBindDirectly:];
-[MLE5OutputPort boundFeatureDirectly];
-[MLE5OutputPort initWithPortHandle:name:featureDescription:];
-[MLE5OutputPort name];
-[MLE5OutputPort setBinder:];
```
