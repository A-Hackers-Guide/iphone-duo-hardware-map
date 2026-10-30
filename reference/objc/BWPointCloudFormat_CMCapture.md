# `BWPointCloudFormat`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFormat`
- Protocols: `BWDataBufferBackedFormat`
- 4 instance variables, 8 properties, 9 instance methods, 3 class methods

## Instance variables

```
Q _maxPoints;
Q _dataBufferSize;
I _dataFormat;
@"NSDictionary" _dataBufferAttributes;
```

## Properties

```
@property (TQ,R,N,V_maxPoints) maxPoints;
@property (TQ,R,N,V_dataBufferSize) dataBufferSize;
@property (TI,R,N,V_dataFormat) dataFormat;
@property (T@"NSDictionary",R,N,V_dataBufferAttributes) dataBufferAttributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPointCloudFormat initialize];
+[BWPointCloudFormat formatByResolvingRequirements:];
+[BWPointCloudFormat formatByResolvingRequirements:printErrors:];
```

## Instance methods

```
-[BWPointCloudFormat formatDescription];
-[BWPointCloudFormat debugDescription];
-[BWPointCloudFormat dealloc];
-[BWPointCloudFormat description];
-[BWPointCloudFormat mediaType];
-[BWPointCloudFormat dataFormat];
-[BWPointCloudFormat dataBufferAttributes];
-[BWPointCloudFormat dataBufferSize];
-[BWPointCloudFormat maxPoints];
```
