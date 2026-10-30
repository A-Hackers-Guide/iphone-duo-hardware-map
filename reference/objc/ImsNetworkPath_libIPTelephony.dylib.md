# `ImsNetworkPath`

- Image: [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](../userland/System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NWPathEvaluator" _pathEvaluator;
{weak_ptr<ImsNetworkPathDelegate>="__ptr_"^{ImsNetworkPathDelegate}"__cntrl_"^{__shared_weak_count}} _delegate;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} _ifaceName;
B _observingPath;
```

## Instance methods

```
-[ImsNetworkPath observeValueForKeyPath:ofObject:change:context:];
-[ImsNetworkPath dealloc];
-[ImsNetworkPath ifaceName];
-[ImsNetworkPath evaluateInterface];
-[ImsNetworkPath initWithInterface:delegate:];
```
