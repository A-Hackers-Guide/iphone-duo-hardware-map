# `MPSGraphVariableInitializer`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 6 instance variables, 1 properties, 3 instance methods, 5 class methods

## Instance variables

```
d _constant;
d _minimum;
d _maximum;
@"NSString" _file;
I initializerType;
I _initializerType;
```

## Properties

```
@property (TI,R,N,V_initializerType) initializerType;
```

## Class methods

```
+[MPSGraphVariableInitializer initializerWithConstant:];
+[MPSGraphVariableInitializer initializerWithFile:];
+[MPSGraphVariableInitializer initializerWithOnes];
+[MPSGraphVariableInitializer initializerWithRandomUniformWithMinimum:maximum:];
+[MPSGraphVariableInitializer initializerWithZeros];
```

## Instance methods

```
-[MPSGraphVariableInitializer init];
-[MPSGraphVariableInitializer initializerType];
-[MPSGraphVariableInitializer initializedDataWithNumberOfValues:dataType:];
```
