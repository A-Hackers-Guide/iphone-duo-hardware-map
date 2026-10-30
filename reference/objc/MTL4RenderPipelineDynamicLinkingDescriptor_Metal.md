# `MTL4RenderPipelineDynamicLinkingDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"MTL4PipelineStageDynamicLinkingDescriptor" _vertexLinkingDescriptor;
@"MTL4PipelineStageDynamicLinkingDescriptor" _fragmentLinkingDescriptor;
@"MTL4PipelineStageDynamicLinkingDescriptor" _tileLinkingDescriptor;
@"MTL4PipelineStageDynamicLinkingDescriptor" _objectLinkingDescriptor;
@"MTL4PipelineStageDynamicLinkingDescriptor" _meshLinkingDescriptor;
```

## Properties

```
@property (T@"MTL4PipelineStageDynamicLinkingDescriptor",R,N,V_vertexLinkingDescriptor) vertexLinkingDescriptor;
@property (T@"MTL4PipelineStageDynamicLinkingDescriptor",R,N,V_fragmentLinkingDescriptor) fragmentLinkingDescriptor;
@property (T@"MTL4PipelineStageDynamicLinkingDescriptor",R,N,V_tileLinkingDescriptor) tileLinkingDescriptor;
@property (T@"MTL4PipelineStageDynamicLinkingDescriptor",R,N,V_objectLinkingDescriptor) objectLinkingDescriptor;
@property (T@"MTL4PipelineStageDynamicLinkingDescriptor",R,N,V_meshLinkingDescriptor) meshLinkingDescriptor;
```

## Instance methods

```
-[MTL4RenderPipelineDynamicLinkingDescriptor init];
-[MTL4RenderPipelineDynamicLinkingDescriptor dealloc];
-[MTL4RenderPipelineDynamicLinkingDescriptor reset];
-[MTL4RenderPipelineDynamicLinkingDescriptor hash];
-[MTL4RenderPipelineDynamicLinkingDescriptor copyWithZone:];
-[MTL4RenderPipelineDynamicLinkingDescriptor isEqual:];
-[MTL4RenderPipelineDynamicLinkingDescriptor fragmentLinkingDescriptor];
-[MTL4RenderPipelineDynamicLinkingDescriptor meshLinkingDescriptor];
-[MTL4RenderPipelineDynamicLinkingDescriptor objectLinkingDescriptor];
-[MTL4RenderPipelineDynamicLinkingDescriptor releaseLinkingDescriptors];
-[MTL4RenderPipelineDynamicLinkingDescriptor tileLinkingDescriptor];
-[MTL4RenderPipelineDynamicLinkingDescriptor vertexLinkingDescriptor];
```
