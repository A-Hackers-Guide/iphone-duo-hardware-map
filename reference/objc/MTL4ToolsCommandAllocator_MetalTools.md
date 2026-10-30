# `MTL4ToolsCommandAllocator`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTL4CommandAllocatorGGDSPI`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<MTL4CommandBuffer>" _currentCommandBuffer;
@"NSString" _label;
```

## Properties

```
@property (T@"NSString",R,V_label) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL4ToolsCommandAllocator label];
-[MTL4ToolsCommandAllocator allocatedSize];
-[MTL4ToolsCommandAllocator reset];
-[MTL4ToolsCommandAllocator addResetHandler:];
-[MTL4ToolsCommandAllocator currentCommandBuffer];
-[MTL4ToolsCommandAllocator initWithBaseObject:parent:];
-[MTL4ToolsCommandAllocator attachCommandBuffer:];
-[MTL4ToolsCommandAllocator detachCommandBuffer];
```
