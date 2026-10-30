# `MPSGraphCallablesDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _callables;
Q _callablesHash;
```

## Properties

```
@property (T@"NSDictionary",&,V_callables) callables;
@property (TQ,V_callablesHash) callablesHash;
```

## Instance methods

```
-[MPSGraphCallablesDescriptor initWithHash:];
-[MPSGraphCallablesDescriptor setCallables:];
-[MPSGraphCallablesDescriptor callables];
-[MPSGraphCallablesDescriptor callablesHash];
-[MPSGraphCallablesDescriptor computeHash];
-[MPSGraphCallablesDescriptor initWithCallables:];
-[MPSGraphCallablesDescriptor initWithCallables:hash:];
-[MPSGraphCallablesDescriptor setCallablesHash:];
```
