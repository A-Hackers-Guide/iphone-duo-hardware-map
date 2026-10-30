# `MTLToolsPerfCounterMailbox`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
^v _requester;
{vector<std::pair<NSData *, unsigned long>, std::allocator<std::pair<NSData *, unsigned long>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _data;
{__wrap_iter<std::pair<NSData *, unsigned long> *>="__i_"^v} _iterator;
```

## Instance methods

```
-[MTLToolsPerfCounterMailbox extractDataAndNumSamples:forRequester:isLast:];
-[MTLToolsPerfCounterMailbox insertData:andNumSamples:forRequester:];
```
