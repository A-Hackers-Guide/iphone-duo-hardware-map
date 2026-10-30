# `ETDataSourceBuf`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ETDataSource`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
{map<std::string, std::shared_ptr<Espresso::blob<float, 2>>, std::less<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 2>>>>>="__tree_"{__tree<std::__value_type<std::string, std::shared_ptr<Espresso::blob<float, 2>>>, std::__map_value_compare<std::string, std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 2>>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::shared_ptr<Espresso::blob<float, 2>>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} blobs;
i number_of_data_points;
```

## Instance methods

```
-[ETDataSourceBuf numberOfDataPoints];
-[ETDataSourceBuf dataAtIndex:key:];
-[ETDataSourceBuf dataPointAtIndex:];
-[ETDataSourceBuf setBlobs:numberOfDataPoints:nonBatches:];
```
