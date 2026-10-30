# `CLNotifierServiceAdapter`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLIntersiloService`
- Protocols: `CLNotifierServiceProtocol`
- 2 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
{unordered_map<unsigned long, int, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, int>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long, int>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, int>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, int>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, int>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, int>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, int>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, int>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _clients;
^{CLNotifierBase=^^?} _notifier;
```

## Properties

```
@property (T^{CLNotifierBase=^^?},R,N,V_notifier) notifier;
@property (TB,N) valid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CLNotifierServiceAdapter debugDescription];
-[CLNotifierServiceAdapter init];
-[CLNotifierServiceAdapter invalidate];
-[CLNotifierServiceAdapter notifier];
-[CLNotifierServiceAdapter forget:];
-[CLNotifierServiceAdapter deleteAdaptedNotifier];
-[CLNotifierServiceAdapter notifierClientNumForCoparty:];
-[CLNotifierServiceAdapter register:forNotification:registrationInfo:];
-[CLNotifierServiceAdapter setAdaptedNotifier:];
-[CLNotifierServiceAdapter unregister:forNotification:];
```
