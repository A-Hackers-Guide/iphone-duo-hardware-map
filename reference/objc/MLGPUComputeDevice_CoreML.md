# `MLGPUComputeDevice`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLComputeDeviceProtocol`
- 1 instance variables, 5 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"<MTLDevice>" _metalDevice;
```

## Properties

```
@property (T@"<MTLDevice>",R,N,V_metalDevice) metalDevice;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLGPUComputeDevice deviceWithMetalDevice:];
```

## Instance methods

```
-[MLGPUComputeDevice metalDevice];
-[MLGPUComputeDevice hash];
-[MLGPUComputeDevice description];
-[MLGPUComputeDevice isEqual:];
-[MLGPUComputeDevice initWithMetalDevice:];
```
