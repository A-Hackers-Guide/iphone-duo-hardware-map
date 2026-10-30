# `NWBrowser`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NWBrowseDescriptor" _descriptor;
@"NWParameters" _parameters;
@"NSObject<OS_nw_browser>" _internalBrowser;
@"NSSet" _internalDiscoveredEndpoints;
```

## Properties

```
@property (T@"NSObject<OS_nw_browser>",R,V_internalBrowser) internalBrowser;
@property (T@"NSSet",&,V_internalDiscoveredEndpoints) internalDiscoveredEndpoints;
@property (T@"NWBrowseDescriptor",R,V_descriptor) descriptor;
@property (T@"NWParameters",R,V_parameters) parameters;
@property (T@"NSSet",R,N) discoveredEndpoints;
```

## Class methods

```
+[NWBrowser automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[NWBrowser parameters];
-[NWBrowser descriptor];
-[NWBrowser dealloc];
-[NWBrowser cancel];
-[NWBrowser internalBrowser];
-[NWBrowser setInternalDiscoveredEndpoints:];
-[NWBrowser copyDiscoveredEndpoints];
-[NWBrowser discoveredEndpoints];
-[NWBrowser initWithDescriptor:parameters:];
-[NWBrowser internalDiscoveredEndpoints];
-[NWBrowser setUpdateHandler];
```
