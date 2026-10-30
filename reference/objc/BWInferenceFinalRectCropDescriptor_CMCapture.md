# `BWInferenceFinalRectCropDescriptor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceCropDescriptor`
- 2 instance variables, 5 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _attachedMediaKey;
```

## Properties

```
@property (Tc,R,N) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWInferenceFinalRectCropDescriptor initialize];
+[BWInferenceFinalRectCropDescriptor finalCropRectDescriptorWithName:];
+[BWInferenceFinalRectCropDescriptor finalCropRectDescriptorWithName:attachedMediaKey:];
```

## Instance methods

```
-[BWInferenceFinalRectCropDescriptor identifier];
-[BWInferenceFinalRectCropDescriptor dealloc];
-[BWInferenceFinalRectCropDescriptor description];
-[BWInferenceFinalRectCropDescriptor copyWithZone:];
-[BWInferenceFinalRectCropDescriptor applicableToSampleBuffer:forMediaKey:];
-[BWInferenceFinalRectCropDescriptor maxCropForDimensions:];
-[BWInferenceFinalRectCropDescriptor rectForSampleBuffer:];
```
