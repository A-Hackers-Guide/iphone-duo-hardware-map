# `MLE5InputPort`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLE5IOPort`
- 3 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
^{e5rt_io_port=} _portHandle;
@"MLE5InputPortBinder" _binder;
```

## Properties

```
@property (T^{e5rt_io_port=},R,V_portHandle) portHandle;
@property (T@"MLE5InputPortBinder",&,V_binder) binder;
@property (TB,R,N) boundFeatureDirectly;
@property (T@"NSString",R,V_name) name;
@property (T@"MLPixelBufferPool",&,N) pixelBufferPool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLE5InputPort setPixelBufferPool:];
-[MLE5InputPort portHandle];
-[MLE5InputPort pixelBufferPool];
-[MLE5InputPort dealloc];
-[MLE5InputPort reset];
-[MLE5InputPort binder];
-[MLE5InputPort copyFeatureValue:error:];
-[MLE5InputPort description];
-[MLE5InputPort reusableForFeatureValue:willBindDirectly:];
-[MLE5InputPort boundFeatureDirectly];
-[MLE5InputPort prepareForFeatureValue:error:];
-[MLE5InputPort initWithPortHandle:name:featureDescription:];
-[MLE5InputPort name];
-[MLE5InputPort setBinder:];
```
