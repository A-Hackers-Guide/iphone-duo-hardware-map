# `ETDataSourceWithCache`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ETDataSource`
- 4 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"<ETDataSource>" _source;
{map<int, ETDataPoint *, std::less<int>, std::allocator<std::pair<const int, ETDataPoint *>>>="__tree_"{__tree<std::__value_type<int, ETDataPoint *>, std::__map_value_compare<int, std::pair<const int, ETDataPoint *>, std::less<int>>, std::allocator<std::pair<const int, ETDataPoint *>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _cache;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} dump_path;
B dump_descriptors;
```

## Instance methods

```
-[ETDataSourceWithCache initWithDataSource:];
-[ETDataSourceWithCache numberOfDataPoints];
-[ETDataSourceWithCache dataPointAtIndex:];
-[ETDataSourceWithCache initWithDataSource:dumpPath:];
```
