# `CoreTelephonyClientMux`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MuxNotificationSinkDelegate`
- 12 instance variables, 7 properties, 42 instance methods, 0 class methods

## Instance variables

```
{map<__unsafe_unretained id, (anonymous namespace)::DelegateContext, std::less<__unsafe_unretained id>, std::allocator<std::pair<const __unsafe_unretained id, (anonymous namespace)::DelegateContext>>>="__tree_"{__tree<std::__value_type<__unsafe_unretained id, (anonymous namespace)::DelegateContext>, std::__map_value_compare<__unsafe_unretained id, std::pair<const __unsafe_unretained id, (anonymous namespace)::DelegateContext>, std::less<__unsafe_unretained id>>, std::allocator<std::pair<const __unsafe_unretained id, (anonymous namespace)::DelegateContext>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _delegates;
@"NSSet" _currentSelectorSet;
{map<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>, std::less<__CTAssertionType *>, std::allocator<std::pair<__CTAssertionType *const, std::pair<dispatch::queue, void (^)(NSError *)>>>>="__tree_"{__tree<std::__value_type<__CTAssertionType *, std::pair<dispatch::queue, void (^)(NSError *)>>, std::__map_value_compare<__CTAssertionType *, std::pair<__CTAssertionType *const, std::pair<dispatch::queue, void (^)(NSError *)>>, std::less<__CTAssertionType *>>, std::allocator<std::pair<__CTAssertionType *const, std::pair<dispatch::queue, void (^)(NSError *)>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _clientCallback;
@"FrameworkCache" _cache;
@"<SystemConfigurationProviding>" _systemConfigProvider;
@"NSXPCConnection" _connection;
{queue="fObj"{object="fObj"^{dispatch_object_s}}} _xpcQueue;
@"NSXPCListenerEndpoint" _endpoint;
@"MuxNotificationSink" _notificationSink;
@"NSError" _reconnectError;
@"NSXPCInterface" _remoteInterface;
@"NSXPCInterface" _exportedInterface;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T{queue={object=^{dispatch_object_s}}},N,V_xpcQueue) xpcQueue;
@property (T@"NSXPCListenerEndpoint",&,N,V_endpoint) endpoint;
@property (T@"MuxNotificationSink",&,N,V_notificationSink) notificationSink;
@property (T@"NSError",&,N,V_reconnectError) reconnectError;
@property (T@"NSXPCInterface",&,N,V_remoteInterface) remoteInterface;
@property (T@"NSXPCInterface",&,N,V_exportedInterface) exportedInterface;
```

## Instance methods

```
-[CoreTelephonyClientMux removeDelegate:];
-[CoreTelephonyClientMux remoteInterface];
-[CoreTelephonyClientMux initWithSink:systemConfigurationProvider:];
-[CoreTelephonyClientMux addDelegate:queue:];
-[CoreTelephonyClientMux setRemoteInterface:];
-[CoreTelephonyClientMux _connection];
-[CoreTelephonyClientMux _computeNotificationSet_sync:];
-[CoreTelephonyClientMux cachedValueForSelector:];
-[CoreTelephonyClientMux _registerForNotifications_sync:shouldForce:completion:];
-[CoreTelephonyClientMux setEndpoint:];
-[CoreTelephonyClientMux init];
-[CoreTelephonyClientMux _ensureConnectionSetup_sync];
-[CoreTelephonyClientMux dealloc];
-[CoreTelephonyClientMux _setReconnectError_sync:];
-[CoreTelephonyClientMux reconnectError];
-[CoreTelephonyClientMux notificationSink];
-[CoreTelephonyClientMux endpoint];
-[CoreTelephonyClientMux exportedInterface];
-[CoreTelephonyClientMux _computeNotificationSet_sync:completion:];
-[CoreTelephonyClientMux _computeNotificationSetForced_sync:];
-[CoreTelephonyClientMux _computeNotificationSetForced_sync];
-[CoreTelephonyClientMux _ensureConnectionSetup_sync:];
-[CoreTelephonyClientMux proxyWithQueue:errorHandler:];
-[CoreTelephonyClientMux setExportedInterface:];
-[CoreTelephonyClientMux cacheValue:forSelector:];
-[CoreTelephonyClientMux sink:handleNotification:];
-[CoreTelephonyClientMux _sendConnectionInterruptedNotification_sync:];
-[CoreTelephonyClientMux createCTAssertionForConnectionType:allocator:proxy:];
-[CoreTelephonyClientMux connection];
-[CoreTelephonyClientMux proxyWithErrorHandler_sync:];
-[CoreTelephonyClientMux setNotificationSink:];
-[CoreTelephonyClientMux setConnection:];
-[CoreTelephonyClientMux setXpcQueue:];
-[CoreTelephonyClientMux _initializeConnection_sync];
-[CoreTelephonyClientMux removeAssertionForInvalidationNotification:];
-[CoreTelephonyClientMux xpcQueue];
-[CoreTelephonyClientMux registerBlockForInvalidationNotification:callbackQueue:callback:];
-[CoreTelephonyClientMux initWithEndpoint:sink:systemConfigurationProvider:];
-[CoreTelephonyClientMux _connect_sync];
-[CoreTelephonyClientMux synchronousProxyWithErrorHandler:];
-[CoreTelephonyClientMux setReconnectError:];
-[CoreTelephonyClientMux _getAssertionTypeId];
```
