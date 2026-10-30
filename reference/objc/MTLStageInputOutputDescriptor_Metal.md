# `MTLStageInputOutputDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 0 instance variables, 4 properties, 3 instance methods, 3 class methods

## Properties

```
@property (T@"MTLBufferLayoutDescriptorArray",R,D) layouts;
@property (T@"MTLAttributeDescriptorArray",R,D) attributes;
@property (TQ,D,N) indexType;
@property (TQ,D,N) indexBufferIndex;
```

## Class methods

```
+[MTLStageInputOutputDescriptor allocWithZone:];
+[MTLStageInputOutputDescriptor stageInputOutputDescriptor];
+[MTLStageInputOutputDescriptor alloc];
```

## Instance methods

```
-[MTLStageInputOutputDescriptor formattedDescription:];
-[MTLStageInputOutputDescriptor reset];
-[MTLStageInputOutputDescriptor copyWithZone:];
```
