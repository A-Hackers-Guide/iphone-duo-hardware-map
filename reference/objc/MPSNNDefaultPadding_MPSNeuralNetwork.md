# `MPSNNDefaultPadding`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MPSNNPadding`
- 2 instance variables, 4 properties, 8 instance methods, 5 class methods

## Instance variables

```
Q _method;
B _mpsOwned;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MPSNNDefaultPadding supportsSecureCoding];
+[MPSNNDefaultPadding paddingWithMethod:];
+[MPSNNDefaultPadding zeroPaddingWithTopAmount:bottomAmount:leftAmount:rightAmount:];
+[MPSNNDefaultPadding paddingForTensorflowAveragePooling];
+[MPSNNDefaultPadding paddingForTensorflowAveragePoolingValidOnly];
```

## Instance methods

```
-[MPSNNDefaultPadding debugDescription];
-[MPSNNDefaultPadding label];
-[MPSNNDefaultPadding dealloc];
-[MPSNNDefaultPadding encodeWithCoder:];
-[MPSNNDefaultPadding initWithCoder:];
-[MPSNNDefaultPadding isEqual:];
-[MPSNNDefaultPadding paddingMethod];
-[MPSNNDefaultPadding initWithPaddingMethod:];
```
