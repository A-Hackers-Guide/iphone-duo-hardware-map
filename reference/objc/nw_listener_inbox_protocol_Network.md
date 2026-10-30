# `nw_listener_inbox_protocol`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `nw_listener_inbox`
- 3 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
{nw_listen_protocol_callbacks="new_flow"^?"disconnected"^?} _listen_callbacks;
{nw_listen_protocol="callbacks"^{nw_listen_protocol_callbacks}"protocol_handler"^{nw_protocol}"protocol_handler_context"^v"handle"^v} _listen_protocol;
@"NSObject<OS_nw_endpoint>" _peer_identity;
```

## Instance methods

```
-[nw_listener_inbox_protocol description];
-[nw_listener_inbox_protocol cancel];
```
