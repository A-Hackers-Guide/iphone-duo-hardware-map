# `nw_listener_inbox_socket`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `nw_listener_inbox`
- 7 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
^v _source;
@"NSObject<OS_nw_fd_wrapper>" _sockfd_wrapper_for_connection_group_only;
i _sockfd_for_logging_only_do_not_close_or_use;
i _sockfd_from_client;
C _ipProtocol;
[16C] _listenUUID;
@"NSObject<OS_nw_endpoint>" _specificSource;
```

## Instance methods

```
-[nw_listener_inbox_socket suspend];
-[nw_listener_inbox_socket start];
-[nw_listener_inbox_socket description];
-[nw_listener_inbox_socket initWithParameters:delegate:];
-[nw_listener_inbox_socket cancel];
-[nw_listener_inbox_socket resume];
```
