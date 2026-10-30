# `MTL4PipelineStageDynamicLinkingDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
Q _maxCallStackDepth;
@"NSArray" _binaryLinkedFunctions;
@"NSArray" _preloadedLibraries;
```

## Properties

```
@property (TQ,N,V_maxCallStackDepth) maxCallStackDepth;
@property (T@"NSArray",C,N,V_binaryLinkedFunctions) binaryLinkedFunctions;
@property (T@"NSArray",C,N,V_preloadedLibraries) preloadedLibraries;
```

## Instance methods

```
-[MTL4PipelineStageDynamicLinkingDescriptor init];
-[MTL4PipelineStageDynamicLinkingDescriptor maxCallStackDepth];
-[MTL4PipelineStageDynamicLinkingDescriptor setMaxCallStackDepth:];
-[MTL4PipelineStageDynamicLinkingDescriptor dealloc];
-[MTL4PipelineStageDynamicLinkingDescriptor preloadedLibraries];
-[MTL4PipelineStageDynamicLinkingDescriptor setPreloadedLibraries:];
-[MTL4PipelineStageDynamicLinkingDescriptor hash];
-[MTL4PipelineStageDynamicLinkingDescriptor copyWithZone:];
-[MTL4PipelineStageDynamicLinkingDescriptor isEqual:];
-[MTL4PipelineStageDynamicLinkingDescriptor binaryLinkedFunctions];
-[MTL4PipelineStageDynamicLinkingDescriptor setBinaryLinkedFunctions:];
```
