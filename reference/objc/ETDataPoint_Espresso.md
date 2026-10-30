# `ETDataPoint`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
{map<std::string, vImage_Buffer, std::less<std::string>, std::allocator<std::pair<const std::string, vImage_Buffer>>>="__tree_"{__tree<std::__value_type<std::string, vImage_Buffer>, std::__map_value_compare<std::string, std::pair<const std::string, vImage_Buffer>, std::less<std::string>>, std::allocator<std::pair<const std::string, vImage_Buffer>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} image_buffers;
{map<std::string, ETDataPoint_buffer, std::less<std::string>, std::allocator<std::pair<const std::string, ETDataPoint_buffer>>>="__tree_"{__tree<std::__value_type<std::string, ETDataPoint_buffer>, std::__map_value_compare<std::string, std::pair<const std::string, ETDataPoint_buffer>, std::less<std::string>>, std::allocator<std::pair<const std::string, ETDataPoint_buffer>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} buffers;
```

## Instance methods

```
-[ETDataPoint dealloc];
-[ETDataPoint bufferWithKey:];
-[ETDataPoint getSampleData];
-[ETDataPoint imageWithKey:];
-[ETDataPoint iterateBuffersByKey:];
-[ETDataPoint setData:size:forKey:freeWhenDone:];
-[ETDataPoint setImage:forKey:];
```
