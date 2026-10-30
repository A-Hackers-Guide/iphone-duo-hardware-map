# `IOSurfaceTransactionListImpl`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `IOSurfaceTransactionList`
- 6 instance variables, 7 properties, 7 instance methods, 0 class methods

## Instance variables

```
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _mtx;
Q _length;
Q _kernelFullListLength;
Q _selectedLength;
{shared_ptr<IOSurfaceTransactionSerialized[]>="__ptr_"^{?}"__cntrl_"^{__shared_weak_count}} _serializedData;
{unordered_map<unsigned long, IOSurfaceTransaction *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, IOSurfaceTransaction *>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, std::__unordered_map_hasher<unsigned long, std::pair<const unsigned long, IOSurfaceTransaction *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::pair<const unsigned long, IOSurfaceTransaction *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::pair<const unsigned long, IOSurfaceTransaction *>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, IOSurfaceTransaction *>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} _txnCache;
```

## Properties

```
@property (TQ,R,V_length) length;
@property (TQ,R,V_kernelFullListLength) kernelFullListLength;
@property (TQ,R,V_selectedLength) selectedLength;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[IOSurfaceTransactionListImpl dealloc];
-[IOSurfaceTransactionListImpl length];
-[IOSurfaceTransactionListImpl eventPortAtIndex:];
-[IOSurfaceTransactionListImpl transactionAtIndex:];
-[IOSurfaceTransactionListImpl initWithSerializedData:numWritten:actualLength:selectedLength:];
-[IOSurfaceTransactionListImpl kernelFullListLength];
-[IOSurfaceTransactionListImpl selectedLength];
```
