# `MTLTensorAuxiliaryPlaneDescriptorMap`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
{map<MTLTensorPlaneType, MTLTensorAuxiliaryPlaneDescriptor *, std::less<MTLTensorPlaneType>, std::allocator<std::pair<const MTLTensorPlaneType, MTLTensorAuxiliaryPlaneDescriptor *>>>="__tree_"{__tree<std::__value_type<MTLTensorPlaneType, MTLTensorAuxiliaryPlaneDescriptor *>, std::__map_value_compare<MTLTensorPlaneType, std::pair<const MTLTensorPlaneType, MTLTensorAuxiliaryPlaneDescriptor *>, std::less<MTLTensorPlaneType>>, std::allocator<std::pair<const MTLTensorPlaneType, MTLTensorAuxiliaryPlaneDescriptor *>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _planeMap;
```

## Instance methods

```
-[MTLTensorAuxiliaryPlaneDescriptorMap init];
-[MTLTensorAuxiliaryPlaneDescriptorMap dealloc];
-[MTLTensorAuxiliaryPlaneDescriptorMap reset];
-[MTLTensorAuxiliaryPlaneDescriptorMap isEmpty];
-[MTLTensorAuxiliaryPlaneDescriptorMap hash];
-[MTLTensorAuxiliaryPlaneDescriptorMap copyWithZone:];
-[MTLTensorAuxiliaryPlaneDescriptorMap isEqual:];
-[MTLTensorAuxiliaryPlaneDescriptorMap descriptorForPlane:];
-[MTLTensorAuxiliaryPlaneDescriptorMap setDescriptor:forPlane:];
```
