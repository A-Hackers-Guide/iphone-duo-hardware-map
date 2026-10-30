# `MPSCNNLossDataDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSData" _data;
Q _layout;
{?="width"Q"height"Q"depth"Q} _size;
Q _bytesPerRow;
Q _bytesPerImage;
```

## Properties

```
@property (TQ,R,N,V_layout) layout;
@property (T{?=QQQ},R,N,V_size) size;
@property (TQ,N,V_bytesPerRow) bytesPerRow;
@property (TQ,N,V_bytesPerImage) bytesPerImage;
```

## Class methods

```
+[MPSCNNLossDataDescriptor cnnLossDataDescriptorWithData:layout:size:];
```

## Instance methods

```
-[MPSCNNLossDataDescriptor debugDescription];
-[MPSCNNLossDataDescriptor bytesPerRow];
-[MPSCNNLossDataDescriptor dealloc];
-[MPSCNNLossDataDescriptor size];
-[MPSCNNLossDataDescriptor setBytesPerRow:];
-[MPSCNNLossDataDescriptor layout];
-[MPSCNNLossDataDescriptor copyWithZone:];
-[MPSCNNLossDataDescriptor bytesPerImage];
-[MPSCNNLossDataDescriptor setBytesPerImage:];
```
