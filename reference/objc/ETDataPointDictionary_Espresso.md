# `ETDataPointDictionary`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
{map<std::string, vImage_Buffer, std::less<std::string>, std::allocator<std::pair<const std::string, vImage_Buffer>>>="__tree_"{__tree<std::__value_type<std::string, vImage_Buffer>, std::__map_value_compare<std::string, std::pair<const std::string, vImage_Buffer>, std::less<std::string>>, std::allocator<std::pair<const std::string, vImage_Buffer>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _image_buffers;
{map<std::string, float_buffer_t, std::less<std::string>, std::allocator<std::pair<const std::string, float_buffer_t>>>="__tree_"{__tree<std::__value_type<std::string, float_buffer_t>, std::__map_value_compare<std::string, std::pair<const std::string, float_buffer_t>, std::less<std::string>>, std::allocator<std::pair<const std::string, float_buffer_t>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _float_buffers;
```

## Properties

```
@property (T{map<std::string, vImage_Buffer, std::less<std::string>, std::allocator<std::pair<const std::string, vImage_Buffer>>>={__tree<std::__value_type<std::string, vImage_Buffer>, std::__map_value_compare<std::string, std::pair<const std::string, vImage_Buffer>, std::less<std::string>>, std::allocator<std::pair<const std::string, vImage_Buffer>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},V_image_buffers) image_buffers;
@property (T{map<std::string, float_buffer_t, std::less<std::string>, std::allocator<std::pair<const std::string, float_buffer_t>>>={__tree<std::__value_type<std::string, float_buffer_t>, std::__map_value_compare<std::string, std::pair<const std::string, float_buffer_t>, std::less<std::string>>, std::allocator<std::pair<const std::string, float_buffer_t>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}},V_float_buffers) float_buffers;
```

## Instance methods

```
-[ETDataPointDictionary dataForKey:error:];
-[ETDataPointDictionary dataArrayForKey:error:];
-[ETDataPointDictionary float_buffers];
-[ETDataPointDictionary image_buffers];
-[ETDataPointDictionary setData:size:forKey:freeWhenDone:];
-[ETDataPointDictionary setFloat_buffers:];
-[ETDataPointDictionary setImage:forKey:];
-[ETDataPointDictionary setImage_buffers:];
```
