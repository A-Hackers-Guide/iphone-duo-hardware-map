# `MTLTensorBufferAttachments`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
{map<MTLTensorPlaneType, BufferAttachment, std::less<MTLTensorPlaneType>, std::allocator<std::pair<const MTLTensorPlaneType, BufferAttachment>>>="__tree_"{__tree<std::__value_type<MTLTensorPlaneType, BufferAttachment>, std::__map_value_compare<MTLTensorPlaneType, std::pair<const MTLTensorPlaneType, BufferAttachment>, std::less<MTLTensorPlaneType>>, std::allocator<std::pair<const MTLTensorPlaneType, BufferAttachment>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _bufferAttachments;
```

## Instance methods

```
-[MTLTensorBufferAttachments init];
-[MTLTensorBufferAttachments dealloc];
-[MTLTensorBufferAttachments reset];
-[MTLTensorBufferAttachments copyWithZone:];
-[MTLTensorBufferAttachments bufferForPlane:];
-[MTLTensorBufferAttachments offsetForPlane:];
-[MTLTensorBufferAttachments setBuffer:offset:forPlane:];
```
