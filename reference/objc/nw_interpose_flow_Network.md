# `nw_interpose_flow`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_interface>" _interface;
@"NSObject<OS_nw_path_flow_registration>" _registration;
@"NSObject<OS_nw_path_flow>" _flow;
@? _eventHandler;
```

## Instance methods

```
-[nw_interpose_flow close];
-[nw_interpose_flow dealloc];
-[nw_interpose_flow clearFlowEventHandler];
-[nw_interpose_flow closeFlow];
-[nw_interpose_flow initWithInterface:registration:eventHandler:];
-[nw_interpose_flow matchNexusAgent:];
-[nw_interpose_flow matchNexusAgentWithFlow:];
-[nw_interpose_flow matchNexusInstance:];
-[nw_interpose_flow notifyFlowEvent:];
-[nw_interpose_flow resetFlow:];
```
