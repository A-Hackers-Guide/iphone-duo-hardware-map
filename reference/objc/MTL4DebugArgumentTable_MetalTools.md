# `MTL4DebugArgumentTable`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsArgumentTable`
- 4 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
{vector<MTL4DebugBindingInfo, std::allocator<MTL4DebugBindingInfo>>="__begin_"^{MTL4DebugBindingInfo}"__end_"^{MTL4DebugBindingInfo}""{?="__cap_"^{MTL4DebugBindingInfo}}} _bufferBindings;
{vector<MTL4DebugBindingInfo, std::allocator<MTL4DebugBindingInfo>>="__begin_"^{MTL4DebugBindingInfo}"__end_"^{MTL4DebugBindingInfo}""{?="__cap_"^{MTL4DebugBindingInfo}}} _textureBindings;
{vector<MTL4DebugBindingInfo, std::allocator<MTL4DebugBindingInfo>>="__begin_"^{MTL4DebugBindingInfo}"__end_"^{MTL4DebugBindingInfo}""{?="__cap_"^{MTL4DebugBindingInfo}}} _samplerBindings;
B _supportsAttributeStrides;
```

## Instance methods

```
-[MTL4DebugArgumentTable setTexture:atIndex:];
-[MTL4DebugArgumentTable setSamplerState:atIndex:];
-[MTL4DebugArgumentTable setAddress:atIndex:];
-[MTL4DebugArgumentTable setAddress:attributeStride:atIndex:];
-[MTL4DebugArgumentTable setResource:atBufferIndex:];
-[MTL4DebugArgumentTable bufferBindingAtIndex:];
-[MTL4DebugArgumentTable initWithArgumentTable:device:descriptor:];
-[MTL4DebugArgumentTable samplerBindingAtIndex:];
-[MTL4DebugArgumentTable textureBindingAtIndex:];
```
